"""
Takes input and performs different tasks
"""
import menu
import analyzer


def main():
    """
    Takes input and performs different tasks with functions from menu and analyzer
    """

    file_name = "phil.txt"

    while(True):
        menu.print_menu()
        choice = input("Choose from menu: ")

        if (choice == "lines"):
            print(analyzer.lines(file_name))
            pressEnterToContinue()

        elif (choice == "words"):
            print(analyzer.words(file_name))
            pressEnterToContinue()

        elif (choice == "letters"):
            print(analyzer.letters(file_name))
            pressEnterToContinue()

        elif (choice == "word_frequency"):
            print(analyzer.word_frequency(file_name))
            pressEnterToContinue()

        elif (choice == "letter_frequency"):
            print(analyzer.letter_frequency(file_name))
            pressEnterToContinue()

        elif (choice == "all"):
            print(analyzer.lines(file_name))
            print(analyzer.words(file_name))
            print(analyzer.letters(file_name))
            print(analyzer.word_frequency(file_name))
            print(analyzer.letter_frequency(file_name))
            pressEnterToContinue()

        elif (choice == "change"):
            file_name = input("Type in name of file (eg 'lorum.txt'): ")
            pressEnterToContinue()

        elif (choice == "q"):
            break

        else:
            print("Bzzt.. not a valid choice")
            pressEnterToContinue()


def pressEnterToContinue():
    """
    Encourages user to press any key before continuing
    """
    input("Please press any key to continue")

if __name__ == "__main__":
    main()
