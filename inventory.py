"""Inventory module, functions for handeling and editing lists. Created for Marvin chatbot"""
def function_call(bag, choice):
    """Top-level logic"""
    choice_list = choice.split(' ')
    new_bag = bag

    if len(choice_list) == 1:
        inventory(bag)
    else:
        if choice_list[1] == 'pick':
            if len(choice_list) > 3:
                new_bag = pick(bag, choice_list[2], choice_list[3])
            elif len(choice_list) == 3:
                new_bag = pick(bag, choice_list[2])
            else:
                #nothing to pick
                print('Nothing to pick')
        elif choice_list[1] == 'drop':
            if len(choice_list) > 2:
                new_bag = drop(bag, choice_list[2])
            else:
                #nothing to drop
                print('Nothing to drop')
        elif choice_list[1] == 'swap':
            if len(choice_list) == 4:
                new_bag = swap(bag, choice_list[2], choice_list[3])
            else:
                #nothing to swap
                print('Nothing to swap')
        else:
            print('Error: That is not a legal option!')
    return new_bag

def inventory(bag):
    """Print inventory and number of elements"""
    print('There are', len(bag),'items. And they are:', bag)

def pick(bag, item, index = -1):
    """Pick up a new element and add it to inventory"""
    try:
        target = int(index)
    except ValueError:
        print("Error: illegal index number!")
    else:
        if len(bag) > target:
            if target > -1:
                bag.insert(target, item)
                print('Marvin picked up', item, 'and put it in slot', index)
            else:
                bag.append(item)
                print('Marvin picked up', item, 'and put it in the bag')

        else:
            print('Error: index:', target, 'is out of bounds!')
    return bag

def drop(bag, item):
    """Drop a given element from inventory"""
    try:
        bag.remove(item)
    except ValueError:
        print("Error: could not drop '" + item + "'")
    else:
        print("Marvin tossed '" + item + "' miles away!")
    return(bag)

def swap(bag, item1, item2):
    """Swaps places of two elements in inventory"""
    try:
        x = bag.index(item1)
        y = bag.index(item2)
    except ValueError:
        print('Error: Can not swap', item1, 'and', item2, 'when thay are not both in the list\n')
    else:
        if x != y:
            bag[x] = item2
            bag[y] = item1
            print(item1,'and', item2, 'magically swaped placeses!')
        else:
            print('Error: No use swapping', item1, 'and', item2)
    return bag
