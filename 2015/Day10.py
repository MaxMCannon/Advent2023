#Advent 2015, Day 10
#Maxwell Cannon
#January 2, 2024
import copy

puzz = open('2015/input.txt').read()

outarr = [puzz]

run = 0

def createarr(line):
    outarr = []
    for c in line:
        outarr.append(c)
    return outarr

# while run < 5:
#     newnum = ''
#     curnum = str(copy.deepcopy(outarr[-1]))
#     print(curnum)
#     curdig = curnum[0]
#     count = 0
#     for i in range(len(curnum)):
#         if curnum[i] == curdig:
#             count += 1
#         if curnum[i] != curdig:
#             newnum += str(count)
#             newnum += curdig
#             curdig = curnum[i]
#             count = 1
#     print(newnum)
#     outarr.append(newnum)
#     run += 1

def step(num):
    outnum = ''
    count = 1
    char = 0
    while char < len(num)-1:
        if num[char] == num[char+1]:
            count += 1
            char += 1
        else:
            outnum += (str(count) + num[char])
            count = 1
            char += 1
            
    # print(outnum)
    return outnum

print(step(puzz))

print(outarr)