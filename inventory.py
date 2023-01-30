""" Functions for Marvin3"""

def pick(list_of_things, thing, index = None):
    """Lägg till i lista"""
    if (index is None):
        if (thing != ""):
            list_of_things.append(thing)
            print("Item '" + thing + "' successfully put in bag.")
        else:
            print("Error. Please write 'inv pick <name of item> (<index>).")
    elif (index == ""):
        print("Error. Index is missing.")
    else:
        try:
            if (int(index) <= len(list_of_things)):
                list_of_things.insert(int(index), thing)
                print("Item " + thing + " successfully put in index " + str(index) + " in bag.")
            else:
                print("Error. I can't put the item in index " + str(index) + " in the bag - " +"index is too large.")
        except ValueError:
            print("Error. Index is not a number - unable to add item.")
            print("Please write in following format: 'inv pick <name of item> (<index>).")
    return list_of_things


def inventory(list_of_things, index_start = None, index_stop = None):
    """Skriv ut vad som finns i '"'väskan'"' """
    if (len(list_of_things) == 0):
        print("My bag is empty. []")
    elif (index_start is None and index_stop is None):
        print("My bag has " + str(len(list_of_things)) + " item(s): " + str(list_of_things))
    elif (index_start is not None and index_stop is not None):
        try:
            print("My bag has " + str(len(list_of_things[int(index_start):int(index_stop)])) + " item(s): "
                + str(list_of_things[int(index_start):int(index_stop)]))
        except ValueError:
            print("Error. Please write 'inv (<start> <stop>), where <start> and <stop> "
            "should be integers.")


def drop(list_of_things, item):
    """Removes an item from the bag"""
    try:
        list_of_things.remove(item)
        print("I have now removed '" + item + "' from my bag.")
    except ValueError:
        print("Error. I can't find " + item + " in my bag.")
    return list_of_things


def swap(list_of_things, thing1, thing2):
    """Byter plats på två element i en lista"""
    if (thing1 == thing2):
        print("Error. Please choose two different items to swap.")
        return list_of_things
    try:
        index1 = list_of_things.index(thing1)
    except ValueError:
        print("Error. I couldn't find '" + thing1 + "' in my bag. "
        "I couldn't swap '" + thing1 + "' and '" + thing2 + "'.")
        return list_of_things
    try:
        index2 = list_of_things.index(thing2)
    except ValueError:
        print("Error. I couldn't find '" + thing2 + "' in my bag. "
        "I couldn't swap '" + thing1 + "' and '" + thing2 + "'.")
        return list_of_things
    list_of_things[index1] = thing2
    list_of_things[index2] = thing1
    print("I have successfully swapped positions of: '" + thing1 + "' and '" + thing2 + "'.")
    return list_of_things



#             if 'pick' in choice:
#                 try:
#                     pos = int(obj[3])
#                 except IndexError:
#                     pos = len(inv)
#                 print(inventory.pick(inv, obj[2], pos))
# _____

# def pick(inv, obj, pos):
#     '''adds obj into list inv at index pos'''
#     try:
#         if pos > len(inv):
#             print('Error ' + str(pos) +  ' is out of range')
#         inv.insert(pos, obj)
#     except ValueError:
#         print('Wrong pos, error') 
#     return inv
