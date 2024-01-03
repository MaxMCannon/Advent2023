#Advent of Code 2015, Day 8
#Maxwell Cannon
#January 2, 2024

lines = open('2015/input.txt').read().splitlines()

lens = []
chars = []

for l in lines:
    lens.append(len(l))
    print(l)

for l in lines:
    count = 0
    i = 1
    while i < len(l)-1:
        if l[i] == '\\' and l[i+1] == 'x':
            print(l[i:i+4])
            count += 1
            i += 4
            continue
        elif l[i] == "\\":
            print(l[i])
            count += 1
            i += 1
        else:
            count += 1 
        i+=1
    chars.append(count)
    print(count)
    print()

print(lens)
print(chars)

print(sum(lens) - sum(chars))