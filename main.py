"""
docstring
"""
import menu
import analyzer
def main():
    """
    main
    """

    while True:
        menu.menu_choice()
        choice = input("--> ")

        if choice == "q":
            print("Bye")
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
            analyzer.all_()

        elif choice == "change":
            n_file = input("Give me a new file: ")
            analyzer.change(n_file)

        else:
            print("That is not a valid choice, try again: ")

if __name__ == "__main__":
    main()
