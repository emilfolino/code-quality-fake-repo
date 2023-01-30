#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Main function that runs the Analyzer program
"""

import menu
import analyzer

def main():
    """
    Main function keeps the program running until user input "q".
    """
    filename = "phil.txt"
    
    while True:
        usr_input = menu.menu().lower()
        
        if usr_input == "q":
            print("Exiting program")
            break
        elif usr_input == "lines":
            print(analyzer.lines(filename))
        elif usr_input == "words":
            print(analyzer.words(filename))
        elif usr_input == "letters":
            print(analyzer.letters(filename))
        elif usr_input == "word_frequency":
            analyzer.word_frequency(filename)
        elif usr_input == "letter_frequency":
            analyzer.letter_frequency(filename)
        elif usr_input == "all":
            print(analyzer.lines(filename))
            print(analyzer.words(filename))
            print(analyzer.letters(filename))
            analyzer.word_frequency(filename)
            analyzer.letter_frequency(filename)
        elif usr_input == "change":
            filename = input("Enter filename: ")
        else:
            menu.not_valid()
        
        input("\nPress enter to continue...")
            

if __name__ == "__main__":
    main()
