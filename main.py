"""main module deciding what different choices do"""

import menu
import analyzer

def main():
    """Contains code for the menu choices"""
    
    selected_file = "phil.txt"

    while True:
        menu.main()

        choice = input("--> ")

        if choice == "q":
            print("Bye!")
            break

        elif choice == "lines":
            print(analyzer.number_of_lines(selected_file))

        elif choice == "words":
            print(analyzer.number_of_words(selected_file))

        elif choice == "letters":
            print(analyzer.number_of_letters(selected_file))

        elif choice == "word_frequency":
            print(analyzer.word_frequency(selected_file))
        
        elif choice == "letter_frequency":
            print(analyzer.letter_frequency(selected_file))

        elif choice == "all":
            print(analyzer.number_of_lines(selected_file))
            print(analyzer.number_of_words(selected_file))
            print(analyzer.number_of_letters(selected_file))
            print(analyzer.word_frequency(selected_file))
            print(analyzer.letter_frequency(selected_file))

        elif choice == "change":
            selected_file = input("Enter file name: ")

        else:
            print("That is not a valid choice. You can only choose from the menu.")

        input("\nPress enter to continue...")

if __name__ == "__main__":
    main()
