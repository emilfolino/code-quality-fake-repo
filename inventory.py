"""
Inventory module for marvin bot 
"""

def inventory(backpack):
    """
    A summary of backpack
    """
    print(f"Backbaf has {len(backpack)} items: {backpack}")

def pick(backpack, item, index=None):
    """
    Add an item to backpackS
    """
    result = backpack
    if index is None:
        result.append(item)
        print(f"'{item}' has been added\n{backpack}")
    else:
        if int(index) > len(backpack) - 1:
            print(f"Error! the given index {index} is för högt.")
        else:
            result.insert(int(index), item)
            print(f"'{item}' has been added on index '{index}'\n{backpack}")
        
    return result


def drop(backpack,item):
    """
    Drop the item from backpack
    """
    try:
        backpack.remove(item)
        print(f"'{item}' removed from backpack!\n{backpack}")
    except ValueError:
        print(f"Error! {item} is not in backpack!\n{backpack}")
    
    return backpack

def swap(backpack, item1, item2):
    """
    Swap item1 with item2 or 
    """
    isValid = item1 in backpack and item2 in backpack
    if isValid:
        index1 = backpack.index(item1)
        index2 = backpack.index(item2)
        backpack[index1] = item2
        backpack[index2] = item1
        print(f"'{item1}' and '{item2}' has been swaped!")
    else:
        print("Error " + item2 + " " + item1)
    return backpack


def manageInvCommands(command, backpack):
    """
    Manage inventory commands
    """
    command = command.strip()
    commandList = command.split(' ')
    if len(commandList) == 1:
        inventory(backpack)
    else:
        if commandList[1] == "pick":
            if len(commandList) <= 2:
                inventory(backpack)
            elif len(commandList) > 4:
                print("Invalid command")
            else:
                try:
                    pick(backpack,commandList[2],commandList[3])
                except IndexError:
                    pick(backpack,commandList[2])
        elif commandList[1] == 'drop':
            if len(commandList) != 3:
                print("Invalid command")
            else:
                drop(backpack, commandList[2])
        elif commandList[1] == 'swap':
            swap(backpack, commandList[2], commandList[3] )
    
    return backpack
