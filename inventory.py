"""Dotline"""

def pick(bag, item, index = ""):
    """Dotline"""
    rbag = bag
    try:
        if (index != ""):
            index = int(index)
            if (len(bag) > index >= 0):
                rbag.insert(index, item)
                print (str(rbag) + " " + str(index))
                return rbag 
            
            print("Error: " + str(rbag) + " " + str(index))
            return rbag
        
        rbag.append(item)
        print (rbag)
        return (rbag)

    except ValueError:
        return "ValueError:"


def inventory(bag):
    """Dotline"""
    rbag = bag
    print (str(rbag) + str(len(rbag)))

def drop (bag, item):
    """Dotline"""
    rbag = bag
    try:
        rbag.remove(item)
        print(item + " has been remove from inventory")
        return rbag
    except ValueError:
        print ("Error " + item + " do not exist in your inventory")
        return rbag

def swap(bag, item_a, item_b):
    """Dotline"""
    rbag = bag
    try:
        if (item_a == item_b):
            print("Error you choose same item to swap with " + item_a)
            return rbag

        a, b = rbag.index(item_a), rbag.index(item_b)
        rbag[b], rbag[a] = rbag[a], rbag[b]
        print(item_a + " have change place with " + item_b)
        return rbag
    except ValueError:
        print("Error " + item_a + " or " + item_b + " do not exist in your inventory")
        return rbag
