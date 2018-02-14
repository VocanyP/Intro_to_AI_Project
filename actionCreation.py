import ast
import itertools

def discard(hand):
    discardList = []    #list to hold possible discard actions
    tempList = []

    for domino in hand:
        tempList.append(list(domino))

    for item in tempList:
        temp = tuple(item)
        discardList.append(temp)

    print(discardList)
