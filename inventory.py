'''
invetory functions
'''

def pick(pack, item, index = None):
    '''
    picks up items from the ground or something
    '''
    if index is not None:
        if index >= len(pack):
            print("Error, InDEX TOO LARGE")
            return pack
        pack.insert(index, item)
        print(f"inserted {item} at {index}")
        
    else:
        pack.append(item)
        print(f"inserted {item}")

    return pack

    
def inventory(backpack):
    '''
    shows inventory and size of it
    '''

    size=len(backpack)
    print(f"backpack has {size} items: {backpack}")

def drop(backpack, item):
    '''
    drops an item from the backpack
    '''

    if  item not in backpack:
        print(f"Error {item} not in backpack")
        return backpack
        

    backpack.remove(item)
    print(f"removed {item} from backpack.")
    return backpack

def swap(backpack, item1, item2):

    '''
    swap items in the backpack
    '''
    
    if  item1 == item2:
        print("Error")
    if item1 not in backpack or item2 not in backpack:
        print("Error Item not in backpack")
        if item1 not in backpack:
            print(f"{item1} not in backpack.")
        if item2 not in backpack:
            print(f"{item2} not in backpack.")

            
            
            
        return backpack

    index1 = backpack.index(item1)
    index2 = backpack.index(item2)

    temp = backpack[index1]
    backpack[index1] = backpack[index2]

    backpack[index2] = temp

    print(f"swapped items {item1} and {item2}.")
    return backpack
    