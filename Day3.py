
lines = open("day3in.txt").read().split()
for line in lines:
    print(line)

def checkaround(i, j):

    return False

# sum = 0

# for line in lines:
#     # print(line)
#     i = 0
#     while i < len(line):
#         print(line[i])
#         tempnum = 0
#         if line[i].isnumeric():
#             j = 0
#             while line[i+j].isnumeric():
#                 # print(line[i+j])
#                 j += 1
#                 # print(j)
#             tempnum = int(line[i:i+j])
#             # if checkaround(i, j):
#             #     sum += tempnum
#             print(tempnum)
#         i += j
#     print()

# print("ans : " + str(sum) + " not done")

# width = len(lines[0])

# fullstr = ""

# for line in lines:
#     fullstr += line

# print(fullstr)

# k = 0
# tempnum = ""
# while k < len(fullstr):
#     if tempnum == "":
#         start = k
#     if fullstr[k].isnumeric():
#         tempnum += fullstr[k]
#     else:
#         end = k - 1
#         print(tempnum)
#         print(start)
#         print(end)
#         tempnum = ""
#     k += 1
    
#look through vals if isnumeric check around (fun), if symbol around, build "word"(fun), convert to int and add.

def checkaround(i, j):
    symb = ["*", "#", "$", "+", "-", "@", "!", "/", "%", "&", "="]
    # print (lines[y][x])
    try:
        if lines[y-1][x] in symb and y > 0: #Up
            return True
    except:
        pass
    try:
        if lines[y+1][x] in symb: #Down
            return True
    except:
        pass
    try:
        if lines[y][x-1] in symb and x > 0: # Left
            return True
    except:
        pass
    try:
       if lines[y][x+1] in symb: #Right
            return True
    except:
        pass
    try:
        if lines[y-1][x-1] in symb and y > 0 and x > 0: #up left
            return True
    except:
        pass
    try:
        if lines[y+1][x-1] in symb and x>0: #down left
            return True
    except:
        pass
    try:
        if lines[y+1][x+1] in symb: #down right
            return True
    except:
        pass
    try:
       if lines[y-1][x+1] in symb and y > 0: #up right
            return True
    except:
        pass
    return False

# partlist = []

# for y in range(len(lines)):
#     added = False
#     tempword = ""
#     for x in range(len(lines[y])):
#         if lines[y][x].isnumeric():
#             tempword += lines[y][x]
#             if not(added):
#                 added = checkaround(x, y)
#                 print(added)
#         elif added:
#             partlist.append(int(tempword))
#             added = False
#             tempword = ""
#         else:
#             tempword = ""
#         if x == 0 and added:
#             continue
#         if x == len(lines[y])-1 and added:
#             try:
#                 partlist.append(int(tempword))
#                 tempword = ""
#             except:
#                 continue
        

# sum = 0
# print(partlist)
# for c in partlist:
#     sum += c

# print(sum)

def buildnum(y, x, pos):
    if pos == "pos1": 
        starty = y - 1
        startx = x - 1
    elif pos == "pos2":
        starty = y - 1
        startx = x
    elif pos == "pos3":
        starty = y - 1
        startx = x + 1
    elif pos == "pos4":
        starty = y
        startx = x - 1
    elif pos == "pos5":
        starty = y
        startx = x + 1
    elif pos == "pos6":
        starty = y + 1
        startx = x - 1
    elif pos == "pos7":
        starty = y + 1
        startx = x
    elif pos == "pos8":
        starty = y + 1
        startx = x + 1

    tempnum = ""
    while lines[starty][startx].isnumeric() and startx > 0 and startx <= len(lines[starty]):
        startx -= 1
    
    i = startx
    while lines[starty][i].isnumeric():
        tempnum += lines[starty][i]
        i += 1
    
    try:
        return int(tempnum)
    except:
        pass  


print(buildnum(1, 3, "pos1"))

poslist = ["pos1", "pos2", "pos3", "pos4", "pos5", "pos6", "pos7", "pos8"]

for y in range(len(lines)):
    for x in range(len(lines[y])):
        if lines[y][x] == "*":
            for pos in poslist:
                print(buildnum(x, y, pos))


# print(tempnum)



