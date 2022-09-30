#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Definierade 'inventory' funktioner."""

def pick(backpack, pickup, index=None):
    """Adds items to backpack."""
    if index is None:
        backpack.append(pickup)
        print(f"{pickup} was inserted into the list!")
    else:
        if int(index) > len(backpack)-1:
            print(f"Error: Index {index} är för högt.")
        else:
            backpack.insert(int(index), pickup) 
            print(f"{pickup} was inserted into the list on index {index}!")
    return backpack

def inventory(backpack):
    """Checks what the backpack contains."""
    print(f"There are {len(backpack)} items in this backpack. The items are: \n")
    print(backpack)
    
def drop(backpack, throw_away):
    """Removes an item from the backpack."""
    if throw_away not in backpack:
        print(f"Error: {throw_away} is not in backpack.")
    else:
        backpack.remove(throw_away)
        print(f"{throw_away} was thrown away!")
    return backpack

def swap(backpack, thing1, thing2):
    """Swaps two things in the backpack."""
    if (thing1 in backpack) and (thing2 in backpack):
        a, b = backpack.index(thing1), backpack.index(thing2)
        backpack[a], backpack[b] = backpack[b], backpack[a]
        print(f"{thing1} was swapped with {thing2} in the backpack!")
    else:
        if (thing1 not in backpack) and (thing2 not in backpack):
            print(f"Error: {thing1} and {thing2} is not in backpack.")
        elif thing1 not in backpack:
            print(f"Error: {thing1} is not in backpack.")
        elif thing2 not in backpack:
            print(f"Error: {thing2} is not in backpack.")
    return backpack
    