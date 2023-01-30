#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Functions for Phoenix to add more options to my chatbot
"""
def inventory(bag):
    """
    Function that shows the size and the content of the bag
    """
    count = len(bag)

    print("There are %s item(s) in the bag:" % str(count), bag)


def pick(bag, item, index = None):
    """
    function that adds item into bag
    """
    if index is None:
        bag.append(item)
        print(item + " has been added to the bag")

    elif len(bag) > int(index):
        bag.insert(int(index), item)

        print(item + " has been added to the bag at index " + str(index))

    elif len(bag) < int(index):

        print("Error: the bags size isn't " + str(index) + " yet")

    else:
        bag.append(item)
        print(item + " has been added to the bag")


    return bag




def drop(bag, item):
    """
    Function that removes an item from the bag
    """
    try:
        bag.remove(item)
        print("%s has been removed from the bag" % item)
        return bag

    except ValueError:
        print("Error: %s is missing in a bag", item)
        return bag


def swap(bag, item1, item2):
    """
    function that swaps items in a bag
    """
    if item1 == item2:
        print("Error: cant swap same items")


    try:
        first_item = item1

        second_item = item2
        
        first_item_1 = bag.index(first_item)

        second_item_2 = bag.index(second_item)

        bag[first_item_1], bag[second_item_2] = bag[second_item_2], bag[first_item_1]

        print(first_item + " and " + second_item  + " have been swapped")

    except ValueError:
        print("Error: " + first_item + " or " + second_item + " is missing from the bag")
    
    return  bag

    
