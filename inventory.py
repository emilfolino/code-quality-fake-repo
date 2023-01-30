"""
Inventory functions
"""

def pick(bag:list, item, index=None): 
    """Puts item into bag either at the end of the list or at the given index"""
    try:
        if index is None:
            bag.append(item)
            print("Added " + item + " to bag.")
        else:
            # Raise error if index is too big or less than 0
            if (int(index) > len(bag)) or (int(index) < 0): 
                raise IndexError("Index " + str(index) + " is out of expected bounds")

            bag.insert(int(index), item)
            print("Added " + item + " to bag at index " + index)
    except IndexError as e:
        print("Error: "+ str(e))
    return bag

def inventory(bag:list, start=0, stop=None):
    """Prints a message with the current elements of the bag. Now optionally in a index range"""
    if (stop is None):
        print("bag has " + str(len(bag)) + " items: " + str(bag))
    else:
        print("" + str(bag[int(start):int(stop)]))

def drop(bag:list, item):
    """Deletes an item from the bag"""
    try:
        bag.remove(item)
        print("Removed " + item)
    except ValueError:
        print("Error: " + item + " does not exist in list")
    return bag

def swap(bag:list, item1, item2):
    """Swaps positions of two items in the bag"""
    try:
        i1 = bag.index(item1)
        i2 = bag.index(item2)

        # Raise error if item1 and item2 are the same
        if i1 == i2:
            raise ValueError("values can not be identical")

        bag[i1] = item2
        bag[i2] = item1

        print("Swapped position of " + item1 + " and " + item2)
    except ValueError as e:
        print("Error: Could not swap, " + item1 + " and " + item2 + ". " + str(e)) # 'value' is not in list
    return bag
