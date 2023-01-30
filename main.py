"""
Main document
"""

import analyzer
import menu

def main():
    """
    Functions from analyzer
    """
    file = "phil.txt"
    while True:
        menu.menu()
        choice = input("--> ")

        if choice == "q":
            print("Bye, come back anytime!")
            break

        elif choice == "lines":
            analyzer.count_lines(file)

        elif choice == "words":
            analyzer.count_words(file)

        elif choice == "letters":
            analyzer.count_letters(file)

        elif choice == "word_frequency":
            analyzer.word_frequency(file)

        elif choice == "letter_frequency":
            analyzer.letter_frequency(file)

        elif choice == "all":
            analyzer.all_functions(file)

        elif choice == "change":
            file = analyzer.change_file()

        else:
            print("Not a valid command.")
        input("\nPress enter to continue...")

if __name__ == "__main__":
    main()
