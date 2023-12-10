#Advent of Code 2023, day 8

lines = open('day8in.txt').read().splitlines()

loop = lines[0]

map = lines[1:]

print(loop)

for m in map:
    print(m)

cleanmap = []

def fixmap(map):
    outarr = []
    key = map.split(" = ")[0]
    rest = map.split(" = ")[1]
    print(key)
    outarr.append(key)
    L = rest.split(", ")[0]
    L = L.remove("(")       #fix this next
    R = rest.split(", ")[1]
    R = R.remove(")")
    outarr.append(L)
    outarr.append(R)
    print(outarr)
    return outarr

for i in range(len(map)):
    if not(map[i] == ''):
        fixmap(map[i])    

print(cleanmap)