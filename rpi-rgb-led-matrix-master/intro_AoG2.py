#-*- coding: utf-8 -*-
from __future__ import unicode_literals
import PIL
from PIL import ImageEnhance
import Image
import ImageDraw
import time
import ImageFont
from rgbmatrix import Adafruit_RGBmatrix


import ImageOps
matrix = Adafruit_RGBmatrix(32, 4)
font=ImageFont.truetype("DejaVuSerif.ttf",size=13)
text="Gunilla & Anders"
print(font.getsize(text))
print((64-font.getsize(text)[0]/2,16-font.getsize(text)[1]/2))
# txt=Image.new("RGB",(128,32))
# draw=ImageDraw.Draw(txt)
# draw.text((64-font.getsize(text)[0]/2,16-font.getsize(text)[1]/2),text,(0,100,100),font)
# matrix.SetImage(txt.im.id, 0,0)
# time.sleep(1)

gardinL = Image.open("gardinL.tiff")
gardinR = Image.open("gardinR.tiff")
size = 2*32,300
gardinL.thumbnail(size, Image.ANTIALIAS)
gardinR.thumbnail(size, Image.ANTIALIAS)
gardinL.load()          # Must do this before SetImage() calls
gardinR.load()          # Must do this before SetImage() calls

width=128
height=32
opacity=0.8
black = (0,0,0)
transparent = (0,0,0,0)
im = Image.new("RGB", (128, 32))
im.paste(gardinL,(-1,0))
im.paste(gardinR,(62,0))
matrix.SetImage(im.im.id, 0,0)
time.sleep(1)
matrix.Clear()
m=0
for n in range(1,58,1):
	im = Image.new("RGB", (128, 32),transparent)
	circ=Image.new('RGB', (128,32))
	draw = ImageDraw.Draw(circ)
	r=12;x=64;y=16;
	draw.ellipse((x-r, y-r, x+r, y+r), fill=(255,255,255))
	if n<30:
		im.paste(circ,(0,0))
	else:
		im.paste(circ,(0-(n-30)*2,0))

	wm = Image.new('RGBA',(width,height),transparent)
	draw = ImageDraw.Draw(wm)
	draw.text((64-font.getsize(text)[0]/2,16-font.getsize(text)[1]/2),text,black,font)
	en = ImageEnhance.Brightness(wm)
	#en.putalpha(mask)
	mask = en.enhance(1-opacity)
	im.paste(wm,(0,0),mask)
	matrix.SetImage(im.im.id, 0,0)

	im.paste(gardinL,(0-n,0))
	im.paste(gardinR,(62+n,0))
	matrix.SetImage(im.im.id, 0,0)
	time.sleep(0.06)
	matrix.Clear()


for n in range(-26,26,1):
	im = Image.new("RGB", (128, 32),transparent)
	circ=Image.new('RGB', (128,32))
	draw = ImageDraw.Draw(circ)
	x=64;y=16;r=12
	draw.ellipse((x-r, y-r, x+r, y+r), fill=(255,255,255))
	im.paste(circ,(n*2,0))
	wm = Image.new('RGBA',(width,height),transparent)
	draw = ImageDraw.Draw(wm)
	draw.text((64-font.getsize(text)[0]/2,16-font.getsize(text)[1]/2),text,black,font)
	en = ImageEnhance.Brightness(wm)
	#en.putalpha(mask)
	mask = en.enhance(1-opacity)
	im.paste(wm,(0,0),mask)
	im.paste(gardinL,(0-57,0))
	im.paste(gardinR,(62+57,0))
	matrix.SetImage(im.im.id, 0,0)
	time.sleep(0.06)
	matrix.Clear()

for n in range(25,0,-1):
	im = Image.new("RGB", (128, 32),transparent)
	circ=Image.new('RGB', (128,32))
	draw = ImageDraw.Draw(circ)
	x=64;y=16;r=12
	draw.ellipse((x-r, y-r, x+r, y+r), fill=(255,255,255))
	im.paste(circ,(n*2,0))
	wm = Image.new('RGBA',(width,height),transparent)
	draw = ImageDraw.Draw(wm)
	draw.text((64-font.getsize(text)[0]/2,16-font.getsize(text)[1]/2),text,black,font)
	en = ImageEnhance.Brightness(wm)
	#en.putalpha(mask)
	mask = en.enhance(1-opacity)
	im.paste(wm,(0,0),mask)
	im.paste(gardinL,(0-57,0))
	im.paste(gardinR,(62+57,0))
	matrix.SetImage(im.im.id, 0,0)
	time.sleep(0.06)
	matrix.Clear()
for n in range(12,64,1):
	im = Image.new("RGB", (128, 32),transparent)
	circ=Image.new('RGB', (128,32))
	draw = ImageDraw.Draw(circ)
	x=64;y=16;r=n
	draw.ellipse((x-r, y-r, x+r, y+r), fill=(255,255,255))
	im.paste(circ,(0,0))
	wm = Image.new('RGBA',(width,height),transparent)
	draw = ImageDraw.Draw(wm)
	draw.text((64-font.getsize(text)[0]/2,16-font.getsize(text)[1]/2),text,black,font)
	en = ImageEnhance.Brightness(wm)
	#en.putalpha(mask)
	mask = en.enhance(1-opacity)
	im.paste(wm,(0,0),mask)

	im.paste(gardinL,(0-57,0))
	im.paste(gardinR,(62+57,0))
	matrix.SetImage(im.im.id, 0,0)
	time.sleep(0.06)
	matrix.Clear()

n=64
im = Image.new("RGB", (128, 32),transparent)
circ=Image.new('RGB', (128,32))
draw = ImageDraw.Draw(circ)
x=64;y=16;r=n
draw.ellipse((x-r, y-r, x+r, y+r), fill=(255,255,255))
im.paste(circ,(0,0))
wm = Image.new('RGBA',(width,height),transparent)
draw = ImageDraw.Draw(wm)
draw.text((64-font.getsize(text)[0]/2,16-font.getsize(text)[1]/2),text,black,font)
en = ImageEnhance.Brightness(wm)
mask = en.enhance(1-opacity)
im.paste(wm,(0,0),mask)
im.paste(gardinL,(0-57,0))
im.paste(gardinR,(62+57,0))
matrix.SetImage(im.im.id, 0,0)
time.sleep(5)
matrix.Clear()	
for n in range(64,12,-11):
	im = Image.new("RGB", (128, 32),transparent)
	circ=Image.new('RGB', (128,32))
	draw = ImageDraw.Draw(circ)
	x=64;y=16;r=n
	draw.ellipse((x-r, y-r, x+r, y+r), fill=(255,255,255))
	im.paste(circ,(0,0))
	wm = Image.new('RGBA',(width,height),transparent)
	draw = ImageDraw.Draw(wm)
	draw.text((64-font.getsize(text)[0]/2,16-font.getsize(text)[1]/2),text,black,font)
	en = ImageEnhance.Brightness(wm)
	#en.putalpha(mask)
	mask = en.enhance(1-opacity)
	im.paste(wm,(0,0),mask)

	# im.paste(gardinL,(0-57,0))
	# im.paste(gardinR,(62+57,0))
	matrix.SetImage(im.im.id, 0,0)
	time.sleep(0.03)
	matrix.Clear()
