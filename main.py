#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
A word analyzing program.
"""

import menu
import analyzer

def main():
    """The program's main() function."""

    with open("/home/dbwebb/repo/me/kmom06/analyzer/phil.txt", "r") as file: 
        #Note to self: /cygdrive/c/users/carlm/dbwebb-kurser/python/me/kmom06/analyzer/phil.txt
        result = []
        result.append(file.readlines())
        file.seek(0)
        result.append(file.read().lower())

    while True:
        menu.menu()
        choice = menu.menu_choice()

        if choice == "q":
            analyzer.menyval_q()
            break

        elif choice == "lines":
            analyzer.menyval_lines(result[0])

        elif choice == "words":
            analyzer.menyval_words(result[1])

        elif choice == "letters":
            analyzer.menyval_letters(result[1])

        elif choice == "word_frequency":
            analyzer.menyval_word_frequency(result[1])

        elif choice == "letter_frequency":
            analyzer.menyval_letter_frequency(result[1])

        elif choice == "all": 
            analyzer.all_function(result[0], result[1])

        elif choice == "change":
            change_file = input("Name of the new file (something.txt): ")
            if change_file == "lorum.txt":
                result = analyzer.change()

        else:
            print("That is not a valid choice. You can only choose from the menu.")

        input("\nPress enter to continue...")

if __name__ == "__main__":
    main()
    