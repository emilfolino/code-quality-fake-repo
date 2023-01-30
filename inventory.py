""" -- """
def inventory(bag):
    """ -- """
    i = len(bag)
    print("\nbag has {} items: {}".format(i, bag))

def pick(bag, choice, *ind):
    """ -- """
    print(ind)
    if choice and not ind:
        try:
            bag.append(choice)
            print("\n{} has been added.".format(choice))
        except (ValueError, IndexError):
            print("Error")

    
    elif choice and ind:
        try:
            ind =  int("".join(str(ind)[2:-3]))
            if int(ind) > len(bag):
                print("Error")
            else:
                bag.insert(ind, choice)
                print("\n{} hsas been added.".format(choice))
        except ValueError:

            print(ind)
            ind = int("".join(str(ind)[1:-2]))
            if int(ind) > len(bag):
                print("Error")
            else:
                bag.insert(ind, choice)
                print("\n{} hsas been added.".format(choice))
            
    else: 
        print("Error")
    return bag



def drop(bag, choice):
    """ -- """
    cSplit = choice.split()
    if choice in bag:
        bag.remove(choice)
        print("{} have been removed!".format(choice))
    
    elif choice not in bag:
        try:
            item = cSplit[2]
            bag.remove(item)
            print("{} have been removed!".format(item))
        except (IndexError, ValueError):
            print("Error {} was not found in the backbag...".format(choice))

    else:
        print("Error")
    return bag


def swap(bag, choice, choice2):
    """ -- """
    cSplit = choice.split()
    cSplit = "".join(str(cSplit[2:3])[2:-2])
    print(cSplit)
    cSplit2 = choice2.split()    
    cSplit2 = "".join(str(cSplit2[3:])[2:-2])
    print(cSplit2)

    if choice in bag and choice2 in bag:
        try:
            index1 = bag.index(choice)
            index2 = bag.index(choice2)
            bag[index1], bag[index2] = bag[index2], bag[index1]
            print("{} and {} have been swaped".format(choice, choice2))
        except (ValueError, IndexError):
            print("Error.....")
    elif cSplit in bag or cSplit2 in bag:
        try:
            index1 = bag.index(cSplit)
            index2 = bag.index(cSplit2)
            bag[index1], bag[index2] = bag[index2], bag[index1]
            print("{} and {} have been swaped".format(cSplit, cSplit2)) 
        except (ValueError, IndexError):
            print("Error.....") 

    elif choice not in bag or choice2 not in bag:
        print("Error {} or {} was not found in list".format(choice, choice2))

    elif cSplit not in bag or cSplit2 not in bag:
        print("Error {} or {} was not found in list".format(cSplit, cSplit2))

    elif choice == choice2:
        print("Error {} is the same as {}".format(choice, choice2))




    return bag

    
