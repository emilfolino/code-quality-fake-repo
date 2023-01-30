"""
Functions for Marvin 3
"""

def pick(bag, thing, index = ...):
    """
    Function to add things to a list
    """
    #bag = bag-list
    #thing = thing to pick
    #index = index, optional standard last place
    #index = int(index)
    if index == ...:
        bag.append(thing)
        print(f"'{thing}' was added!")
    else:
        index = int(index)
        if index <= len(bag):
            bag.insert(index, thing)
            print(f"'{thing}' was added at index '{index}'!")
        else:
            print(f"Error! {index} is out of range for this list!")
    return bag

def inventory(bag):
    """
    Function to see what is in the list
    """
    count = 0
    for _ in bag:
        count +=1
    print(f"Your bag contains '{count}' things, which is \n '{bag}'")

def drop(bag, thing):
    """
    Function to drop things from a list
    """
    try:
        bag.remove(thing)
        print(f"'{thing}' was thrown away.")
        return bag
    except ValueError:
        print(f"Error! '{thing}' does not exist in your bag!")
        return bag

def swap(bag, thing1, thing2):
    """
    Function to swap index between things
    """
    if thing1 != thing2:
        try: 
            if thing1 and thing2 in bag:
                # hitta index för things
                index_thing1 = bag.index(thing1) # ex 1
                index_thing2 = bag.index(thing2) # ex 3
                #print(index_thing1, index_thing2)

                # byt plats med insert
                bag.pop(index_thing1)
                bag.insert(index_thing1, thing2)
                bag.pop(index_thing2)
                bag.insert(index_thing2, thing1)
                #print(bag)
                print(f"Success! '{thing1}' switched position with '{thing2}'")
            elif thing1 and thing2 not in bag:
                print(f"Error! '{thing1}' and '{thing2}' does not exist in your list!")
            return bag

        except ValueError:
            if thing1 in bag:
                print(f"Error! '{thing2}' does not exist in your list!")
            elif thing2 in bag:
                print(f"Error! '{thing1}' does not exist in your list!")
            else:
                print("Error! Your list seems to be empty!")
            return bag
    else:
        print("Error! You try to switch something with identical names!")
        return bag

if __name__ == "__main__":
    pass
