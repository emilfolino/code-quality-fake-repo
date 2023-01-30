#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Main for the text analysis program
"""

import analyzer
import menu

"""
Its an eternal loop, until q is pressed.
It should check the choice done by the user and call a appropriate
function.
"""
def main():
    """Main method containing structure for program"""

    filename = "phil.txt"
    with open(filename) as filehandle:
        phil = filehandle.readlines()

    while True:

        choice = menu.menu_choice()

        if choice == "q":
            analyzer.choice_q()
            break

        elif choice == "lines":
            numberNonEmptyLines = analyzer.lines(phil)
            print("Number of non-empty lines in {txtname} is equal to {numberRows}".
            format(txtname = filename, numberRows = numberNonEmptyLines))

        elif choice == "words":
            numberWords = analyzer.words(phil)
            print("Number of words in {txtname} is equal to {words}".
            format(txtname = filename, words = numberWords))

        elif choice == "letters":
            numberLetters = analyzer.letters(phil)
            print("Number of letters in {txtname} is equal to {letters}".
            format(txtname = filename, letters = numberLetters))

        elif choice == "word_frequency":
            wordFreq = analyzer.word_frequency(phil)
            print(wordFreq)

        elif choice == "letter_frequency":
            letterFreq = analyzer.letter_frequency(phil)
            print(letterFreq)

        elif choice == "all":
            allText = analyzer.allFunc(phil)
            print(allText)

        elif choice == "change":
            philOld = phil
            phil = analyzer.change(phil)
            if philOld != phil:
                print("\nFile has been changed")
            else:
                print("\nFile has not been changed")

        else:
            analyzer.not_valid()

        analyzer.continue_func()

if __name__ == "__main__":
    main()
