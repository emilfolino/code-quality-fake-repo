#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Program that receive input and can analyze a text.
"""

import menu
import analyzer

def main():
    """
    Its an eternal loop, until q is pressed.
    It should check the choice done by the user and call a appropriate
    function.
    """
    textFile = "phil.txt"

    menu.menuPrint()

    while True:
        choice = input("--> ")

        if choice == "q":
            print("Exiting program!")
            break
        
        elif choice == "lines":
            print(analyzer.lines_count(textFile))

        elif choice == "words":
            print(analyzer.words_count(textFile))

        elif choice == "letters":
            print(analyzer.letters_count(textFile))

        elif choice == "word_frequency":
            analyzer.word_frequency(textFile)

        elif choice == "letter_frequency":
            analyzer.letter_frequency(textFile)

        elif choice == "all":
            analyzer.all_function(textFile)

        elif choice == "change":
            change = input("Enter text file to change to: ")
            if change == "lorum.txt":
                textFile = "lorum.txt"
            else:
                textFile = "phil.txt"

        else:
            print("That is not a valid choice. You can only choose from the menu.")

        input("\nPress enter to continue...")
        menu.menuPrint()

if __name__ == "__main__":
    main()
