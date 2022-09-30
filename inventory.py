"""
denna fil håller alla argument relaterade till listor
"""


def inventory(invent, start = 0, stop = 0):
    """
    printar ryggan samt säger hur många objekt den inehåller
    """
    lengt = len(list(invent))
    if start == 0 and stop == 0: 
        print(f"ryggsäcken innehåller {lengt} objekt")
        print(invent)
    else:
        sliced_rygga = invent[int(start):int(stop)]
        print(sliced_rygga)


def pick(ryggsäck, objektet = "", the_index = -1):
    """
    lägger till objekt i ryggan, fins alternativ för att uppge indexet för objektet
    """
    if int(the_index) <= len(ryggsäck):

        if the_index != -1:
            ryggsäck.insert(int(the_index), objektet)
            print(f"{objektet} lades till i ryggsäcken på index {the_index}")

        else:
            ryggsäck.append(objektet)
            print(f"{objektet} lades till i ryggsäcken")
        
    else:
        print(f"Error index to high, the index {the_index} is out of bound")

    return ryggsäck



def drop(inv, objekt):
    """
    tar bort ett spesefikt objekt
    """
    try:
        inv.remove(objekt)
        print(f"{objekt} kastades bort ur ryggsäcken")
        
    except ValueError:
        print(f"Error du kan ej kasta bort något du ej har. objekt {objekt} finns ej i ryggan")

    return inv


def swap(inv, obj1, obj2):
    """
    swap two items in the inventory
    """
    if obj1 != obj2:
        try:
            index1 = inv.index(obj1)
            index2 = inv.index(obj2)
            inv[index1], inv[index2] = obj2, obj1

            print(f"{obj1} och {obj2} bytte plats")
        
        except ValueError:
            print(f"Error the objekt {obj1} or {obj2} dose not exist in the bag")
            return inv
    
    else:
        print("Error. just why...")
        
    return inv
