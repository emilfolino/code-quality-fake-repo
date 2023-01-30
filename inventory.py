"""
Contains inventory functions for Marvin.
"""


def pick(backpack, item, position=-100):
    """
    Picks something up and puts it in the inventory.
    """

    try:
        position = int(position)
    except ValueError:
        position = -100

    if position > len(backpack):
        print(f'Error! You can not insert an item at position {position}.')
    elif position == -100:
        backpack.append(item)
        print(f'{item} was added to your backpack')
    else:
        backpack.insert(position, item)
        print(f'{item} was added to position {position} in your backpack.')

    return backpack


def inventory(backpack, start=0, end=None):
    """
    Prints current inventory
    """
    start = int(start)
    if end is None:
        pass
    else:
        end = int(end)
        backpack = backpack[start:end]

    print(
        f'You have {len(backpack)} items in your bag. These are the items: {backpack}.')


def drop(backpack, item):
    """
    Drops something out of the inventory.
    """
    try:
        backpack.remove(item)
        print(f'{item} was removed from your bag.')
    except ValueError:
        print(f'Error! {item} does not exist in your bag.')

    return backpack


def swap(backpack, item1, item2):
    """
    Swaps two items in the inventory.
    """
    if item1 == item2:
        print(f'Error! {item1} and {item2} are the same item.')
    else:
        try:
            item1_place = backpack.index(item1)
            item2_place = backpack.index(item2)

            backpack[item1_place], backpack[item2_place] = backpack[item2_place], backpack[item1_place]

            print(f'You swapped {item1} for {item2}.')

        except ValueError:
            print(f'Error! {item1} and/or {item2} does not exist.')

    return backpack
