"""
Function for marvins list-sack
"""

bag1 = [2, 5, 6, 7, 8, "pappa", "k", "o"]
def pick(bag, item, pos = None ):
    """
    pick function for marvin:
    Places item in specific position in list.
    """
    try:
        if pos is None:
            pos = len(bag)
        elif pos.isdigit():
            pos = int(pos)
        if pos > len(bag):
            print(f"Error {pos} out of range in bag! Current inventory range {len(bag)}")
            return bag
        bag.insert(pos, item)
        print(f"{item} has been added at {pos}")

    except IndexError:
        print(f"Error invalid position: {pos}! in inventory")
    except TypeError:
        print(f"Error invalid INDEX: {pos}! in inventory")
    
    return bag

def inventory(bag):
    """
    Print out the inventory
    """
    nr_inv = len(bag)
    print(f"Number of items in bag: {nr_inv}")
    print(bag)


def drop(bag, item):
    """
    removes item from list
    """
    try:

        bag.remove(item)
        print(f"{item} has been removed")

    except ValueError:
        print(f"{item} not in the bag Error")
    return bag

def swap(bag, item, item2):
    """
    Swap places for items in list
    """
    try:
        if item == item2:
            print("Error: same name")

        elif item and item2 in bag:
            item, item2 = bag.index(item), bag.index(item2)
            bag[item], bag[item2] = bag[item2], bag[item]
            print(f"{bag[item2]} & {bag[item]} swapped places")

        elif item not in bag and item2  not in bag:
            print(f"Error {item} and {item2} not in bag")

        elif item in bag:
            print(f"Error {item2} not in bag")

    except ValueError as error:
        print(f"Error: {error}") 
        print(bag)
    return bag
