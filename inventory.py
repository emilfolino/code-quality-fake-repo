#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    Inventory funktioner
"""

def inventory(bagg):
    """ Skriver ut bagg """
    print("Items in bag: " + str(len(bagg)))
    print(bagg)

def pick(bagg, item, indx = -1):
    """ Sätt i item i bagg """
    try:
        indx = int(indx)
    except ValueError:
        print("Error wrong arguments")
        return bagg
    if indx < len(bagg):
        if indx == -1:
            bagg.append(item)
            print("Added " + item)
            return bagg
        
        bagg.insert(indx, item)
        print("Added " + item + " at index " + str(indx))
        return bagg
    
    print("Error That index is too high")
    print("index you choose: " + str(indx))
    return bagg

def drop(bagg, item):
    """ Ta bort item """
    try:
        bagg.remove(item)
        print("Dropped " + item)
        return bagg
    except ValueError:
        print("Error You dont have a " + item)
        return bagg

def swap(bagg, item, item2):
    """ swappa item """
    if item == item2 or bagg.count(item) > 1 or bagg.count(item2) > 1:
        print("Error Cannot have same item twice, in argument or in list")
        return bagg
    try:
        print("swapping " + item + " with " + item2)

        key1 = bagg.index(item)
        key2 = bagg.index(item2)
        bagg[key1] = item2
        bagg[key2] = item

        return bagg
    except ValueError:
        print(f"Error Cannot swap, {item} or {item2} don't exist")
        return bagg
