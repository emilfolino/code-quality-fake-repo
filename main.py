#!/usr/bin/env python3
# -- coding: utf-8 --
"""
Main.py Funktionen
"""
import analyzer
import menu

def main ():
    """
    Main Function 
    """
    while True:
        menu.menu()

        Value = 'q' , 'Q'
        Choice = ""

        Choice = input("--> ")

        
        if Choice in Value:
            print("Oh, well, ill see you soon again!")
            break

        elif Choice == "lines":
            print(analyzer.LineCount())

        elif Choice == "words":
            print(analyzer.WordCount())

        elif Choice == "letters":
            print(analyzer.LetterCount())

        elif Choice == "letter_frequency":
            analyzer.letter_frequency()

        elif Choice == "word_frequency":
            analyzer.word_frequency()

        elif Choice == "change":
            FilensNamn = input("Enter Filename: ")
            analyzer.ChangeFile(FilensNamn)
            
        elif Choice == "all":
            analyzer.AllData()

if __name__ == "__main__":
    main()
