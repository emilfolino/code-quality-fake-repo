#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Inventory functions for marvin"""

def pick(backpack, item, index=None):
    """Pickups an item and place it in invenory at index position."""
    if index is None:
        index = len(backpack)
    index = int(index)
    if index > int(len(backpack)):
        print("Error: Index " + str(index) + " too large.")
        return backpack
    backpack.insert(index, item)
    print(str(item) + " has been added in position " + str(index) + ". This is now your inventory: " + str(backpack))
    return backpack

def inventory(backpack):
    """The inventory or backpack where items are placed."""
    nr_items = len(backpack)
    print("Backpack contains " + str(nr_items) + " items which are: " + str(backpack))
    
def drop(backpack, item):
    """Drops/removes an item from the backpack."""
    try:
        backpack.remove(item)
        print(str(item) + " has been dropped.")
        return backpack
    except ValueError:
        print("Error. " + item + " does not exist.")
        return backpack

def swap(backpack, item1, item2):
    """Swaps the index position of item1 with item2."""
    if item1 == item2:
        print("Error: Identical items can't change place.")
        return backpack
    if item1 and item2 in backpack:
        if item1 in backpack:
            if item2 in backpack:
                index_1 = backpack.index(item1)
                index_2 = backpack.index(item2)
                temp_index = item1

                backpack[index_1] = backpack[index_2]
                backpack[index_2] = temp_index
                print(item1 + " changed place with " + item2 + ".")
                return backpack
            print("Error: " + item2 + " is not in your inventory.")
            return backpack
        print("Error: " + item1 + " is not in your inventory.")
        return backpack
    print("Error: " + item1 + " and " + item2 + " is not in your inventory.")
    return backpack
