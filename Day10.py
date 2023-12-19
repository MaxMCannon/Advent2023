#Advent 2023, Day 10

lines = open('day10in.txt').read().splitlines()

for l in lines:
    print(l)
 


def findstart():
    for y in range(len(lines)):
        for x in range(len(lines[y])):
            if lines[y][x] == "S":
                return [x, y]

startpos = findstart() ### x, y            
print(startpos)
currpos = startpos
dir = 0 ## 0-up 1-right 2-down 3-left

# | is a vertical pipe connecting north and south.
# - is a horizontal pipe connecting east and west.
# L is a 90-degree bend connecting north and east.
# J is a 90-degree bend connecting north and west.
# 7 is a 90-degree bend connecting south and west.
# F is a 90-degree bend connecting south and east.

def changedir(dir, sym):
    if dir == 0 and sym == "|":
        return 0
    elif dir == 0 and sym == "7":
        return 3
    elif dir == 0 and sym == "F":
        return 1
    #########
    if dir == 1 and sym == "-":
        return 1
    elif dir == 1 and sym == "J":
        return 0
    elif dir == 1 and sym == "7":
        return 2
    #########
    if dir == 2 and sym == "|":
        return 2
    if dir == 2 and sym == "L":
        return 1
    if dir == 2 and sym == "J":
        return 3
    #########
    if dir == 3 and sym == "-":
        return 3
    if dir == 3 and sym == "L":
        return 0
    if dir == 3 and sym == "F":
        return 2
    return 0

def movedir(dir):
    if dir == 0:
        currpos[1] -= 1
    if dir == 1:
        currpos[0] += 1
    if dir == 2:
        currpos[1] += 1
    if dir == 3:
        currpos[0] -= 1
    return 0
for y in range(len(lines)):
    for x in range(len(lines[y])):
        break
    break

