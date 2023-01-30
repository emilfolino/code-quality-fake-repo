#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Inventory functions
"""

def pick(inv, thing, place=""):
    """
    Pick an item and place it in inventory
    """
    try: 
        if place == "":
            inv.append(thing)
            print("You added " + thing + " to your inventory at index " + str(inv.index(thing)) + "!")
        elif int(place) > len(inv):
            print("Error: " + place + " is out of range!")
        else:
            inv.insert(int(place), thing)
            print("You added " + thing + " to your inventory at index " + str(inv.index(thing)) + "!")
    except IndexError:
        print(place + " is out of range!")
    return inv

def inventory(inv, start=0, stop="default"):
    """
    Check inventory
    """
    if stop == "default":
        stop = len(inv)
    print("Here's your inventory: ")
    print(inv[int(start):int(stop)])
    print("You have " + str(len(inv)) + " things in it.")

def drop(inv, thing):
    """
    Drops items
    """
    try:
        inv.remove(thing)
        print("You removed " + thing)
    except Exception:
        print("Error: " + thing + " is not in your inventory!")
    return inv

def swap(inv, thing1, thing2):
    """
    Swaps items
    """
    try:
        index1 = inv.index(thing1)
        index2 = inv.index(thing2)
        if index1 == index2:
            print("Error: you can't swap things with the same name!")
        else:
            inv[index1] = thing2
            inv[index2] = thing1
            print("Successfully swapped " + thing1 + " and " + thing2)
    except ValueError:
        print("Error: " + thing1 + " or " + thing2 + " is not in your inventory!")
    return inv
