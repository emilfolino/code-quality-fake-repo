#!/usr/bin/env python3

"""
The main file for the text analyzer
"""

import menu
import analyzer

filename = "phil.txt"

def main():
    """Main loop where user chooses action"""
    while True:
        global filename
        menu.print_menu()
        choice = input("--> ")

        if choice == "q":
            print("See you another time!")
            break

        elif choice == "lines":
            text = analyzer.read_file(filename)
            lines = analyzer.count_lines(text)
            print(lines)

        elif choice == "words":
            text = analyzer.read_file(filename)
            words = analyzer.count_words(text)
            print(words)

        elif choice == "letters":
            text = analyzer.read_file(filename)
            letters = analyzer.count_letters(text)
            print(letters)
        
        elif choice == "word_frequency":
            text = analyzer.read_file(filename)
            analyzer.word_frequency(text)

        elif choice == "letter_frequency":
            text = analyzer.read_file(filename)
            analyzer.letter_frequency(text)
        
        elif choice == "all":
            text = analyzer.read_file(filename)
            lines = analyzer.count_lines(text)
            print(lines)
            words = analyzer.count_words(text)
            print(words)
            letters = analyzer.count_letters(text)
            print(letters)
            analyzer.word_frequency(text)
            analyzer.letter_frequency(text)
        
        elif choice == "change": 
            filename = input("Input the new filename: ")

if __name__ == "__main__":
    main()
