#!/usr/bin/env python3
 
"""
Inventory functions for marvin chatbot to be called in main.py
"""

def inventory(backpack, start = 0, stop = None):
    """ Takes three arguments, a list called backpack, prints all the items
    in the list as well as the number of items. If the second and third 
    arguments are given, these are used as indexes to print out a slice of the
    list.""" 

    try:
        if not stop:
            stop = len(backpack)

        print("There are " + str(len(backpack[int(start):int(stop)])) 
              + " items in the backpack. They are as follows:")
        print('\n[' + ' '.join(backpack[int(start):int(stop)]) + "]")
    except ValueError:
        print('Start and/or stop values not valid')
    except IndexError:
        print('Start and/or stop values out of range')

def pick(backpack, item, position = None):
    """ Takes three arguments, a list called backpack, a variable called
    item to put in the list backpack and an optional index for
    where to put the item. Returns the updated list""" 
    
    try:
        if not position:
            backpack.append(item)
            print(item + " was added to the backpack.")
        elif int(position) > len(backpack):
            print("Error: the position " + str(position) + " is out of range.")
        else:
            backpack.insert(int(position), item)
            print(item + " was added to the backpack in position " + str(position))
    
    except ValueError:
        print("Error: a valid position not given.")

    return backpack

def swap(backpack, item1, item2 ):
    """ Takes three arguments, a list called backpack and two variables,
    item1 and item2. The positions of item1 and item2 are swapped and
    the list returned. If there are multiple instances of an item,
    the first instance is swapped. If one ore more of the items are
    not in the list or if the two items are the same,
    an error message is printed.""" 

    if item1 != item2:
        try:
            index1 = backpack.index(item1)   
            try:
                index2 = backpack.index(item2)
                backpack[index1], backpack[index2] = backpack[index2], backpack[index1]
                print("The positions of " + item1 + " and " + item2 + " were swapped.")            
            except ValueError:
                print("Error: " + item2 + " was not found in the backpack")
        except ValueError:
            if item2 in backpack:
                print("Error: " + item1 + " was not found in the backpack")
            else:
                print("Error: " + item1 + " and " + item2 + " were not found in the backpack")
    else:
        print("Error: Items with the same name cannot be swapped.")

    return backpack

def drop(backpack, item):
    """ Takes two arguments, a list called backpack, and one variable,
    item. The item is found in the list and removed. 
    If there are multiple instances of an item,
    the first instance is removed. If the item is not in the list, 
    an error message is printed.""" 
    
    if item in backpack:
        backpack.remove(item)
        print(item + " was dropped from the backpack.")
    else:
        print("Error: " + item + " was not found in the backpack.")

    return backpack
