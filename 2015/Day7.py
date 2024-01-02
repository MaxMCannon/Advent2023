#Advent of Code 2015, Day 7
#Maxwell Cannon
#January 1st, 2024

circuit = open('2015/input.txt').read().splitlines()

# for c in circuit:
#     print(c)

cmap = {}

for c in circuit:
    wire = c.split(' ')[-1]
    cmap[wire] = cmap.setdefault(wire, '.')

while cmap['a'] == '.':
    for c in circuit:
        inst = c.split(' -> ')[0]
        outwire = c.split('-> ')[-1]
        dir = inst.split(' ')
        # print(dir)
        if len(dir) == 1 and dir[0].isnumeric():
            cmap[outwire] = int(inst)
        elif len(dir) == 1 and not dir[0].isnumeric():
            cmap[outwire] = cmap[dir[0]]
        elif len(dir) == 2 and cmap[dir[-1]] != '.':
            cmap[outwire] = 65535 - cmap[dir[-1]]
        elif len(dir) == 3 and dir[1] == 'LSHIFT' and cmap[dir[0]] != '.':
            cmap[outwire] = cmap[dir[0]] << int(dir[-1])
        elif len(dir) == 3 and dir[1] == 'RSHIFT' and cmap[dir[0]] != '.':
            cmap[outwire] = cmap[dir[0]] >> int(dir[-1])
        try:
            if len(dir) == 3 and dir[0].isnumeric() and cmap[dir[2]] != '.':
                if dir[1] == 'AND':
                    cmap[outwire] = int(dir[0]) & cmap[dir[2]]
                if dir[1] == 'OR':
                    cmap[outwire] = int(dir[0]) | cmap[dir[2]]
            elif len(dir) == 3 and cmap[dir[0]] != '.' and dir[2].isnumeric():
                if dir[1] == 'AND':
                    cmap[outwire] = cmap[dir[0]] & int(dir[2])
                if dir[1] == 'OR':
                    cmap[outwire] = cmap[dir[0]] | int(dir[2])
            elif len(dir) == 3 and cmap[dir[0]] != '.' and cmap[dir[2]] != '.':
                if dir[1] == 'AND':
                    cmap[outwire] = cmap[dir[0]] & cmap[dir[-1]]
                if dir[1] == 'OR':
                    cmap[outwire] = cmap[dir[0]] | cmap[dir[-1]]
        except:
            pass
    # print(cmap)

print(cmap['a'])
