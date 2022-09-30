"""
A text analyzer in python.
"""

import menu
import analyzer

def main():
    """
    This i a eternal loop until a certain key is pressed.
    """

    analyzing_file = "phil.txt"

    menu.menu_text()

    while True: 
        
        choice = input("--> ") 

        if choice == "q":
            print("Bye, I hope you got the knowledge you were looking for!")
            break
        elif choice == "menu":
            menu.menu_text()
        elif choice == "lines":
            analyzer.count_lines(analyzing_file)
        elif choice == "words":
            analyzer.count_words(analyzing_file)
        elif choice == "letters":
            analyzer.count_letters(analyzing_file)
        elif choice == "word_frequency":
            analyzer.word_frequency(analyzing_file)
        elif choice == "letter_frequency":
            analyzer.letter_frequency(analyzing_file)
        elif choice == "all":
            analyzer.everything(analyzing_file)
        elif choice == "change":
            analyzing_file = analyzer.change_file()
        else:
            print("This is not a valied choice.")

if __name__ == "__main__":
    main()
