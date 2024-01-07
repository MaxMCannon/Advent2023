#Advent of Code 2015, Day 13
#Maxwell Cannon
#January 6th, 2024

import itertools

lines = open('2015/input.txt').read().splitlines()

glist = []
for l in lines: 
    if l.split(' ')[0] not in glist: 
        glist.append(l.split(' ')[0])
# print(glist)

clean_instructions = []
all_haps = []

for l in lines:
    tempdir = []
    tempdir.append(l.split(' ')[0])
    dirtychange = l.split('would ')[1].split(' happiness')[0]
    change = '' 
    if dirtychange.split(' ')[0] == 'gain':
        change += dirtychange.split(' ')[1]
    elif dirtychange.split(' ')[0] == 'lose':
        change += '-' + dirtychange.split(' ')[1]
    tempdir.append(int(change))
    tempdir.append(l.split(' ')[-1].replace('.',''))
    # print(tempdir)
    clean_instructions.append(tempdir)
    
def checkneighbors(ln, p, rn):
    tothappy = 0
    for j in range(len(clean_instructions)):
        if clean_instructions[j][0] == p and (clean_instructions[j][2] == ln or clean_instructions[j][2] == rn):
            tothappy += clean_instructions[j][1]
    return tothappy

def gethappiness(arr):
    happy = []
    # print(arr)
    for i in range(len(arr)):
        happy.append(0)
    for i in range(len(arr)):
        if i == 0:
            happy[i] = (checkneighbors(arr[-1], arr[i], arr[i+1]))
            continue
        elif i == len(arr)-1:
            happy[i] = (checkneighbors(arr[i-1], arr[i], arr[0]))
            continue
        else:
            happy[i] = (checkneighbors(arr[i-1], arr[i], arr[i+1]))
    print(happy)
    print(sum(happy))
    return sum(happy)

    


arrangements = list(itertools.permutations(glist, len(glist)))
for a in arrangements:
    # print(a)
    print(a)
    all_haps.append(gethappiness(list(a)))

print(max(all_haps)) # Untested, Part 1 should be 709


