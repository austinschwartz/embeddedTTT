#!/usr/bin/python

import time
from random import randint
from rgbmatrix import Adafruit_RGBmatrix

br = 0
bg = 150
bb = 0

gr = 150
gg = 00
gb = 0

def r():
	br = randint(0, 255)
	bg = randint(0, 255)
	bb = randint(0, 255)
	gr = randint(0, 255)
	gg = randint(0, 255)
	gb = randint(0, 255)

def makeX(i, j):
	l = 5
	for k in range(0, l):
		matrix.SetPixel(i + k, j + k, gr, gg, gb)
		matrix.SetPixel(i + l - k-1, j + k, gr, gg, gb)

def makeO(i, j):
	l = 5
	for k in range(0, l - 2):
		matrix.SetPixel(i, j + k + 1, gr, gg, gb)
		matrix.SetPixel(i + 4, j + k + 1, gr, gg, gb)
	for k in range(0, l - 2):
		matrix.SetPixel(i + k + 1, j, gr, gg, gb)
		matrix.SetPixel(i + k + 1, j + 4, gr, gg, gb)

def winner(bv):
	for i in range(4):
		square(bv)
		time.sleep(0.2)
		matrix.Clear()
		time.sleep(0.2)
	

def square(bv):
	matrix.Clear()
	if ((bv >> 18) & 1):
		winner(bv ^ (1 << 18))
		return

	for i in range(0, 32):
		matrix.SetPixel(0, i, br, bg, bb)
		matrix.SetPixel(i, 0, br, bg, bb)
		matrix.SetPixel(i, 30, br, bg, bb) # right edge
		matrix.SetPixel(i, 31, br, bg, bb) # right edge 2
		matrix.SetPixel(30, i, br, bg, bb) # bottom edge
		matrix.SetPixel(31, i, br, bg, bb) # bottom edge 2
		matrix.SetPixel(10, i, br, bg, bb) # 1st vertical line
		matrix.SetPixel(20, i, br, bg, bb) # 2nd vertical line
		matrix.SetPixel(i, 10, br, bg, bb) # 1st horizontal line
		matrix.SetPixel(i, 20, br, bg, bb) # 2nd horizontal line


	# FIRST ROW
	if   ((bv >> 0) & 1) == 1: makeX(3, 3)
	elif ((bv >> 1) & 1) == 1: makeO(3, 3)
	if   ((bv >> 2) & 1) == 1: makeX(13, 3)
	elif ((bv >> 3) & 1) == 1: makeO(13, 3)
	if   ((bv >> 4) & 1) == 1: makeX(23, 3)
	elif ((bv >> 5) & 1) == 1: makeO(23, 3)

	# SECOND ROW
	if   ((bv >> 6) & 1) == 1: makeX(3, 13)
	elif ((bv >> 7) & 1) == 1: makeO(3, 13)
	if   ((bv >> 8) & 1) == 1: makeX(13, 13)
	elif ((bv >> 9) & 1) == 1: makeO(13, 13)
	if   ((bv >> 10) & 1) == 1: makeX(23, 13)
	elif ((bv >> 11) & 1) == 1: makeO(23, 13)

	# THIRD ROW
	if   ((bv >> 12) & 1) == 1: makeX(3, 23)
	elif ((bv >> 13) & 1) == 1: makeO(3, 23)
	if   ((bv >> 14) & 1) == 1: makeX(13, 23)
	elif ((bv >> 15) & 1) == 1: makeO(13, 23)
	if   ((bv >> 16) & 1) == 1: makeX(23, 23)
	elif ((bv >> 17) & 1) == 1: makeO(23, 23)
	
		
		

matrix = Adafruit_RGBmatrix(32, 1)

x = 0
y = 0

#square(368929)
square(106785)


time.sleep(100.0)
matrix.Clear()
