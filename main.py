"""
The main file
"""

import menu
import analyzer

def main():
    """The function which our menu lies within"""

    filename = "phil.txt"

    while True:
        menu.menu_print()

        choice = input("--> ")

        if choice == "q":
            print("Bye, bye - and welcome back anytime!")
            break
        
        
        elif choice == "lines":
            line_amount = analyzer.lines(filename)
            print(line_amount)

        
        elif choice == "words":
            word_amount = analyzer.words_amount(filename)
            print(word_amount)

        
        elif choice == "letters":
            letter_amount = analyzer.letters_amount(filename)
            print(letter_amount)


        elif choice == "word_frequency":
            analyzer.word_frequency(filename)
            
            
        elif choice == "letter_frequency":
            analyzer.letter_frequency(filename)
            
        
        elif choice == "all":
            analyzer.show_all(filename)

        
        elif choice == "change":
            filename = input("State your file: ")


if __name__ == "__main__":
    main()
