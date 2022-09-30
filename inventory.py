#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Module that contains the functions for handling the inventory in main.py
"""

def pick(backpack, item, index="last"):
    """
    Function to add items to the inventory.
    returns the updated inventory
    """
    if index == "last":
        try:
            backpack.append(item)
            print("Item: " + item + " was added to inventory.")
        except AttributeError:
            print("First argument not a list!")
    else:
        try:
            index_input = int(index)
            if index_input >= len(backpack):
                print("Error: Out of index range (0 - " + str(len(backpack) - 1) + ") with input index; " + str(index))
            else:
                backpack.insert(index_input, item)
                print("Item: " + item + " was added to inventory at index " + index)
        except AttributeError:
            print("First argument not a list!")
        except TypeError:
            print("Index is of a type not castable to int!")

    return backpack

def inventory(backpack):
    """
    Function to display the items in the inventory.
    """
    print("In the backpack there are " + str(len(backpack)) + " items.\n"
          + str(backpack))

    #for item_i in backpack:
        #print(item_i)

def drop(backpack, item):
    """
    Function to remove item from the inventory.
    returns the updated inventory
    """
    if item in backpack:
        try:
            backpack.remove(item)
            print("Item: " + item + " was removed from backpack.")
        except AttributeError:
            print("First argumnet not a list!")
    else:
        print("Error: Backpack does not contain " + item + "!")
    return backpack

def swap(backpack, item_1, item_2):
    """
    Function to swap the location of two items in the inventory
    returns the updated inventory
    """
    if item_1 in backpack and item_2 in backpack and item_1 != item_2:
        try:
            item_1_index = backpack.index(item_1)
            item_2_index = backpack.index(item_2)
            backpack[item_1_index] = item_2
            backpack[item_2_index] = item_1
            print(item_1 + " swaped places with " + item_2)
        except AttributeError:
            print("First argument not a list!")
    else:
        print("Error: Backpack not containing " + item_1 + " or/and " + item_2 + 
              " or items are the same.")
    return backpack
