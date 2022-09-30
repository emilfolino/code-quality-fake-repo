#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Inventory fucntions. A collection of functions that main.py will call when
selected from the menu.
"""


def pick(backpack, item, index=None):
    """
    Adds item to backpack at index if index is passed, at end if not
    Prints what was done and returns updated backpack
    """
    if index is not None and len(backpack) < int(index):
        print(f"Error, index {index} out of range")
        return backpack
    if index is not None:
        backpack.insert(int(index), item)
        print(f"{item} was added at index {index}")
        return backpack
    backpack.append(item)
    print(f" {item} was added at the end of the backpack")
    return backpack


def inventory(backpack, start=0, stop=None):
    """
    Prints contents of backpack and number of items
    """

    number_items = len(backpack[start:stop])
    if number_items > 0:
        items = ""
        items = items.join(backpack[start:stop])
        print(
            f"The backpack contains {number_items} items and they are: {items}")
    else:
        print(f"Error, {backpack} contains {number_items} items")


def drop(backpack, item=None):
    """
    Drops item from backpack, returns updated backpack
    """
    if item in backpack:
        backpack.remove(item)
        print(f"{item} was removed from the backpack")
        return backpack

    print(f"Error, {item} was not in the bag!")
    return backpack


def swap(backpack, item1=None, item2=None):
    """
    Swaps index between item1 and item2, returns updated backpack
    """
    new_bag = []
    if item1 in backpack and item2 in backpack and item1 != item2:
        for item in backpack:
            if item == item1:
                new_bag.append(item2)
            elif item == item2:
                new_bag.append(item1)
            else:
                new_bag.append(item)
        print(f"{item1} and {item2} successfully swapped!")
        return new_bag
    print(f"Error, {item1} or {item2} is not in the bag or the same")
    return backpack
