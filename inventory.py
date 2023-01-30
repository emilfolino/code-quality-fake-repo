#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
functions inventory
"""

def pick(backpack,item,index="hej"):
    """
    pick
    """
    try:
        if index == "hej":
            backpack.append(item)
            print(item + " has been added to the backpack")
        else:
            copy1 = backpack[int(index):]
            copy2 = backpack[:]
            copy2[int(index)] = item
            copy3 = copy2[:(int(index)+1)]
            backpack =  copy3 + copy1
            print(item + " has been added to the backpack, in position " + str(index))
        return backpack
    except IndexError:
        print("Error " + index + ": is to high")
        return backpack

def inventory(backpack,start="start",stop="stop"):
    """
    inventory
    """
    if start != "start" and stop != "stop":
        inv_slice = backpack[int(start):int(stop)]
        print(", ".join(inv_slice))
    else:
        print("There is now " + str(len(backpack)) + " items in the backpack")
        print(backpack)


def drop(backpack,item):
    """
    drop
    """
    try:
        backpack.remove(item)
        print(item + " was removed from the backpack")
        return backpack
    except ValueError:
        print("Error " + item + " was not found in the backpack")
        return backpack

def swap(backpack,item1,item2):
    """
    swap
    """
    if(item1 == item2):
        print("Error " + item1 + " is the same as " + item2)
        return backpack
    try:
        index1 = backpack.index(item1)
        index2 = backpack.index(item2)
        backpack[index1] = item2
        backpack[index2] = item1
        print(item1 + " have swapped place with " + item2)
        return backpack
    except ValueError:
        print("Error " + item1 + " and/or " + item2 + " was not in the backpack")
        return backpack
