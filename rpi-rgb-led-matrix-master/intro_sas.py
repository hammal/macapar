#-*- coding: utf-8 -*-
from __future__ import unicode_literals
from PIL import ImageEnhance

import Image
import ImageDraw
import time
import ImageFont
from rgbmatrix import Adafruit_RGBmatrix

import ImageOps
import pickle
import random

with open("antiklist.txt", "rb") as fp:   # Unpickling
    emojilist = pickle.load(fp)

print(len(emojilist))
# print(emojilist[0:10])
matrix = Adafruit_RGBmatrix(32, 4)
num=len(emojilist)
transparent = (0,0,0,0)

im = Image.new("RGBA", (128, 32),transparent)
txt=Image.new("RGB",(128,32))
d=ImageDraw.Draw(txt)
font=ImageFont.truetype("DejaVuSerif.ttf",size=16)
text="ANTIKRUNDAN"
d.text((64-font.getsize(text)[0]/2,16-font.getsize(text)[1]/2),text,(100,100,0),font)
size = 32,32
for n in range(0,4,1):
	d1=random.randint(0,16)*4
	d2=random.randint(0,16)*4
	d3=random.randint(0,16)*4
	d4=random.randint(0,16)*4
	pos=range(32,0,-1)
	for n in range(0,32,1):
		pos.append(n)
	pos1=[]
	for n in range(0,d1,1):
		pos1.append(33)
	for n in range(0,len(pos),1):
		pos1.append(pos[n])
	for n in range(0,128-len(pos1),1):
		pos1.append(33)
	pos2=[]
	for n in range(0,d2,1):
		pos2.append(33)
	for n in range(0,len(pos),1):
		pos2.append(pos[n])
	print(len(pos2))
	for n in range(0,128-(len(pos2)),1):
		pos2.append(33)
	pos3=[]
	for n in range(0,d3,1):
		pos3.append(33)
	for n in range(0,len(pos),1):
		pos3.append(pos[n])
	print(len(pos3))
	for n in range(0,128-(len(pos3)),1):
		pos3.append(33)
	pos4=[]
	for n in range(0,d4,1):
		pos4.append(33)
	for n in range(0,len(pos),1):
		pos4.append(pos[n])
	print(len(pos4))
	for n in range(0,128-(len(pos4)),1):
		pos4.append(33)

	posmat=[pos1,pos2,pos3,pos4]


	opacity=1
	emoji1 = Image.open(emojilist[random.randint(0,num-1)])
	im_emoji1 = Image.new("RGBA", (32, 32),transparent)
	emoji1.thumbnail(size, Image.ANTIALIAS)
	im_emoji1.paste(emoji1,(0,0))
	im_emoji1.load()          # Must do this before SetImage() calls	
	emoji2 = Image.open(emojilist[random.randint(0,num-1)])
	im_emoji2 = Image.new("RGBA", (32, 32),transparent)
	emoji2.thumbnail(size, Image.ANTIALIAS)
	im_emoji2.paste(emoji2,(0,0))
	im_emoji2.load()          
	emoji3 = Image.open(emojilist[random.randint(0,num-1)])
	im_emoji3 = Image.new("RGBA", (32, 32),transparent)
	emoji3.thumbnail(size, Image.ANTIALIAS)
	im_emoji3.paste(emoji3,(0,0))
	im_emoji3.load()          
	emoji4 = Image.open(emojilist[random.randint(0,num-1)])
	im_emoji4 = Image.new("RGBA", (32, 32),transparent)
	emoji4.thumbnail(size, Image.ANTIALIAS)
	im_emoji4.paste(emoji4,(0,0))
	im_emoji4.load()          
	for m in range(0,128,1):
		im.paste(txt,(0,0))
		en = ImageEnhance.Brightness(im_emoji1)
		mask = en.enhance(1-opacity)
		im.paste(im_emoji1,(0,posmat[0][m]),mask)
		en = ImageEnhance.Brightness(im_emoji2)
		mask = en.enhance(1-opacity)
		im.paste(im_emoji2,(32,posmat[1][m]),mask)
		en = ImageEnhance.Brightness(im_emoji3)
		mask = en.enhance(1-opacity)
		im.paste(im_emoji3,(64,posmat[2][m]),mask)
		en = ImageEnhance.Brightness(im_emoji4)
		mask = en.enhance(1-opacity)
		im.paste(im_emoji4,(96,posmat[3][m]),mask)
		matrix.SetImage(im.im.id, 0, 0)
		time.sleep(0.05)

# print(im.size[0])
# for n in range(128, -im.size[0], -1): # Scroll R to L

# 	matrix.SetImage(im.im.id, n, 0)
# 	time.sleep(0.02)