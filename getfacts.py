import sys
import re
import urllib.request
import json

if len(sys.argv) < 2:
  print("Usage: python getfacts.py demozoo_urls.txt")
  exit()

demofile = open(sys.argv[1])

for in_line in demofile.readlines():
  in_line = in_line.rstrip("\n")
  if "demozoo" in in_line:
    searcher = re.search("https://demozoo.org/productions/([0-9]+)/", in_line)
    dz_id = searcher.group(1)
  with urllib.request.urlopen(f"http://demozoo.org/api/v1/productions/{dz_id}/?format=json") as url:
    data = json.loads(url.read().decode())
    filename=in_line
    youtube_link_object=next(filter(lambda ext: ext['link_class'] == 'YoutubeVideo', data['external_links']), None)
    if youtube_link_object:
      filename =youtube_link_object['url']
    title=data['title']
    artist=" & ".join(map(lambda auth: auth["name"], data['author_nicks']))
    year=data['release_date'].split("-")[0]
    if len(data['competition_placings']) > 0:
      competition_data=data['competition_placings'][0]['competition']
      party=competition_data['party']['name']
      platform=competition_data['name']
    else:
      party=""
      platform="-"
    print(f"{filename},{title},{artist},{year},{party},{platform}")
