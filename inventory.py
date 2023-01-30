"""
Inventory functions

    """
def pick(bag, item, pos=-1):
    """
picks up item and puts in bag

    """
    try:
        pos = int(pos)
        if  pos == -1:
            bag.append(item)
            message = item + " har lagts till sist i ryggsäcken"
        elif len(bag) > pos > -1:
            bag.insert(pos, item)
            message = item + " har lagts till ryggsäcken i position: "+ str(pos)
        else:
            message = "Error "+str(pos)+" is out of range" 
        print(message)
        return bag
    except IndexError:
        message = "error"
        print(message)
        return bag


def inventory(bag):
    """
checks bag inventory 

    """
    message = "In the bag there is " + str(len(bag)) + " items. The items are " + str(bag)
    print(message)

def drop(bag, item):
    """
drops items in bag 

    """
    if item in bag:       
        bag.remove(item)
        message = item + "has been dropped"
    else:
        message = "Error " + item + "isn't in bag"
    print(message)
    return bag 

def swap(bag,item,item2):
    """
swaps items in bag 

    """
    if item in bag:
        pos1 = bag.index(item)
    else:
        if item2 in bag:
            message = "Error " + item + " isn't in bag"
            print(message)
             
        else:
            message = "Error " + item +" and " + item2 + " isn't in bag"
            print(message)
        return bag 

    if item in bag:
        pos2 = bag.index(item2)
    else:
        if item in bag:
            message = "Error " + item2 + " isn't in bag"
            print(message)
             
        else:
            message = "Error " + item +" and " + item2 + " isn't in bag"
            print(message)
        return bag 
        
    if item == item2:
        message = "Error you can't swap the same item"
        print(message)
    else:
        bag[pos1], bag[pos2] = bag[pos2], bag[pos1]
        message = item + " has swapped place with " + item2
        print(message)
    return bag
