# Field-FX Demoshow Tools

aldroid used these to make demoshows quickly and easily from demozoo entries and youtube videos.

## Requirements

- Python (written on 3.6.12)
- ffmpeg (for generating titles)
- youtube-dl (if you're pulling videos from youtube)
- Oxanium font installed on your system

### Installing python requirements

Run `pip install -r requirements.txt`

## Example 1 - Generating titles

If you already have some demo capture videos and you know the information for them, start here.

Create a csv file, e.g. `demo_details.csv`

Each line in the csv file should be in the format

```
path to video.file,Demo Title,Group / Artist,Release Year,Party,Platform
```

e.g.

```
303 - Acme.mp4,303,Acme,1997,X Party,PC
```

Run `maketitles.py`

```
python maketitles.py demo_details.csv`
```

The titled videos will be output to `intermediate/`

## Example 2 - Fetching demo information and pulling videos from youtube

Make a list of Demozoo URLs, e.g.

```
https://demozoo.org/productions/2/
https://demozoo.org/productions/300867/
https://demozoo.org/productions/173425/
```

Save it as a txt file, e.g. `demos.txt`

Run `getfacts.py`

```
python getfacts.py demos.txt > demo_details.csv
```

This gives you the titles and so forth. Also links to youtube videos.

Run `pulllist.py`

```
python pulllist.py demo_details.csv
```

Wait for hours while youtube-dl does its thing.

Once you've got titles and locally-stored videos, update the youtube URLs in column 1 of `demo_details.csv` to the paths to the actual videos (can be relative). If a filename contains commas or any other weird characters, you can put the filename column in quotes.

Also check that the Demozoo prod details are correct (I generally strip the year from the Party name, because it's displayed separately anyway. Also platform is usually a bit generic coming from Demozoo so make it more specific).

Now generate the titles as per the previous example.
