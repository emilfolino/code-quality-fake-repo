"""
Inventory for marvin
"""
def pick(bp, x, i=-1):
    """
    Add item too backpack
    """
    if i == -1:
        bp.append(x)
        print("pick up one “" + x + "” and put in at the end of the inventory")
        return bp
    if int(i) >= len(bp) and i != 0:
        print("Error! Index " + str(i) + " is too high.")
    elif int(i) < -len(bp):
        print("Error! Index " + str(i) + " is too low.")
    else:
        bp.insert(int(i), x)
        print("pick up one “" + x + "” and on index “" + str(i) + "” in inventory")
    return bp

def drop(bp, x):
    """
    Remove item from backpack
    """
    try:
        bp.remove(x)
    except ValueError:
        print("Error! " + x + " is not in inventory.")
        return bp
    print("Throw away " + x)
    return bp

def swap(bp, x, y):
    """
    Swap places on two items
    """
    if x == y:
        print("Error! Cant swap a item with it self.")
        return bp

    try_x = try_y = True
    try:
        index1 = bp.index(x)
    except ValueError:
        try_x = False
    try:
        index2 = bp.index(y)
    except ValueError:
        try_y = False
    if try_x is False and try_y is False:
        print("Error! " + x + " and " + y + " is not in inventory.")
    elif try_x is False:
        print("Error! " + x + " is not in inventory.")
    elif try_y is False:
        print("Error! " + y + " is not in inventory.")
    else:
        bp.remove(x)
        bp.insert(index2, x)
        bp.remove(y)
        bp.insert(index1, y)
        print("Swap places on " + x + " and " + y)
    return bp

def inventory(bp, s=0, e=-1):
    """
    Show contents in backpack
    """
    if e == -1:
        e = len(bp)
    print("The number of items is " + str(len(bp[s:e])) + " and the items are: ", bp[s:e])
