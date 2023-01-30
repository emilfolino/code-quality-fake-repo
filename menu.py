#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
This file contains the menu.
"""

def display(text_file):
    """Function to show the menu"""
    print(chr(27) + "[2J" + chr(27) + "[;H")

    print(f"What do you want to do with {text_file}?\n")

    print("           [lines] Count the lines")
    print("           [words] Count the words")
    print("           [letters] Count the letters")
    print("  [word_frequency] Find the 7 most used words")
    print("[letter_frequency] Find the 7 most used letters")
    print("             [all] All of the above")
    print("          [change] Change file")
    print("               [q] Quit \n")
