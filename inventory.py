"""
The inventory functions
"""

# if "inv pick" in choice
def pick(bag, item, place=False):
    """
    Takes arguments bag, item and optional place. 
    Places the given item last in the bag or at the given index position.
    Incase of indexError, original bag will be returned along with an error message.
    """
    if place:
        try:
            check_item = bag[int(place)] # check_item is created in order to check if index in list
            bag.insert(bag.index(check_item), item)
            print(f"{item} was picked up and has index position {str(place)} in backpack.")
        except ValueError:
            print(f"Error, the given index {place} is not a valid integer.")
        except IndexError:
            print(f"Error, {item} can not be picked since {place} index ranges outside of bag")
    else:
        bag.append(item)
        print(f"{item} was picked up and has been placed in backpack.")
    return bag

# if "inv" in choice
def inventory(bag, start="0", stop=0):
    """
    Checks the items as well as the amount of items in the bag and prints it out.
    """
    try:
        if stop == 0:
            item_count = len(bag[int(start):])
            bag = bag[int(start):]
        else:
            item_count = len(bag[int(start):int(stop)])
            bag = bag[int(start):int(stop)]
        print(f"There are a total of {item_count} items. Here is the list of items:")
        print(bag)
    except ValueError:
        print("Either or both start and stop arguments is/are not valid integers.")


# if "inv drop" in choice
def drop(bag, item_drop):
    """
    Drops a given item from bag and prints out a message saying so.
    """
    try:
        bag.remove(item_drop)
        print(f"{item_drop} was dropped from bag.")
    except ValueError:
        print(f"Error, {item_drop} cannot be found in backpack.") 
    return bag

# if "inv swap" in choice
def swap(bag, item1, item2):
    """
    Swaps the places of the two given items.
    """
    if item1 == item2:
        print(f"Error {item1} and {item2} are identical.")
    try:
        swapped1 = [item1]
        index_item1 = bag.index(item1)
        index_item2 = bag.index(item2)
        bag[index_item1:index_item1 + 1] = [item2]
        bag[index_item2: index_item2 + 1] = swapped1
        print(f"{item1} has successfully switched places with {item2}.")
    except ValueError:
        print(f"Error, {item1} or {item2} cannot be found in backpack.") 
    return bag

if __name__ == "__main__":
    backpack = ["alone", "toy", "book", "pencil"]
    inventory(backpack, 2)
