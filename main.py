""" Analyzer main module"""

import menu
import analyzer


def main():
    """ Main function for Analyzer """
    file_name = "phil.txt"
    while True:
        menu.show_menu()
        choice = input("--> ")

        if choice == "q":
            print("Bye, bye - and welcome back anytime!")
            break

        if choice == "lines":
            print(analyzer.count_lines(file_name))
        elif choice == "words":
            print(analyzer.count_words(file_name))
        elif choice == "letters":
            print(analyzer.count_letters(file_name))
        elif choice == "word_frequency":
            print(analyzer.word_frequency(file_name))
        elif choice == "letter_frequency":
            print(analyzer.letter_frequency(file_name))
        elif choice == "all":
            print(analyzer.all_function(file_name))
        elif choice == "change":
            file_input = input("Enter filename: ")
            file_name = file_input
        else:
            print("This option doesn't seem to exist.\n")

if __name__ == "__main__":
    main()
