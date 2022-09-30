"""
functions used for patrics backpack
"""
def inventory(tmp_list, start = 0, stop = -1):
    """
    Prints out the amount of items in a list, and prints the list.
    Start and stop is optional, are used to print a sliced version
    of the lists instead. (list[start : stop])
    """
    if start == 0 and stop == -1:
        print(f"Backpack has {len(tmp_list)} items: {tmp_list}")
    else:
        return_list = tmp_list[int(start):int(stop)]
        print(return_list)

def pick(tmp_list, item, place = -1):
    """
    Adds an item to the list and takes the arguments: tmp_list (the list), 
    item (item to add) and place (index).
    If place is not given, the item will be placed at the end of the list.
    """
    if place == -1:
        tmp_list.append(item)
        print(f"{item} added at index {len(tmp_list) - 1}")
    else:
        if int(place) > (len(tmp_list) - 1):
            print(f"Error: Index {place} is too high, try a lower index.")
        else:
            tmp_list.insert(int(place), item)
            print(f"{item} added at index {place} :)")
    return tmp_list

def drop(tmp_list, item):
    """
    Removes one item from the list, takes argument tmp_list (a list) and item
    """
    if item in tmp_list:
        tmp_list.remove(item)
        print(f"{item} has been removed from the backpack")
    else:
        print(f"Error: {item} is not in the backpack")
    return tmp_list

def swap(tmp_list, item_1, item_2):
    """
    swaps two items in a list, takes arguments tmp_list ( a list), item_1, item_2.
    finds index of both items then puts each item at the others index
    """
    if item_1 == item_2:
        print("Error: can't swap the same item")
    if (item_1 not in tmp_list) and (item_2 not in tmp_list):
        print(f"Error: {item_1} and {item_2} is not in the backpack")
    elif item_1 not in tmp_list:
        print(f"Error: {item_1} is not in the backpack")
    elif item_2 not in tmp_list:
        print(f"Error: {item_2} is not in the backpack")
    else:
        index_1 = tmp_list.index(item_1)
        index_2 = tmp_list.index(item_2)

        tmp_list[index_1] = item_2
        tmp_list[index_2] = item_1

        print(f"{item_1} and {item_2} has swapped places")
    return tmp_list
