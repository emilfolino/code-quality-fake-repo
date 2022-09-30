
"""
Analyzer main
"""

import menu as m
import analyzer as a


def main():
    """Main function"""

    filename = "phil.txt"

    while True:
        m.print_menu()

        choice = input("--> ")

        if choice == "q":
            print("exiting...")
            break
        elif choice == "lines":
            print(a.count_lines(filename))
        elif choice == "words":
            print(a.count_words(filename))
        elif choice == "letters":
            print(a.count_letters(filename))
        elif choice == "word_frequency":
            a.word_frequency(filename)
        elif choice == "letter_frequency":
            a.letter_frequency(filename)
        elif choice == "all":
            print(a.count_lines(filename))
            print(a.count_words(filename))
            print(a.count_letters(filename))
            a.word_frequency(filename)
            a.letter_frequency(filename)
        elif choice == "change":
            filename = input("New file name: ")
        else:
            print("Not a valid choice, try again...")
        input("...")

if __name__ == "__main__":
    main()
