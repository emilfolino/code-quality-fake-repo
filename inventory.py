#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Funktioner för Mr Marvins ryggsäck
"""
def inventory(bag_list, start_str=None, stop_str=None):
    """ 
    visar innehållet i ryggsäcken
    """
    if start_str is None:
        start = 0
    else:
        start = int(start_str)
    
    if stop_str is None:
        stop = len(bag_list)
    else:
        stop = int(stop_str)

    temp_list = bag_list[start:stop]
    print(f"ryggsäcken innehåller {len(temp_list)} saker")
    print(temp_list)
    for item in temp_list:
        print(item)


def pick(bag_list, item, x=None):
    """ 
    lägger till item i ryggsäcken
    """
    # om inte index är angivet
    if x is None:
        i = len(bag_list)
    else:
        i = int(x)
        
    if i > len(bag_list):
        print(f"Error: index {i} är 'out of range'")
        return bag_list

    # tillägg i listan
    bag_list.insert(i, item)
    if x is None:
        print(f"{item} har lagts in i ryggsäcken")
    else:
        print(f"{item} har lagts in i ryggsäcken på position {i}")
    return bag_list
    

def swap(bag_list, item1, item2):
    """
    byter plats på två element i ryggsäcken
    """
    i1 = find_index(bag_list, item1)
    i2 = find_index(bag_list, item2)
    if (i1 < 0) or (i2 < 0):
        return bag_list

    if item1 == item2:
        print(f"Error: {item1} och {item2} har samma värde")
        return bag_list

    temp = bag_list[i1]
    bag_list[i1] = bag_list[i2]
    bag_list[i2] = temp

    print(f"{item1} och {item2} har nu bytt plats")
    return bag_list


def find_index(bag_list, item):
    """
    returnerar position för angivet item
    """
    try:
        return bag_list.index(item)
    except ValueError:
        print(f"Error: {item} finns inte i ryggsäcken")
        return -1


def drop(bag_list, item):
    """
    tar bort angivet item ur ryggsäcken
    """
    try:
        bag_list.remove(item)
    except ValueError:
        print(f"Error: {item} finns inte i ryggsäcken")
        return bag_list

    print(f"har tagit bort {item} ur ryggsäcken")
    return bag_list


def handle_choice(bag_list, choice_str):
    """
    delar upp input till argument
    returnerar en uppdaterad lista
    """
    choice = choice_str.split(" ")

    if choice[1] == "pick":
        item = choice[2]
        if len(choice) > 3:
            position = choice[3]
            bag_list = pick(bag_list, item, position)
        else:
            bag_list = pick(bag_list, item)

    if choice[1] == "swap":
        item1 = choice[2]
        item2 = choice[3]
        bag_list = swap(bag_list, item1, item2)

    if choice[1] == "drop":
        item = choice[2]
        bag_list = drop(bag_list, item)

    return bag_list

# används vid test av enbart denna modul
# exekveras inte när modulen importeras till annan fil
if __name__ == "__main__":
    bag = ["blomma","pengar","mobil"]
    inventory(bag)

    print(bag)
    pick(bag, "karta")
    print(bag)
    pick(bag, "stövlar", 10)
    print(bag)
    pick(bag, "jacka", 4)
    print(bag)
    print()

    swap(bag,"pengar","mobil")
    print(bag)
    print()

    drop(bag, "blomma")
    print(bag)
    print()
