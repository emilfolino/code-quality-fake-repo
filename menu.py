#!/usr/bin/env python3
"""
Menu module for the analyzer
"""

def menu():
    """
    Menu function for analyzer
    """
    print(
        """
        lines) Count lines
        words) Count words
        letters) Count letters
        word_frequency) Find 7 most used words
        letter_frequency) Find 7 most used letters
        all) Do everything
        change) Change file
        q) quit
        """
    )
    choice = input("--> ")

    return choice
