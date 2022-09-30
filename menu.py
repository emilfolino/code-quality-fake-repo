#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Module containing function to display the menu
"""

def printMenu():
    """
    function to print the menu options.
    Returns the option that was selected
    """
    print("lines) Count lines")
    print("words) Count words")
    print("letters) Count letters")
    print("word_frequency) Find 7 most used words")
    print("letter_frequency) Find 7 most used letters")
    print("all) Do everything")
    print("change) Change file to analyze")
    print("q) Quit")

    choice = input("-->")
    return choice
