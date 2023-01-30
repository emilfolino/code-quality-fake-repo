"""Main"""

import menu
import analyzer


def main():
    """Call all other funtions to run the program"""
    while True:
        menu.menu()
        choice = input("\nEnter your selection: ")
        
        if choice == "q":
            print("Goodbye :)")
            break
        
        elif choice == "lines":
            print(analyzer.lines())

        elif choice == "words":
            print(analyzer.words())

        elif choice == "letters":
            print(analyzer.letters())

        elif choice == "word_frequency":
            print(analyzer.word_frequency())

        elif choice == "letter_frequency":
            print(analyzer.letter_frequency())

        elif choice == "all":
            print(analyzer.All())

        elif choice == "change":
            analyzer.change()

        input("\nPress enter to continue...")



if __name__ == "__main__":
    main()
