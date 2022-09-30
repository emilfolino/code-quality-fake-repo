"""
functions for Alfs inventory
"""



def inventory(bag):
    """
    Prints the bags inventory
    """

    print(f"Number of items: {len(bag)} \nItems: {bag}")


def pick(bag, item, index=-1):
    """
    function to pick from Alfs bag
    """
    if index == -1:
        bag.append(item)
        print(f"{item} was placed last in bag.")
        return(bag)
    if int(index) > len(bag):
        print(f"Error: index {index} to high!")
        return(bag)

    bag.insert(int(index), item)
    print(f"{item} was placed in position: {index}")
    return(bag)

def drop(bag, item):
    """
    function to remove item from Alfs bag
    """
    try:
        bag.remove(item)
        print(f"Removed {item} from bag")
        return(bag)
    except ValueError:
        print(f"Error {item} not in bag!")
        return(bag)

def swap(bag, item_1, item_2):
    """
    function to swap items in bag
    """
    if item_1 == item_2:
        print(f"Error: {item_1} and {item_2} are the same!")
        return(bag)

    try:
        index_1 = bag.index(item_1)
        index_2 = bag.index(item_2)
    except ValueError:
        print(f"Error: {item_1} or {item_2} not in bag!")
        return(bag)

    bag[index_1], bag[index_2] = bag[index_2], bag[index_1]
    print(f"Swaped {item_1} and {item_2} in bag")
    return(bag)
