#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Contains all funtionality for the menu.
"""

def menu():
    """
    Prints the menu selection
    """
    
    print(chr(27) + "[2J" + chr(27) + "[;H")
    print("lines) Count lines")
    print("words) Count words")
    print("letters) Count letters")
    print("word_frequency) Find 7 most used words")
    print("letter_frequency) Find 7 most used letters")
    print("all) Do everythin")
    print("change) Change file")
    print("q) quit.")
    
    usr_input = input("--> ")
    
    return usr_input

def not_valid():
    """
    Prints a prompt that input is not a valid choice.
    """
    print("Error. That is not a valid choice.")
