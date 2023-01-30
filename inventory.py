"""
Module for Marvins inventory
"""

def pick(inv, item, place = -1):
    """
    picks up item and places it into inv at place if place is defined
    """
    place = int(place)
    if place < len(inv):
        if place >= 0:
            inv.insert(place, item)
        else:
            inv.append(item)
        print(''.join(inv) + f"{item} was added at index {place}")
    else:
        print("Error: index too big: 2")
    return inv

def inventory(inv, start = 0, stop = -1):
    """
    prints inventory
    """
    if stop != -1 or start != 0:
        while stop >= len(inv):
            stop-=1
        print(inv[start:stop])
    else:
        print(start, stop)
        print(f"Your inventory has {len(inv)} items:")
        print(inv)

def drop(inv, item):
    """
    drops an item from inventory
    """
    try:
        inv.index(item)
        inv.remove(item)
        print(f"{item} was dropped")
    except ValueError:
        print(f"Error: Item not found, {item}")
    return inv

def swap(inv, item, item1):
    """
    swaps position of two items
    """
    if item is not item1:
        try:
            index1 = inv.index(item)
            inv.remove(item)
            index2 = inv.index(item1)
            inv.remove(item1)
            inv.insert(index2, item)
            inv.insert(index1, item1)
            print(f"{item} has swapped places with {item1}")
        except ValueError:
            missing = item if inv.count(item) == 0 else ""
            missing1 = item1 if inv.count(item1) == 0 else ""
            print(f"Error: One or more items not found, {missing} {missing1}")
    else:
        if inv.count(item) == 2:
            print("Error: ambiguous reference")
        else:
            print(f"{item} has swapped places with {item1}")
    return inv
