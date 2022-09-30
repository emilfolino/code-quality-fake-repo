"""Functions"""

def pick(backpack, str_object, index = ""):
    """Insert"""

    if index == "":
        backpack.append(str_object)
        answer = str_object + " has been added in backpack"

    elif int(index) > len(backpack):
        answer = "Error " + str(index)
        
    else:
        backpack.insert(int(index), str_object)
        answer = str_object + " has been added on index " + str(index) + " in backpack"

    print(answer)
    return backpack
    
    

def inventory(backpack):
    """"Inventory"""
    count = len(backpack)
    print("There are " + str(count) + " and are " + str(backpack))

def drop(backpack, delete):
    """Delete"""
    try:
        backpack.remove(delete)
        print(delete + " Has been deleted from backpack")

    except ValueError:
        print("Error: " + delete + " Are not found in the backpack")

    return backpack

def swap(backpack, arg1, arg2):
    """Swap"""
    if arg1 != arg2:
        try:
            position1 = backpack.index(arg1, 0, len(backpack))
            position2 = backpack.index(arg2, 0, len(backpack))

            backpack[position1] = arg2
            backpack[position2] = arg1

            print(arg1 + " har bytt plats med " + arg2)
            
        except ValueError:
            print("Error: " + arg1 + " or " + arg2 + "is not in the backpack" )
    else:
        print("Error: Both objects in the Backpack is the same")

    return backpack
