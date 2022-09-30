"""
Module for the menu
"""


def menu():
    """
    The menu function
    """
    print("lines) Count lines")
    print("words) Count words")
    print("letters) Count letters")
    print("word_frequency) Find 7 most used words")
    print("letter_frequency) Find 7 most used letters")
    print("all) Do everything")
    print("change) Change file")
    choice = input("--> ")
    return choice
