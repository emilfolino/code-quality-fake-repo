"""Inv module"""


def nothing_added():

    """ Docstring"""

    no_nothing = "Nothing was added, try again"
    print(no_nothing)
    
def pick(inv, choice, position = None):

    """ Docstring"""
    
    try:
        if position is not None and int(position) > len(inv):
            added = "Error that is a too high number " + str(position) 

        else: 
            if position is None:
                inv.append(choice)
                added = "I have now added: " + choice + " in position " +  str(inv.index(choice))
            else:
                inv.insert(int(position), choice)
                added = "I have now added: " + choice + " in position " +  str(inv.index(choice))
    except ValueError:
        added = "Error that is not a possible position"
    print(added)
    return(inv)
            
def inventory(inv):

    """ Docstring"""

    constant_inv = "Backpack has " + str(len(inv)) + " " + "items: " + str(inv)
    print(constant_inv)



def swap(inv, choice, choice2):

    """ Docstring"""
         
    nothing = False
    if len(inv) == 0 or len(inv) == 1:

        swaped = "Error there is no such item in the backpack " + choice + " " + choice2
    elif choice == choice2:
        swaped = "Error there is no such item in the backpack " + choice + " " + choice2
    else:
        if choice in inv and choice2 in inv:                
            place_in_list1 = inv.index(choice)
            place_in_list2 = inv.index(choice2)
            inv[place_in_list1], inv[place_in_list2] = inv[place_in_list2], inv[place_in_list1]
            swaped = "The items have now been swapped" + ":" + str(inv)
        else:
            nothing = True
        
        if nothing:
            swaped = "Error there is no such item in the backpack " + choice + " " + choice2

    
    print(swaped)
    return(inv)

def drop(inv, choice):

    """ Docstring"""
    
    something = False
    thing = False
    if len(inv) == 0:
        dropped = "Error there is no such item in the backpack " + choice
    else:
        for old_item in inv:
            if old_item == choice:
                thing = True      

        if thing:
            dropped = "I have now removed: " + choice
            inv.remove(choice)
        else:
            something = True
                    
                    
        if something:
            dropped = "Error there is no such item in the backpack " + choice

    print(dropped)
    return(inv)
