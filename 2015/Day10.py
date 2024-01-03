#Advent 2015, Day 10
#Maxwell Cannon
#January 2, 2024

puzz = open('2015/input.txt').read()

outarr = [puzz]

print(puzz)

nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

run = 0

while run < 5:
    count = 0
    tempnum = ''
    currnum = ''
    switch = True
    st = outarr[-1]
    for i in range(1, len(outarr[-1])):
        print(outarr[-1])
        currnum = st[i-1]
        print(currnum)
        if st[i] == st[i-1]:
            count += 1
        else:
            tempnum = str(count) + currnum
    outarr.append(tempnum)


    run += 1

print(outarr)