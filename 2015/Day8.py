#Advent of Code 2015, Day 8
#Maxwell Cannon
#January 2, 2024

lines = open('2015/input.txt').read().splitlines()

clinlines = []

special_characters = "\"!@#$%^&*()-+?_=,<>/\\"

lens = []
chars = []

lens1 = []
lens2 = []

for l in lines:
    lens1.append(len(l))
    print(l)

print() 
def cleanlines(l):
    chars = []
    newchars = []
    for c in l:
        chars.append(c)
    # print(chars)
    newchars.append('\"')
    for i in chars:
        if i in special_characters:
            newchars.append('\\')
            newchars.append(i)
        else:
            newchars.append(i)
    newchars.append('\"')
    outstr = ''
    for c in newchars:
        outstr += c
    # print(outstr)
    return outstr

for i in lines:
    clinlines.append(cleanlines(i))

for l in clinlines:
    lens2.append(len(l))
    print(l)

for l in clinlines:
    count = 0
    i = 1
    while i < len(l)-1:
        if l[i] == '\\' and l[i+1] == 'x':
            print(l[i:i+4])
            count += 1
            i += 4
            continue
        elif l[i] in special_characters:
            print(l[i])
            count += 1
            i += 1
        else:
            count += 1 
        i+=1
    chars.append(count)
    print(count)
    print()

print(lens1)
print(lens2)

# print(sum(lens) - sum(chars))

print('p2 : ' + str(sum(lens2)-sum(lens1)))