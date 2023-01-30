#!/usr/bin/env python3

"""
Main file for text analyzer
"""

import menu
import analyzer

def main():
    """
    Main loop for text analyzer
    """
    file_name = "phil.txt"
    menu.print_menu()
    while True:
        choice = input("> ")
        if choice == "menu":
            menu.print_menu()
        elif choice == "lines":
            print(analyzer.count_lines(file_name))
        elif choice == "words":
            print(analyzer.count_words(file_name))
        elif choice == "letters":
            print(analyzer.count_letters(file_name))
        elif choice == "word_frequency":
            print(analyzer.frequent_words(file_name))
        elif choice == "letter_frequency":
            print(analyzer.frequent_letters(file_name))
        elif choice == "all":
            print(analyzer.count_lines(file_name))
            print(analyzer.count_words(file_name))
            print(analyzer.count_letters(file_name))
            print(analyzer.frequent_words(file_name))
            print(analyzer.frequent_letters(file_name))
        elif choice == "change":
            file_name = input("Enter new file name: ")
        elif choice == "q":
            break

if __name__ == "__main__":
    main()
