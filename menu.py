#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
modul-dokument, skall enbart innehålla kod för att visa menyn.
"""

def menu():
    """
    skriver ut menyval
    """
    print(chr(27) + "[2J" + chr(27) + "[;H")
    print("lines) Analyze lines")
    print("words) Analyze words.")
    print("letters) Analyze letters.")
    print("word_frequency) Find 7 most used words.")
    print("letter_frequency) Find 7 most used letters.")
    print("all) Do everything.")
    print("change) Change file.")
    print("q) Exit the program.")
