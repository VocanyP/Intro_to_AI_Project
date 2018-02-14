import ast
import itertools

def discard(hand):
    discardList = []    #list to hold possible discard actions
    tempList = []

    for domino in hand:
        tempList.append(list(domino))

    for item in tempList:
        temp = tuple(item)
        temp2 = []
        temp2.append(temp)
        discardList.append(temp2)

    print(discardList)
