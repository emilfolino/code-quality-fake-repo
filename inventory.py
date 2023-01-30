
"""
    bagpack fun
"""
def inventory(bag):
    """
    bagpack inv
    """
    if len(bag) !=0:
        print(f"Bagpack has {len(bag)} items: {bag}")
    print(bag)
    
    
def pick (bag , word, index = ""):
    """
    bagpack pick
    """
    if index == "":
        bag.append(word) 
        print(f'"{word}" has been added.')
        return bag
    if len(bag) >= int(index):
        bag[int(index):int(index)] = [word]
        print(f'"{word}" has been added on index {index}.')
        return bag
    print(f'Error: the index({index}) is too high') 
    return bag
def swap(bag, wordOne, wordTwo):
    """
    bagpack swap
    """
    try:
        if wordOne == wordTwo:
            print("Error") 
            return bag
        pos1 = bag.index(wordOne)
        pos2 = bag.index(wordTwo)
        bag[pos1], bag[pos2] = bag[pos2], bag[pos1]
        print(f'"{wordOne}" and "{wordTwo}" has been swaped.')
        return bag
    except ValueError:
        if wordOne not in bag and wordTwo not in bag:
            print(f'Error: I have no "{wordOne}" and "{wordTwo}" in bagpack.')
            return bag
        if wordOne not in bag:
            print(f'Error: I have no "{wordOne}" in bagpack.')
            return bag

        print(f'Error: I have no "{wordTwo}" in bagpack.')    
        return bag
      
def drop(bag, wordDel):
    """
    bagpack drop
    """
    try:
        bag.remove(wordDel)
        print(f'"{wordDel}" has been removed.')
        return bag
    except ValueError:
        print(f'Error: "{wordDel}" is not in the bagpack')   
        return bag
