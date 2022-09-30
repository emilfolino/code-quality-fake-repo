"""
Functions for inventory commands
"""
def pick(bag, element , index = -1 ):
    """
    pick function is used to add elements to preexcited bag.
    """

    if index == -1:
        bag.append(element)
        print(element, "has been added.")
    
    elif int(index)!= -1 and int(index) <= len(bag)-1:
        bag.insert(int(index),element)
        print(element,"has been added and has index " + str( index))

    elif int(index) >= len(bag)-1:
        print("Error", index, "is out of range.")

    return bag




def inventory(bag):
    """
    inventory is a function that print the list(bag).
    """
    print("the number of elements in the bag is ", len(bag), "and the element of the bag is",bag )


def drop(bag,unwanted):
    """
    drop is a function that takes away an element of the bag.
    """
    try:

        bag.remove(unwanted)
        print(unwanted, "have been removed from the bag.")
    except ValueError:
        print("Error can't find" ,unwanted, "in",bag)


    return bag


def swap(bag,first_element,second_element):
    """
    swap is a function that swaps tow elements in the bag.
    """
   
    if first_element == second_element or bag ==[]:
        print("Error",first_element,second_element,"is not found in the bag")
        

        
    elif first_element not in bag:
        print("Error",first_element)
        

      

    elif second_element not in bag:
        print("Error",second_element)
        
    else:   
        
        first_element = bag.index(first_element)

        
        second_element = bag.index(second_element)



        x = bag[first_element]
        bag[first_element]= bag[second_element]
        bag[second_element] = x
        
        print("the new placing in the bag", bag)
        return bag
    return bag       
     