#!/usr/bin/env python3
"""
Main module for the analyzer
"""

import menu
import analyzer

def main():
    """
    Main function for analyzer
    """
    #Variable for filename
    filename = "phil.txt"

    run = True
    while run:
        choice = menu.menu()

        if choice == "lines":
            try:
                print(str(analyzer.count_lines(filename)))
            except FileNotFoundError as e:
                print(str(e))
            except ValueError as e:
                print(str(e))
        elif choice == "words":
            try:
                print(str(analyzer.count_words(filename)))
            except FileNotFoundError as e:
                print(str(e))
            except ValueError as e:
                print(str(e))
        elif choice == "letters":
            try:
                print(analyzer.count_letters(filename))
            except FileNotFoundError as e:
                print(str(e))
            except ValueError as e:
                print(str(e))
        elif choice == "word_frequency":
            try:
                print(analyzer.frequency_result_to_string(analyzer.word_frequency(filename)))
            except FileNotFoundError as e:
                print(str(e))
            except ValueError as e:
                print(str(e))
        elif choice == "letter_frequency":
            try:
                print(analyzer.frequency_result_to_string(analyzer.letter_frequency(filename)))
            except FileNotFoundError as e:
                print(str(e))
            except ValueError as e:
                print(str(e))
        elif choice == "all":
            try:
                print(analyzer.analyzer_data_as_string(analyzer.analyze_everything(filename)))
            except FileNotFoundError as e:
                print(str(e))
            except ValueError as e:
                print(str(e))
        elif choice == "change":
            filename = analyzer.change()
        elif choice == "q":
            print("Bye bye")
            run = False
        else:
            print("Not a valid choice")

if __name__ == "__main__":
    main()
