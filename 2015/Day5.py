#Advent of Code 2015, Day 5
#Maxwell Cannon
#December 30, 2023

strings = open('2015/input.txt').read().splitlines()

# for s in strings:
#     print(s)

bads = ['ab', 'cd', 'pq', 'xy']
vowels = ['a', 'e', 'i', 'u', 'o']

def checkvowels(s):
    outmap = {}
    sum = 0
    for c in s:
        outmap[c] = outmap.setdefault(c, 0) + 1
    for v in vowels:
        if v in outmap.keys():
            sum += outmap.get(v)
    if sum >= 3:
        return True
    return False

def checkdups(s):
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            return True
    return False

def checkbads(s):
    for i in range(len(s)-1):
        if s[i:i+2] in bads:
            # print(s[i:i+2])
            return False
    return True

def doubles(s):
    for i in range(len(s)-1):
        for j in range(i+2, len(s)-1):
            if s[i:i+2] == s[j:j+2]:
                print(s[i:i+2])
                return True
    return False

def splitcheck(s):
    for i in range(len(s)-2):
        if s[i] == s[i+2]:
            print(s[i:i+3])
            return True
    return False

# print(splitcheck(strings[0]))

count = 0
for s in strings:
    #part1
    # if checkvowels(s) and checkbads(s) and checkdups(s):
    #     print(s)
    #     count += 1
    #Part 2
    if doubles(s) and splitcheck(s):
        print(s)
        count += 1
    
print(count)

