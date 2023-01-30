"""
main method for the text analyzer
"""

import menu
import analyzer

def main():
    """
    main function for running the analyzer
    """

    file = "phil.txt"

    while True:
        menu.showMenu()
        choice = input("--> ")

        if choice == "lines":
            analyzer.lines(file)
        elif choice == "words":
            print(analyzer.words(file))
        elif choice == "letters":
            analyzer.letters(file)
        elif choice == "word_frequency":
            analyzer.word_frequency(file)
        elif choice == "letter_frequency":
            analyzer.letter_frequency(file)
        elif choice == "all":
            analyzer.everything(file)
        elif choice == "change":
            file = analyzer.change(file)
        elif choice == "q":
            break
        else: 
            print("This is not a valid menu choice.")

if __name__ == "__main__":
    main()
