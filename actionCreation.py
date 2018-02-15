###Vocany Pitia
###CSCE 4310
###Homework 3
###actionCreation.py

import itertools

def discard(hand):
    discardList = []    #list to hold possible discard actions

    for item in hand:
        temp = tuple(item)
        tempList = []
        tempList.append(temp)
        discardList.append(tempList)

    return discardList

def leftMatch(table, hand):
    tableLeft = []
    finalLeft = []

    for domino in hand:
        for pip in table:
            if domino[0] == pip[0]:
                temp = tuple(pip)
                tableLeft.append(temp)
        if len(tableLeft) != 0:
            for x in range(1, len(tableLeft) + 1):
                for subset in itertools.combinations(tableLeft, x):
                    print(subset)
                    tempList = legalCheck(tableLeft, domino, "left")
                    if len(tempList) != 0:
                        finalLeft.append(tempList)
        tableLeft = []

    return finalLeft

def rightMatch(table, hand):
    tableRight = []
    finalRight = []

    for domino in hand:
        for pip in table:
            if domino[1] == pip[1]:
                temp = tuple(pip)
                tableRight.append(temp)
        if len(tableRight) != 0:
            for x in range(1, len(tableRight) + 1):
                for subset in itertools.combinations(tableRight, x):
                    tempList = legalCheck(subset, domino, "right")
                    if len(tempList) != 0:
                        finalRight.append(tempList)
        tableRight = []

    return finalRight

def doubles(table, hand):
    tableDoubles = []
    finalDoubles = []

    for dblPip in table:
        if dblPip[0] == dblPip[1]:
            temp = tuple(dblPip)
            tableDoubles.append(temp)

    for domino in hand:
        if domino[0] == domino[1]:
            for x in range(1, len(tableDoubles) + 1):
                for subset in itertools.combinations(tableDoubles, x):
                    tempList = legalCheck(subset, domino, "double")
                    if len(tempList) != 0:
                        finalDoubles.append(tempList)

    return finalDoubles

def legalCheck(inputList, domino, test):
    legalActionDouble = []
    legalActionLeft = []
    legalActionRight = []
    totalSum = 0

    if test == "double":
        for item in inputList:
            totalSum = totalSum + item[0]
        totalSum = totalSum + domino[0]
        if totalSum % 5 == 0 and totalSum != 0:
            legalActionDouble.append(domino)
            for table in inputList:
                legalActionDouble.append(table)
        totalSum = 0
        return legalActionDouble
    elif test == "left":
        for item in inputList:
            totalSum = totalSum + item[1]
        totalSum = totalSum + domino[1]
        if totalSum % 5 == 0 and totalSum != 0:
            legalActionLeft.append(domino)
            for table in inputList:
                legalActionLeft.append(table)
        totalSum = 0
        return legalActionLeft
    elif test == "right":
        for item in inputList:
            totalSum = totalSum + item[0]
        totalSum = totalSum + domino[0]
        if totalSum % 5 == 0 and totalSum != 0:
            legalActionRight.append(domino)
            for table in inputList:
                legalActionRight.append(table)
        totalSum = 0
        return legalActionRight
    else:
        print("No legal actions found")
        return

