#advent 2023 Day 6

intxt = open("day6in.txt").read().splitlines()
timetxt = intxt[0]
disttxt = intxt[1]

def tonums(nums):
    arr = []
    for i in nums:
        if i == '':
            continue
        arr.append(int(i))
    return arr

times = tonums(timetxt.split(":")[1].split(" "))
dists = tonums(disttxt.split(":")[1].split(" "))
print(times)
print(dists)

def getdist(speed, time):
    return speed*time

def getwins(time, record):
    arr = []
    speed = 0
    
    for holdt in range(time):
        speed = holdt
        dist = speed * (time-holdt)
        if dist > record:
            arr.append(dist)
    # print(arr)
    return arr

prodsol = 1

for i in range(len(times)):
    prodsol *= len(getwins(times[i], dists[i]))

print("part 1 solution : " + str(prodsol))

print("Part 2 solution : " + str(len(getwins(58819676, 434104122191218))))
