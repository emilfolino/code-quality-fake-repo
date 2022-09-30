#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Presenting the app menu
"""

MSG = """lines) Count lines
words) Count words
letters) Count letters
word_frequency) Find 7 most used words
letter_frequency) Find 7 most used letters
all) Do everything
change) Change file
q) Quit
"""

def printMenu():
    """
    Prints a menu and let's the user decide what the program does. Returns user choice
    """

    choice = input(MSG)

    return choice

if __name__ == "__main__":
    pass
