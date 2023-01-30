"""
Functions for marvins inventory
"""

def pick(backpack, item, position="none"):
    """
    Function for adding items to the backpack
    """
    
    if position != "none" and int(position) > len(backpack):
        print(f"Error! The number '{position}' for index seems too high!")
    else:
        if position == "none":
            backpack.append(item)
        else:
            backpack.insert(int(position), item)
        print(f"{item} added to inventory at index {position}")
    return backpack


def inventory(backpack):
    """
    Function for displaying the backpack
    """
    number_of_items = len(backpack)
    print(f"{number_of_items} items.")
    print(backpack)

def drop(backpack, item):
    """
    Function for dropping an item
    """

    try:
        backpack.remove(item)
        print(f"I dropped {item} from my backpack")
    except ValueError: 
        print(f"Error! There's no {item} in my backpack!")
    return backpack

def swap(backpack, item1, item2):
    """
    Function for swaping items
    """
    if item1 in backpack and item2 in backpack:
        if item1 != item2:
            if item1 in backpack:
                if item2 in backpack:
                    index1 = backpack.index(item1)
                    index2 = backpack.index(item2)
                    backpack[index1], backpack[index2] = backpack[index2], backpack[index1]
                    print(f"I swapped {item1} and {item2} for you!")
                else:
                    print(f"Error! There's no {item2} in my backpack!")
            else:
                print(f"Error! There's no {item1} in my backpack!")
        else:
            print(f"Error! Why should we swap {item1} and {item2}, they're the same!")
    else:
        print(f"Error! There's no {item1} or {item2} in my backpack!")
    return backpack
