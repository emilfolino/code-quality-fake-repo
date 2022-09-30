"""
main.py för kmom06
uppgift analyzer

Sharif Outagourte
"""

import menu
import analyzer as a

def main():
    """
    Run main
    """

    fil = "phil.txt"

    while(True):
        
        print(chr(27) + "[2J" + chr(27) + "[;H")

        menu.menu()

        print(f"currently in {fil}\n")

        choice = input("--> ")

        if choice == "q":
            break

        elif choice == "lines":
            a.lines(fil)

        elif choice == "words":
            a.words(fil)

        elif choice == "letters":
            a.letters(fil)

        elif choice == "word_frequency":
            a.word_frequency(fil)

        elif choice == "letter_frequency":
            a.letter_frequency(fil)

        elif choice == "all":
            a.all_f(fil)

        elif choice == "change":
            print(fil)
            fil = a.change()
            print(fil)

        else:
            print("Thats not a valid choice")

        input("Press Enter to continue..")

if __name__ == "__main__":
    main()
