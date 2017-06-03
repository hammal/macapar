#-*- coding: utf-8 -*-
from __future__ import unicode_literals
import Image
import ImageDraw
import time
import ImageFont
from rgbmatrix import Adafruit_RGBmatrix

import ImageOps
matrix = Adafruit_RGBmatrix(32, 4)
im = Image.new("RGB", (128, 32))

emoji = Image.open("emojis/1f3a8.png")
size = 32,32
emoji.thumbnail(size, Image.ANTIALIAS)
emoji.load()          # Must do this before SetImage() calls
for m in range(1,6,1):
	for n in range(128, -emoji.size[0], -1): # Scroll R to L
		matrix.SetImage(emoji.im.id, n, 0)
		time.sleep(0.025)