"""---"""

import menu as mu
import analyzer as a

mu.menu()

def main():

    """
    Its an eternal loop, until q is pressed.
    It should check the choice done by the user and call a appropriate
    function.
    """
    cfile = "phil.txt"
    while True:
        choice = input("--> ")
        

        if choice == "q":
            print("Bye, bye - and welcome back anytime!")
            break
        elif choice == "lines":
            print(a.linesCount(cfile))
        elif choice == "words":
            print(a.wordsCount(cfile))
        elif choice == "letters":
            print(a.lettersCount(cfile))
        elif choice == "word_frequency":
            a.word_frequency(cfile)
        elif choice == "letter_frequency":
            a.letter_frequency(cfile)
        elif choice == "all":
            a.printAll(cfile)
        elif choice == "change":
            
            cfile = input("Enter new file name: ")
            
        elif choice == "pfile":
            print(cfile)
     

        else:
            print("That is not a valid choice. You can only choose from the menu.")

        input("\nPress enter to continue...")

if __name__ == "__main__":
    main()
