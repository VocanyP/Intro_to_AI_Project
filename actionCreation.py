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

def doubles(table, hand):
    tableDoubles = []

    for dblPip in table:
        if dblPip[0] == dblPip[1]:
            temp = tuple(dblPip)
            tableDoubles.append(temp)
    print(tableDoubles)

    for domino in hand:
        if domino[0] == domino[1]:
            #tableDoubles = [domino] + tableDoubles
            #print(tableDoubles)
            for x in range(1, len(tableDoubles) + 1):
                for subset in itertools.combinations(tableDoubles, x):
                    print(subset)

    #doubleList(table, domino)

#def doubleList(table, domino):
