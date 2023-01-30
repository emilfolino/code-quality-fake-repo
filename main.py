
"""
This whole program is used to analyse txt-files

Its an eternal loop, until q is pressed.
It should check the choice done by the user and call a appropriate
function.
"""

import menu
import analyzer

def main():
    """
    The main function of main.py and analyzer.py
    """
    file = "phil.txt"
    
    while True:
        menu.print_menu()
        choice = input("--> ")

        if choice == "q":
            break

        elif choice == "lines":
            print(analyzer.lines(file))

        elif choice == "words":
            print(analyzer.words(file))

        elif choice == "letters":
            print(analyzer.letters(file))

        elif choice == "word_frequency":
            print(analyzer.word_frequency(file))

        elif choice == "letter_frequency":
            print(analyzer.letter_frequency(file))

        elif choice == "all":
            print(analyzer.run_all(file))

        elif choice == "change":
            file = input("Enter filename: ")
            
        else:
            print("That is not a valid choice. You can only choose from the menu.")

        input("\nPress enter to continue...")

if __name__ == "__main__":
    main()
