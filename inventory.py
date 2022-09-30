"""
This file contains all functions that are called from the options that start with 'inv' in main.py.
"""

def inventory(inv_name):
    """
    This function prints what the current inventory contains and how many items are in it,
    by concatenating the items from the list into a string, plus len() value of the string.
    """
    print("The inventory contains " + str(len(inv_name)) + " things which are: " + str(inv_name) + ".")

def pick(inv_name, thing, position=-1):
    """
    This function adds an item to the inventory, in whatever position the user inputs secondary.
    If the position is bigger than the amount of items in the list, it prints an Error message.
    If the entered position is not an integer, it also prints an error message.
    If no position is entered it adds the item to the end of the list.
    """
    try:
        if int(position) <= (len(inv_name)):
            if int(position) < 0:
                if int(position) == -1:
                    print("Successfully added " + thing + " to position " + str(len(inv_name)) + ".")
                    inv_name.append(thing)
                else:
                    print("Successfully added " + thing + " to position " + position + ".")
                    inv_name.insert(int(position)+1, thing)
            else:
                inv_name.insert(int(position), thing)
                print("Successfully added " + thing + " to position " + position + ".")
        else:
            print("Error: Position" + str(position) + " is too high!")
    except ValueError:
        if position in ("", " "):
            print("Successfully added " + thing + " to position " + str(len(inv_name)) + ".")
            inv_name.append(thing)
        else:
            print("Error: " + str(position) + " is not a valid position!")
    return inv_name

def drop(inv_name, throw):
    """
    This function removes an item from the inventory.
    If the entered item does not correlate with the name of an item in the inventory,
    it prints an Error message.
    If two items in the inventory have the same name, it removes the first one.
    """
    try:
        inv_name.remove(throw)
        print("Successfully removed " + throw + " from the inventory.")
    except ValueError:
        print("Error: Item '" + throw + "' does not exist.")
    return inv_name
    

def swap(inv_name, thing1, thing2):
    """
    Switches the position of two items in the inventory.
    If one if the items do not exist, it prints an Error message with the item
    that does not exist within the inventory.
    """    
    error1 = 0
    error2 = 0
    try:
        inv_name.index(thing1)
    except ValueError:
        error1 = 1
    try:
        inv_name.index(thing2)
    except ValueError:
        error2 = 1
    if error1 == 0 and error2 == 0 and thing1 != thing2:
        thing2pos = inv_name.index(thing2)
        inv_name[inv_name.index(thing1)] = thing2
        inv_name[thing2pos] = thing1
        print("Successfully swapped the positions of " + thing1 + " and " + thing2 + ".")
    elif error1 == 1 and error2 == 1:
        print("Error: Items '" + str(thing1) + "' and '" + str(thing2) + "' do not exist.")
    else:
        if error1 == 1:
            print("Error: Item '" + thing1 + " do not exist.")
        else:
            if error2 == 1:
                print("Error: Item '" + thing2 + " do not exist.")
            else:
                print("Error: Swapping two identical items doesn't change anything.")
    return inv_name
