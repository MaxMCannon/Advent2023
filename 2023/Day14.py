#Advent 2023 Day 14

lines = open('day14in.txt').read().splitlines()
for l in lines:
    print(l)

copy = lines

def movenorth():
    for y in range(1, len(lines)):
        for x in range(len(lines[y])):
            if lines[y][x] == "O":
                if lines[y-1][x] == '.':
                    lines[y] = lines[y][:x] + "." + lines[y][x+1:]
                    lines[y-1] = lines[y-1][:x] + "O" + lines[y-1][x+1:]
                else:
                    continue

def movewest():
    for y in range(0, len(lines)):
        for x in range(1, len(lines[y])):
            if lines[y][x] == "O":
                if lines[y][x-1] == '.':
                    lines[y] = lines[y][:x] + "." + lines[y][x+1:]
                    lines[y] = lines[y][:x-1] + "O" + lines[y][x:]
                else:
                    continue

def movesouth():
    for y in range(len(lines)-2, -1, -1):
        for x in range(len(lines[y])):
            if lines[y][x] == "O":
                if lines[y+1][x] == '.':
                    lines[y] = lines[y][:x] + "." + lines[y][x+1:]
                    lines[y+1] = lines[y+1][:x] + "O" + lines[y+1][x+1:]
                else:
                    continue

def moveeast():
    for y in range(0, len(lines)):
        for x in range(len(lines[y])-2, -1, -1):
            # print(x)
            if lines[y][x] == "O":
                if lines[y][x+1] == '.':
                    lines[y] = lines[y][:x] + "." + "O" + lines[y][x+2:]
                else:
                    continue

def countohs(line):
    count = 0
    for c in line:
        if c == "O":
            count += 1
    return count


for i in range(2):
    print("cycle : " + str(i))
    for x in range(len(lines)):
        movenorth()
    for x in range(len(lines)):
        movewest()
    for x in range(len(lines)):
        movesouth()
    for x in range(len(lines)):
        moveeast()
    if i > 1 and lines == copy:
        print("loop length")
        print(1000000000 % i)       # Have to figure out the loop size here, going through 1B iterations is days of processing
        break

for l in lines:
    print(l)

mult = len(lines)
# print(mult)
load = 0
for l in lines:
    load += mult * countohs(l)
    mult -= 1
print(load)

