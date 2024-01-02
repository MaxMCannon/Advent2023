#Advent of Code 2015, Day 7
#Maxwell Cannon
#January 1st, 2024

circuit = open('2015/input.txt').read().splitlines()

for c in circuit:
    print(c)

def getbit(num):
    return bin(num)

def getnum(bi):
    return int(bi, 2)

def customnot(num):
    pass

cmap = {}


for c in circuit:
    wire = c.split(' ')[-1]
    print(wire)
    cmap[wire] = cmap.setdefault(wire, 0)

print(cmap)

for c in circuit:
    inst = c.split(' -> ')[0]
    outwire = c.split('-> ')[-1]
    if inst.isnumeric():
        cmap[outwire] = cmap[outwire] + int(inst)
    else:
        dir = inst.split(' ')
        if len(dir) == 2:
            if dir[0] == 'NOT':
                cmap[outwire] = getnum(getbit(255) - getbit(int(dir[-1])))
        else:
            if dir[1] == 'AND':
                cmap[outwire] = cmap[dir[0]] & cmap[dir[-1]]
            if dir[1] == 'OR':
                cmap[outwire] = cmap[dir[0]] | cmap[dir[-1]]
            if dir[1] == 'LSHIFT':
                cmap[outwire] = cmap[dir[0]] << int(dir[-1])
            if dir[1] == 'RSHIFT':
                cmap[outwire] = cmap[dir[0]] >> int(dir[-1])
print(cmap)


# print(getbit(4))
# print(getnum(getbit(4)))