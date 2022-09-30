"""
Inv functions
"""
def pick(print_list, choice_string, choice_index=None):
    """
    Spara stränger med positioner i listan eller utan
    """
    if choice_index is None:
        print_list.append(choice_string)
        print(f"{choice_string} has been added.")
    else:
        if int(len(print_list)) >= int(choice_index):
            print_list.insert(int(choice_index), choice_string)
            print(f"{choice_string} has been added to index \"{choice_index}\".")
        else:
            print(f"Error: Position {choice_index} is out of the bagpack range")

    return print_list

def inventory(bagpack): 
    """
    ett meddelande som innehåller hur många saker som befinner sig i ryggsäcken 
    och alla saker som ligger där inne.
    """
    tot = len(bagpack)
    answer = f"Bagback has {tot} items: {bagpack}"
    return print(answer)

def drop(print_list, word):
    """
    kasta bort en sak från ryggsäcken.
    """
    try:
        i = print_list.index(word)
        print_list.pop(i)
        print(f"{word} has been removed.")
    except (ValueError, IndexError):
        print(word)
        print("Error: I have no index like that in the bagpack")
    
    return print_list


def swap(bagpack, position1, position2):
    """
    Bytr plats på saker i listan
    """
    try:
        if position1 != position2:
            pos1 = bagpack.index(position1)
            pos2 = bagpack.index(position2)
            temp = bagpack[pos1]
            bagpack[pos1] = bagpack[pos2]
            bagpack[pos2] = temp
            print(f"\"{position1}\" and \"{position2}\" has been swaped.")
        else:
            print("Error")
    except ValueError:
        print(f"Error: I have no \"{position1}\" or \"{position2}\" in the bagpack.")
    return bagpack
