"""
inventory
"""
import main


def pick(backpack, item, position=-1):
    """
    Picks up an item and places it last in backpack,
    or picks up an item and places it at specified index-point in the list.
    """
    if position == -1:
        backpack.append(item)
        print(f"You picked up the {item}.")

    elif int(position) > len(backpack):
        print(f"Error: Your index {int(position)} is too high.")

    else:
        backpack.insert(int(position), item)
        print(f"You picked up the {item} and added it to position {int(position)}")

    main.backpack = backpack
    return backpack

def swap(backpack, item, item2):
    """
    Swaps an item in backpack with another one.
    """
    if len(backpack) == 0:
        print(f"Error: your inventory is empty. The {item} and the {item2} could not be swapped.")

    elif item not in backpack or item2 not in backpack:
        print(f"Error: You do not have either {item} or {item2} in your inventory, the switch could not be made.")

    elif item == item2:
        print("Error: You can not switch the same item.")

    else:
        a = backpack.index(item)
        b = backpack.index(item2)
        backpack[a], backpack[b] = backpack[b], backpack[a]
        print(f"You swapped the place of the {item} with the place of the {item2}.")

    main.backpack = backpack
    return backpack

def drop(backpack, item):
    """
    Drops an item in your backpack.
    """
    if item in backpack:
        backpack.remove(item)
        print(f"You threw out the {item} from your backpack.\nYour current items in your backpack are: {backpack}.")
    
    elif item not in backpack:
        print(f"Error: There is no {item} in your backpack.\nYour current items in your backpack are: {backpack}.")
    
    main.backpack = backpack
    return backpack

def inventory(backpack):
    """
    Your inventory.
    """
    baginventory = backpack
    return print(f"There are {len(baginventory)} items in your backpack. The items contained are: {baginventory}.")
