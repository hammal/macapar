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
font=ImageFont.truetype("DejaVuSerif.ttf",size=14)

text1="Reading status"
img=Image.new('RGB',(128,32))
d=ImageDraw.Draw(img)
d.text((0,0),text1,fill=(0,200,200),font=font)
matrix.SetImage(img.im.id, 0, 0)

time.sleep(0.2)
text2="."
img=Image.new('RGB',(128,32))
d=ImageDraw.Draw(img)
d.text((0,0),text2,fill=(0,200,200),font=font)

for m in range(1,6,1):
	for n in range(106,120,3):
		matrix.SetImage(img.im.id, n, 0)
		time.sleep(0.3)

time.sleep(2)

matrix.Clear()

text3="Exception processing message X9990??+? Parameter 0x000000986 009776544x8"
img=Image.new('RGB',(600,32))
d=ImageDraw.Draw(img)
d.text((0,0),text3,fill=(200,0,0),font=font)

for n in range(128,-img.size[0], -1):
	matrix.SetImage(img.im.id, n, 0)
	time.sleep(0.005)

time.sleep(2)

matrix.Clear()
# Mikrofoner
# Talföljden redo
# 

