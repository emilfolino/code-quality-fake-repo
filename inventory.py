"""
Here is the inventory FUNCTIONS
"""

def pick(backpack, picker, pos = ""):
    """
    Puts thing in another thing
    """
    try:
        pos = int(pos)
        if len(backpack) >= pos >= 0:
            backpack.insert(pos,picker)
        elif pos >= len(backpack):
            print("Error")
            print(pos)
            return backpack
        else:
            backpack.append(picker)
    except ValueError:
        backpack.append(picker)
    for (i, item) in enumerate(backpack):
        print(i,item)
    return backpack

def inventory(backpack, start = "", stop = ""):
    """
    Backpack size
    """
    if start != "" and stop != "":
        print(backpack[start:stop])
    else:
        print(backpack)
        print(len(backpack))

def drop(backpack, the_thing):
    """
    Throw away thingy in backpacky
    """
    if(the_thing in backpack):
        backpack.remove(the_thing)
        print(the_thing, " Kastades")
    else:
        print(the_thing)
        print("Error")
    return backpack

def swap(backpack, the_thing, right_thing):
    """
    Swappy thingy in the backpack
    """
    if the_thing in backpack and right_thing in backpack and the_thing != right_thing:
        i = backpack.index(the_thing)
        y = backpack.index(right_thing)
        backpack[i], backpack[y] = backpack[y], backpack[i]
    elif the_thing not in backpack and right_thing not in backpack:
        print("Error")
        print(the_thing, right_thing)
    elif the_thing == right_thing:
        print("Error")
    elif the_thing not in backpack:
        print("Error")
        print(the_thing)
    elif right_thing not in backpack:
        print("Error")
        print(right_thing)
    print(backpack)
    return backpack
