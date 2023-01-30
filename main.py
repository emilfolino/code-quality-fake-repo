"""
Contains the commando loop
"""

import menu
import analyzer

def main():
    """
    starts the program
    """
    text_to_analyze = "phil.txt"

    while True:
        print(chr(27) + "[2J" + chr(27) + "[;H")
        print(menu.menu_show())
        choice = input("--> ")
        
        if choice == "q":
            break

        elif choice == "words":
            try:
                print(analyzer.word_count(text_to_analyze))
            except FileNotFoundError as e:
                print(str(e))

        elif choice == "lines":
            try:
                print(analyzer.line_count(text_to_analyze))
            except FileNotFoundError as e:
                print(str(e))

        elif choice == "letters":
            try:
                print(analyzer.letter_count(text_to_analyze))
            except FileNotFoundError as e:
                print(str(e))
                
        elif choice == "word_frequency":
            try:
                print(analyzer.word_frequency(text_to_analyze))
            except FileNotFoundError as e:
                print(str(e))

        elif choice == "letter_frequency":
            try:
                print(analyzer.letter_frequency(text_to_analyze))
            except FileNotFoundError as e:
                print(str(e))

        elif choice == "all":
            try:
                print(str(analyzer.word_count(text_to_analyze)) + "\n" + str(analyzer.line_count(text_to_analyze))+
                "\n" + str(analyzer.letter_count(text_to_analyze)) +
                "\n" + str(analyzer.word_frequency(text_to_analyze)) +
                str(analyzer.letter_frequency(text_to_analyze)))
            except FileNotFoundError as e:
                print(str(e))
        
        elif choice == "change":
            print("File in use right now: " + text_to_analyze)
            text_to_analyze = input("Enter new filename:\n") 
        else:
            print("Not a valid choice")

        input("\nPress enter to continue...")

if __name__ == "__main__":
    main()
    