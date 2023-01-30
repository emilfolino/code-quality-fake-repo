#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Command loop for analyzer"""

import analyzer
import menu

def main():
    """Main menu choice loop"""
    filename = "phil.txt"
    while True:
        menu.menu()

        choice = input("--> ")

        if choice == "q":
            print("Bye, bye - and welcome back anytime!")
            break
        
        elif choice == "menu":
            continue

        elif choice == "lines":
            print(analyzer.lines_analysis(filename))

        elif choice == "words":
            print(analyzer.words_analyzer(filename))

        elif choice == "letters":
            print(analyzer.letters_analyzer(filename))

        elif choice == "word_frequency":
            analyzer.word_frequency(filename)

        elif choice == "letter_frequency":
            analyzer.letter_frequency(filename)

        elif choice == "all":
            print(analyzer.lines_analysis(filename))
            print(analyzer.words_analyzer(filename))
            print(analyzer.letters_analyzer(filename))
            analyzer.word_frequency(filename)
            analyzer.letter_frequency(filename)

        elif choice == "change":
            filename = input("Enter filename: ")
            print("File changed to " + filename)

        else:
            print("That is not a valid choice. You can only choose from the menu.")

        input("\nPress enter to continue...")


if __name__ == "__main__":
    main()
