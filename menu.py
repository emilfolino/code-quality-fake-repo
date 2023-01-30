#!/usr/bin/env python3

"""menu options for analyzer"""

import analyzer

def menu():
    """menu selector"""
    print_menu()
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
            print_menu()
        elif choice == "active":
            print(current_file)
        elif choice == "print":
            print(current_content)
        elif choice == "q":
            break

def print_menu():
    """menu printer"""
    print("""
    lines| count lines
    words| count words
    letters| count letters
    word_frequency| find 7 most used words
    letter_frequency| find 7 most used letters
    all| do everything
    change| change file
    menu| displays menu
    active| show active file
    print| show content
    q| quit
    
    """, end='')
