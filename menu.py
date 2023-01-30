#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""this module holds the menu for the main program"""

def menu():
    """this function prints out menus"""
    print(chr(27) + "[2J" + chr(27) + "[;H")
    print("lines) count the number of lines")
    print("words) count the number of words ")
    print("letters) count the letters of words ")
    print("letter_frequncy) gets the seven most used letters")
    print("word_frequncy) gets the seven most used words")
    print("all) gets all the above")
    print("Type q for quitting")
    print("Type change) to change filename")
    choice = input("----->   ")
    return choice
