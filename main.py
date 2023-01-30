"""
loop for program 
"""

import menu
import analyzer

def main():
    """
    Main menu
    """
    filename = "phil.txt"
    while True:
        choice = menu.menu()

        if choice == "q":
            print("Bye, bye - and welcome back anytime!")
            break

        elif choice == "lines":
            analyzer.count_lines(filename)

        elif choice == "words":
            analyzer.count_words(filename)

        elif choice == "letters":
            analyzer.count_letters(filename)
        
        elif choice == "word_frequency":
            analyzer.word_frequency(filename)

        elif choice == "letter_frequency":
            analyzer.letter_frequency(filename)

        elif choice == "all":
            analyzer.print_all(filename)
        
        elif choice == "change":
            filename = analyzer.change()

if __name__ == "__main__":
    main()
