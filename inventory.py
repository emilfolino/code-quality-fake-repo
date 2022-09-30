#!/usr/bin/env python3

"""Functions managing Marvin's backpack."""

def inventory(backpack):
    """Print what's in the backpack"""
    print("There are", len(backpack), "items in the backpack.")
    print("The items in the backpack are: ", backpack)

def pick(backpack, item, position = ""):
    """Pick up an item and put it in the backpack"""
    if position == "":
        backpack.append(item)
        print(item, "was picked up and put in the backpack.")        
    else:
        try:
            if len(backpack) >= int(position):
                backpack.insert(int(position), item)
                print(item, "was picked up and put in the backpack",
                      "on position", int(position))
            else:
                print("Error, the position", position, "is greater",
                      "than the amount of items in the backpack.")
        except ValueError:
            print("Error, the position must be an integer.")
    return backpack

def swap(backpack, item1, item2):
    """Swap places on two items in the backpack"""
    error = False
    try:
        index1 = backpack.index(item1)
    except ValueError:
        print("Error", item1, "does not exist in the backpack.")
        error = True
    try:    
        index2 = backpack.index(item2)
    except ValueError:
        print("Error", item2, "does not exist in the backpack.")
        error = True
    if error:
        pass
    elif index1 == index2:
        print("Error, two different items are required for me to",
              "switch their places.")
    else:
        backpack[index1], backpack[index2] = backpack[index2],\
        backpack[index1]
        print("The", item1, "switched places with the", item2)
    return backpack

def drop(backpack, item):
    """Drop an item from the backpack"""
    try:
        backpack.remove(item)
        print(item, "was dropped from the backpack.")
    except ValueError:
        print("Error, there is no", item, "in the backpack.")
    return backpack
