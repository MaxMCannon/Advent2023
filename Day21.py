#Advent 2023, Day 21

#example is 6 more steps
#problem is 64 more steps

map = open('day21in.txt').read().splitlines()

steps = 64

def printmap():
    for m in map:
        print(m)

def getstartpos():
    for y in range(len(map)):
        for x in range(len(map)):
            if map[y][x] == 'S':
                return [y, x]

def getOs():
    Os = []
    for y in range(len(map)):
        for x in range(len(map)):
            if map[y][x] == 'O':
                Os.append([y, x])
    return Os

def addO(y, x):
    map[y] = map[y][:x] + 'O' + map[y][x+1:]

def rmO(y, x):
    map[y] = map[y][:x] + '.' + map[y][x+1:]

def updatearoundpoint(y, x):
    if y != 0:
        if map[y-1][x] == '.' or map[y-1][x] == 'O':
            addO(y-1, x)
            rmO(y, x)
    if y != len(map) - 1:
        if map[y+1][x] == '.' or map[y+1][x] == 'O':
            addO(y+1, x)
            rmO(y, x)
    if x != 0:
        if map[y][x-1] == '.' or map[y][x-1] == 'O':
            addO(y, x-1)
            rmO(y, x)
    if x != len(map[y])-1:
        if map[y][x+1] == '.' or map[y][x+1] == 'O':
            addO(y, x+1)
            rmO(y, x)

startpos = getstartpos()
printmap()
updatearoundpoint(startpos[0], startpos[1])
print()
printmap()
for step in range(steps-1):
    Os = getOs()
    for O in Os:
        updatearoundpoint(O[0],O[1])
    printmap()
    print()

print(len(getOs()))