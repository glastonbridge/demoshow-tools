import cairo

import sys
import subprocess
from os.path import exists

d_name = sys.argv[1]
d_author = sys.argv[2]
d_year = sys.argv[3]
d_event = sys.argv[4]
d_plat = sys.argv[5]
inputvid = sys.argv[6]
outputfile = sys.argv[7]

if exists(f"{outputfile}.mp4"):
  print(f"{outputfile} exists")
  exit()

imagesize = (1920,1080)

def make_frame(t):
  surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, *imagesize)

  cr = cairo.Context(surface)

  cr.set_source_rgba(0.0, 0.0, 0.0, 0.0)
  cr.rectangle(0, 0, 1920,1080)
  cr.fill()
  fay_doubt = max(min(1, (300-t)/30),0)

  cr.set_source_rgba(0.2,0.2,0.2,max(1, (t-30)/120)*fay_doubt*0.8)
  cr.rectangle(0,820,max(0,min(1920,(t-30)*80)),160)
  cr.fill()

  cr.select_font_face("Oxanium", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)
  cr.set_font_size(68)
  

  cr.set_source_rgba(1,0.9,0.8, min(1, (t-55)/40)*fay_doubt)

  cr.move_to(240, 880)
  cr.show_text(d_name)
  
  cr.select_font_face("Oxanium", cairo.FONT_SLANT_ITALIC, cairo.FONT_WEIGHT_NORMAL)
  cr.set_font_size(38)
  cr.move_to(240, 920)
  cr.show_text(d_author)

  cr.select_font_face("Oxanium", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)
  cr.set_font_size(30)
  cr.move_to(240, 960)
  cr.show_text(f"{d_event}, {d_year} ({d_plat})")
  
  logo = cairo.ImageSurface.create_from_png("./logo.png")

  scale_xy = 1/4
  cr.save()
  cr.translate(0,800)
  cr.scale(scale_xy, scale_xy)
  cr.set_source_surface(logo, 0, 0)
  cr.paint_with_alpha(min(1, t/60)*fay_doubt)
  cr.restore()


  frameno = str(t).zfill(4)

  surface.write_to_png(f"frames/frame{frameno}.png")

for t in range(0,300):
  make_frame(t)

ffmpeg_cmd = f"ffmpeg -i \"{inputvid}\" -framerate 60 -i frames/frame%04d.png -y -filter_complex scale=1920:1080:'force_original_aspect_ratio=decrease,pad=1920:1080:\(ow-iw\)/2'[scaled]\;[scaled]overlay=x=0:y=0:enable='between\(t\,0\,10\)'[out] -map [out] -map 0:a -max_muxing_queue_size 9999 \"{outputfile}.mp4\""

print(f"Command: ${ffmpeg_cmd}")
subprocess.run(ffmpeg_cmd, shell=True)

