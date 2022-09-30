"""Module with functions for marvin ver3"""

def pick(backpack, item, index=-1):
    """adds item to backpack list"""
    if index == -1:
        backpack.append(item)
        print(item + " has been added to your backpack")
    else:
        if int(index) > len(backpack):
            print(f"Error: {index} doesn't exist in backpack")
        else:
            backpack.insert(int(index), item)
            print(item + " has been added to your backpack at position " + str(index))
    return backpack

def inventory(backpack):
    """prints backpack"""
    amount = len(backpack)
    print(f"There is {amount} items in the backpack. Here are the items: {backpack}")

def drop(backpack, item):
    """Removes item from backpack"""
    try:
        backpack.remove(item)
    except ValueError:
        print(f"Error: You didn't specify what to remove or {item} doesn't exist")
        return backpack
    else:
        print(f"{item} was removed from the backpack")
        return backpack

def swap(backpack, item, item2):
    """swaps places of items in backpack"""
    if item == item2:
        print(f"Error: {item} and {item2} are the same")
        return backpack
    try:
        index = backpack.index(item)
        index2 = backpack.index(item2)
        backpack[index], backpack[index2] = backpack[index2], backpack[index]
        print(f"{item} and {item2} swapped places in the backpack")
    except ValueError:
        if item or item2 not in backpack:
            print(f"Error: {item} or {item2} is not in backpack")
    return backpack
