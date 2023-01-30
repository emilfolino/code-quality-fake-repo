" Main module for text analyzer "


import menu
import analyzer


def main():
    """
    Main method for text analyzer
    """
    menu.menu()
    while True:
        choice = input("--> ")
        if choice == "q":
            print("Bye, bye - and welcome back anytime!")
            break
        elif choice == "lines":
            print(analyzer.lines())
        elif choice == "words":
            print(analyzer.words())
        elif choice == "letters":
            print(analyzer.letters())
        elif choice == "word_frequency":
            analyzer.word_frequency()
        elif choice == "letter_frequency":
            analyzer.letter_frequency()
        elif choice == "all":
            analyzer.all()
        elif choice == "change":
            analyzer.change()
        elif choice == "menu":
            menu.menu()
        else:
            print("That is not a valid choice. You can only choose from the menu.")
        print("\nEnter another option, or type 'menu' to see the options again.")
        # input("\nPress enter to continue...")


if __name__ == "__main__":
    main()
