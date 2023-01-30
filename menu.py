"""
This file is only used to print options for main.py
"""

def print_menu():
    """
    Print text describing menu options for main.py
    """
    print(chr(27) + "[2J" + chr(27) + "[;H")
    print("lines)   Count lines")
    print("words)   Count words")
    print("letters) Count letters")
    print("word_frequency)   Find 7 most used words")
    print("letter_frequency) Find 7 most used letters")
    print("all) Do everything")
    print("change) Change file")
    print("q) Quit.\n")
