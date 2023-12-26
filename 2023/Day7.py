#Advent of Code 2023 Day 7 

lines = open("day7in.txt").read().splitlines()
# for l in lines:
    # print(l)
cardlist = {"T": 10, "J": 11, "Q": 12, "K": 13, "A":14}

def fixties(h1, h2):
    
    for i in range(len(h1)):
        if h1[i].isnumeric() and h1[i] > h2[i]:
            return h1
        elif h1[i].isnumeric and h1[i] < h2[i]:
            return h2

#hand types: 5 of a kind, 4 of a kind, full house, 3 of a kind, two pair, one pair, high card

def getrank(hand):
    cards = {}
    for i in hand:
        try:
            cards[i] += 1
        except:
            cards.setdefault(i, 1)
    # print(cards)
    for k in cards.values():
        if k == 5:
            print("five of a kind")
            return 100
        elif k == 4:
            print("four of a kind")
            return 90
        if k == 3 and len(cards) == 2:
            print("full house")
            return 80
        elif k == 3:
            print("three of a kind")
            return 70
        if k == 2 and len(cards) == 3:
            print("two pair")
            return 60
        if k == 1 and len(cards) == 4:
            print("one pair")
            return 50
        else:
            print("high card")
            return 40
        

hands = []
bids = []
for l in lines:
    hand = l.split(" ")[0]
    bid = l.split(" ")[1]
    hands.append(hand)
    bids.append(int(bid))
    print(hand)
    getrank(hand)


# test = "A5432"
# print(getrank(hands[4]))
# print(getrank(test))




# print(hands)
# print(bids)

    