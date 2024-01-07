#Advent of Code 2015, Day 12,
#Maxwell Cannon
#January 6, 2024

line = open('2015/input.txt').read()

print(line)

allnums = []

tempnum = ''
start = False
for i in range(len(line)):
    if line[i] == '-' or line[i].isdigit(): 
        tempnum += line[i]
    else:
        if tempnum != '':
            allnums.append(int(tempnum))
            tempnum = ''
    
print(allnums)
print('Part 1 ans : ' + str(sum(allnums))) # Untested answer should be : 191164