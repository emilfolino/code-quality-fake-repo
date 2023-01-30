
"""
Functions for inventory manegment
"""


def pick(backpack, thing, index=None):
    """
    Function to pick "thing" up and place it in the "backpack" on the "index" position
    """
    if index is not None:
        if int(index) >= len(backpack):
            print("Error")
            print(f"{thing} was not added to your inventory")
            print(f"Reason: {int(index)} is too high of a number")
        else:
            backpack.insert(int(index), thing)
            print(f"{thing} has been added to your inventory")
            print(f"{thing} was placed as your {int(index)} item")
    elif index is None:
        backpack.append(thing)
        print(f"{thing} has been added to your inventory")
    return backpack


def inventory(backpack):
    """
    Tells the length and value of the input
    """
    amount = len(backpack)
    print(f"There are {amount} items inside your backpack")
    print(f"The items that you have gathered are: {backpack}")


def drop(backpack, thing):
    """
    Removes second input from first input
    """
    if check(backpack, thing, False) is True:
        backpack.remove(thing)
        print(f"The item {thing} has now been removed from your inventory")
    return backpack

def swap(backpack, first, second):
    """
    Swaps the position of two inputs, inside the first input
    """
    if check(backpack, first, second) is True:
        index_one = backpack.index(first)
        index_two = backpack.index(second)
        backpack[index_one], backpack[index_two] = backpack[index_two], backpack[index_one]
        print(f"{first} and {second} have now switched place in your inventory")
    return backpack

def check(backpack, first, second):
    """
    Checks if all inputs are existing
    """
    value = True
    if first in backpack:
        if second is False or second in backpack:
            value = True
        else:
            value = False
            print("Error")
            print(f"{second} is not in your invetory")
    else:
        if second is False or second in backpack:
            value = False
            print("Error")
            print(f"{first} is not in your inventory")
        else:
            value = False
            print("Error")
            print(f"{first} and {second} is not in your inventory")
    return value
