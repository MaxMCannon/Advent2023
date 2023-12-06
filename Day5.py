#Advent of Code day 5

import math

input = open("day5in.txt").read().splitlines()

maps = input[2:] 

# line structure : destination, source, len notes
# diff = num - source 
# if diff < len: destination + diff

# 79 to 81 to 81 to 81 to 74 to 78 to 78 to 82
# 14 to 14 to 53 to 49 to 42 to 42 to 43 to 43

# for m in maps:
#     print(m)

def tonums(nums):
    arr = []
    for i in nums:
        arr.append(int(i))
    return arr
    

seeds = tonums(input[0].split(": ")[1].split(' '))
print("seeds = " + str(seeds))

def checkline(seed, map):
    deststart = map[0]
    sourcestart = map[1]
    length = map[2]
    diff = math.fabs(seed - sourcestart)    
    if diff < length:
        return(int(deststart + diff))
    else:
        return seed



def convertseed(seed):
    tempseed = seed
    arr = [tempseed]
    for m in maps:
        if m == "":
            arr.append(tempseed)
            continue
        if not(m[0].isnumeric()):
            continue
        nums = tonums(m.split(" "))
        # print(nums)
        tempseed = checkline(tempseed, nums)        
    return arr

print("path = " + str(convertseed(14)))
      
# for s in seeds:
#     print(convertseed(seeds))


