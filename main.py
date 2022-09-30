"""
Analyse a text
"""
import menu
import analyzer


def main():
    """
    Its an eternal loop, until q is pressed.
    It should check the choice done by the user and call a appropriate
    function.
    """

    menu.menu()
    name_of_file = "phil.txt"
    while True:
        choice = input("--> ")

        if choice == "q":
            print("Bye, bye - and welcome back anytime!")
            break

        elif choice == "menu": 
            #Stor förvirring råder! Ska menu vara som i uppgiftsfilmen (inte finnas som ett eget menyval)?
            print(menu.menu())

        elif choice == "lines":
            result = analyzer.lines(name_of_file)
            print(result)

        elif choice == "words":
            result = analyzer.words(name_of_file)
            print(result)

        elif choice == "letters":
            result = analyzer.letters(name_of_file)
            print(result)

        elif choice == "word_frequency":
            analyzer.word_frequency(name_of_file)

        elif choice == "letter_frequency":
            analyzer.letter_frequency(name_of_file)

        elif choice == "all2": #så här hade jag det först
            print(analyzer.lines(name_of_file))
            print(analyzer.words(name_of_file))
            print(analyzer.letters(name_of_file))
            analyzer.word_frequency(name_of_file)
            analyzer.letter_frequency(name_of_file)

        elif choice == "all": 
            #Här är en funktion som kallar på de andra funktionerna, 
            #så att det finns minst en funktion för varje menyval(?)
            analyzer.all_included(name_of_file)


        elif choice == "change":
            fname = input('Enter the file name: ')
            try:
                with open(fname) as _:
                    print("File to analyze: ", fname)
                name_of_file = fname
            except FileNotFoundError:
                print("File could not be opened: ", fname)

        else:
            print("That is not a valid choice. You can only choose from the menu.")

        input("\nPress enter to continue...")


if __name__ == "__main__":
    main()
