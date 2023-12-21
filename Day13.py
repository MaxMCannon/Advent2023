#Advent 2023 day 13

lines = open('day13in.txt').read().splitlines()

maps = []

counter = 0
for l in lines:
    if l != '':
        maps.append([])
        maps[counter].append(l)
    else:
        counter += 1

while [] in maps:
    for m in maps:
        if m == []:
            maps.pop()

for m in maps:
    print(m)
    
def pprint(map):
    for l in map:
        print(l)

def Reverse(lst):
   new_lst = lst[::-1]
   return new_lst

def getlen(m1, m2):
    if len(m1) < len(m2):
        return len(m1)
    if len(m2) < len(m1):
        return len(m2)

def rotatemap(map):
    pprint(map)
    rotmap = []
    line = ""
    x = 0
    while x < len(map[0]):
        for y in range(len(map)):
            line += map[y][x]
        rotmap.append(line)
        line = ""
        x += 1
    pprint(rotmap)
    return rotmap


def findhor(map):
    for y in range(1, len(map)):
        # pprint(map[:y])
        # print("-")
        # pprint(map[y:y+y])
        # print()
        if (map[:y] == Reverse(map[y:y+y])):
            # pprint(map[:y])
            return y
    
    counter = 1
    for y in range(len(map)-1, -1, -1):
        # pprint(map[y:])
        # print("-")
        # pprint(map[y-counter:y])
        # print()
        if (map[y:] == Reverse(map[y-counter:y])):
            # pprint(map[y:])
            return y
        
        counter += 1

    return -1




sum = 0
for i in range(len(maps)):
    if findhor(maps[i]) == -1:
        sum += findhor(rotatemap(maps[i]))
    else:
        sum += 100 * findhor(maps[i])

print(sum)  

# print(findhor(maps[1]))
# rotatemap(maps[0])


# for m in maps[1]:
#     print(m)