"""
Menu for the analyze text program
"""

def show_menu():
    """
    Show menu
    """
    print(chr(27) + "[2J" + chr(27) + "[;H")
    print("lines) Count lines")
    print("words) Count words")
    print("letters) Count letters")
    print("word_frequency) Find 7 most used words") 
    print("letter_frequency) Find 7 most used letters") 
    print("all) Do averything")
    print("change) Change file")
    print("q) quit")
