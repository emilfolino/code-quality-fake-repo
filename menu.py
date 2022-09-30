"""
printing out menu
"""

def menu():
    """
prints out different menu options
"""
    print("lines) Count lines")
    print("words) Count words")
    print("letters) Count letters")
    print("word_frequency) Find 7 most used word")
    print("letter_frequency) Find 7 most used letter")
    print("all) Do everything")
    print("change) Change file")
    print("q) quit.")
    choice = input("--> ")
    return choice
