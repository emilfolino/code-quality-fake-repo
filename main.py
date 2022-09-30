#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Program for analyzing text files. 
"""



from menu import printMenu as choiceMenu
import analyzer as anz

def main():
    """
    Text analyzer with a simple menu to start up with.
    """
    choice = ""
    file_to_read = "phil.txt"

    while choice != "q":
        choice = choiceMenu()
        
        if choice == "lines":
            anz.print_lines(file_to_read)
        elif choice == "words":
            anz.print_words(file_to_read)
        elif choice == "letters":
            anz.print_letters(file_to_read)
        elif choice == "word_frequency":
            anz.print_word_frequency(file_to_read)
        elif choice == "letter_frequency": 
            anz.print_letter_frequency(file_to_read)
        elif choice == "all":
            anz.print_all_info(file_to_read)
        elif choice == "change":
            file_to_read = anz.change()
        else:
            print("Not a valid command")


if __name__ == "__main__":
    main()
