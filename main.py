#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Analyzer analyzes a given text file
"""

import menu
import analyzer


def main ():
    """
    Eternal loop until user choses to quit
    """
    text_file = "text/phil.txt"
    while True:
        menu.print_menu()
        choice = input("--> ")

        if choice == "q":
            print("Bye, bye - and welcome back anytime!")
            break
        elif choice == "lines":
            print(analyzer.count_lines(text_file))

        elif choice == "words":
            print(analyzer.word_count(text_file))

        elif choice == "letters":
            print(len(analyzer.letter_count(text_file)))

        elif choice == "word_frequency":
            print(analyzer.word_frequency(text_file))

        elif choice == "letter_frequency":
            print(analyzer.letter_frequency(text_file))

        elif choice == "all":
            analyzer.all_functions(text_file)

        elif choice == "change":
            # print(text_file)
            text_file = analyzer.change()

        else:
            print("Not a valid choice!")


        input("\nPress enter to continue...")

if __name__ == "__main__" :
    main()
