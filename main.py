#!/usr/bin/env python3
"""
Main program
"""

import menu
import analyzer
"""
Importing modules
"""

def main():
    """
    Function for main program that holds the while loop/menu options.
    """
    filename = "phil.txt"
    while True:
        choice = menu.menu()

        if choice == "q":
            print("\nSee you soon!")
            break

        elif choice == "lines":
            print(analyzer.number_of_lines(filename))

        elif choice == "words":
            print(analyzer.number_of_words(filename))

        elif choice == "letters":
            print(analyzer.number_of_letters(filename))

        elif choice == "word_frequency":
            analyzer.word_frequency(filename)

        elif choice == "letter_frequency":
            analyzer.letter_frequency(filename)

        elif choice == "all":
            analyzer.all_funcs(filename)

        elif choice == "change":
            filename = input("Enter filename: ")

        else:
            print("That is not a valid choice. You can only choose from the menu.")

        input("\nPress enter to continue...")

if __name__ == "__main__":
    main()
