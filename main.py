#Project by Croyse

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Main sidan
'''
import menu
import analyzer

def main():
    '''
    Main
    '''
    file = "phil.txt"
    
    while True:

        menu.menu()
        choice = input("--> ")

        if choice in ('q', 'Q'):
            print("Goodbye!")
            break
        
        elif choice == "lines":
            print("Line Count:", analyzer.line_counter(file))

        elif choice == "words":
            print("Number of words:",analyzer.word_counter(file))
        
        elif choice == "letters":
            print("Number of letters:",  analyzer.letter_counter(file))

        elif choice == "word_frequency":
            print(analyzer.word_frequency(file))

        elif choice == "letter_frequency":
            print(analyzer.letter_frequency(file))
        
        elif choice == "all":
            print("All:" , analyzer.every_function(file))

        elif choice == "change":
            file = "lorum.txt" if file == "phil.txt" else "phil.txt"

        else:
            print("That is not valid. Choose a valid option.")


if __name__ == "__main__":
    main()
