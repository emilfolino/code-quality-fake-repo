#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" Methods for menu"""

def menu_choice():
    """Printing menu method"""
    print(chr(27) + "[2J" + chr(27) + "[;H")
    print("\nWhat can I do for you?:\n")
    print("lines) \t\t\t---\t Print number of lines")
    print("words) \t\t\t---\t Print number of words")
    print("letters) \t\t---\t Print number of letters")
    print("word_frequency) \t---\t Print frequency of the most frequent words")
    print("letter_frequency) \t---\t Print frequency of the most frequent letters")
    print("all) \t\t\t---\t run whole analysis")
    print("change) \t\t---\t Change input file")
    print("q) \t\t\t---\t Quit.")
    print("\n\n")
    print("--------------------------")

    choiceInput = input("--> ")
    return choiceInput
