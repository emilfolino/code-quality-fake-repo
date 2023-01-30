"""
Function page for inventory
"""
def inventory(backpack):
    """
    Shows inventory
    """
    total_items= len(backpack)
    print(f"The backpack has {total_items} items and those are {backpack}")

def pick (backpack, item, pos = -1):
    """
    Pickup item
    """
    pos = int(pos)
    if pos <= (len(backpack) - 1):
        if pos > -1:
            backpack.insert(pos, item)
            print(f"'{item}' has been added to the backpack in position {pos}")
            
        else:
            backpack.append(item)
            print(f"'{item}' has been added to the backpack")
    else:
        print(f"Error {pos} is to high of index")
    
    return backpack

def drop(backpack, item):
    """
    Drop item
    """
    try:
        backpack.remove(item)
        print(f"{item} have been removed from the backpack")
    except ValueError:
        print(f"Error {item} does not exist in the backpack")
    
    return backpack

def swap(backpack, item1, item2):
    """
    Swap items
    """
    print(item1)
    print(item2)
    try:
        item1_index = backpack.index(item1)
        item2_index = backpack.index(item2)

        backpack[item1_index] = item2
        backpack[item2_index] = item1

        print(f"{item1} have swap place with {item2} in the backpack")
    except ValueError:
        print(f"Error {item1} and/or {item2} does not exist in the backpack")

    return backpack
