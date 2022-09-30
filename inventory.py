"""
You can manipulate lists with these 'inv' commands.
"""

def pick(backpack, item, i=None):
    """
    Adds an item to the backpack at the optional index i, prints confirmation or error
    and returns new inventory.
    """
    if i is None:
        backpack.append(item)
        print("My log added '{item}'.".format(item=item))
    else:
        try:
            i = int(i)
        except ValueError:
            print("My log is upset that you entered a non-integer index.")
            return backpack
        if i >= len(backpack) or i <= len(backpack) * -1:
            print("Error: Index {} not found.".format(i))
        else:
            backpack.insert(i, item)
            print("My log added '{item}' at index {i}.".format(item=item, i=i))
    return backpack

def inventory(backpack, start=None, stop=None):
    """
    Prints the number of items and a list of items in the inventory,
    with optional start and stop indices.
    """
    if start is None and stop is None:
        print("Your backpack contains {} item(s):".format(len(backpack)))
        print(backpack)
    else:
        try:
            start = int(start)
            stop = int(stop)
            print(backpack[start:stop])
        except ValueError:
            print("Error: The stop and start indices must be integers.")

def drop(backpack, item):
    """
    Removes an item from the inventory.
    """
    if item in backpack:
        backpack.remove(item)
    else:
        print("Error: '{}' not in backpack.".format(item))
    print("My log removed '{}'.".format(item))
    return backpack

def swap(backpack, item_i, item_j):
    """
    "Swap two items' places in the inventory."
    """
    if item_i == item_j:
        print("Error: The items have the same name. That's too confusing. Don't do that.")
    elif item_i not in backpack and item_j not in backpack:
        print("Error: Neither '{}' nor '{}' in backpack.".format(item_i, item_j))
    elif item_i not in backpack:
        print("Error: '{}' not in backpack.".format(item_i))
    elif item_j not in backpack:
        print("Error: '{}' not in backpack.".format(item_j))
    else: 
        i = backpack.index(item_i)
        j = backpack.index(item_j)
        backpack[j:j+1] = [item_i]
        backpack[i:i+1] = [item_j]
        print("My log swapped the positions of {} and {}.".format(item_i, item_j))
    return backpack
