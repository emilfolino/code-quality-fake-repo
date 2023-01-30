"""Inventory"""


def pick(inv, obj, index=-1):
    """Pick up an object and place it in inventory"""
    if int(index) >= 0 and int(index) <= len(inv):
        inv.insert(int(index), obj)
        print(f"\n'{obj}' has been added in slot {index}")
        
    elif int(index) < 0:
        inv.append(obj)
        print(f"\n'{obj}' has been added to your inventory")
    
    else:
        print(f"Error: '{index}' is too high for a current inventory slot")

    return inv


def inventory(inv, start=0, stop="stop"):
    """Shows the users current inventory"""
    if start == 0 and stop in ("stop", 0):
        print(f"Your inventory contains {len(inv)} items, these are: {inv}")
    
    else:
        slice_interval = slice(start, stop)
        print(f"Your partial inventory contains {len(inv[slice_interval])} items, these are: {inv[slice_interval]}")


def drop(inv, obj):
    """Remove an item from inventory"""
    if obj in inv:
        inv.remove(obj)
        print(f"'{obj}' has been removed from your inventory")
    else:
        print(f"Error: '{obj}' couldn't be removed as it is not in your inventory")

    return inv


def swap(inv, obj1, obj2):
    """Swap inventory slot of 2 items"""
    if obj1 in inv and obj2 in inv and not obj1 == obj2:
        index1 = inv.index(obj1)
        index2 = inv.index(obj2)
        inv[index1] = obj2
        inv[index2] = obj1

        print(f"Objects '{obj1}' and '{obj2}' have now swapped places")
    
    elif not obj1 in inv and not obj2 in inv:
        print(f"Error: Objects '{obj1}' and '{obj2}' are not in your inventory")

    elif not obj1 in inv:
        print(f"Error: Object '{obj1}' is not in your inventory")

    else:
        print(f"Error: Object '{obj2}' is not in your inventory")

    return inv
