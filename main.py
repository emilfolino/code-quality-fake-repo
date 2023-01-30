#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
main file for analyzer
"""
import menu
import analyzer

def main():

    """ Main"""
    the_new_file = "phil.txt"
    menu.menu()

    while True:

        choice = input("--> ") 
        if choice == "lines":
            print(analyzer.line_count(the_new_file))

        elif choice == "words":
            print(analyzer.word_count(the_new_file))

        elif choice == "letters":
            print(analyzer.letter_count(the_new_file))

        elif choice == "word_frequency":
            print(analyzer.word_frequency(the_new_file))

        elif choice == "letter_frequency":
            print(analyzer.letter_frequency(the_new_file))

        elif choice == "all":
            analyzer.analyze_all(the_new_file)

        elif "change" in choice:
            new_file = input("New file to use: ")
                
            the_new_file = analyzer.change_read_file(new_file)
            print("This is the new file being used: " + the_new_file)

        elif choice == "q":
            print("Bye, bye - and welcome back anytime!")
            break
                
            
        else:
            print("That is not a valid choice. You can only choose from the menu.")

        input("Press enter to continue...")

if __name__ == "__main__":
    main()
