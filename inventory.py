"""
Inventory som innehåller alla funktioner för att hantera en ryggsäck.
"""
def pick(backpack, item, index = -1):
    """
    Funktion som tar emot tre argument och lägger till item längst bak i array.
    """ 
    if int(index) < 0:
        index = len(backpack)       
    else:
        index = int(index) 
    if int(index) > len(backpack):
        print("Error! Out of line", index)
        return backpack
    
    backpack.insert(index, item)
    print(item, " has been added to ", backpack, " on index " , index)  
    return backpack

def inventory(backpack):
    """
    Kontrollererar ryggsäcken och skriver ut innehållet på skärmen
    """
    print("Backpack contains: ", len(backpack), " and the back" ,backpack)
     
def drop(backpack, item):
    """
    Tar bort saker från "bag" och skriver sedan ut kvarvarande innehåll.
    """
    try:
        backpack.remove(item)
        print("You have removed ", item, " from the backpack")
    except ValueError:
        print("Error you cant remove ", item, " cause it is not in the backpack!!")
    return backpack

def swap(backpack, item1, item2):
    """
    Byter plats på saker. a och b är platserna som byts
    """
    try:
        a, b = backpack.index(item1), backpack.index(item2)
        backpack[b], backpack[a] = backpack[a], backpack[b]
        print("Items: ", item1, " and ", item2, " has now changed places")
    except ValueError:
        print("Error", item1, " or ", item2, " is not in the backpack so you cant swap it!!")
    return backpack
    