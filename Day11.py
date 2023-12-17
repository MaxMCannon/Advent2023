#Advent 2023 Day 11
import math as m

lines = open('day11in.txt').read().splitlines()
space = lines

def checkcol(x):
    colcheck = ''
    
    y = 0
    while y < len(space):
        colcheck += space[y][x]
        y+=1
    if len(set(colcheck)) == 1:
        return True
    return False

def insertcol(x):
    y = 0
    while y < len(space):
        # print(space[y])
        space[y] = space[y][:x] + '.' + space[y][x:]
        y+=1

def expandgals():
    y = 0
    while y < len(space):
        emptrow = "." * len(space[y])
        if len(set(space[y])) == 1:
            space.insert(y+1, emptrow)
            y += 2
        y+=1 
    x = 0
    while x < len(space[0]):
        if checkcol(x):
            insertcol(x)
            x+=1
        x += 1
    
expandgals()
for l in space:
    print(l)

def getgals():
    outarr = []
    for y in range(len(space)):
        for x in range(len(space[y])):
            if space[y][x] == "#":
                outarr.append([x, y])
    print(outarr)
    return outarr

gals = getgals()

def measuredist(p1, p2):
    dist = m.fabs(p2[0]-p1[0]) + m.fabs(p2[1]-p1[1])
    print(int(dist))
    return int(dist)


totalsum = 0
for i in range(len(gals)):
    for j in range(i+1, len(gals)):
        totalsum += measuredist(gals[i], gals[j])
print(totalsum)
    