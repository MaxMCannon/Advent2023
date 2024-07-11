#Advent of Code 2024, Day 17
#Maxwell Cannon
#July 11, 2024
from itertools import combinations 

containers = [int(i) for i in open("2015/input.txt").read().splitlines()]
print(containers)

comb = []
numcontainers = []
count = 0
for i in range(len(containers)):
    temp = combinations(containers, i)
    for t in list(temp):
        if sum(t) == 150:
            # print(len(t))
            numcontainers.append(len(t))
            count+=1

    temp = []

print(min(numcontainers))
print(numcontainers.count(min(numcontainers)))
print(count)