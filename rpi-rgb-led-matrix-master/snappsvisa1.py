#-*- coding: utf-8 -*-
from __future__ import unicode_literals
import Image
import ImageDraw
import time
import ImageFont
from rgbmatrix import Adafruit_RGBmatrix

# Rows and chain length are both required parameters:
matrix = Adafruit_RGBmatrix(32, 4)
font=ImageFont.load_default()
font=ImageFont.truetype("DejaVuSerif.ttf",size=11)

img=Image.new('RGB',(128,32))
text1="Fååm fååm"
text2="Fååm fååm"
text3="Fåm vi lite upp i kosi"
text4="Jengan gå jengan gå jengan gå jengan teee"
for n in range(1,3,1):
	time.sleep(0.5)
	img=Image.new('RGB',(128,32))
	d=ImageDraw.Draw(img)
	d.text((-1,0),text1,fill=(0,200,200),font=font)
	matrix.SetImage(img.im.id, 0, 0)
	time.sleep(3)

	img=Image.new('RGB',(128,32))
	d=ImageDraw.Draw(img)
	d.text((-1,0),text2,fill=(200,200,0),font=font)
	matrix.SetImage(img.im.id, 65, 0)
	time.sleep(3)

	img=Image.new('RGB',(128,32))
	d=ImageDraw.Draw(img)
	d.text((-1,0),text3,fill=(0,200,0),font=font)
	matrix.SetImage(img.im.id, 0, 15)
	time.sleep(5.5)

	matrix.Clear()

font=ImageFont.truetype("DejaVuSerif.ttf",size=14)
img=Image.new('RGB',(300,32))
d=ImageDraw.Draw(img)
d.text((1,0),text4,fill=(200,0,200),font=font)
for n in range(128, -img.size[0], -1): # Scroll R to L
	matrix.SetImage(img.im.id, n, 8)
	time.sleep(0.018)


# //: Fåm, fåm, fåm, fåm, fåm vi lite opp i kosa :// 
# Jen gang och jen gang och jen gang och jen gang te 
# Jen gang och jen gang och jen gang och jen gang te
