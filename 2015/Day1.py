#Advent of Code 2015, Day 1
# Written by : Maxwell Cannon
# Dec 26, 2023

input = open('2015/input.txt').read()

#Part 1
tracker = 0
for i in input:
    if i == '(':
        tracker += 1
    else:
        tracker -=1

print(tracker)

#Part 2
floor = 0
for l in range(len(input)):
    if input[l] == '(':
        floor += 1
    else:
        floor -= 1
    
    if floor == -1:
        print(l+1)
        break