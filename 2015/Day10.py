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
    count = 0
    cur = num[0]
    if len(num) == 1:
        return ('1' + str(num)) + 'x'
    else:
        for i in range(len(num)):
            n = num[i]
            if i == len(num):
                if n == cur:
                    outnum = outnum + str(count)
                    outnum = outnum + n
                else:
                    outnum = outnum + '1'
                    outnum = outnum + n
                return outnum + 'x'
            if n == cur:
                count += 1
            else:
                outnum = outnum + str(count)
                outnum = outnum + cur
                cur = n
                count = 1
        # print(outnum)
        return outnum + 'x'

run = 0
while run < 50:
    # print(outarr[-1])
    outarr.append(step(outarr[-1]))
    run += 1

# print(outarr)
print(len(outarr[-1])-1)