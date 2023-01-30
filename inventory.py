"""Marvin backpack code"""


def pick(bp: list, thing: str, index=-1) -> list:
    """
    Add a thing to backpack.
    If index is given, insert thing at index.
    """
    if index == -1:
        bp.append(thing)
        print("You picked up the {}.".format(thing))
    else:
        index = int(index)
        print(index)
        if(len(bp)-1 < index):
            print("Error, item {} cant be picked up since index out of range {}".format(
                thing, index))
        else:
            bp.insert(index, thing)
            print("You picked up the {} at index {}.".format(thing, index))
    return bp


def drop(bp: list, thing: str) -> list:
    """
    Remove a thing from backpack.
    """
    try:
        bp.remove(thing)
        print("You dropped the {}.".format(thing))
    except ValueError:
        print("Error, you dont have {}".format(thing))
    return bp


def swap(bp: list, thing1: str, thing2: str) -> list:
    """
    Swap two things in backpack.
    """
    if thing1 == thing2:
        print("Error, thats the same thing")
        return bp
    try:
        t1Index = bp.index(thing1)
        t2Index = bp.index(thing2)
        bp[t1Index] = thing2
        bp[t2Index] = thing1

        print("You swapped {} and {}.".format(thing1, thing2))
    except ValueError:
        print("Error, you dont have {} or {}".format(thing1, thing2))
    return bp


def inventory(bp: list, start="", stop="") -> list:
    """Prints backpacks items"""
    if (start == "" and stop == ""):
        print("You have {} items".format(len(bp)))
        print(bp)
    else:
        print("You have {} items".format(len(bp[int(start):int(stop)])))
        print(bp[int(start):int(stop)])
