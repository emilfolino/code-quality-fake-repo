"""
inventory functions for marvin3
"""

def pick(bag, saken, positie=None):
    """
    function takes 3 arguments(1 optional)
    if only the item is sent to the function, it appends to the list
    if index is also sent, it adds it to the index
    """
    if positie is None:
        bag.append(saken)
        print(saken + " has been added!")
    else:
        if int(positie) in range(0, len(bag)+1):
            bag.insert(int(positie), saken)
            print(saken + " has been added on index " + str(positie))
        else:
            print("Error " + str(positie) + " is too high..")

    return bag

def inventory(bag, index1=None, index2=None):
    """
    if indexes are not sent, it prints the list
    if indexes are also sent, it uses the slice
    """
    if index2 is None or index1 is None:
        print("Bagpack has " + str(len(bag)) + " items: " +str(bag))
    else:
        print(bag[int(index1):int(index2)])

def drop(bag, sak):
    """
    if the item is not in the list it prints the error message
    otherwise, it removes the item from the list
    """
    if sak not in bag:
        print("Error " + sak +" not in the list")
    else:
        bag.remove(sak)
        print(sak + " has been dropped")
    return bag

def swap(bag, sak_1, sak_2):
    """
    if lenght of list is 0
        or item1 or item2 is not in the list
            it prints error message
    otherwise it swaps the items
    """
    if len(bag) == 0:
        print("Error "+ sak_1 + sak_2 +  " not in the list")
    if sak_1 not in bag:
        print("Error "+ sak_1 + " not in the list")
    if sak_2 not in bag:
        print("Error "+ sak_2 + " not in the list")
    try:
        index_1 = bag.index(sak_1)
        index_2 = bag.index(sak_2)
        temp = bag[index_1]
        bag[index_1] = bag[index_2]
        bag[index_2] = temp
        print(sak_1 + " and " + sak_2 + " has been swapped.")
        return bag
    except ValueError:
        print("Error")

    return bag
