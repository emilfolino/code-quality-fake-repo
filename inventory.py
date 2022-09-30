
""" 
This module contains functions for extra inv options when using Marvin
"""


def pick(inv, item, pos = -1):
    """Adds an item into the backpack at the selected index. If no index add it last."""
    if int(pos) > len(inv):
        print(f"Error: Index {pos} too high.")
        return inv
    if pos == -1:
        inv.append(item)
    else:
        inv.insert(int(pos),item)
    print(f"{item} was added into the backpack at index {pos}")
    return inv

def inventory(inv,start=0,stop=-1):
    """Prints info about the inventory's content"""
    if start != 0 or stop != -1:
        print (inv[start:stop])
    else:
        for item in inv:
            print(item)
    invCount = len(inv)
    print("The inventory contains " + str(invCount) + " items.")
    
def drop(inv,item):
    """Removes an item from the inventory"""
    if item in inv:
        inv.remove(item)
        print(f"{item} was removed from the inventory.")
        return inv
    print(f"Error: No {item} in the inventory.")
    return inv

def swap(inv,item1,item2):
    """Swap two items."""
    if item1 == item2:
        print("Error: Same item twice.")
        return inv
    if item1 not in inv or item2 not in inv:
        print(f"Error: {item1} or {item2} not in list.")
        return inv
    newInv = inv.copy()
    newInv[inv.index(item1)] = item2
    newInv[inv.index(item2)] = item1
    print(f"{item1} was swapped with {item2}.")
    return newInv
