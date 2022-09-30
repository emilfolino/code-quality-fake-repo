""" Module for inventory functions"""

def SplitInputIntoList(inputArg):
    """Function which splits the userinput into a list"""
    x = list(map(str, inputArg.split(',')))
    return x

def swap(arg1, arg2, arg3):
    """ Swap two items"""
    newBackpack = arg1
    item1Found = False
    item2Found = False
    msg = ""
    try:
        a = newBackpack.index(arg2)
        #print("a:", a, " : ", arg2)
        item1Found = True
    except Exception:
        msg += arg2 + "not found "
    try:
        b = newBackpack.index(arg3)
        #print("b:", b, " : ", arg3)
        item2Found = True
    except Exception:
        msg += arg3 + "not found "

    if not item1Found or not item2Found:
        print("Error ", msg)
        return newBackpack

    print("newBackpack[b]", newBackpack[b])
    print("newBackpack[a]", newBackpack[a])

    newBackpack[b], newBackpack[a] = newBackpack[a], newBackpack[b]
    return newBackpack


def drop(arg1, arg2):
    """ Drop a item"""
    newBackpack = arg1
    dropedItem = False
    while arg2 in arg1:
        newBackpack.remove(arg2)
        print(arg2, " successfully removed from backpack!")
        dropedItem = True
    if not dropedItem:
        print("Error item does no exist in backpack: ", arg2)
        return newBackpack
    return newBackpack


def inventory(arg1):
    """ Inv information"""
    backpackLength = len(arg1)
    msg = str(backpackLength)+ " "
    print(msg," ", arg1)


def DoesItemExistReturnIndex(listArg, item):
    """Check if a item exist in a list and return its index """
    try:
        return listArg.index(item)
    except Exception:
        return -1


def pick(arg1, arg2, arg3=False):
    """ Adding new item to backpack"""
    newBackpack = arg1
    backpackLength = len(newBackpack)
    if not arg3:
        newBackpack.append(arg2)
        print(arg2, " has been added last in backpack")
    else:
        #ar2 = DoesItemExistReturnIndex(arg1, arg2)
        #print("backpackLength-1 :" , backpackLength-1, "int(arg3): ", int(arg3))
        if int(backpackLength-1) >= int(arg3):
            newBackpack.insert(int(arg3), arg2)
            print(arg2, " has been added go backpack at position ", arg3)
        else:
            print("Error index out of bounce ", arg3)
    return newBackpack
