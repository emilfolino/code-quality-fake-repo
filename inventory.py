"""
inventory functions for marvin
"""
def pick(bag, item, position = None):
    """
    Pick-function:
    Pick up an item and put it in the backpack, at certain point if wanted. 
    """
    
    if position is None:
        bag.append(item)
        print(bag)
    else:
        if 0 <= int(position) <= len(bag) :
            bag.insert(int(position), item)
        else:
            print(f"Error! Error! There is no position {position}")
        print(f"Item {item} is now at position {position}") 
    return bag


def inventory(bag, start = None, stop = None):
    """
    Inventory function:
    Print contents of backpack. 
    If a sequence is entered, print the contents thereof.
    """
    if start is None and stop is None:
        itemlist = len(bag)
        print(f"The backpack contains following {itemlist} item(s): {bag}")
        return
    try:
        sliced_list = bag[int(start):int(stop)]
        sliced_list_msg = ", ".join(sliced_list)
        print(f"You picked the following item(s): {sliced_list_msg}")
    except IndexError:
        print("Something went wrong")


def drop(bag, trash):
    """
    Drop-function:
    Drop an item from the backpack. Update the contents of the backpack. 
    """
    if trash in bag: 
        bag.remove(trash)
        print(f"All is well. Marvin dropped: {trash}.")
    else: 
        print(f"Error! Error! Could not remove nothing. There was no {trash} to remove.")
    return bag


def swap(bag, item1, item2):
    """
    Swap-function: 
    Let two items swap places. Update the contents of the backpack. 
    """
    fail = False
    if item1 not in bag:
        print(f"Error! Error! {item1} not in bag")
        fail = True
    if item2 not in bag:
        print(f"Error! Error! {item2} not in bag")
        fail = True
    if item1 == item2:
        print("Error! Error!")
        fail = True
    if fail:
        return bag
    place1 = bag.index(item1)
    place2 = bag.index(item2)
    tempItem = bag[place1]
    bag[place1] = bag[place2]
    bag[place2] = tempItem

    print(f"{item1} and {item2} successfully swapped places")
    return bag


def check_extra(choice):
    """
    Check stuff for inventory management
    """
    split_choice = choice.split()
    if len(split_choice) != 3:
        return False
    if split_choice[0] != "inv":
        return False
    try:
        int(split_choice[1])
        int(split_choice[2])
        return True
    except ValueError:
        return False
        
if __name__ == "__main__":
    print("Hello from inventory.py")
    