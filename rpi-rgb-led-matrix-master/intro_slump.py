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
import math
import sys


import namesList
names=namesList.names
random.shuffle(names)
print(len(names))

talare=str(sys.argv[1])
names[-2]=talare
# print(emojilist[0:10])
matrix = Adafruit_RGBmatrix(32, 4)
font=ImageFont.truetype("DejaVuSerif.ttf",size=18)
h=0
heighttext=[]
im=Image.new("RGB",(128,30*len(names)))
for n in range(0,len(names),1):
	txt=Image.new("RGB",(128,29))
	d=ImageDraw.Draw(txt)
	text=names[n]
	d.text((0,0),text,(100,100,0),font)
	im.paste(txt,(0,h))
	heighttext.append(font.getsize(text)[1])
	h=h+heighttext[n]

print(h)
pos=(range(32,-(h-heighttext[-1]-heighttext[-2]-5),-1))

timeind=[]
maxhast=0.01
breakpoint1=100
breakpoint2=50
for n in range(1,len(pos)-breakpoint1,1):
	timeind.append(maxhast/len(pos)*n)
for n in range(len(pos)-breakpoint1,len(pos)-breakpoint2):
	timeind.append(maxhast/len(pos)*(len(pos)-(breakpoint1-1)))
for n in range(len(pos)-breakpoint2,len(pos)+1,1):
	timeind.append(maxhast/len(pos)*(len(pos)-(breakpoint2-1)))

print(len(pos))
print(len(timeind))
# print(timeind[-100:-1])
for n in range(0,len(pos),1):
	matrix.SetImage(im.im.id,0,pos[n])
	time.sleep(timeind[n])
	matrix.Clear()
matrix.SetImage(im.im.id,0,pos[-1])
time.sleep(1)
print(font.getsize(text[0]))
for n in range(18,40):
	font=ImageFont.truetype("DejaVuSerif.ttf",size=n)
	text=names[-2]
	if font.getsize(text)[0] > 128:
		stopsize=n-1
		matrix.Clear()
		break
	txt=Image.new("RGB",(128,29))
	d=ImageDraw.Draw(txt)
	d.text((0,0),text,(random.randint(0,255),random.randint(0,255),random.randint(0,255)),font)
	matrix.SetImage(txt.im.id,0,16-font.getsize(text)[1]/2)
	time.sleep(0.1)
	matrix.Clear()
	print(n)
	stopsize = n


for n in range(0,100):
	font=ImageFont.truetype("DejaVuSerif.ttf",size=stopsize)
	text=names[-2]
	txt=Image.new("RGB",(128,29))
	d=ImageDraw.Draw(txt)
	d.text((0,0),text,(random.randint(0,255),random.randint(0,255),random.randint(0,255)),font)
	matrix.SetImage(txt.im.id,0,16-font.getsize(text)[1]/2)
	time.sleep(.05)
