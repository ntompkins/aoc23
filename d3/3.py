#!/usr/bin/env python3
from collections import deque

numbercoords = deque()
with open("sample") as f:
    contents = f.read().splitlines()
    for row,line in enumerate(contents):
        num =""
        start = 0
        for col, char in enumerate(line.strip()):
            # lookahead to next nondigit
            if char.isdigit():
                num += char
            else:
                numbercoords.append(num)
    print(numbercoords)
#        numbers = deque()
#        for column,c in enumerate(line):
#            if not c.isdigit() and c!='.':
#                # 1 row up
#                for i in contents[row-1]:
#                    if i.isdigit():
#
#                contents[row][column].isdigit()
#
