""" Alla nya funktioner för inv-kommandon"""

#def inventory(bag):
#    """Print the backpack"""
#    print("Your bag conatins " + str(len(bag)) + " things.")
#    print(bag)

def inventory(bag, start=0, stop=0):
    """Print the backpack"""
    if start == 0 and stop == 0:
        start = 0
        stop = len(bag)
        print("Your bag conatins " + str(len(bag)) + " things.")
        print(bag)
    else:
        print(bag[start:stop])

def errorcode(bag, thing):
    """Errorcode"""
    print("Error! Your bag does not contain: " + str(thing))
    print("Here you can see what's in your backpack!")
    inventory(bag,0,0)


def pick(bag,thing,pos = -1):
    """Add a new thing to the backpack"""
    
    try:
        pos = int(pos)
    except ValueError:
        print("Error! You haven't entered a number")
        return bag
    
    if pos > len(bag):
        print("Error! " + str(pos) + " is a too high number")
        return bag
    
    if pos == -1:
        bag.append(thing)
    else:
        bag[pos:pos] = [thing]        
        
    print(thing + " was added to postition " + str(pos))
    inventory(bag,0,0)
    return bag


def drop(bag, thing):
    """Removes something from the backpack"""
    try:
        bag.remove(thing)
        print("You have dropped " + str(thing))
        inventory(bag,0,0)
        return bag
    except ValueError:
        errorcode(bag,thing)
        return bag

def swap(bag, first, second):
    """Rearanges two things in the backpack"""
    if first == second:
        errorcode(bag, first)
    try:
        first_i = bag.index(first)
        second_i = bag.index(second)
        bag[first_i] = second
        bag[second_i] = first
        print("You have swopped the items " + str(first) 
            + " and " + str(second))
        inventory(bag,0,0)
        return bag
    except ValueError:
        if second in bag:
            errorcode(bag,first)
        elif first in bag:
            errorcode(bag,second)
        else:
            errorcode(bag,first)
            errorcode(bag,second)
        return bag

if __name__ == "__main__":
    stuff = ["apa", "banan"]
    inventory(stuff,0,0)
