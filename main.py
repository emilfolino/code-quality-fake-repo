#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Module containing main loop. Imports all the functions for the menu choices
"""

from menu import printMenu 
from analyzer import linesAnalyzer, wordsAnalyzer, lettersAnalyzer, wordFrequencyAnalyzer
from analyzer import letterFrequencyAnalyzer, allAnalyzer, changeFile

def main():
    """
    Mainfunction for the text analyzer.
    Prints a menu and based on user input calls the right analyzer function.
    """

    analyzingText = "phil.txt"

    while True:

        choice = printMenu()

        if choice == "lines":
            print(linesAnalyzer(analyzingText))
        elif choice == "words":
            print(wordsAnalyzer(analyzingText))
        elif choice == "letters":
            print(lettersAnalyzer(analyzingText))
        elif choice == "word_frequency":
            wordFrequencyAnalyzer(analyzingText)
        elif choice == "letter_frequency":
            letterFrequencyAnalyzer(analyzingText)
        elif choice == "all":
            allAnalyzer(analyzingText)
        elif choice == "change":
            analyzingText = changeFile(analyzingText)
        elif choice == "q":
            break
        else:
            print("Not a valid command!")
        


if __name__ == "__main__":
    main()
