#Advent of Code 2023, Day 9

lines = open('day9in.txt').read().splitlines()

inarr = []

def tonums(nums):
    arr = []
    for i in nums:
        arr.append(int(i))
    return arr
    

for l in lines:
    inarr.append(tonums(l.split()))

print(inarr)

def checkzero(hist):
    out = True
    for i in hist:
        if i > 0 or i < 0:
            out = False
    return out

def predictone(hist):
    pyramid = []
    pyramid.append(hist)
    start = hist
    temparr = []
    print(start)
    while not(checkzero(start)):
        for i in range(len(start)-1):
            temparr.append(start[i+1]-start[i])
        pyramid.append(temparr)
        start = temparr
        temparr = []
        # print(start)
    
    for k in range(len(pyramid)-1, -1, -1):
        if checkzero(pyramid[k]):
            pyramid[k].append(0)
        else:
            pyramid[k-1].append(pyramid[k-1][-1]+pyramid[k][-1])
        print(pyramid[k])
    # for l in pyramid:
    #     print(l)
    
    return pyramid[0][-1]

#Part 1
# ans = 0
# for l in inarr:
#     ans += predictone(l)
# print(ans)

def predicttwo(hist):
    pyramid = []
    pyramid.append(hist)
    start = hist
    temparr = []
    # print()
    while not(checkzero(start)):
        for i in range(len(start)-1):
            temparr.append(start[i+1]-start[i])
        pyramid.append(temparr)
        start = temparr
        temparr = []
        # print(start)
    # for l in pyramid:
    #     print(l)
    ascending = True
    if pyramid[0][-1] < pyramid[0][0]:
        ascending = False

    if ascending:
        for k in range(len(pyramid)-1, -1, -1):
            if checkzero(pyramid[k]):
                pyramid[k].insert(0, 0)
            else:
                pyramid[k-1].insert(0, (pyramid[k-1][0] - pyramid[k][0]))
    else:
        for k in range(len(pyramid)-1, -1, -1):
            if checkzero(pyramid[k]):
                pyramid[k].insert(0, 0)
            else:
                pyramid[k-1].insert(0, (pyramid[k-1][0] + (-1 * pyramid[k][0])))

    # for k in range(len(pyramid)-1, -1, -1):
    #     if checkzero(pyramid[k]):
    #         pyramid[k].insert(0, 0)
    #     else:
    #         pyramid[k-1].insert(0, (pyramid[k+1][0] - pyramid[k][0]))
    #     print(pyramid[k])
    for l in pyramid:
        print(l)
    print(pyramid[0][0])
    return pyramid[0][0]


#Part 2
ans = 0
for l in inarr:
    # print(predicttwo(l))
    ans += predicttwo(l)
print(ans)