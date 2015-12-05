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
    
