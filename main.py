"""
This is the main file where the eternal loop is.
"""

import menu
import analyzer

def main():
    """
    The loops checks what the user want to do and then does what the user told it to.
    """
    while True:

        menu.print_menu()

        choice = input("--> ")

        if choice == "q":
            print("Bye, bye - and welcome back anytime!")
            break

        elif choice == "lines":
            print(analyzer.amount_of_lines())

        elif choice == "words":
            print(analyzer.amount_of_words())

        elif choice == "letters":
            print(analyzer.amount_of_letters())

        elif choice == "word_frequency":
            analyzer.word_frequency()

        elif choice == "letter_frequency":
            analyzer.letter_frequency()

        elif choice == "all":
            analyzer.print_all()

        elif choice == "change":
            inp = input("Enter filename: ")
            analyzer.change(inp)


        else:
            print("That is not a valid choice. You can only choose from the menu.")

        input("\nPress enter to continue...")

if __name__ == "__main__":
    main()
