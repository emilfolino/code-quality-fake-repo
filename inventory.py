"""
inventory, functions
"""
#Till alla except skrev jag först bara så except 
# så den kunde fånga alla fel men det fick jag ej för pylint

def pick(bag, item, index1="defult"):
    """
    pick
    """
    if index1 == "defult":
        index1 = len(bag)
    if int(index1) > len(bag):
        print(f"Error! {int(index1)} is larger than your bag!")
    else:
        bag.insert(int(index1), item)
        print(f"item has been placed at index {index1} in bag\n{bag}")
    return bag

def inventory(bag):
    """
    inventory
    """
    print(f"Your bag has: {len(bag)} items and contains: {bag}")

def drop(bag, item):
    """
    drop
    """
    try:
        if bag.index(item) is not None:
            bag.remove(item)
            print(f"{item} has been dropped from bag!")
            print(bag)
    except ValueError:
        print(f"There has been a Error! {item} does not exist!")
    print(bag)
    return bag

def swap(bag, item, item2):
    """
    swap
    """
    backupBag = bag
    try:
        index1 = bag.index(item)
        index2 = bag.index(item2)
        if index1 is index2:
            print(f"Error! you are tying to move {index1} to {index2}´s location")
            bag = backupBag
        else:
            bag[int(index2)] = item
            bag[int(index1)] = item2
    except (IndexError, ValueError, UnboundLocalError):
        print(f"Error! due to {item} and {item2}")
    print(bag)
    return bag
