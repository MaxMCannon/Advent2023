#Advent of Code 2015, Day 11
#Maxwell Cannon
#January 6th, 2024

spass = open('2015/input.txt').read()

#ord() gets unicode
#chr() gets char from unicode

def inc(p):
    parr = []
    test = True
    for c in p:
        parr.append(c)
    for i in range(len(parr)):
        if set(parr[i:]) == {'z'}:
            test = False
            for j in range(i, len(parr)):
                parr[j] = 'a'
            parr[i-1] = chr(ord(parr[i-1])+1)
            break
    if test:
        if ord(parr[-1]) < 122:
            parr[-1] = chr(ord(parr[-1])+1)
        else:
            parr[-1] = 'a'
    
    outstr = ''
    for c in parr:
        outstr += c
    return outstr

def checktrip(p):    # Returns true if there are a triples set
    triplets = []
    for i in range(len(p)-2):
        triplets.append(p[i:i+3])
    # print(triplets)
    for t in triplets:
        if (ord(t[2]) - ord(t[1])) == 1 and (ord(t[1]) - ord(t[0])) == 1:
            return True
    return False
        
def checkoil(p):    #Returns true if it contains a bad letter
    bads = ['o', 'i', 'l']
    for c in p:
        if c in bads:
            return True
    return False

def checkdubs(p):
    count = 0
    doubles = []
    for i in range(len(p)-1):
        doubles.append(p[i:i+2])
    print(doubles)
    ch = 0
    while ch < len(doubles):
        d = doubles[ch]
        if d[1] == d[0]:
            count += 1
            ch += 1
        ch += 1
    if count >= 2:
        return True
    return False
    

def checkpass(p):
    if checktrip(p) and not checkoil(p) and checkdubs(p):
        return True
    return False

print(spass)
npass = inc(spass)

for i in range(1000000):
    print(npass)
    if checkpass(npass):
        print(npass)
        break
    npass = inc(npass) 

# answer part 1 = hepxxyzz ?? Untested