"""funktioner till marvin3:s ryggsäck"""


def pick(bag, insert_list, rand=-1):
    """Lägger till vad sak listan"""
    last = len(bag)
    if int(rand) < 0:
        bag.append(insert_list)
        print(f"You added {insert_list} in place {last}")
    elif int(rand) > len(bag):
        print("Error, " + str(rand) + " is non existing")
    else:
        bag.insert(int(rand), str(insert_list))
        print(f"You added {insert_list} in place {rand}")
    return bag






def inventory(bag):
    """Tittar vad som ligger i ryggsäcken"""
    print(bag)
    print(len(bag))


def drop(bag, choice):
    """tar bort vat ord från ryggsäcken"""
    try:
        new_inv = choice.split()
        word_1 = new_inv[-1]
        bag.remove(word_1)
        print("Word " + word_1 + " is removed from your bag: " + str(bag))
        return bag
    except ValueError:
        print("Error, backpack is " + str(word_1) + " , " + str(new_inv) + " and thats not in backpack")
        return bag

    except TypeError:
        print("Error, backpack is " + str(bag) + " , " + str(new_inv) + " and thats not in backpack")
        return bag
    except IndexError:
        print("Error, backpack is " + str(bag) + " , " + str(new_inv) + " and thats not in backpack")
        return bag


def swap(bag, word1, word2):
    """byter plats på två ord i ryggsäcken"""
    try:
        if word1 == word2:
            print("Error, you can not choose the same word " + str(word1) + " in " + str(bag))
            
        elif word1 and word2 in bag: 
            index1 = bag.index(word1)
            index2 = bag.index(word2)
            index1 = int(index1)
            index2 = int(index2)
            bag[index1], bag[index2] = bag[index2], bag[index1]
            print("You have now swapt places for " + word1 + " and " + word2 + " in " + str(bag))
            
        else:
            print("Error, backpack is " + str(bag) + " and " + word1 + word2 + " is non-existing")
        return bag


    except TypeError:
        print("Error, backpack is " + str(bag) + word1 + word2 + " is non-existing")
        return bag
    except ValueError:
        print("Error, backpack is " + str(bag) + word1 + word2 + " is non-existing")
        return bag
    except IndexError:
        print("Error, ryggsäcken är " + str(bag) + word1 + word2 + " fanns inte med")
        return bag
