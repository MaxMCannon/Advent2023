#Advent of Code 2024, Day 16
#Maxwell Cannon
#July 10, 2024

suelines = open('2015/input.txt').read().splitlines()

# children: 3
# cats: 7
# samoyeds: 2
# pomeranians: 3
# akitas: 0
# vizslas: 0
# goldfish: 5
# trees: 3
# cars: 2
# perfumes: 1

thesue = [3,7,2,3,0,0,5,3,2,1]
sues = []

def getsue(suesplit):
    sueline = [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]
    for detect in suesplit:
        if detect.split(": ")[0] == "children":
            sueline[0] = int(detect.split(": ")[1])
        if detect.split(": ")[0] == "cats":
            sueline[1] = int(detect.split(": ")[1])
        if detect.split(": ")[0] == "samoyeds":
            sueline[2] = int(detect.split(": ")[1])
        if detect.split(": ")[0] == "pomeranians":
            sueline[3] = int(detect.split(": ")[1])
        if detect.split(": ")[0] == "akitas":
            sueline[4] = int(detect.split(": ")[1])
        if detect.split(": ")[0] == "vizslas":
            sueline[5] = int(detect.split(": ")[1])
        if detect.split(": ")[0] == "goldfish":
            sueline[6] = int(detect.split(": ")[1])
        if detect.split(": ")[0] == "trees":
            sueline[7] = int(detect.split(": ")[1])
        if detect.split(": ")[0] == "cars":
            sueline[8] = int(detect.split(": ")[1])
        if detect.split(": ")[0] == "perfumes":
            sueline[9] = int(detect.split(": ")[1])
    print(sueline)
    return sueline


for s in suelines:
    s = s.lstrip("Sue1234567890: ")
    # print(s)
    suesplit = s.split(", ")
    sues.append(getsue(suesplit))

for i in range(len(sues)):
    # Part 1
    # match = [False,False,False,False,False,False,False,False,False,False]
    # for j in range(len(thesue)):
    #     if sues[i][j] == thesue[j]:
    #         match[j] = True
    #     elif sues[i][j] == -1: 
    #         match[j] = True
    # if False not in match:
    #     print(i+1)
    #     break
    # print(match)

    #Part 2
    match = [False,False,False,False,False,False,False,False,False,False]
    for j in range(len(thesue)):
        if j == 1 or j == 7:
            if sues[i][j] > thesue[j]:
                match[j] = True
            elif sues[i][j] == -1: 
                match[j] = True
        elif j == 3 or j == 6:
            if sues[i][j] < thesue[j]:
                match[j] = True
            elif sues[i][j] == -1: 
                match[j] = True
        else:
            if sues[i][j] == thesue[j]:
                match[j] = True
            elif sues[i][j] == -1: 
                match[j] = True
    if False not in match:
        print(i+1)
        break
    print(match)