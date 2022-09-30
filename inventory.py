#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
This file handles Marv-inu's inventory
"""

import marvin

def inventory(bag, start_index = None, end_index = None):
    """Function to display Marv-inu's inventory"""

    try:
        selected_items = bag[int(start_index) : int(end_index)]
        marvinu_message = f"There are {len(selected_items)} items between index {start_index} and {end_index}: "
        marvinu_message += f"{selected_items}"
    except TypeError:
        marvinu_message = f"I have {len(bag)} items in there: {bag}"
    finally:
        marvin.redraw_marvinu(marvinu_message)

def pick(bag, item, bag_index = None):
    """Function to pick things up and put them in Marv-inu's inventory"""
    disclaimer = ""

    try:
        bag_index = int(bag_index)
        if bag_index > len(bag):
            plural_s = ""
            verb = "is"
            if len(bag) > 1:
                plural_s = "s"
                verb = "are"
            marvinu_message = f"Error! I cant put the {item} at index {bag_index}, "
            marvinu_message += f"there {verb} only {len(bag)} thing{plural_s} in there!"
        elif bag_index < 0:
            marvinu_message = f"Error! I cant put the {item} at a negative index!"
    except ValueError: # If the third argument is not an int, add it to the item.
        item += " " + bag_index # This way Marv-inu can pick upp two-word items like "sea cucumber"
        marvinu_message = f"I picked up {item}!"
        marvinu_message += "\n I won't be able to drop it or swap it though, since it has more than one word in it."
        bag.append(item)
        marvin.redraw_marvinu(marvinu_message)
        return bag
    except TypeError: # If there is no third argument
        bag.append(item)
        marvinu_message = f"I picked up {item}!  {disclaimer}"

    if bag_index is not None and bag_index in range(len(bag)):
        bag.insert(bag_index, item)
        marvinu_message = f"I picked up {item} and added it to index {bag_index}!"



    marvin.redraw_marvinu(marvinu_message)
    return bag


def drop(bag, item):
    """Function to drop things from Marv-inu's inventory"""

    try:
        item_index = bag.index(item)
        bag.remove(item)
        marvinu_message = f"Removed {item} from index {item_index}!"
    except ValueError:
        marvinu_message = f"Error! I can't find any {item} in there!"

    marvin.redraw_marvinu(marvinu_message)
    return bag

def swap(bag, item_1, item_2 = None):
    """Function to swap two things in Marv-inu's inventory"""

    if item_1 == item_2:
        item_2 = None
    try:
        item_1_index = bag.index(item_1)
        item_2_index = bag.index(item_2)
        bag[item_1_index] = item_2
        bag[item_2_index] = item_1
        marvinu_message = f"Swapped {item_1} and {item_2}!"


    except ValueError:
        if item_2 is None:
            marvinu_message = "Error! You have to tell me two things to swap"
            if item_1 in bag:
                marvinu_message += f", I can't just swap the {item_1} with itself"
            marvinu_message += "!"

        if item_1 not in bag and item_2 not in bag:
            not_found = f"{item_1} or {item_2}"
        elif item_1 not in bag:
            not_found = item_1
        elif item_2 not in bag:
            not_found = item_2

        if item_2:
            marvinu_message = f"Error! I can't find any {not_found} in there!"


    marvin.redraw_marvinu(marvinu_message)
    return bag
