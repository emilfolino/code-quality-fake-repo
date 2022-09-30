"""
All codes relevent to showing menu
"""

def showMenu():
    """
    Show the menu  
    """
    print(chr(27) + "[2J" + chr(27) + "[;H")
    menu = """

        lines) Count lines
        words) Count words
        letters) Count letters
        word_frequency) Find 7 most used words
        letter_frequency) Find 7 most used letters
        all) Do everything
        change) Change file
        q) Quit

    """
    print(menu)
