"""
A module with functions for marvin options kmom04
"""

def pick(list_arg, new_item, new_item_index=None):
    """
    Adds the new item to the list
    """
    if new_item_index is None:
        list_arg.append(new_item)
        print(f"You put {new_item} in your bag with index {len(list_arg)-1}.")
        inventory(list_arg)
        return list_arg
    if int(new_item_index) <= len(list_arg)-1:
        list_arg.insert(int(new_item_index), new_item)
        print(f"You put {new_item} in your bag with index {new_item_index}.")
        inventory(list_arg)
        return list_arg
    print(f"Error! The index number {new_item_index} is too high!")
    return list_arg

def drop(list_arg, item_dropped):
    """
    Remove the dropped item from the list
    """
    try:
        list_arg.remove(item_dropped)
        print(f"You dropped {item_dropped} from the bag.")
        inventory(list_arg)
    except ValueError:
        print(f"Error! {item_dropped} doesn't exist!")
    return list_arg

def swap(list_arg, item_swap1, item_swap2):
    """
    Swap two items in the list
    """
    try:
        if item_swap1 != item_swap2:
            key1, key2 = list_arg.index(item_swap1), list_arg.index(item_swap2)
            list_arg[key1], list_arg[key2] = item_swap2, item_swap1
            print(f"You switched switched places of {item_swap1} and {item_swap2}.")
            inventory(list_arg)
        else:
            print("Error! Can't swap two items with the same name.")
    except ValueError:
        print(f"Error! {item_swap1} and/or {item_swap2} doesn't exist!")
    return list_arg

def inventory(list_arg, start = None, stop = None):
    """
    Prints out the list
    """
    if start is not None:
        if int(start) > len(list_arg) and int(stop) >= len(list_arg):
            print(f"Error! Both your index {start} and {stop} are too high.")
        elif int(start) > len(list_arg):
            print(f"Error! Your startindex {start} is too high.")
        elif int(stop) > len(list_arg):
            print(f"Error! Your endindex {stop} is too high.")
        elif stop is None:
            stop = len(list_arg)
            print(f"Your bag consists of {list_arg[int(start):stop]} from index {start}.")
        else:
            print(f"Your bag consists of {list_arg[int(start):int(stop)]} within index range {start} - {stop}.")
    else:
        print(f"Your bag consists of {len(list_arg)} things: {list_arg}.")
