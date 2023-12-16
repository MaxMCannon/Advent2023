#Advent 2023 Day 11

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
    

def pt1main():
    return False

expandgals()


for l in space:
    print(l)