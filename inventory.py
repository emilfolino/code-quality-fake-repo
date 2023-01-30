#!/usr/bin/env python3

"""Marvin inventory module"""
import time

def pick(bag, thing, index = -1): 
    """allows user to pick items"""
    temp_list = bag
    index = int(index)
    if index == -1: # no index specified, could be prettier
        temp_list.append(thing)
        print(str(thing) + " was added to backpack at index " + str(len(temp_list) - 1))
    elif index > len(temp_list) - 1: # throw error if index too high
        print("Error - the specified index " + str(index) + " is too large")
    else: #pick the thing at specific position and move everything else
        print(index)
        temp_index = temp_list[index:len(temp_list)]
        temp_list[index] = thing
        temp_list[index+1:len(temp_list)] = temp_index
        print(str(thing) + " was added to backpack at index " + str(index))
    return temp_list

def inventory(bag): 
    """allows user to list items"""
    print("This many things in the backpack: " + str(len(bag)))
    print("backpack contains: " + str(bag))
    time.sleep(1)

def drop(bag, thing): 
    """allows user to drop items"""
    temp_list = bag
    thing = str(thing)
    if thing not in temp_list: #if not in bag throw error
        print("Error: no " + thing + " in backpack")
    else: # drop the thing
        thing_index = temp_list.index(thing)
        temp_list.pop(thing_index)
        print(thing + " was removed from backpack.")
    return temp_list

def swap(bag, thing1, thing2):
    """allows user to swap items"""
    temp_list = bag

    if thing1 == thing2: # you shouldnt be able to swap similar things
        print("Error: can not swap the same thing!")

    try:
        thing1_index = temp_list.index(str(thing1)) 
        thing2_index = temp_list.index(str(thing2))
    except ValueError: # throw error if one of things not in bag
        print("Error: one of " + str(thing1) + " or " + str(thing2) + " not in the backpack.")
        return temp_list

    tempItem = temp_list[thing2_index] #copy back to temp
    temp_list[thing2_index] = temp_list[thing1_index] #copy front to back
    temp_list[thing1_index] = tempItem # copy temp to front

    print(str(thing1) + " and " + str(thing2) + " swapped places.")

    return temp_list
