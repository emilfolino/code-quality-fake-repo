#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
Main program file for Analyzer
"""


# Module imports
import menu
import analyzer


def main(filename="phil.txt"):
    """ Main module, loads menu and handles input"""

    while True:

        menu.menu()

        command = input("Enter command: ").lower()

        if command == "q":

            print("exiting script...")
            break

        elif command == "lines":

            print(analyzer.count_lines(filename))

        elif command == "words":

            print(analyzer.count_words(filename))

        elif command == "letters":

            print(analyzer.count_letters(filename))

        elif command == "word_frequency":

            print(analyzer.word_frequency(filename))

        elif command == "letter_frequency":

            print(analyzer.letter_frequency(filename))

        elif command == "all":

            print(analyzer.all_show(filename))

        elif command == "change":
            filename = input("Enter filename: ")


if __name__ == "__main__":
    main()
