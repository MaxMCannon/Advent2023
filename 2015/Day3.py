#Advent of Code 2015, Day 3
#Maxwell Cannon
#Dec 26, 2023 
import copy

input = open('2015/input.txt').read()

poslist = ['0, 0'] #y, x
poslist2 = ['0, 0'] #y, x


# for c in input:
#     currpos = poslist[-1]
#     print(currpos)
#     y = int(currpos.split(', ')[0])
#     x = int(currpos.split(', ')[1])
#     print(y)
#     print(x)
#     if c == '^':
#         y -= 1
#     elif c == 'v':
#         y += 1
#     elif c == '>':
#         x += 1
#     elif c == '<':
#         x -= 1
#     print(y)
#     print(x)
#     out = str(y)+', '+str(x)
#     poslist.append(out)

# print(len(set(poslist)))

def move(c, ps):
    currpos = ps[-1]
    print(currpos)
    y = int(currpos.split(', ')[0])
    x = int(currpos.split(', ')[1])
    if c == '^':
        y -= 1
    elif c == 'v':
        y += 1
    elif c == '>':
        x += 1
    elif c == '<':
        x -= 1

    out = str(y)+', '+str(x)
    if ps == poslist:
        poslist.append(out)
    else:
        poslist2.append(out)

for i in range(0, len(input), 2):
    move(input[i], poslist)

for j in range(1, len(input)-1, 2):
    move(input[j], poslist2)

finallist = poslist + poslist2

print(len(set(finallist)))

