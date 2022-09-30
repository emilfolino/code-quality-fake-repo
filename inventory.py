"""
Bagpack functions
"""

def inventory(bagpack):
    """
    Print the bagpack
    """
    print(f"{bagpack} has {len(bagpack)} in the list")

def pick(bagpack,str_1,str_2=2):
    """
    Add something the bagpack
    """
    if (int(str_2) - 1) >= len(bagpack):
        print(f"Error index {str_1} or {str_2} problem")
        return bagpack
    
    bagpack.insert(int(str_2),str_1)
    print(f"{bagpack} has been added to index {str_2}")
    return bagpack


def drop(bagpack,str_1):
    """
    remove something from the bagpack
    """
    if str_1 not in bagpack :
        print("Error " + str_1 +" not in the bagpack")
    if str_1 in bagpack :
   
        bagpack.remove(str_1)
        print(str_1 + " has been removed.")

    return bagpack 
 
def swap(bagpack, str_1, str_2):
    """
    Swap 2 things in the bagpack
    """
    if len(bagpack) == 0 :
        print("Error, no item in backpack")
    if str_1 == str_2 :
        print("Error! ether " + str_1 + str_2 + " does not exist")
    if str_1 not in bagpack :
        print("Error " + str_1 + str_2 +  " is not in the bagpack")
    else :
        swap_str1 = bagpack.index(str_1)
        swap_str2 = bagpack.index(str_2)
        swap1 = int(swap_str1) + 1
        swap2 = int(swap_str2) + 1
        bagpack.insert(swap_str1,str_2)
        bagpack.pop(swap1)
        bagpack.insert(swap_str2,str_1)
        bagpack.pop(swap2)
        print("Success! " + str_1 + " and " + str_2 + "have swaped" )

    return bagpack
