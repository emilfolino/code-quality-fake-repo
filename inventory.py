"""
This is a module for marvins inventory
"""
def pick(bag, item, index="last"):
    """
    This function puts an item in the bag
    """
    try:
        if index == "last":
            bag.append(item)
            print(f"'{item}' has been added.")
        else:
            if len(bag) >= int(index):
                bag.insert(int(index), item)
                print(f"'{item}' has been added on index '{index}'.")
            else:
                print(f"Error: Index '{index}' doesn't exist")
        return bag
    except ValueError:
        print("Error")
        return bag

def inventory(bag):
    """
    This function prints the bag
    """
    print(f"bag has {len(bag)} items: {bag}")

def drop(bag, item):
    """
    This function drops an item
    """
    try:
        bag.remove(item)
        print(f"'{item}' has been dropped.")
        return bag
    except ValueError:
        print(f"Error: '{item}' doesn't exist in bag.")
        return bag

def swap(bag, item1, item2):
    """
    This function swaps the places of two items.
    """
    try:
        if item1 == item2:
            print("Error: Can't swap items with same name")
            return bag
        index1 = bag.index(item1)
        index2 = bag.index(item2)
        bag[index1], bag[index2] = bag[index2], bag[index1]
        print(f"'{item1}' and '{item2}' swapped places.")
        return bag
    except ValueError:
        print(f"Error: I have no '{item1}' or '{item2}' in the bag.")
        return bag
