""""
"""
def pick(backpack, argument, position=None):
    """
    function for picking up items in backpack with or without specific position
    """
    try:
        if not argument:
            print("Error: you did not enter an item to pick to backpack")
            return backpack
        if argument not in backpack:
            if position:
                if int(position) > len(backpack):
                    print("Error:" + str(position) + " Too high index number")
                    return backpack
                backpack.insert(int(position), argument)
                print(argument + " Was added to backpack in position: " + str(position))
            if not position:    
                backpack.append(argument)
                print(argument + " Was added to backpack")
        else:
            print(argument + " Already in backpack")
    except IndexError: 
        print("Error: you did not enter valid item to pick in backpack")
        
    return backpack


def inventory(backpack):
    """
    Printing out current items in backpack
    """
    num_item = len(backpack)
    print("There are currently " + str(num_item) + " items in backpack")
    print(backpack)

def drop(backpack, argument):
    """
    Deleting items from backpack
    """
    try:
        backpack.remove(argument)
        print(argument + " Is no longer in backpack")
    except ValueError:
        print("Error: " + argument + " There is no such item in backpack")
    return backpack

def swap(backpack, thing, other_thing): 
    """
    swaps position for two items in backpack
    """
    try:
        if thing == other_thing:
            print("Error")
        pos1 = backpack.index(thing)
        pos2 = backpack.index(other_thing)
        backpack[pos1], backpack[pos2] = backpack[pos2], backpack[pos1] 
        print(thing + " Has swapped place with " + other_thing)
    except ValueError:
        print("Error: " + thing + other_thing + " There is no such item in backpack")
        return backpack
    return backpack
