# Advent of Code 2023 Day 2
# Max Cannon

lines = open("day2in.txt").read().splitlines()

# for line in lines:
#     print(line) 

#checked
def getgamenum(line):
    temp = line.split(":")
    return int(temp[0].split()[1])
    
def checkgame(line):
    print(line)
    redmax = 12
    greenmax = 13
    bluemax = 14
    game = line.split(":")[1].split(";")
    for g in game:
        counts = g.split(",")
        # print(counts)
        for i in range(len(counts)):
            tempnum = int(counts[i].split(" ")[1])
            tempcol = counts[i].split(" ")[-1]
            # print(tempnum)
            # print(tempcol)
            if tempcol == "red" and tempnum > redmax:
                print("fail")
                return 0
                return getgamenum(line)
            elif tempcol == "green" and tempnum > greenmax:
                print("fail")
                return 0
                return getgamenum(line)
            elif tempcol == "blue" and tempnum > bluemax:
                print("fail")
                return 0
                return getgamenum(line)
    return getgamenum(line)
            
    # print(game)

# sum = 0
# for line in lines:
#     print(checkgame(line))
#     sum += checkgame(line)
# print(sum)


def checkgame2(line):
    print(line)
    redmax = 0
    greenmax = 0
    bluemax = 0
    game = line.split(":")[1].split(";")
    for g in game:
        counts = g.split(",")
        # print(counts)
        for i in range(len(counts)):
            tempnum = int(counts[i].split(" ")[1])
            tempcol = counts[i].split(" ")[-1]
            # print(tempnum)
            # print(tempcol)
            if tempcol == "red" and tempnum > redmax:
                redmax = tempnum
            elif tempcol == "green" and tempnum > greenmax:
                greenmax = tempnum
            elif tempcol == "blue" and tempnum > bluemax:
                bluemax = tempnum
    print(redmax)
    print(greenmax)
    print(bluemax)
    return redmax*greenmax*bluemax
    return getgamenum(line)

sum2 = 0
for line in lines:
    sum2 += checkgame2(line)

print(sum2)
