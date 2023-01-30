#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Code for showing the menu.
"""

def menu():
    """Prints the different parts of the menu."""
    print("Hi, what can I do for you today?")
    print("'lines' - Prints the amount of lines in a textfile.")
    print("'words' - Prints the amount of words in a textfile.")
    print("'letters' - Prints the amount of letters in a textfile.")
    print("'word_frequency' - Prints the frequency of words in a textfile.")
    print("'letter_frequency' - Prints the frequency of letters in a textfile.")
    print("'all' - Prints all of the above at the same time.")
    print("'change' - Changes the textfile, which the program reads data from.")
    print("'q' - Quit.")

def menu_choice():
    """Returns the value of the input prompt."""
    choice = input("--> ")
    return choice
