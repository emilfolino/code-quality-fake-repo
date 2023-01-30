"""
Inventory functions
"""

def inventory(backpack):
    """ Displays the inventory """
    print(str(backpack) + " with " + str(len(backpack)) + " items")

def pick(backpack, pickupp, position = -1):
    """ Puts an item in the inventory """

    if(len(backpack) < int(position)):
        error_msg = 'Error: Position ' + position + ' doesnt exist in the backpack'
        print(error_msg)
    elif(position == -1):
        backpack.append(pickupp)
        print('"'+ pickupp +'" has been added.')
    else:
        backpack.insert(int(position), pickupp)
        print('"'+ pickupp +'" has been added. On index: ' + position)
    
    return backpack


def drop(backpack, dropoff):
    """ Removes an item from the inventory """

    if dropoff not in backpack:
        print("Error: This " + dropoff + " doesn't exist in the backpack.")
    else:
        backpack.remove(dropoff)
        print(dropoff +" has been removed.")

    return backpack

def swap(backpack, swap_first, swap_second):
    """ Swaps positions of two items in the inventory """

    if swap_first not in backpack and swap_second:
        print("Error: Neither of " + swap_first + " or " + swap_second +" is in the backpack")
    elif swap_first not in backpack:
        print("Error: "+ swap_first +" doesn't exist in the backpack.")
    elif swap_second not in backpack:
        print("Error: "+ swap_second +" doesn't exist in the backpack.")
    elif swap_second == swap_first:
        print("Error: You can't switch " + swap_first + " and " + swap_second +"")
    else:
        index_first = backpack.index(swap_first)
        index_second = backpack.index(swap_second)

        backpack[index_first], backpack[index_second] = backpack[index_second], backpack[index_first]
        print(f"{backpack[index_first]} and {backpack[index_second]} was swapped")

    return backpack
