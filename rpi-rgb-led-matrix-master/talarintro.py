#-*- coding: utf-8 -*-
from __future__ import unicode_literals
import Image
import ImageDraw
import time
import ImageFont
from rgbmatrix import Adafruit_RGBmatrix

import ImageOps
matrix = Adafruit_RGBmatrix(32, 4)
font=ImageFont.truetype("DejaVuSerif.ttf",size=18)
text="Leif"
print(font.getsize(text)[0])
print((64-font.getsize(text)[0]/2,16-font.getsize(text)[1]/2))
im = Image.new("RGB", (128, 32))
txt=Image.new('RGB', (128,32))
d = ImageDraw.Draw(txt)
d.text((64-font.getsize(text)[0]/2,16-font.getsize(text)[1]/2),text,  font=font, fill=(255,255,0))
w=txt.rotate(0, expand=0)
im.paste(w, (0,0))
guitar = Image.open("guitar.tif")
size = 50,50
guitar.thumbnail(size, Image.ANTIALIAS)
guitar.load()          # Must do this before SetImage() calls
print("hej")
for m in range(1,5,1):
	for n in range(1,361,2):
		d.text((64-font.getsize(text)[0]/2,16-font.getsize(text)[1]/2),text,  font=font, fill=(200+10*n%255,n + 255 % 255,n %255))
		w=txt.rotate(n,expand=0)
		im.paste(w, (0,0))
		im.paste(guitar,(128-n*2,5))
		im.paste(guitar,(128*4-n*2,5))
		matrix.SetImage(im.im.id, 0,0)
		time.sleep(0.02)
		matrix.Clear()