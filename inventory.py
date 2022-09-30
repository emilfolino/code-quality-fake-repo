#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Module Inventory
"""

def pick(bag, item, index=None):
    """
    Adds new item in list, with our without a given index.
    Error message is displayed if given index is too high.
    """
    if index is not None:
        index = int(index)
        if index > len(bag):
            print("Error! Index too high. " + str(index))
            return bag
        bag.insert(index, item)
        print("\"" + item + "\" has been added at index " + str(index) + ".")
    else:
        bag.append(item)
        print("\""+ item +"\" has been added.")
    return bag

def drop(bag, item):
    """
    Item is removed from list. If item is not in the list, an error message
    is displayed.
    """
    if item not in bag:
        print("Error! \""+ item +"\" not in bag.")
        return bag
    bag.remove(item)
    print("\""+ item +"\" has been removed.")
    return bag

def swap(bag, item1, item2):
    """
    Items swap places. If items do not exist or they are the same, an error
    message is displayed.
    """
    if item1 == item2 or item1 not in bag or item2 not in bag:
        print("Error! \""+ item1 +"\" or \""+ item2 +"\" not in bag.")
        return bag
    index1 = bag.index(item1)
    index2 = bag.index(item2)
    temp = bag[index1]
    bag[index1] = bag[index2]
    bag[index2] = temp
    print("\""+ item1 +"\" and \""+ item2 +"\" have been swapped.")
    return bag

def inventory(bag):
    """
    Displays the inventory of the bag.
    """
    print("Bag has", len(bag), "item/s:", bag)
