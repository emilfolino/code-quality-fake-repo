#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
my collection of marvin functions 2
"""

import pprint

def pick(backpack, item, index=""):
    ''' adds item to backpack '''
    try:
        if int(index) > len(backpack):
            print("Error: invalid index \'" + str(index) + "\'")
            return backpack
        backpack.insert(int(index), item)
        print("\'" + item + "\' was added at index: " + str(index))
    except ValueError:
        backpack.append(item)
        print("\'" + item + "\' was added at the end")

    return backpack

def inventory(backpack):
    ''' prints the backpack '''
    print("The backpack contains " + str(len(backpack)) + " items and those are:")
    pprint.pprint(backpack)

def drop(backpack, item):
    ''' removes item from backpack '''
    try:
        backpack.remove(item)
        print("\'" + item + "\' was removed from backpack")
    except ValueError:
        print("Error: \'" + item + "\' was not in backpack")

    return backpack

def swap(backpack, item1, item2):
    ''' swaps index of items '''
    if item1 == item2:
        print("Error")
    else:
        try:
            index1 = backpack.index(item1)
            index2 = backpack.index(item2)
            backpack[index1], backpack[index2] = backpack[index2], backpack[index1]
            print("\'" + item1 + "\' and \'" + item2 + "\' have now swapped places")

        except ValueError:
            print("Error: atleast one of your inputs(" + item1 + " or " + item2 + ") were not in backpack")

    return backpack
