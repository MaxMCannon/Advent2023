
lines = open("day3in.txt").read().split()
# print(lines)

def checkaround(i, j):
    return False

# sum = 0

# for line in lines:
#     # print(line)
#     i = 0
#     while i < len(line):
#         print(line[i])
#         tempnum = 0
#         if line[i].isnumeric():
#             j = 0
#             while line[i+j].isnumeric():
#                 # print(line[i+j])
#                 j += 1
#                 # print(j)
#             tempnum = int(line[i:i+j])
#             # if checkaround(i, j):
#             #     sum += tempnum
#             print(tempnum)
#         i += j
#     print()

# print("ans : " + str(sum) + " not done")

# width = len(lines[0])

fullstr = ""

for line in lines:
    fullstr += line

print(fullstr)

k = 0
tempnum = ""
while k < len(fullstr):
    if tempnum == "":
        start = k
    if fullstr[k].isnumeric():
        tempnum += fullstr[k]
    else:
        end = k - 1
        print(tempnum)
        print(start)
        print(end)
        tempnum = ""
    k += 1
    

# print(tempnum)



