'''
Meyval inventory
'''
def pick(backpack_list , thing , index = -1):
    '''
    Funktion som ska agera som en ryggsäck
    '''
    index = int(index)

    if index == -1:
        backpack_list.append(thing)
        print(f"{thing} has been added in your backpack, son.")

    elif index > len(backpack_list):
        print(f"Error! The index {index} can not input here, son.")
        
    else:
        backpack_list.insert(index, thing)
        print(f"{thing} has been added to your backpack in place {index}, son.")
        
    return backpack_list

def inventory(backpack_list):
    '''
    Vad som finns i ryggsäcken
    '''
    lenght = len(backpack_list)
    print(f"There are {lenght} things in your backpack and has {backpack_list} in it, son.")
    
def drop(backpack_list, thing):
    '''
    Tar ut ur ryggsäcken
    '''
    try:
        backpack_list.remove(thing)
        print(f"{thing} has been removed, son.")
    
    except ValueError:
        print(f"Error!{thing} is not in your backpack, son.")
    
    return backpack_list

def swap(backpack_list, thing1, thing2):
    '''
    Byter plats på två saker i ryggsäcken
    '''
    if thing1 == thing2:
        print("Error!")

    else:
        try:
            index1 = backpack_list.index(thing1)
            index2 = backpack_list.index(thing2)

            backpack_list[index1], backpack_list[index2] = backpack_list[index2], backpack_list[index1]
            print(f"You have switched places between {thing1} and {thing2}, son.")
        except ValueError:
            print(f"Error {thing1} {thing2}!")
    return backpack_list
