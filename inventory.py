"""
module for main.py
"""
def pick(list_arg, item, index=-1):
    """
    Add item in list at given index or default if none is given.
    """
    try:
        lst = list_arg
        if int(index) == -1:
            lst.append(item)
            print('"{}" has been added.'.format(item))
        else:
            if int(index) > len(lst):
                raise IndexError
            end = slice(int(index), len(lst), 1)
            beginning = slice(int(index))
            lst = lst[beginning] + [item] + lst[end]
            print('"{}" has been added at index "{}".'.format(item, index))
        return lst
    except IndexError:
        print("Error! There is no position", index, "in backpack.")
        return list_arg

def inventory(list_arg):
    """
    Display length of the list and the values inside.
    """
    print(f"Backpack has {len(list_arg)} items: {list_arg}")

def drop(list_arg, item):
    """
    Remove an item from the list.
    """
    try:
        lst = list_arg
        lst.remove(item)
        print(item, "has been removed.")
        return lst
    except ValueError:
        print('Error! I have no "{}" in the backpack.'.format(item))
        return list_arg

def swap(list_arg, item1, item2):
    """
    Swap postions between two values in list.
    """
    try:
        if item1 == item2:
            print("Error! Both items are the same.")
            return list_arg
        lst = list_arg
        item1_pos = lst.index(item1)
        item2_pos = lst.index(item2)
        lst[item1_pos] = item2
        lst[item2_pos] = item1
        print('"{}" and "{}" has been swapped.'.format(item1, item2))
        return lst
    except ValueError:
        print('Error! I have no "{}" or "{}" in the backpack.'.format(item1, item2))
        return list_arg
