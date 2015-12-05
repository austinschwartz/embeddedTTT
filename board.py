#!/usr/bin/python
import time
import sys
from random import randint

br = 0
bg = 150
bb = 0

gr = 150
gg = 00
gb = 0

def ledBoard(matrix, bv):
    from rgbmatrix import Adafruit_RGBmatrix
    square(matrix, bv)

def makeX(matrix, i, j):
    l = 5
    for k in range(0, l):
        matrix.SetPixel(i + k, j + k, gr, gg, gb)
        matrix.SetPixel(i + l - k-1, j + k, gr, gg, gb)

def makeO(matrix, i, j):
    l = 5
    for k in range(0, l - 2):
        matrix.SetPixel(i, j + k + 1, gr, gg, gb)
        matrix.SetPixel(i + 4, j + k + 1, gr, gg, gb)
    for k in range(0, l - 2):
        matrix.SetPixel(i + k + 1, j, gr, gg, gb)
        matrix.SetPixel(i + k + 1, j + 4, gr, gg, gb)

def square(matrix, bv):
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
    if   ((bv >> 0) & 1) == 1: makeX(matrix, 3, 3)
    elif ((bv >> 1) & 1) == 1: makeO(matrix, 3, 3)
    if   ((bv >> 2) & 1) == 1: makeX(matrix, 13, 3)
    elif ((bv >> 3) & 1) == 1: makeO(matrix, 13, 3)
    if   ((bv >> 4) & 1) == 1: makeX(matrix, 23, 3)
    elif ((bv >> 5) & 1) == 1: makeO(matrix, 23, 3)

    # SECOND ROW
    if   ((bv >> 6) & 1) == 1: makeX(matrix, 3, 13)
    elif ((bv >> 7) & 1) == 1: makeO(matrix, 3, 13)
    if   ((bv >> 8) & 1) == 1: makeX(matrix, 13, 13)
    elif ((bv >> 9) & 1) == 1: makeO(matrix, 13, 13)
    if   ((bv >> 10) & 1) == 1: makeX(matrix, 23, 13)
    elif ((bv >> 11) & 1) == 1: makeO(matrix, 23, 13)

    # THIRD ROW
    if   ((bv >> 12) & 1) == 1: makeX(matrix, 3, 23)
    elif ((bv >> 13) & 1) == 1: makeO(matrix, 3, 23)
    if   ((bv >> 14) & 1) == 1: makeX(matrix, 13, 23)
    elif ((bv >> 15) & 1) == 1: makeO(matrix, 13, 23)
    if   ((bv >> 16) & 1) == 1: makeX(matrix, 23, 23)
    elif ((bv >> 17) & 1) == 1: makeO(matrix, 23, 23)

def getCell(bv, r, c):
    if ((bv >> getCellNumber(r, c, 'o')) & 1) != 0:
        return 'o'
    if ((bv >> getCellNumber(r, c, 'x')) & 1) != 0:
        return 'x'
    return ' '

def getCellNumber(r, c, t):
    return r * 6 + c * 2 + (1 if t == 'o' else 0)

def drawBoard(bv):
    # first row
    str = "     |     |     \n  "
    if   ((bv >> 0) & 1) == 1: str += 'x'
    elif ((bv >> 1) & 1) == 1: str += 'o'
    else: str += ' '
    str += '  |  '
    if   ((bv >> 2) & 1) == 1: str += 'x'
    elif ((bv >> 3) & 1) == 1: str += 'o'
    else: str += ' '
    str += '  |  '
    if   ((bv >> 4) & 1) == 1: str += 'x'
    elif ((bv >> 5) & 1) == 1: str += 'o'
    else: str += ' '
    str += '  \n     |     |     \n'
    str += '-----------------\n     |     |     \n  '

    # second row
    if   ((bv >> 6) & 1) == 1: str += 'x'
    elif ((bv >> 7) & 1) == 1: str += 'o'
    else: str += ' '
    str += '  |  '
    if   ((bv >> 8) & 1) == 1: str += 'x'
    elif ((bv >> 9) & 1) == 1: str += 'o'
    else: str += ' '
    str += '  |  '
    if   ((bv >> 10) & 1) == 1: str += 'x'
    elif ((bv >> 11) & 1) == 1: str += 'o'
    else: str += ' '
    str += '  \n     |     |     \n'
    str += '-----------------\n     |     |     \n  '

    # third row
    if   ((bv >> 12) & 1) == 1: str += 'x'
    elif ((bv >> 13) & 1) == 1: str += 'o'
    else: str += ' '
    str += '  |  '
    if   ((bv >> 14) & 1) == 1: str += 'x'
    elif ((bv >> 15) & 1) == 1: str += 'o'
    else: str += ' '
    str += '  |  '
    if   ((bv >> 16) & 1) == 1: str += 'x'
    elif ((bv >> 17) & 1) == 1: str += 'o'
    else: str += ' '
    str += '  \n     |     |     \n'

    print(str)

def equalCells(bv, i1, j1, i2, j2, i3, j3):
    if (getCell(bv, i1, j1) == getCell(bv, i2, j2) == getCell(bv, i3, j3)) and getCell(bv, i1, j1) != ' ':
        return True

def winner(bv):
    # check rows
    for i in range(0, 3):
        if (equalCells(bv, i, 0, i, 1, i, 2) == True):
            return getCell(bv, i, 0)

    # check cols
    for i in range(0, 3):
        if (equalCells(bv, 0, i, 1, i, 2, i) == True):
            return getCell(bv, 0, i)

    # diagnals
    if (equalCells(bv, 0, 0, 1, 1, 2, 2) == True):
        return getCell(bv, 0, 0)
    if (equalCells(bv, 0, 2, 1, 1, 0, 2) == True):
        return getCell(bv, 0, 2)

    return ' '
    
