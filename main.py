"""
Main code of the analyze text program
"""

import menu
import analyzer

def main():
    """
    Its an eternal loop, until q is pressed.
    It should check the choice done by the user and call a appropriate
    function.
    """

    OPENFILE = "phil.txt"

    while True:
        menu.show_menu()
        choice = input("--> ")

        content = []
        with open(OPENFILE) as filehandle:
            lines = filehandle.readlines()
        for e in lines:
            content.append(e.strip())

        if choice == "q":
            print("Bye, bye - and welcome back anytime!")
            break

        elif choice == "lines":
            print(analyzer.lines(content))

        elif choice == "words":
            print(analyzer.words(content))
            
        elif choice == "letters":
            print(analyzer.letters(content))

        elif choice == "word_frequency":
            analyzer.word_frequency(content)

        elif choice == "letter_frequency":
            analyzer.letter_frequency(content)

        elif choice == "all":
            analyzer.show_all(content)

        elif choice == "change":
            OPENFILE = analyzer.change()

        else:
            print("That is not a valid choice. You can only choose from the menu.")

        input("\nPress enter to continue...")

if __name__ == "__main__":
    main()
