import csv
import sys
import subprocess

if len(sys.argv) < 2:
  print("Usage: python maketitles.py csvfile.csv")
  print("csv rows should be formatted: video_filename,Demo Title,Author,Year,Party,Platform")
  exit()

demofile = open(sys.argv[1])
demoreader = csv.reader(demofile)

for row in demoreader:
  filename,title,artist,year,party,platform,*rest = row
  cleantitle = title.replace("/","_")
  subprocess.run(["python", "gentitle.py", title, artist, year, party, platform, filename, f"intermediate/{cleantitle} - {artist}"])

