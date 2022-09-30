"""module for handling all the inventory commands."""

def pick(pack, item, ind = None):
    """places an item in the inventory"""
    origPack = pack
    if ind is not None:
        if int(ind) <= len(pack):
            print(str(ind))
            pack.insert(int(ind), item)
            print("the " + item + " was placed at " + ind)
            return pack
        print("Error: index(" + str(ind) + ") out of range")
        return origPack
    pack.append(item)
    print("the " + item + " was placed at the end of the backpack")
    return pack
    
    

def inventory(pack):
    """checks the inventory"""
    print("Backpack has " + str(len(pack)) + " items: " + str(pack))

def drop(pack, item):
    """drops/removes an item from the inventory"""
    origPack = pack
    try:
        pack.remove(item)
        print("Dropped: " + str(item))
        return pack
    except ValueError:
        print("Error: " + str(item) + "was not found in the backpack")
        return origPack

def swap(pack, item1, item2):
    """swaps two items in the inventory"""
    origPack = pack
    try:
        if( item1 == item2 ):
            print("Error: The two items are the same")
            return origPack
        ind1 = pack.index(item1)
        ind2 = pack.index(item2)
        tmp = pack[ind1]
        pack[ind1] = pack[ind2]
        pack[ind2] = tmp
        print("swapped " + str(item1) + " with " + str(item2))
        return pack
    except ValueError:
        print("Error: " + str(item1) + " " + str(item2) + "was not found in the backpack")
        return origPack
