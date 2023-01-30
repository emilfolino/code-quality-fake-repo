#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    Inventory functions for marvin
"""


def pick(marvin_backpack, item, item_index = ""):
    """
    Adds item to marvin_backpack, if no index is given item will be placed last in the list
    """
    try:
        if int(item_index) > len(marvin_backpack):
            print(f"Error! Index {item_index} too high")
        else:
            marvin_backpack.insert(int(item_index), str(item))
            print(f"{item} has been added at index: {item_index} " + str(marvin_backpack))
    except ValueError:
        marvin_backpack.append(item)
        print(f"{item} has been added " + str(marvin_backpack))

    return marvin_backpack


def inventory(marvin_backpack, start = 0, stop = ""):
    """
    Prints the amount of items in marvins backpack and what it contains
    """
    try:
        stop = int(stop)
        start = int(start)
        slice_inventory = slice(start, stop)
        print(str(marvin_backpack[slice_inventory]))
    except ValueError:
        print("Marvins backpack has " + str(len(marvin_backpack)) + " item(s): " + str(marvin_backpack))


def drop(marvin_backpack, item):
    """
    Removes an item from marvins backpack
    """
    try:
        marvin_backpack.remove(item)
        print(f"{item} has been removed from Marvins backpack.")
    except ValueError:
        print(f"Error! {item} is not in marvins backpack!")
    return marvin_backpack


def swap(marvin_backpack, item1, item2):
    """
    Swaps the position of two items in marvins backpack
    """
    if item1 == item2:
        print("Error! Items are the same")
    else:
        try:
            index1 = marvin_backpack.index(item1)
            index2 = marvin_backpack.index(item2)
            marvin_backpack[index1], marvin_backpack[index2] = marvin_backpack[index2],marvin_backpack[index1]
            print(f"{item1} and {item2} have swapped places")
        except ValueError:
            print(f"Error! {item1} or {item2} is not in Marvins backpack")
    return marvin_backpack
