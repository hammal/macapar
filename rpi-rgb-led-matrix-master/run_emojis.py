#-*- coding: utf-8 -*-
from __future__ import unicode_literals
import Image
import ImageDraw
import time
import ImageFont
from rgbmatrix import Adafruit_RGBmatrix

import ImageOps
import pickle

with open("emojiemotionlist.txt", "rb") as fp:   # Unpickling
    emojilist = pickle.load(fp)

print(len(emojilist))
# print(emojilist[0:10])
matrix = Adafruit_RGBmatrix(32, 4)
num=len(emojilist)
rep=4
im = Image.new("RGB", (32*num*rep, 32))
size = 32,32

for n in range(0,rep*num,1):
	print(emojilist[n%num])
	emoji = Image.open(emojilist[n%num])
	emoji.thumbnail(size, Image.ANTIALIAS)
	emoji.load()          # Must do this before SetImage() calls	
	im.paste(emoji,(n*32+1,0))

print(im.size[0])
for n in range(128, -im.size[0], -1): # Scroll R to L

	matrix.SetImage(im.im.id, n, 0)
	time.sleep(0.002)