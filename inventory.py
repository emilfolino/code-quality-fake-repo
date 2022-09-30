""" Inventory Module """


def pick(backpack, item, index=None):
    """Cark will add an item to the backpack"""
    if index is not None:
        index = int(index)
        if index > (len(backpack) - 1):
            print(f"Error: {index} out of bounds")
            return backpack
        backpack.insert(index, item)
        print(f"{item} was added to the backpack at position {index}")
    else:
        backpack.append(item)
        print(f"{item} was added to the backpack at position {len(backpack)-1}")
    return backpack


def inventory(backpack):
    """Cark will list the items in the backpack"""
    print(f"{len(backpack)} items are in the backpack. These are the items: {backpack}")


def drop(backpack, item):
    """Cark will remkove the specified item from the backpack"""
    if item not in backpack:
        print(f"Error: {item} is not in the backpack")
    else:
        backpack.remove(item)
        print(f"{item} was removed from the backpack")
    return backpack


def swap(backpack, item1, item2):
    """Cark will swap places for the specified items"""
    if item1 not in backpack and item2 not in backpack:
        print(f"Error: {item1} and {item2} are not in the backpack.")
        return backpack
    if item1 not in backpack:
        print(f"Error: {item1} is not in the backpack.")
        return backpack
    if item2 not in backpack:
        print(f"Error: {item2} is not in the backpack.")
        return backpack
    item1_index = backpack.index(item1)
    item2_index = backpack.index(item2)
    backpack[item1_index] = item2
    backpack[item2_index] = item1
    print(f"Swapped positions for {item1} and {item2}.")
    return backpack
