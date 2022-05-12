import csv
import sys
import subprocess
from time import sleep

if len(sys.argv) < 2:
  print("Usage: python pullist.py csvfile.csv")
  exit()

demofile = open(sys.argv[1])
demoreader = csv.reader(demofile)

for row in demoreader:
  filename,title,artist,year,party,platform,*rest = row
  if "youtube" in filename:
    print(f"Pulling {filename} ...")
    subprocess.run(["youtube-dl", filename])
    sleep(5)

