#!/usr/bin/env python3

"""main for analyzer"""

import menu
import analyzer

def main():
    """menu selector"""
    menu.print_menu()
    current_file = "phil.txt"
    current_content = analyzer.file_loader(current_file) #init for workfile

    while True:

        choice = input("--> ")

        if choice == "lines":
            print(analyzer.count_lines(current_content)) 
        elif choice == "words":
            print(analyzer.count_words(current_content))  
        elif choice == "letters":
            print(analyzer.count_letters(current_content)) 
        elif choice in ("word_frequency","wf"):
            analyzer.pretty_print(analyzer.word_frequency(current_content))
        elif choice in ("letter_frequency","lf"):
            analyzer.pretty_print(analyzer.letter_frequency(current_content))
        elif choice == "all":
            print(analyzer.count_lines(current_content))
            print(analyzer.count_words(current_content))
            print(analyzer.count_letters(current_content))
            analyzer.pretty_print(analyzer.word_frequency(current_content))
            analyzer.pretty_print(analyzer.letter_frequency(current_content))
        elif choice == "change":
            current_file = input("Enter filename: ")
            current_content = analyzer.file_loader(current_file)
        elif choice == "menu":
            menu.print_menu()
        elif choice == "active":
            print(current_file)
        elif choice == "print":
            print(current_content)
        elif choice == "q":
            break

if __name__ == "__main__":
    main()
    