#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
modul dokument
"""

def pick(bag, item, index = -1):
    """
    Lägger till saker i listan
    """
    if int(index) > len(bag):
        print("Error! %s is too high index!" % index)
        return bag
    if index != -1:
        bag.insert(int(index), item)
        index = bag.index(item)
        print("You added %s to the backpack on index %s" % (item, index))
    else:
        bag.append(item)
        print("You added %s to the backpack" % item)	
    return bag

def inventory(bag):
    """
    prints lenght of list
    """
    lenght = len(bag)
    print("The amount of stuff in the backpack are %s and the backpack contains following: %s" % (lenght, bag))

def drop(bag, item):
    """
    removes stuff from the backpack
    """
    try:
        bag.remove(item)
    except ValueError:
        print("Error! %s is not in the backpack" % item)
        return bag  
    print("You removed %s from the backpack" % item)
    return bag

def swap(bag, item1, item2):
    """
    changes index
    """
    if item1 == item2:
        print("Error!, you can't switch place with the same item")
        return bag
    try:
        a, b = bag.index(item1), bag.index(item2)
        bag[b], bag[a] = bag[a], bag[b]
    except ValueError:
        print("Error! %s or/and %s is not in the backpack" % (item1, item2))
        return bag
    print("You swapped place for %s and %s in the backpack" % (item1, item2)) 
    return bag
