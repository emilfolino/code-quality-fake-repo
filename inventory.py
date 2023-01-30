#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Inventory functions for Marvin
"""

def check_sequence(string):
    """
    "Takes a string and checks if it contains
    two ints at position 1 and 2. Returns true
    if thats the case and false otherwise
    """
    #Check the len if it's shorter than 3 it's not a correct string
    if len(string) < 3:
        return False
    #Try to convert the expected "int-strings" to ints
    #If not succesful it's not a correct string
    try:
        int(string[1])
        int(string[2])
    except ValueError:
        return False

    #It is a correct string
    return True

def pick(bag, thing, position=None):
    """
    Takes a list, a value to insert in the list and optionally a position
    in the list where the value should be inserted. If no position 
    is given the function will append the value to the list. Returns the
    modified list.
    """
    #Initialize variable for a message
    message = ""
    #If a third argument(position) is given
    if position is not None:
        try:
            position = int(position)
        except ValueError:
            print("Position must be an int")
            return bag
        #If the position is greater than last index in list
        if position > len(bag) - 1:
            print(f"Error index {position} is not in the bag")
            return bag
        #Insert the second argument (thing) at the third argument (position)
        #using list.insert()
        # then assign a string to message
        bag.insert(position, thing)
        message = f"Added {thing} at position {position} in my bag"
    #No position is given, append the second argument to the list using list.append()
    #Then assign a string to message
    else:
        bag.append(thing)
        message = f"Added {thing} at the last position in my bag"
    #Print the stored string
    print(message)
    return bag

def inventory(bag, start=None, stop=None):
    """
    Takes a list and checks the length, prints a message
    with length of the list and the list. Optionaly
    two ints can be supplied then only the values
    in that range in the list will be printed
    """
    #If argument two and three are given(start and stop indices for a slice)
    if start is not None and stop is not None:
        try:
            start = int(start)
            stop = int(stop)
        except ValueError:
            print("Start and stop values must be ints")
            return
        #Construct and print an output string by slicing the list,
        #using string.join()
        output = ""
        bag_slice = bag[start:stop]
        output = ", ".join(bag_slice)
        print(output)
    #If no start and stop indices are given print
    #nr of items and the list
    else:
        items = len(bag)
        print(f"My bag has {items} items: {bag}")

def drop(bag, thing):
    """
    Takes a list and removes the (first encountered) supplied thing
    from it. If succesful returns the modified list
    """
    #Try to remove the second argument(thing) from the list using list.remove()
    #If thing is not in list print an error message and 
    #return the list
    try:
        bag.remove(thing)
        print(f"Removed {thing} from my bag - I will miss it!" )
        return bag
    except ValueError:
        print(f"Error no {thing} in my bag")
        return bag

def swap(bag, thing1, thing2):
    """
    Takes a list and swaps places between the two supplied things
    in it. If succesful returns the modified list, else returns
    original list
    """
    #Initialize a variable used to determine if there was an error
    error = False
    #Try to find the index of the second argument (thing1) in the list
    #If the thing is not in the list print an error message and set
    #error to True
    try:
        thing1_index = bag.index(thing1)
    except ValueError:
        print(f"Error no {thing1} in my bag!")
        error = True

    #Try to find the index of the third argument (thing2) in the list
    #If the thing is not in the list print an error message and set
    #error to True
    try:
        thing2_index = bag.index(thing2)
    except ValueError:
        print(f"Error no {thing2} in my bag!")
        error = True

    #If there was an error return the unmodified bag
    if error:
        return bag

    #Switch places between the items at the found indices
    temp = bag[thing1_index]

    bag[thing1_index] = bag[thing2_index]

    bag[thing2_index] = temp

    print(f"Switched places between {thing1} and {thing2} in my bag!")

    #Return the modified bag
    return bag
