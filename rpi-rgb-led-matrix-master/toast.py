#!/usr/bin/python

# A more complex RGBMatrix example works with the Python Imaging Library,
# demonstrating a few graphics primitives and image loading.
# Note that PIL graphics do not have an immediate effect on the display --
# image is drawn into a separate buffer, which is then copied to the matrix
# using the SetImage() function (see examples below).
# Requires rgbmatrix.so present in the same directory.

# PIL Image module (create or load images) is explained here:
# http://effbot.org/imagingbook/image.htm
# PIL ImageDraw module (draw shapes to images) explained here:
# http://effbot.org/imagingbook/imagedraw.htm

import Image
import ImageDraw
import time
from rgbmatrix import Adafruit_RGBmatrix

# Rows and chain length are both required parameters:
matrix = Adafruit_RGBmatrix(32, 4)


im1 = Image.open("glas1.tif")
im2 = Image.open("glas1.tif")
size = 32,32
print(im2.size)
im1.thumbnail(size, Image.ANTIALIAS)
im1.load() 
im2.thumbnail(size, Image.ANTIALIAS)
im2.load()     
print(im1.size)
     # Must do this before SetImage() calls
# matrix.Fill(0x6F85FF) # Fill screen to sky color
# for m in range(1,6,1):
# 	for n in range(128, -image.size[0], -1): # Scroll R to L
# 		matrix.SetImage(image.im.id, n, 0)
# 		time.sleep(0.025)
# 		matrix.Clear()

for m in range(1,6,1):
	for n in range(128, 64, -1): # Scroll R to L
		matrix.SetImage(im1.im.id, n, 0)
		matrix.SetImage(im2.im.id, -(n-128+im2.size[0]), 0)
		time.sleep(0.025)
		matrix.Clear()
	for n in range(64, 128, 1): # Scroll R to L
		matrix.SetImage(im1.im.id, n, 0)
		matrix.SetImage(im2.im.id, -(n-128+im2.size[0]), 0)
		time.sleep(0.025)
		matrix.Clear()


# # 24-bit RGB scrolling example.
# # The adafruit.png image has a couple columns of black pixels at
# # the right edge, so erasing after the scrolled image isn't necessary.
matrix.Clear()
