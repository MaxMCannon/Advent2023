#Advent of Code 2015, Day 2 
#Maxwell Cannon
#Dec 26, 2023

dims = open('2015/input.txt').read().splitlines()

sum = 0

def getSA(l, w, h):
    return ((2*l*w) + (2*w*h) + (2*h*l))

def getArea(l, w, h):
    return l*w*h

def getsmall(l, w, h):
    sides = [l*w, w*h, h*l]
    sides.sort()
    return(sides[0])

def getRib(l, w, h):
    edges = [l, w, h]
    edges.sort()
    return(2*edges[0] + 2*edges[1])

for d in dims:
    l = int(d.split('x')[0])
    w = int(d.split('x')[1])
    h = int(d.split('x')[2])
    sum += getSA(l, w, h) + getsmall(l, w, h)

print("Part 1 :" + str(sum))

p2sum = 0
for d in dims:
    l = int(d.split('x')[0])
    w = int(d.split('x')[1])
    h = int(d.split('x')[2])
    p2sum += getArea(l, w, h) + getRib(l, w, h)

print(p2sum)