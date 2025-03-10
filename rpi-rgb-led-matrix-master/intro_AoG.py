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
text="Gunilla och Anders"
print(font.getsize(text)[0])
print((64-font.getsize(text)[0]/2,16-font.getsize(text)[1]/2))
im = Image.new("RGB", (128, 32))
# Text
txt=Image.new('RGB', (128,32))
d = ImageDraw.Draw(txt)
d.text((64-font.getsize(text)[0]/2,16-font.getsize(text)[1]/2),text,  font=font, fill=(200,200,0,0))
# w=txt.rotate(0, expand=0)
# im.paste(txt, (0,0))
# matrix.SetImage(im.im.id, 0,0)
# time.sleep(5)


gardinL = Image.open("gardinL.tiff")
gardinR = Image.open("gardinR.tiff")
size = 2*32,300
gardinL.thumbnail(size, Image.ANTIALIAS)
gardinR.thumbnail(size, Image.ANTIALIAS)
gardinL.load()          # Must do this before SetImage() calls
gardinR.load()          # Must do this before SetImage() calls
# im.paste(gardinL,(-20,0))
# im.paste(gardinR,(62,0))
# matrix.SetImage(im.im.id, 0,0)
# time.sleep(5)

# d.text((64-font.getsize(text)[0]/2,16-font.getsize(text)[1]/2),text,  font=font, fill=(200+10*n%255,n + 255 % 255,n %255))
# w=txt.rotate(n,expand=0)
# im.paste(w, (0,0))
# im.paste(guitar,(128-n*2,5))
# im.paste(guitar,(128*4-n*2,5))
# matrix.SetImage(im.im.id, 0,0)
# pos=range(1,64,1)
im = Image.new("RGB", (128, 32))
im.paste(gardinL,(-1,0))
im.paste(gardinR,(62,0))
matrix.SetImage(im.im.id, 0,0)
time.sleep(1)
matrix.Clear()

width=128
height=32
opacity=0.8
black = (0,0,0)
transparent = (0,0,0,0)

for n in range(1,30,1):
	im = Image.new("RGB", (128, 32),transparent)
	circ=Image.new('RGB', (128,32))
	draw = ImageDraw.Draw(circ)
	x=64;y=16;r=12
	draw.ellipse((x-r, y-r, x+r, y+r), fill=(255,255,255))
	im.paste(circ,(0-n,0))

	wm = Image.new('RGBA',(width,height),transparent)
	draw = ImageDraw.Draw(wm)
	draw.text((0,0),text,black,font)
	en = ImageEnhance.Brightness(wm)
	#en.putalpha(mask)
	mask = en.enhance(1-opacity)
	im.paste(wm,(0,font.getsize(text)[1]),mask)
	matrix.SetImage(im.im.id, 0,0)

	im.paste(gardinL,(0-n*2,0))
	im.paste(gardinR,(62+n*2,0))
	matrix.SetImage(im.im.id, 0,0)
	time.sleep(0.06)
	matrix.Clear()
for n in range(30,49,1):
	im = Image.new("RGB", (128, 32),transparent)
	circ=Image.new('RGB', (128,32))
	draw = ImageDraw.Draw(circ)
	x=64;y=16;r=10
	draw.ellipse((x-r, y-r, x+r, y+r), fill=(255,255,255))
	im.paste(circ,(0-n,0))

	wm = Image.new('RGBA',(width,height),transparent)
	draw = ImageDraw.Draw(wm)
	draw.text((0,0),text,black,font)
	en = ImageEnhance.Brightness(wm)
	mask = en.enhance(1-opacity)
	im.paste(wm,(0,font.getsize(text)[1]),mask)
	matrix.SetImage(im.im.id, 0,0)

	im.paste(gardinL,(0-29*2,0))
	im.paste(gardinR,(62+29*2,0))
	matrix.SetImage(im.im.id, 0,0)
	time.sleep(0.06)
	matrix.Clear()
for n in range(-47,32,1):
	im = Image.new("RGB", (128, 32),transparent)
	circ=Image.new('RGB', (128,32))
	draw = ImageDraw.Draw(circ)
	x=64;y=16;r=10
	draw.ellipse((x-r, y-r, x+r, y+r), fill=(255,255,255))
	im.paste(circ,(n,0))

	wm = Image.new('RGBA',(width,height),transparent)
	draw = ImageDraw.Draw(wm)
	draw.text((0,0),text,black,font)
	en = ImageEnhance.Brightness(wm)
	mask = en.enhance(1-opacity)
	im.paste(wm,(0,font.getsize(text)[1]),mask)
	matrix.SetImage(im.im.id, 0,0)

	im.paste(gardinL,(0-29*2,0))
	im.paste(gardinR,(62+29*2,0))
	matrix.SetImage(im.im.id, 0,0)
	time.sleep(0.06)
	matrix.Clear()

for n in range(32,0,-1):
	im = Image.new("RGB", (128, 32),transparent)
	circ=Image.new('RGB', (128,32))
	draw = ImageDraw.Draw(circ)
	x=64;y=16;r=10
	draw.ellipse((x-r, y-r, x+r, y+r), fill=(255,255,255))
	im.paste(circ,(n,0))

	wm = Image.new('RGBA',(width,height),transparent)
	draw = ImageDraw.Draw(wm)
	draw.text((0,0),text,black,font)
	en = ImageEnhance.Brightness(wm)
	mask = en.enhance(1-opacity)
	im.paste(wm,(0,font.getsize(text)[1]),mask)
	matrix.SetImage(im.im.id, 0,0)

	im.paste(gardinL,(0-29*2,0))
	im.paste(gardinR,(62+29*2,0))
	matrix.SetImage(im.im.id, 0,0)
	time.sleep(0.06)
	matrix.Clear()
for n in range(10,200,1):
	im = Image.new("RGB", (128, 32),transparent)
	circ=Image.new('RGB', (128,32))
	draw = ImageDraw.Draw(circ)
	x=64;y=16;r=n
	draw.ellipse((x-r, y-r, x+r, y+r), fill=(255,255,255))
	im.paste(circ,(0,0))

	wm = Image.new('RGBA',(width,height),transparent)
	draw = ImageDraw.Draw(wm)
	draw.text((0,0),text,black,font)
	en = ImageEnhance.Brightness(wm)
	mask = en.enhance(1-opacity)
	im.paste(wm,(0,font.getsize(text)[1]),mask)
	matrix.SetImage(im.im.id, 0,0)

	im.paste(gardinL,(0-29*2,0))
	im.paste(gardinR,(62+29*2,0))
	matrix.SetImage(im.im.id, 0,0)
	time.sleep(0.06)
	matrix.Clear()
time.sleep(5)
# im2 = Image.new('RGBA',(width,height),transparent) # Change this line too.

# circ=Image.new('RGB', (128,32))
# draw = ImageDraw.Draw(circ)
# x=16;y=5;r=10
# draw.ellipse((x-r, y-r, x+r, y+r), fill=(200,200,0))
# im2.paste(circ,(0,0))

# wm = Image.new('RGBA',(width,height),transparent)
# draw = ImageDraw.Draw(wm)
# draw.text((0,0),text,black,font)
# en = ImageEnhance.Brightness(wm)
# #en.putalpha(mask)
# mask = en.enhance(1-opacity)
# im2.paste(wm,(0,0),mask)
# matrix.SetImage(im2.im.id, 0,0)


# # matrix.SetImage(circ.im.id, 0,0)
# time.sleep(5)
