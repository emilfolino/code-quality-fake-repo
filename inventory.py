#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Contains all functions related to lists.
"""
import marvin

def pick(array, string, index=None):
    """
    Add item to backpack at last index if no index is specified.
    """
    try:
        if index is None:
            array.append(string)
        elif int(index) > len(array):
            print("Error, index " + index + " is to high")
            return array        
        else:
            array.insert(int(index), string)
    except ValueError:
        marvin.not_valid()
        return array

    if index is None:
        print('"' + string + '" has been added')
    else:
        print('"' + string + '" has been added on index "' + index + '".')
    return array

def inventory(array):
    """
    Prints number of items and items them self.
    """

    print("Backpack har " + str(len(array)) + " items: " + str(array))

def drop(array, string):
    """
    Removes item from backpack.
    """
    try:
        array.remove(string)
    except ValueError:
        print('Error. "' + string + '" is not found in the bag.')
        return array
    
    print('"' + string + '" has been removed')
    return array

def swap(array, string1, string2):
    """
    Swaps two items
    """
    if string1 == string2:
        print('Error. "' + string1 + '" and "' + string2 + '" is the same.')
        
    try:
        i, j = array.index(string1), array.index(string2)
        array[i], array[j] = array[j], array[i]
    except ValueError:
        print('Error. "' + string1 + '" or "' + string2 + '" is missing.')
        return array
    
    print('"' + string1 + '" and "' + string2 + '" has been swaped')
    return array
