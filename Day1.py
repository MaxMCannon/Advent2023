# Advent of Code 2023, Day 1 
# Max Cannon
# 12/1/2023

list = open("day1in.txt").read().split()

#Part 1 helper function
def getCal(line):
    numArr = []
    for k in range(len(line)):
       temp = 0
       try:
           temp = int(line[k])
           numArr.append(temp)
           temp = 0
       except:
           continue
    # print(numArr)
    return numArr[0]*10 + numArr[-1]

#Part 2 helper function
def readLeftTextNums(line):
    numArr = []
    for i in range(len(line)):
        temp = 0
        try:
            temp = int(line[i])
            numArr.append(temp)
            temp = 0
        except:
            if line[i:i+3] == "one":
                numArr.append(1)
            if line[i:i+3] == "two":
                numArr.append(2)
            if line[i:i+5] == "three":
                numArr.append(3)
            if line[i:i+4] == "four":
                numArr.append(4)
            if line[i:i+4] == "five":
                numArr.append(5)
            if line[i:i+3] == "six":
                numArr.append(6)
            if line[i:i+5] == "seven":
                numArr.append(7)    
            if line[i:i+5] == "eight":
                numArr.append(8)
            if line[i:i+4] == "nine":
                numArr.append(9)

    # print(numArr)
    return numArr[0]*10 + numArr[-1]

#Part 1 code Starts----------------------------------------------
sum = 0

for line in list:
    # print(getCal(line))
    sum += getCal(line)

print("Part One: " + str(sum))
#Part 2 code Ends------------------------------------------------

#Part 2 code Starts----------------------------------------------
sumP2 = 0

for line in list:
    # print(readLeftTextNums(line))
    sumP2 += readLeftTextNums(line)

print("Part Two: " + str(sumP2))
#Part 2 code Ends------------------------------------------------ 