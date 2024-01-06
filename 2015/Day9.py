#Advent of Code 2015, Day 9
#Maxwell Cannon
#January 5th, 2024

import itertools

dists = open('2015/input.txt').read().splitlines()

distarr = []
paths = []
locs = []
pathlen = []

for d in dists:
    distarr.append(d.split(' '))

for d in distarr:
    d.remove('to')
    d.remove('=')
    d[-1] = int(d[-1])

for d in distarr:
    print(d)
    for i in range(len(d)-1):
        if d[i] not in locs:
            locs.append(d[i])
    # paths.append([d[0], d[1]])
    # paths.append([d[1], d[0]])

print(locs)
loccount = len(locs)

paths = list(itertools.permutations(locs, len(locs)))
print(paths)
print()
# for p in paths:
#     while len(p) < loccount:
#         for d in distarr:
#             if d[0] == p[-1] and d[1]:
#                 p.append(d[1])
#                 if len(p) == loccount:
#                     break
#             elif d[1] == p[-1] and d[0]:
#                 p.append(d[0])
#                 if len(p) == loccount:
#                     break
    # print(p)

for i in range(len(paths)):
    plen = 0
    for k in range(len(paths[i])-1):
        for d in distarr:
            if paths[i][k] in d and paths[i][k+1] in d:
                plen += d[-1]
    pathlen.append(plen)

print(pathlen)

lowest = pathlen[0]
highest = 1

for p in pathlen:
    if p < lowest:
        lowest = p

print(len(paths))
print(lowest)

for p in pathlen:
    if p > highest:
        highest = p

print(highest)
