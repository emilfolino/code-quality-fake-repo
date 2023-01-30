"""
Contains the commando loop, like the while loop for marvin.
"""

import menu
import analyzer


def main():
    """
    Menu driven function, getting returns from analyzer.py
    """
    while True:
        menu.print_menu()
        choice = input("--> ")


        if choice == "q":
            print("Welcome back!")
            break
        
        elif choice == "lines":
            print(analyzer.line_count())

        elif choice == "words":
            print(analyzer.word_count())

        elif choice == "letters":
            print(analyzer.letter_count())

        elif choice == "word_frequency":
            print(analyzer.word_freq())

        elif choice == "letter_frequency":
            print(analyzer.letter_freq())

        elif choice == "all":
            print(analyzer.all_file())

        elif choice == "change":
            file = str(input("Enter the new filename: "))
            analyzer.change_file(file)
            print(f"File changed to: {file}")

        else:
            print("Not a valid choice, try again!")



if __name__ == "__main__":
    main()
