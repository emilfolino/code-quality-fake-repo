#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""this module is the main program"""

import menu
import analyzer

def main():
    """this function holds the main choices"""
    filename = "phil.txt"
    while True:

        choice = menu.menu()

        if choice == "q":
            break

        if choice == "change":
            filename = analyzer.change()

        if choice == "word_frequency":
            analyzer.word_frequency(filename)

        if choice == "lines":
            analyzer.lines_analyzer(filename)

        if choice == "words":
            analyzer.words_analyzer(filename)

        if choice == "letters":
            analyzer.letters_analyzer(filename)

        if choice == "letter_frequency":
            analyzer.letter_frequency(filename)

        if choice == "all":
            #analyzer.all(filename)
            analyzer.lines_analyzer(filename)
            analyzer.words_analyzer(filename)
            analyzer.letters_analyzer(filename)
            analyzer.word_frequency(filename)
            analyzer.letter_frequency(filename)







if __name__ == "__main__":
    main()
