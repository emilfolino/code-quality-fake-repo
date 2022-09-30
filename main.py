"""
Main function containing the program loop
"""

import menu
import analyzer


def main():
    """
    This is the main function where the functions are being called
    """
    change = "phil.txt"
    while True:
        choice = menu.menu()
        if choice == "lines":
            print(analyzer.line_count(change))

        elif choice == "words":
            print(analyzer.word_count(change))

        elif choice == "letters":
            print(analyzer.letter_count(change))

        elif choice == "word_frequency":
            analyzer.word_frequency(change)

        elif choice == "letter_frequency":
            analyzer.letter_frequency(change)

        elif choice == "all":
            analyzer.print_all(change)

        elif choice == "change":
            new_file = input("Insert file: ")
            change = analyzer.change_file(new_file)

        elif choice == "q":
            print("Quitting program")
            break

        else:
            print("That is not a valid choice")
        input("Press enter to continue")

if __name__ == "__main__":
    main()
