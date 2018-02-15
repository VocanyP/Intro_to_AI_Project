###Vocany Pitia
###CSCE 4310
###Homework 3
###actionCreation.py

import itertools

#Function to create the legal discard moves
def discard(hand):
    discardList = []    #list to hold possible discard actions

    #Loop to add each domino in the players hand
    #to the list of legal discard actions
    for item in hand:
        tempList = []
        tempList.append(item)
        discardList.append(tempList)

    return discardList

#Function to facilitate the creation of legal left match moves
def leftMatch(table, hand):
    tableLeft = []              #List to hold dominos on the table that match on the left with the player's chosen domino from the hand
    finalLeft = []              #Contains the final list of all left match legal moves availble to the player

    for domino in hand:
        for pip in table:
            if domino[0] == pip[0]:     #Check to see if the domino's match on the left pip
                tableLeft.append(pip)   #If they mach, add it to the tableLeft list
        if len(tableLeft) != 0:
            #Create a combination of all the left pip matches
            for x in range(1, len(tableLeft) + 1):
                for subset in itertools.combinations(tableLeft, x):
                    tempList = legalCheck(tableLeft, domino, "left")    #Check if the list contains legal actions
                    if len(tempList) != 0:
                        finalLeft.append(tempList)
        tableLeft = []

    return finalLeft

#Function to facilitate the creation of legal right match moves
#Mirrors the leftMatch function
def rightMatch(table, hand):
    tableRight = []
    finalRight = []

    for domino in hand:
        for pip in table:
            if domino[1] == pip[1]:
                tableRight.append(pip)
        if len(tableRight) != 0:
            for x in range(1, len(tableRight) + 1):
                for subset in itertools.combinations(tableRight, x):
                    tempList = legalCheck(subset, domino, "right")
                    if len(tempList) != 0:
                        finalRight.append(tempList)
        tableRight = []

    return finalRight

#Function to facilitate the creatino of legal double match moves
def doubles(table, hand):
    tableDoubles = []
    finalDoubles = []

    #This for loop checks to see if the dominos on the table are doubles
    #If so, it adds it to the last of tableDoubles
    for dblPip in table:
        if dblPip[0] == dblPip[1]:
            tableDoubles.append(dblPip)

    #This for loop checks to see if the dominos in the player's hand are doubles
    #Then creates a list of combinations between the player's hand and the table
    for domino in hand:
        if domino[0] == domino[1]:
            for x in range(1, len(tableDoubles) + 1):
                for subset in itertools.combinations(tableDoubles, x):
                    tempList = legalCheck(subset, domino, "double")
                    if len(tempList) != 0:
                        finalDoubles.append(tempList)

    return finalDoubles

#Function to check if the doubleList, leftMatch List, and rightMatch List are legal
def legalCheck(inputList, domino, test):
    legalActionDouble = []
    legalActionLeft = []
    legalActionRight = []
    totalSum = 0                #Used to keep track of the sum of the pips to determine if they are legal moves

    if test == "double":                            #Handles list of doubles
        for item in inputList:                      #Finds the sum of the non matching pips in the list of possible moves
            totalSum = totalSum + item[0]
        totalSum = totalSum + domino[0]
        if totalSum % 5 == 0 and totalSum != 0:     #If the sum is a multiple of 5, add it to the list of legal moves
            legalActionDouble.append(domino)
            for table in inputList:
                legalActionDouble.append(table)
        return legalActionDouble
    elif test == "left":                            #Handles list of left matches
        for item in inputList:
            totalSum = totalSum + item[1]
        totalSum = totalSum + domino[1]
        if totalSum % 5 == 0 and totalSum != 0:
            legalActionLeft.append(domino)
            for table in inputList:
                legalActionLeft.append(table)
        return legalActionLeft
    elif test == "right":                           #Handles list of right matches
        for item in inputList:
            totalSum = totalSum + item[0]
        totalSum = totalSum + domino[0]
        if totalSum % 5 == 0 and totalSum != 0:
            legalActionRight.append(domino)
            for table in inputList:
                legalActionRight.append(table)
        return legalActionRight
    else:
        print("No legal actions found")
        return

