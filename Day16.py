#Advent 2023, Day 16

map = open('day16in.txt').read().splitlines()

for m in map:
    print(m)

# Template of lights - [xpos, ypos, dir] Dir map [0 - up, 1 - right, 2 - down, 3 - left]
lights = [[0, 0, 1]]

def looknext(light):
    xpos = light[0]
    ypos = light[1]
    dir = light[2]
    if dir == 0:
        return map[ypos-1][xpos]
    elif dir == 1:
        return map[ypos][xpos+1]
    elif dir == 2:
        return map[ypos+1][xpos]
    elif dir == 3:
        return map[ypos][xpos-1]

def splitter(light):
    xpos = light[0]
    ypos = light[1]
    dir = light[2]
    if dir == 0:
        lights.append([xpos-1, ypos, 3])
        lights.append([xpos+1, ypos, 1])
    if dir == 1:
        lights.append([xpos, ypos-1, 0])
        lights.append([xpos, ypos+1, 2])
    if dir == 2:
        lights.append([xpos+1, ypos, 3])
        lights.append([xpos-1, ypos, 1])
    if dir == 3:
        lights.append([xpos, ypos+1, 0])
        lights.append([xpos, ypos-1, 2])


def checkrange(light):
    for i in light:
        if i < 0 or i > len(map):
            return False
    return True

def fixlights():
    for l in lights:
        if not checkrange(l):
            lights.remove(l)


print(lights)
splitter(lights[0])
print(lights)
fixlights()
print(lights)