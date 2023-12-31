#Advent of Code 2015, Day 4
#Max Cannon
#December 30, 2023
import hashlib

input = open('2015/input.txt').read()
print(input)


print(hashlib.md5(input.encode('utf-8')).hexdigest())

hashval = hashlib.md5(input.encode('utf-8')).hexdigest()

counter = 1500000

temp = ''

while hashval[0:6] != '000000':
    temp = input + str(counter)
    hashval = hashlib.md5(temp.encode('utf-8')).hexdigest()
    print(counter)
    counter += 1


print(temp)
print(counter-1)
    