"""
Prints the menu used in the analysis program
"""
def print_menu():
    """
    Prints most of the text used in the menu
    """
    print(chr(27) + "[2J" + chr(27) + "[;H")
    print("lines) Count lines")
    print("words) Count words")
    print("letters) Count letters")
    print("word_frequency) 7 most used words")
    print("letter_frequency) 7 most used letters")
    print("all) Do everything")
    print("change) Change file")
    print("--------------------------")
    print("Type quit or q to exit")
    print("--------------------------\n")
