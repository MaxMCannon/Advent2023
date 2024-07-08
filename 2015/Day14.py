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
    move_counter = 0
    rest_counter = 0
    leader = False
    points = 0

    def updatepos(self):
        if self.resting:
            if self.rest_counter == 1:
                self.resting = False
                self.move_counter = self.move_duration
            self.rest_counter -= 1
        else:
            self.pos += self.speed
            if self.move_counter == 1:
                self.resting = True
                self.rest_counter = self.rest_duration
            self.move_counter -= 1
    
    def resetcounters(self):
        self.move_counter = self.move_duration
        self.rest_counter = self.rest_duration
        
    def addpoint(self):
        self.points += 1

    def printDeer(self):
        if self.resting == False:
            print('Name: %s is at Pos: %s - Speed: %s for %s seconds, then rest %s seconds'
                % (self.name, self.pos, self.speed, self.move_counter, self.rest_duration))
        # if self.resting:
        #     print('Name: %s is at Pos: %s - Resting for %s seconds, then moving %s for %s seconds'
        #         % (self.name, self.pos, self.rest_counter, self.speed, self.move_duration))

DeerList = []
poslist = []
points = []

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

for d in DeerList:
    d.resetcounters()
    poslist.append(0)
    points.append(0)

timer = 0
while timer <= 2504:
    for i in range(len(DeerList)):
        poslist[i] = DeerList[i].pos
        DeerList[i].printDeer()
        DeerList[i].updatepos()

    for l in range(len(poslist)):
        if poslist[l] == max(poslist):
            points[l] += 1
    timer += 1

for d in DeerList:
    print(d.name + ': ' + str(d.pos))
print(poslist)
print(points)