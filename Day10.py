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

def checkdir(dir, pos):
    

for y in range(len(lines)):
    for x in range(len(lines[y])):
        

