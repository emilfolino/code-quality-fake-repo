"""
A module called inventory for marvin3
"""

def pick(backpack, pick_item, item_index=False):          
    """The function picks up items and puts in Marvins backpack."""
    if item_index is False:
        #append pick_item till sist i listan
        backpack.append(pick_item)
        print("You want to pick up the item: " + pick_item )
    else:
        #insert pick_item till givet index
        if len(backpack) >= int(item_index): 
            backpack.insert(int(item_index), pick_item)
            print(pick_item, "has index:", str(item_index))
        else:
            print("There was an Error, can't insert picked item in index", str(item_index))
    
    print("The items in the backpack are: " + str(backpack))
    return backpack


def inventory(backpack):
    """The function tells the amount and which things are in backpack."""

    print("There are:", str(len(backpack)), "items in the backpack.")
    print("The items are:", str(backpack))

def drop(backpack, drop_item):
    """The function drops the given item from backpack."""
    if drop_item in backpack:
        backpack.remove(drop_item)
        print("The item:", drop_item, "is dropped from backpack.")
    
    else: 
        print("Error: The item", drop_item, "is not in the backpack!")

    print(backpack)
    return backpack

def swap(backpack, item1, item2):
    """The function swaps places between two items in the backpack."""

    if item1 != item2:
        if item1 in backpack and item2 in backpack:
            i_1 = backpack.index(item1)
            i_2 = backpack.index(item2)
            backpack[i_1] = item2
            backpack[i_2] = item1
        
        elif item1 not in backpack and item2 not in backpack:
            print("Error, there are neither", item1, "nor", item2, "in the backpack!")

        else:
            if item1 not in backpack:
                print("Error:" ,item1, "is not in backpack.")
            elif item2 not in backpack:
                print("Error:" ,item2, "is not in backpack.")
    
    else:
        print("Error! We can't swap identical things with one another!")

    print(backpack)
    return backpack
