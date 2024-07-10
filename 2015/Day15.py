#Advent of Code 2024, Day 15
#Maxwell Cannon
#July 8, 2024

lines = open("2015/input.txt").read().splitlines()

ingredients = []
portions = []

temp = []
for l in lines:
    temp.append(l.split(": ")[0])
    for i in range(5):
        temp.append(int(l.split(', ')[i].split(' ')[-1]))
    ingredients.append(temp)
    temp = []

# Name, capacity, durability, flavor, texture, calories
for i in ingredients:
    print(i)

def parsein(s):
    out = s.split(',')
    for i in range(len(out)):
        out[i] = int(out[i])
    if sum(out) != 100:
        print("ERROR - not max")
    return out

def calculatescore(portions):
    scores = []
    if len(portions) != len(ingredients):
        print("ERROR - wrong nums")
    cap = []
    dur = []
    flav = []
    tex = []
    cals = []
    k = 0
    while k < len(portions):
        for i in range(1, 6):
            if i == 1:
                cap.append(portions[k]*ingredients[k][i])
            if i == 2:
                dur.append(portions[k]*ingredients[k][i])
            if i == 3:
                flav.append(portions[k]*ingredients[k][i])
            if i == 4:
                tex.append(portions[k]*ingredients[k][i])
            if i == 5:
                cals.append(portions[k]*ingredients[k][i])
        k += 1
    # print(cap)
    # print(dur)
    # print(flav)
    # print(tex)
    if sum(cap) <= 0 or sum(dur) <= 0 or sum(flav) <= 0 or sum(tex) <= 0:
        return 0
    elif sum(cals) == 500: #Part 2, simply move line 60 to 61 to get part 1.
        return(sum(cap)*sum(dur)*sum(flav)*sum(tex))
    return 0
            
# 44,56
def step(into):
    outto = into
    if into[3] == 99:
        outto[3] = 0
        outto[2] = into[2] + 1
    elif into[2] == 99:
        outto[2] = 0
        outto[1] = into[1] + 1
    elif into[1] == 99:
        outto[1] = 0
        outto[0] = into[0] + 1
    else:
        outto[3] = into[3] + 1
    return outto

curmax = 0 
into = [1, 1, 1, 97]

while into[0]<97:
    into = step(into)
    if sum(into) != 100:
        continue
    print(into)
    portions = into
    curscore = calculatescore(portions)
    # print(curscore)
    if curscore >= curmax:
        curmax = curscore
    
print(curmax)