"""The main loop for the analyzer program."""

import analyzer
import menu

def main():
    """The main loop of the program. Asks for a user selection and then
    runs the approriate function."""
    filename = "phil.txt"
    while True:

        choice = menu.menu()

        if choice == "q":
            break

        elif choice == "lines":
            print(analyzer.lines(filename))

        elif choice == "words":
            print(analyzer.words(filename))

        elif choice == "letters":
            print(analyzer.letters(filename))

        elif choice == "word_frequency":
            analyzer.word_frequency(filename)

        elif choice == "letter_frequency":
            analyzer.letter_frequency(filename)

        elif choice == "all":
            analyzer.print_all(filename)

        elif choice == "change":
            filename = input("What's the name of the new file?")
        
        else:
            print("No such option!")

if __name__ == "__main__":
    main()
