import ast
import itertools

def discard(hand):
    discardList = []    #list to hold possible discard actions

    for item in hand:
        temp = tuple(item)
        tempList = []
        tempList.append(temp)
        discardList.append(tempList)

    print(discardList)

    return discardList
