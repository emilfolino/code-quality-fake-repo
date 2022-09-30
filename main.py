#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Word analyzer.
"""
import menu
import analyzer


def main():
    """
    Never ending loop
    """
    
    file_name = 'phil.txt'
    content = analyzer.read_file(file_name)

    menu.menu()

    while(True):

        #content = analyzer.read_file(file_name)
        choice = input("--> :")
        
        if choice == "q":
            break
        
        if choice == "menu":
            menu.menu()

        elif choice == "lines":
            print(analyzer.lines(content))

        elif choice == "words":
            print(analyzer.words(content))

        elif choice == "letters":
            print(analyzer.letters(content))

        elif choice == "word_frequency":
            print(analyzer.word_frequency(content))

        elif choice == "letter_frequency":
            print(analyzer.letter_frequency(content))

        elif choice == "all":
            print(analyzer.do_all(content))

        elif choice == "change":
            file_name = input("new file: ")
            content = analyzer.read_file(file_name)

if __name__ == "__main__":
    
    main()
