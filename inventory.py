"""Inventory asset for marvin"""

def pick(backpack, item, index=-1):
    """Picks an item and put it in the backpack at an specific index if its given."""
    if int(index) >= 0:
        if int(index) < len(backpack):
            backpack.insert(int(index), item)
            print("I added " + str(item) + " to the backpack in the position " + str(index))
        else: 
            print("Error: Index " + str(index) + " is out of range.")
    else:   
        backpack.append(item)
        print("I added " + str(item) + " to the backpack!")

    return backpack
    
def inventory(backpack):
    """Show how many items there is in the backpack and the items."""
    backpack_length = len(backpack)
    fixed_string = ", ".join(backpack)
    print("There is " + str(backpack_length) + " amount of items in the backpack")
    if backpack_length > 0:
        print("The items are: " + fixed_string)
    else:
        print(backpack)

def drop(backpack, item):
    """Removes an element from the backpack."""
    modified_backpack = backpack
    check = 0
    if item in modified_backpack:
        modified_backpack.remove(item)
        check += 1

    if check == 0:
        print("Error: " + str(item) + " does not exist in the backpack.")
    else:
        print("I removed " + str(item) + " from the backpack.") 


    return modified_backpack

def swap(backpack, item_one, item_two):
    """Swap the pos of two item."""
    modified_backpack = backpack
    if (item_one in backpack) and (item_two in backpack):
        if item_one != item_two:
            index_of_item_one = backpack.index(item_one)
            index_of_item_two = backpack.index(item_two)
            modified_backpack[index_of_item_one] = item_two
            modified_backpack[index_of_item_two] = item_one
            print(item_one + " and " + item_two + " changed place in the backpack.")
        else:
            print("Error: You cant change place of the same item.")
    else:
        if (item_one in backpack):
            print("Error: " + item_two + " does not exist in the backpack.")
        elif (item_two in backpack): 
            print("Error: " + item_one + " does not exist in the backpack.")
        else:
            print("Error: " + item_one + " and " + item_two + " does not exist in the backpack.")

    return modified_backpack
