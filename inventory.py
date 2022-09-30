#!/usr/bin/env python3

"""
Inventory for Marvin
"""

def pick(backpack, item, index = None):
    """
    Adds item to backpack
    """
    if index is None:
        backpack.append(item)
    elif int(index) < len(backpack):
        backpack.insert(int(index), item)
    else:
        print(f"Error: index {index} too high")
        return backpack
    print(f"{item} added to backpack" + f" at index {index}" * int(index is not None))
    return backpack

def inventory(backpack):
    """
    Prints contents of backpack
    """
    print("Backpack contains", len(backpack), "items")
    print(backpack)

def drop(backpack, item):
    """
    Drops item from backpack
    """
    try:
        backpack.remove(item)
    except ValueError:
        print(f"Error: item {item} not in backpack")
        return backpack
    print(f"Dropped {item} from backpack")
    return backpack

def swap(backpack, item1, item2):
    """
    Swap places for item1 and item2 in backpack
    """
    if item1 == item2:
        print("Error: items are identical")
        return backpack
    error = False
    try:
        index1 = backpack.index(item1)
    except ValueError:
        print(f"Error: item {item1} not in backpack")
        error = True
    try:
        index2 = backpack.index(item2)
    except ValueError:
        print(f"Error: item {item2} not in backpack")
        error = True
    if error:
        return backpack
    backpack[index1] = item2
    backpack[index2] = item1
    print(f"Swapped places for {item1} and {item2}")
    return backpack
