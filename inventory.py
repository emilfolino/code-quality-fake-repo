"""
this is Marvin's backpack with all the new functions for the inventory
"""

def pick(backpack, my_object, position=""):
    """
    adds an object to the backpack (with the option of chosing the index)
    """
    if position == "": #if there is no position given
        position = len(backpack) #just take the length as position (add it to the end)
    position = int(position) #for validation
    if position <= len(backpack): #if the position is on the list
        backpack.insert(position,my_object) #insert the object
        print("The object {} has been added to the backpack at index {}".format(my_object,position))
    else: #if the index is too high
        print("Error! Index {} does not exist.".format(position))
    return backpack

def inventory(backpack,int1="",int2=""):
    """
    prints how many things are in the backpack and lists them
    """
    if int1 == "" or int2 == "": #if there is no start or stop specified, count and list the items:
        print("There are {} objects in the backpack. Here they are: ".format(len(backpack)))
        print(backpack)
    else: #if there is start and stop, list the items in range:
        int1 = int(int1) #for validation
        int2 = int(int2) #for validation
        print(backpack[int1:int2])

def drop(backpack, my_object):
    """
    throws out an object from the backpack
    """
    try:
        backpack.remove(my_object)
        print("{} has been removed.".format(my_object))
    except ValueError:
        print("Error! Object {} is not in the backpack.".format(my_object))
    return backpack
        
def swap(backpack, obj1, obj2):
    """
    swaps two objects in the backpack
    """
    while True:
        if obj1 == obj2:
            print("Error! These objects are identical.")
            break
        present = 0 #keeps track of how many of the 2 objects are present
        try:
            ind1 = backpack.index(obj1)
            present += 1 #if object1 is found, count it
        except ValueError: #if object1 is not found
            print("Error! Object {} is not in the backpack.".format(obj1))
        try:
            ind2 = backpack.index(obj2)
            present += 1 #count if found
        except ValueError: #if object2 is not found
            print("Error! Object {} is not in the backpack.".format(obj2))
        if present == 2: #if both objects are present, swap them:
            backpack[ind1] = obj2
            backpack[ind2] = obj1
            print("Object {o1} has been moved from position {p1} to {p2}. Object {o2} had been moved from {p2} to {p1}."
            .format(o1=obj1,p1=ind1,p2=ind2,o2=obj2))
        break
    return backpack
