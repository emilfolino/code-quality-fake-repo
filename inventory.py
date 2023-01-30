#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" Methods for marvins the chat bot inventory"""

def run(wordsInput, inventoryList):
    """" Running inventory module """

    if len(wordsInput) == 1:
        if len(wordsInput[0]) == 3:
            inventory(inventoryList)


    elif "pick" in wordsInput:
        if len(wordsInput) == 3:
            inventoryList = pick(inventoryList, wordsInput[2])

        elif len(wordsInput) == 4:
            try:
                int(wordsInput[3])
            except ValueError:
                print("\nError: The position command is not an integer number!")
            else:
                inventoryList = pick(inventoryList, wordsInput[2], int(wordsInput[3]))
        else:
            notValidInv(wordsInput)

    elif "drop" in wordsInput:
        if len(wordsInput) == 3:
            inventoryList = drop(inventoryList, wordsInput[2])
        else:
            notValidInv(wordsInput)

    elif "swap" in wordsInput:
        if len(wordsInput) == 4:
            inventoryList = swap(inventoryList, wordsInput[2], wordsInput[3])
        else:
            notValidInv(wordsInput)


    else:
        notValidInv(wordsInput)

def inventory(inventoryList):
    """ Checking inventory status """
    print("\nYou have: " + str(len(inventoryList)) + " item in the backpack.")
    print("The bagpack contains this: ")
    print(inventoryList)

def pick(inventoryList, itemInput, indexValue="last"):
    """ insert item in backpack """

    if isinstance(indexValue, (int, float)):
        indexValue = str(indexValue)

    if indexValue == "last":
        indexValue = len(inventoryList)
        inventoryList.insert(indexValue, itemInput)
        print("\n" + itemInput + " was added to the backpack")
        print("\nThe bagpack contains this: ")
        print(inventoryList)
    else:
        try:
            1/indexValue.isnumeric()
        except ZeroDivisionError:
            print("\nError: The position command is not an integer number!")
        else:
            if int(indexValue) > len(inventoryList):
                print("\nError: The index position " + indexValue + " is not valid")
            else:
                inventoryList.insert(int(indexValue), itemInput)
                print("\n" + itemInput + " was added to the backpack in position " + indexValue)
                print("\nThe bagpack contains this: ")
                print(inventoryList)

    return inventoryList

def drop(inventoryList, itemInput):
    """ drop item from backpack """

    try:
        1/(itemInput in inventoryList)
    except ZeroDivisionError:
        errorMessage(itemInput)
    else:
        print(inventoryList)
        inventoryList.remove(itemInput)
        print("\n" + itemInput + " was removed from the backpack")

    return inventoryList

def swap(inventoryList, itemInput1, itemInput2):
    """ swap items from backpack """

    itemInput = ""
    if (itemInput1 in inventoryList):
        test1 = True
    else:
        test1 = False
        itemInput += "(" + itemInput1 + ")"

    if (itemInput2 in inventoryList):
        test2 = True
    else:
        test2 = False
        itemInput += "(" + itemInput2 + ")"

    try:
        1/(test1*test2)
    except ZeroDivisionError:
        errorMessage(itemInput)
    else:
        a, b = inventoryList.index(itemInput1), inventoryList.index(itemInput2)
        inventoryList[b], inventoryList[a] = inventoryList[a], inventoryList[b]
        print("\n" + itemInput1 + " swapped place with " + itemInput2)

    return inventoryList

def errorMessage(itemInput):
    """ error message item doesn't exist """
    print("\n Error: " + itemInput + " is not in the backpack!")

def notValidInv(wordsInput):
    """ error message invalid inv input """
    orginalInput = " ".join(wordsInput)
    print("\n Error: \"" + orginalInput + "\"" + " is not a valid \"inv\" command")
