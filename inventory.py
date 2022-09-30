"""Inventory Docstring"""

def inventory(backpack):
    """
    Backpack
    """
    print(f"There are {len(backpack)} items in the backpack and they are {backpack}")



def pick(backpack, item, i=-1):
    """Pick up items to put in your backpack """
    if i == -1:
        backpack.append(item)
        print(f"You picked up {item} and put it in the backpack at position {(len(backpack))}.")
    
    elif int(i) > len(backpack):
        print(f"Error. It doesn't fit here{i}.")

    else:
        backpack.insert(int(i), item)
        print(f"You successfully picked up {item} and put it {i} in order.")

    return backpack



def drop(backpack, item):
    """Removes the item from your backpack"""
    if item not in backpack:
        print(ValueError(f"Error. {item} wasn't in the backpack and could therefore not be removed."))

    
    else: 
        backpack.pop(backpack.index(item))
        print(f"{item} has now been removed from your backpack.")
    return backpack



def swap(backpack, item1, item2):
    """
    Swap places between items in your backpack.
    """
    if item1 == item2:
        print("Error, can't swap the same item. ")
        return backpack
    backpack_list = []
    try:
        if item1 not in backpack:
            backpack_list.append(item1)
        if item2 not in backpack:
            backpack_list.append(item2)
        if backpack_list:
            raise ValueError
        backpack[backpack.index(item2)] = item1
        backpack[backpack.index(item1)] = item2
        print(f"{item1} and {item2} have swapped places in your backpack. ")
        return backpack

    except ValueError:
        if len(backpack_list) == 2:
            print(f"Error! Either or  {backpack_list[0]} and {backpack_list[1]} isn't in your backpack")

        else:
            print(f"Error, There's no {backpack_list[0]}")
            print("You can't swap something that's not in your backpack. ")
        return backpack
#Error line 66 "There's no swap"
#Den sätter in swap som ett index i backpack_list 
