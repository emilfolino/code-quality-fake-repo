"Backpack for marvin, kmom04"


def pick(invlista, word, pos = None):
    "Adds to inventory"
    try:
        if len(invlista) >= int(pos):
            print (len(invlista))
            invlista.insert(int(pos), word)
            print(word + " has been added to index " + str(pos))
        else:
            print("Error, Number " + str(pos) + " is bigger then list")
    except: # pylint: disable=bare-except
        try:
            invlista.insert(int(pos), word)
            print(word + " has been added to index " + str(pos))
        except: # pylint: disable=bare-except
            invlista.append(word)
            print(word + " has been added")
    
    return invlista

def inventory(invlist1):
    "checks inventory"
    totlist = len(invlist1) 
    return print("There is " + str(totlist) + " items in the backpack: " + str(invlist1))

def drop(invlist2, dropthis):
    "drops stuff from inventory"
    if dropthis in invlist2:
        print(dropthis + " has been removed from backpack")
        invlist2.remove(dropthis)
    else:
        print("Error, There is no " + dropthis + " in the backpack")
    return invlist2  

def swap(invlist3, value1, value2):
    "Swap places of items in inventory"
    if value1 in invlist3:
        if value2 in invlist3:
            if value1 == value2:
                print("Error, they are the same")
            else:
                indev1 = invlist3.index(value1)
                indev2 = invlist3.index(value2)
                invlist3[indev1], invlist3[indev2] = invlist3[indev2], invlist3[indev1]    
                print(value1 + " and " + value2 + " has been swapped")        
        else:
            print("Error, There is no " + value2 + " in backpack")
        
    else:
        if value2 not in invlist3:
            print("Error, There is no " + value2 + " in backpack")
            
        print("Error, There is no " + value1 + " in backpack")
    return invlist3
