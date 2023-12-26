#Advent 2023, Day 15

# Determine the ASCII code for the current character of the string.
# Increase the current value by the ASCII code you just determined.
# Set the current value to itself multiplied by 17.
# Set the current value to the remainder of dividing itself by 256.

lines = open('day15in.txt').read().splitlines()

codes = ''

for l in lines:
    codes += l + ','

print(codes)

totalval = 0
currval = 0

for c in codes:
    if c == ',':
        totalval += currval
        currval = 0
        continue
    else:
        currval += ord(c)
    # print(currval)
    
    currval = currval * 17

    # print(currval)
    currval = currval % 256

print(totalval)