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

def lefteMatch():
    print("Nothing")

def rightMatch():
    print("Nothing")

def doubles(table, hand):
    tableDoubles = []
    finalDoubles = []

    for dblPip in table:
        if dblPip[0] == dblPip[1]:
            temp = tuple(dblPip)
            tableDoubles.append(temp)
    print(tableDoubles)

    for domino in hand:
        if domino[0] == domino[1]:
            for x in range(1, len(tableDoubles) + 1):
                for subset in itertools.combinations(tableDoubles, x):
                    print(subset)
                    tempList = legalCheck(subset, domino, "double")
                    if len(tempList) != 0:
                        finalDoubles.append(tempList)
                    print("Final Double ")
                    print(finalDoubles)
    return finalDoubles

def legalCheck(doublelist, domino, test):
    legalAction = []
    totalSum = 0

    if test == "double":
        for item in doublelist:
            print("Domino is ", domino, " Item is ", item)
            totalSum = totalSum + item[0]
        totalSum = totalSum + domino[0]
        print(totalSum)
        if totalSum % 5 == 0:
            legalAction.append(domino)
            for table in doublelist:
                legalAction.append(table)
        totalSum = 0
    else:
        print("Test not equal to double")
    print("Legal Action ", legalAction)
    return legalAction

