"""
Module for Marvin inventory
"""


def pick(backpack, item, index=-1):
    """
    Add an item to the backpack
    """
    if index == -1:
        backpack.append(item)
        print(f"{item} has been added")
    elif int(index) + 1 > len(backpack):
        print(f"Error: Index {index} too big")
    else:
        backpack.insert(int(index), item)
        print(f"{item} has been added on index {index}")
    return backpack


def inventory(backpack):
    """
    Prints how many and what items in backpack
    """
    print(f"Backpack has {len(backpack)} items {backpack}")


def drop(backpack, item):
    """
    Drops an item and removes it from the list
    """
    drop_item = item.replace("inv drop ", "")
    try:
        backpack.remove(drop_item)
        print(f"{drop_item} has been dropped")
    except ValueError:
        print(f"Error: {drop_item} not in list")
    return backpack


def str_to_list(string):
    """
    Makes a list out of a string
    """
    new_list = string.split(" ")
    return new_list


def swap(backpack, item_one, item_two):
    """
    Swaps two items
    """
    if item_one != item_two:
        try:
            index_of_one = backpack.index(item_one)
            index_of_two = backpack.index(item_two)
        except ValueError:
            print(f"Error: {item_one} or {item_two} not in list")
        else:
            backpack.insert(index_of_one, item_two)
            backpack.pop(index_of_one + 1)
            backpack.insert(index_of_two, item_one)
            backpack.pop(index_of_two + 1)
            print(f"{item_one} and {item_two} is now swapped ")
    else:
        print("Error")
    return backpack
