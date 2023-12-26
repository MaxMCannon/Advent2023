#Advent of code 2023, day 4

inlines = open("day4in.txt").read().splitlines()
# print(inlines)

sum = 0
cardcount = 0
gamelib = {} 

for line in inlines:
    
    cardnum = line.split(":")[0]
    gamelib.setdefault(cardnum, 1)

scores = []
games = []

for line in inlines:
    
    cardnum = line.split(":")[0]
    # print(cardnum)
    rest = line.split(":")[1]
    winners, mine = rest.split("|")[0].split(" "), rest.split("|")[1].split(" ")
    while "" in winners:
        winners.remove("")
    while "" in mine:
        mine.remove("")
    for i in range(len(winners)):
        winners[i] = int(winners[i])
    for j in range(len(mine)):
        mine[j] = int(mine[j])
    
    
    # print(winners)
    # print(mine)
    tempscore = 0
    for m in mine:
        if m in winners:
            tempscore += 1
    scores.append(tempscore)
    tempscore = 0

    #Part 1 business
    # for m in mine:
    #     if m in winners and tempscore >= 1:
    #         tempscore *= 2
    #     elif m in winners:
    #         tempscore += 1
    sum += tempscore
    tempscore = 0


for i in range(len(scores)):
    games.append(1)

for k in range(1, len(games)):
    for j in range(k, k + scores[k-1]):
        games[j] += games[k-1]

for g in games:
    sum += g

print(scores)
print(games)

print(sum)
