"""
All the inv functions
"""
def pick(backpack,object1,position = ""):
    """
    Lägger till ett object i backpack listan
    """
    if position == "":
        backpack.append(object1)
        print("['" + "','".join(backpack) + "']")
        return backpack

    if len(backpack) < int(position):
        print("Error: You can't put it there be because the index: '"+ str(position) + "' is to high!")
        
    else: 
        backpack.insert(int(position), object1)
    print("['" + "','".join(backpack) + "'] "+  str(position))
    return backpack

def inventory(backpack, start = "", stop = ""):
    """
    Printar ut vad som finns i backpack listan
    """
    if start == "" and stop == "":
        print("The backpack has " + str(len(backpack)) + " items: " + "[" + "', '".join(backpack) + "]")
    else:
        x = (backpack[int(start):int(stop)])
        print(",".join(x))
        

def drop(backpack, drop_item):
    """
    Tar bort ett item ur backpacken listan
    """
    if drop_item in backpack:
        backpack.remove(drop_item)
        print(drop_item + " has been removed!")
    else:
        print("Error: '" +drop_item + "' does not exist in backpack!")
        return(backpack)
    return(backpack)

def swap(backpack, item_a, item_b):
    """
    Byter plats på två items som finns i backpack listan
    """
    try:

        if item_a == item_b:
            print("Error: it's is the same word!")
            return(backpack)
        if item_a and item_b in backpack:
            position_a = backpack.index(item_a)
            position_b = backpack.index(item_b)
            backpack[position_a], backpack[position_b] = backpack[position_b], backpack[position_a]
            print(backpack)
        elif item_a not in backpack:
            if item_b not in backpack:
                print("Error: '" + item_a + "' or '" + item_b + "' is not in the list!")
        elif item_b not in backpack:
            print("Error: '" + item_b + "' is not in backpack!")
        return(backpack)
            
    except ValueError:
        print("Error: '" + item_a + "' is not in the backpack!")
        return(backpack)
    

#def start_stop(backpack, start, stop):
    """
    Skickar ut ord från listan mellan start och stop
    """
    
    #x = (backpack[int(start):int(stop)])
    #print(",".join(x))
    #return(backpack)
