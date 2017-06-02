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
font=ImageFont.truetype("DejaVuSerif.ttf",size=10)

img=Image.new('RGB',(128,32))
d=ImageDraw.Draw(img)
text="Hellööå"
d.text((1,0),text,fill=(200,200,0),font=font)

for n in range(128, -img.size[0], -1): # Scroll R to L
	matrix.SetImage(img.im.id, n, 0)
	time.sleep(0.025)

matrix.SetImage(img.im.id, 0, 0)
time.sleep(3)