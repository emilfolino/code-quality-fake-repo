"""Main module for running the analyzer"""

import menu
import analyzer as a

def main():
    """main function loop"""
    while True:
        menu.printMenu()

        choice = input("--> ")

        if choice == "q":
            print("Closing analyzer..")
            break
        elif choice == "lines":
            print(a.lines())
        elif choice == "words":
            print(a.words())
        elif choice == "letters":
            print(a.letters())
        elif choice == "word_frequency":
            a.word_frequency()
        elif choice == "letter_frequency":
            a.letter_frequency()
        elif choice == "all":
            a.all_functions()
        elif choice == "change":
            name = input("Enter filename: ")
            a.change(name)

        input("\nPress enter to continue...")

if __name__ == '__main__':
    main()
