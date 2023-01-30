#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Prints menu for analyzer"""

def menu():
    """Prints menu"""

    menu_string = """
    Welcome to file language analyzer,
    please type in one of the menu options below:
    
    lines               Count number of lines in file
    words               Count number of words in file
    letters             Count number of letters in file
    word_frequency      Shows word frequency
    letter_frequency    Shows word frequency
    all                 Runs all checks

    change              Changes file
    menu                Shows this menu
    q                   Quit
    """

    print(menu_string)
