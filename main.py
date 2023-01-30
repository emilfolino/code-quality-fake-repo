#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Main program Analyzer
"""
import menu
import analyzer

def main():
    """
    Main function
    """

    file = "phil.txt"

    while True:
        menu.print_menu()
        choice = input("--> ")

        if (choice in ("q", "Q")):
            print("Bye, bye - and welcome back anytime!")
            break # När man trycker Q hoppar den ur while-satsen

        # elif "menu" in choice:
        #     menu.print_menu()

        elif "lines" in choice:
            print(analyzer.lines(file))

        elif "words" in choice:
            print(analyzer.words(file))

        elif "letters" in choice:
            print(analyzer.letters(file))

        elif "word_frequency" in choice:
            analyzer.word_frequency(file)

        elif "letter_frequency" in choice:
            analyzer.letter_frequency(file)

        elif "all" in choice:
            analyzer.all_functions(file)

        elif "change" in choice:
            file = analyzer.change(file)

        else:
            print("That is not a valid choice. You can only choose from the menu")

        input("\nPress enter to continue...")

if __name__ == "__main__":
    main()
