###Vocany Pitia
###CSCE 4310
###Homework 3
###generateActions.py

import ast
import itertools
from actionCreation import *


def actions(table, hand):
    '''
    :param table - the cards on the table:
    :param hand - the cards on the player's hand:
    :return: list of all possible actions given the Game table and the player's hand
    '''
    finalList = []

    ####################################
    ####### YOUR CODE GOES HERE ########
    ####################################

    discardList = discard(hand)             #List of discard legal actions
    leftList = leftMatch(table, hand)       #List of legal actions where the left pips match
    rightList = rightMatch(table, hand)     #List of legal actions where the right pips macth
    doubleList = doubles(table, hand)       #List of legal actions where there are doubles
    finalList = discardList + leftList + rightList + doubleList     #The final list of legal actions composed of all legal actions

    return finalList

def sortLists(listOfLegalAction):
    finallist = []
    for legalAction in listOfLegalAction:
        temp = []
        for domino in legalAction:
            temp = temp + [sorted(domino)]
        finallist = finallist + [sorted([tuple(x) for x in temp])]

    return sorted(finallist)


def testLegalActionGeneration(table, hand, testcase):
    legalActions = actions(table, hand)  # generating all the legal actions given the table and the hand
    legalActions = sortLists(legalActions)  # sorting the list of legal actions
    testcase = sortLists(testcase)  # sorting the list of legal actions in the test case

    if legalActions == testcase:
        return True

    return False


if __name__ == "__main__":

    ### Leave this file in the folder where you run the code from or modify the path accordingly
    F = open("studentTestCases_legalActions.txt", "r")

    correct = 0
    for line in F:
        split = line.split("##")
        split[0] = ast.literal_eval(split[0])
        split[1] = ast.literal_eval(split[1])
        split[2] = ast.literal_eval(split[2])
        if testLegalActionGeneration(split[0], split[1], split[2]):
            correct += 1
        else:
            print("This test case failed: " + line)

    print("FinalScore: " + str(correct))