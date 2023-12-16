#Advent of Code 2023, day 8

lines = open('day8in.txt').read().splitlines()

loop = lines[0]

map = lines[1:]

# print(loop)

# for m in map:
#     print(m)

cleanmap = []

def fixmap(map):
    outarr = []
    key = map.split(" = ")[0]
    rest = map.split(" = ")[1]
    # print(key)
    outarr.append(key)
    L = rest.split(", ")[0]
    L = L.replace("(",'')       #fix this next
    R = rest.split(", ")[1]
    R = R.replace(")",'')
    outarr.append(L)
    outarr.append(R)
    # print(outarr)
    return outarr

for i in range(len(map)):
    if not(map[i] == ''):
        cleanmap.append(fixmap(map[i]))

# print(cleanmap)

def getline(start):
    for i in range(len(cleanmap)):
        if cleanmap[i][0] == start:
            return i
    return 0

startline = getline('AAA')
endline = getline('ZZZ')
currline = startline

steps = 0
i = 0
while currline != endline:
    if i >= len(loop):
        i = 0
    
    if loop[i] == "L":
        currline = getline(cleanmap[currline][1])
    elif loop[i] == "R":
        currline = getline(cleanmap[currline][2])
    steps += 1
    i += 1

print("Answer is : " + str(steps))

    