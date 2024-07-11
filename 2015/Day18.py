#Advent of Code 2024, Day 18
#Maxwell Cannon
#July 11, 2024
import copy

lights = open('2015/input.txt').read().splitlines()

def pprint(map):
    for m in map:
        print(m)

def addborder(map):
    outmap = []
    outmap.append('.'+'.'*len(map[0])+'.')
    for i in range(len(map)):
        outmap.append('.'+map[i]+'.')
    outmap.append('.'+'.'*len(map[-1])+'.')
    pprint(outmap) 
    return outmap

lights = addborder(lights)
tempmap = copy.deepcopy(lights)

def countaround(y, x):
    counts = 0
    # print(lights[y][x])
    if lights[y][x] == '#':
        counts -= 1
        for i in range(y-1, y+2):
            for j in range(x-1, x+2):
                if lights[i][j] == '#':
                    counts += 1
    else:
        for i in range(y-1, y+2):
            for j in range(x-1, x+2):
                if lights[i][j] == '#':
                    counts += 1

    # print(counts)
    return counts

def update():
    for i in range(1, len(lights)-1):
        for j in range(1, len(lights[i])-1):
            countout = countaround(i, j)
            if (i == 1 and j == 1) or (i == 1 and j == len(lights)-2) or (i == len(lights)-2 and j == len(lights)-2) or (i == len(lights)-2 and j == 1):
                tempmap[i] = tempmap[i][:j] + '#' + tempmap[i][j+1:]
            if lights[i][j] == '#' and (countout == 2 or countout == 3):
                tempmap[i] = tempmap[i][:j] + '#' + tempmap[i][j+1:]
            elif lights[i][j] == '#':
                tempmap[i] = tempmap[i][:j] + '.' + tempmap[i][j+1:]
            
            if lights[i][j] == '.' and (countout == 3):
                tempmap[i] = tempmap[i][:j] + '#' + tempmap[i][j+1:]
            elif lights[i][j] == '.':
                tempmap[i] = tempmap[i][:j] + '.' + tempmap[i][j+1:]
            
            if (i == 1 and j == 1) or (i == 1 and j == len(lights)-2) or (i == len(lights)-2 and j == len(lights)-2) or (i == len(lights)-2 and j == 1):
                tempmap[i] = tempmap[i][:j] + '#' + tempmap[i][j+1:]
            
steps = 0
while steps < 100:
    update()
    pprint(tempmap)
    lights = copy.deepcopy(tempmap)
    print()
    steps += 1


finalcount = 0
for i in range(1, len(lights)-1):
    for j in range(1, len(lights[i])-1):
        if lights[i][j] == '#':
            finalcount += 1

print(finalcount)