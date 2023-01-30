#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Main menu for anaylising text and words in kmom06
"""

import analyzer
import menu

def main():
    """
    Its an eternal loop, until q is pressed.
    It checks the input string done by the user and call function.
    """
    file = ("phil.txt")
    print(menu.menu())
    while(True):
        choice = input("--> ")
        if choice == "q":
            print("Auf Wiedersehn!")
            break

        elif "lines" in choice:
            print(analyzer.line_count(file))

        elif "words" in choice:
            print(analyzer.word_count(file))

        elif "letters" in choice:
            print(analyzer.letter_count(file))

        elif "word_frequency" in choice:
            analyzer.word_frequency(file)

        elif "letter_frequency" in choice:
            analyzer.letter_frequency(file)

        elif "all" in choice:
            print(analyzer.alla(file))

        elif "change" in choice:
            file = analyzer.change(file)

        else:
            print("That is not a valid choice. You can only choose from the menu.")

        # input("\nPress enter to continue...")


if __name__ == "__main__":
    main()
