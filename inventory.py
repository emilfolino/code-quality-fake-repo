#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Functions for Marvin3
"""
def pick(backpack, item, pos = None):
    """
    (inv pick) put item in backpack at index. Old value moves to index+1.
    If no index just append.
    If index doesnt exist print Error msg.
    """
    bag = backpack
    if pos is not None:
        #print(f"index is type : {type(index)}")
        if int(pos) <= len(bag):
            bag.insert(int(pos), item)
            print(f"{item} was added at index {pos}.")
        else:
            print(f"Error : Index {pos} doesn't exist.")    
    else:
        bag.append(item)
        print(f"{item} was added.")
    return bag

def inventory(backpack, start = None, stop = None):
    """
    (inv) print the contents in backpack
    extra: print the content between start and stop.
    """
    if start is not None and stop is not None:
        try:
            sta = int(start)
            sto = int(stop)
            print(f"{backpack[sta:sto]}")# varför inte IndexError om > len(bag)
        except ValueError:
            print("Error : both start and stop need to be a nr.")
        except IndexError:
            print("Error : index doesn't exist")
    else:
        print(f"Backpack has {len(backpack)} items: {backpack}")

def drop(backpack, item):
    """
    (inv drop) Remove item from backpack
    print result
    """
    bag = backpack
    try:
        bag.remove(item)
        print(f"{item} was removed.")
    except ValueError:
        print(f"Error : {item} doesn't exist.")
    return bag

def swap(backpack, item1, item2):
    """
    (inv swap) swap position of item1 and item2
    if either item doesn't exist, print Error msg
    """
    bag = backpack
    if item1 in bag and item2 in bag:
        a = bag.index(item1)
        b = bag.index(item2)
        bag[a], bag[b] = bag[b], bag[a]
        print(f"{item1} and {item2} changed positions. New list: {bag}")
    else:
        if item1 not in bag and item2 not in bag:
            print(f"Error : {item1} and {item2} are not in the bag.")
        elif item1 not in bag:
            print(f"Error : {item1} is not in the bag.")
        else:
            print(f"Error : {item2} is not in the bag.")
    return bag
