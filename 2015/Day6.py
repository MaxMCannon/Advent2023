#Advent of Code 2015, Day 6
#Maxwell Cannon
#December 30, 2023

directions = open('2015/input.txt').read().splitlines()
map = []

for i in range(1000):
    line = []
    for x in range(1000):
        line.append(0)
    map.append(line)

def on(x1, y1, x2, y2):
    for y in range(y1, y2+1):
        for x in range(x1, x2+1):
            # map[y][x] = 1
            map[y][x] += 1

def off(x1, y1, x2, y2):
    for y in range(y1, y2+1):
        for x in range(x1, x2+1):
            if map[y][x] > 0:
                # map[y][x] = 0
                map[y][x] -= 1

def toggle(x1, y1, x2, y2):
    for y in range(y1, y2+1):
        for x in range(x1, x2+1):
            # if map[y][x] == 0:
            #     map[y][x] = 1
            # elif map[y][x] == 1:
            #     map[y][x] = 0
            map[y][x] += 2
for d in directions:
    print(d)

print()

def countlights():
    count = 0
    for y in range(len(map)):
        for x in range(len(map[y])):
            count += map[y][x]
    return count

for d in directions:
    act = d.split(' ')[0]
    if act == 'turn':
        act = d.split(' ')[1]
    startpos = ''
    for i in range(len(d)):
        if d[i].isnumeric():
            startpos += d[i]
        if d[i] == ',':
            startpos += ','
        if d[i:i+7] == 'through':
            startpos += ','
    lightarr = startpos.split(',')
    for i in range(len(lightarr)):
        lightarr[i] = int(lightarr[i])
    # print(act)
    # print(lightarr)
    
    if act == 'on':
        on(lightarr[0],lightarr[1], lightarr[2], lightarr[3])
    if act == 'off':
        off(lightarr[0],lightarr[1], lightarr[2], lightarr[3])
    if act == 'toggle':
        toggle(lightarr[0],lightarr[1], lightarr[2], lightarr[3])

    
print(countlights())