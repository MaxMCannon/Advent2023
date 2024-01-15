#Advent of Code 2024, Day 14
#Maxwell Cannon
#January 11, 2024

dirs = open('2015/input.txt').read().splitlines()

class Reindeer():
    name = ''
    speed = 0
    move_duration = 0
    rest_duration = 0
    pos = 0
    resting = False

    def updatepos(time):
        if Reindeer.resting:
            return None
        else:
            Reindeer.pos += Reindeer.speed
    
    # def printDeer():
    #     print('Name: %s is at Pos: %s - Speed: %s for %s seconds, then rest %s seconds'
    #           % (name, pos, speed, move_duration, rest_duration))

DeerList = []

def makeDeer(l):
    deer = Reindeer()
    deer.name = l.split(' ')[0]
    deer.speed = int(l.split('fly ')[1].split(' ')[0])
    deer.move_duration = int(l.split('for ')[1].split(' seconds')[0])
    deer.rest_duration = int(l.split('rest for ')[1].split(' ')[0])
    deer.resting = False
    DeerList.append(deer)

for dir in dirs:
    makeDeer(dir)

time = 0 
def printstatus():
    print(time)
    for d in DeerList:
        print(str(d.name) + ' at Pos : ' + str(d.pos))

while time < 10:
    for d in DeerList:
        d.updatepos(time)
    printstatus()
    time += 1



    