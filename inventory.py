#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Functions for marvin inventory
"""

def inventory(bag):
    """
    Prints the bag.
    """
    print(f"Bagpack has {len(bag)} items: {bag}")
    

def pick(bag, obj, index = -9000):
    """
    adds items to bag at given index or detault last
    returns bag
    """
    try:
        index = int(index)
    except ValueError:
        print("Error index needs to be a number")
        return bag
    
    if index >= len(bag):
        print(f"Error index={index} is out of range")
        return bag

    msg = f"{obj} has been added"
    if index != -9000:
        bag.insert(index, obj)
        msg += f" at index {index}"
    else:
        bag.append(obj)
    
    print(msg)
    return bag

def drop(bag, obj):
    """
    removes object from list
    """
    try:
        bag.remove(obj)
        print(f"{obj} dropped from bag")
    except ValueError:
        print(f"Error: {obj} not in bag")
    return bag
        
def swap(bag, item_one, item_two):
    """
    swaps places between item_one and item_two 
    returns the updated bag
    """
    if item_one == item_two:
        print("Error item one and two are the same")
        return bag     
    
    one_in_bag = True
    two_in_bag = True
    
    try:
        index_one = bag.index(item_one)
    except ValueError:
        one_in_bag = False

    try:
        index_two = bag.index(item_two)
    except ValueError:
        two_in_bag = False
            
    if one_in_bag and two_in_bag:
        bag[index_one], bag[index_two] = bag[index_two], bag[index_one]
        msg = f"{item_one} and {item_two} has been swaped"
        
    else: 
        msg = "Error "
        if not one_in_bag and not two_in_bag:
            msg += f"{item_one} and {item_two} is not in the bag"
        elif not one_in_bag:
            msg += f"{item_one} is not in the bag"
        else:
            msg += f"{item_two} is not in the bag"

    print(msg)
    return bag
