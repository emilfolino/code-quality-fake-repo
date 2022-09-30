"""
Detta är en modul string för att berätta vad denna modul gör.
"""

def printInvAdd():
    """
    Prints the add for the inv commands
    """
    print("\nTry out my \"inv\" commands!")
    print("-----------")


def pick(backpack: list, adding: str, index: int = -1):
    """
    This methods adds an object last in a list or at a specified index
    """
    if int(index) > -1:
        if int(index) in range(len(backpack) + 1):
            backpack = handle_pick_command(backpack, adding, index)
            print_pick(backpack)
            print(str(adding) + " was put in the backpack at location " + str(index))

        else:
            print("Error: Så många saker har du inte. Ditt intex var: " + str(index))
    else:
        backpack = handle_pick_command(backpack, adding)
        print_pick(backpack)
        print(adding + " was put in the backpack.")
    return backpack[:]


def print_pick(backpack: list):
    """
    This method will print out what is inside a list.
    """
    print(backpack)


def handle_pick_command(backpack: list, picking, index: int = -1):
    """
    This method will handle the pick command
    """
    if int(index) < 0:
        index = len(backpack)
    backpack.insert(int(index), picking)
    return backpack[:]


def inventory(backpack: list):
    """
    Prints the inventory in the backpack
    """
    print("Rygg saken har " + str(len(backpack)) + " saker i sig. Och dessa är: \n")
    print(backpack)


def drop(backpack: list, throw: str):
    """
    This method will remove a item in the backpack
    """
    if throw in backpack:
        backpack.remove(throw)
        print(throw + " was removed from the backpack.")
    else:
        print("Error: " + throw + " som skulle kastas finns inte.")
    return backpack[:]


def swap(backpack: list, swap1: str, swap2: str):
    """
    Swaps two objects in the backpack if they exist
    """
    if swap1 != swap2 and swap1 in backpack and swap2 in backpack:
        index1 = backpack.index(swap1)
        index2 = backpack.index(swap2)
        backpack[index1] = swap2
        backpack[index2] = swap1
        print("Bytte plats på " + swap1 + " och " + swap2)
    else:
        print("Error: En eller båda av " + swap1 + " och " + swap2 + " finns inte. ")
    return backpack[:]
