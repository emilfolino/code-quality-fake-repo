"""
import menu 

    """
import menu

import analyzer

def main(file = 'phil.txt'):
    """
main function

    """
    while True:
        choice = input("input: \n")
        if choice == "menu":
            menu.menu()
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
            print(analyzer.lines(file))
            print(analyzer.words(file))
            print(analyzer.letters(file))
            print(analyzer.word_frequency(file))
            print(analyzer.letter_frequency(file))
        elif choice == "change":
            fil = input("Vad heter filen du vill ändra till? ")
            file = fil

        elif choice == "q":
            print("Bye, bye - and welcome back anytime!")
            break

        else:
            print("That is not a valid choice. You can only choose from the menu.")
        
        input("\nPress enter to continue...")

if __name__ == "__main__":
    main()
