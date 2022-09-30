#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
main-dokument, innehåller evighetsloop tills input q
"""

import menu
import analyzer


def main(filename = "phil.txt"):
    """
    innehåller en evighetsloop tills q trycks
    """
    while True:
        menu.menu()
        choice = input("--> ")

        if choice == "q":
            print("Bye, bye - and welcome back anytime!")
            break

        elif choice == "change":
            inp = input("Enter filename: ")
            if inp == "lorum.txt":
                filename = "lorum.txt"
            else:
                filename = "phil.txt"

        elif choice == "lines":
            result = analyzer.lines(filename)
            print(result)
            print("\nWhat's next?")

        elif choice == "words":
            result = analyzer.words(filename)
            print(result)
            print("\nWhat's next?")
        
        elif choice == "letters":
            result = analyzer.letters(filename)
            print(result)
            print("\nWhat's next?")
        
        elif choice == "word_frequency":
            analyzer.word_frequency(filename)
            print("\nWhat's next?")

        elif choice == "letter_frequency":
            analyzer.letter_frequency(filename)
            print("\nWhat's next?")

        elif choice == "all":
            print(analyzer.lines(filename))
            print(analyzer.words(filename))
            print(analyzer.letters(filename))
            analyzer.word_frequency(filename)
            analyzer.letter_frequency(filename)
            print("\nWhat's next?")

        else:
            print("Wrong choice, I can't help you with that:(")
        input("\nPress enter to see more ->")

if __name__ == "__main__":
    print(main())
