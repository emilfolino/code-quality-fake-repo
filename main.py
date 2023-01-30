"""Module for frequency counting"""

import menu
import analyzer

def main():
    """Main file where you can make choices"""
    print("Hello! Make a choice! \n")

    while True:
        menu.menu(print)  
        input_1 = input("Make a choice --->")

        choice = input_1

        if choice == "q":
            print("Farewell")
            file_1 = "phil.txt"
            analyzer.change_file(file_1)
            break
            
        elif choice == "change":
            file_1 = input("Give me a filename: ")
            analyzer.change_file(file_1)


        elif choice == "lines":
            file_1 = analyzer.open_file()
            analyzer.count_lines(file_1)

        elif choice == "words":
            file_1 = analyzer.open_file()
            analyzer.count_word(file_1)

        elif choice == "letters":
            file_1 = analyzer.open_file()
            analyzer.count_letter(file_1)

        elif choice == "word_frequency":
            file_1 = analyzer.open_file()
            analyzer.word_frequency(file_1)

        elif choice == "letter_frequency":
            file_1 = analyzer.open_file()
            analyzer.letter_frequency(file_1)

        elif choice == "all":
            file_1 = analyzer.open_file()
            analyzer.count_lines(file_1)
            file_1 = analyzer.open_file()
            analyzer.count_word(file_1)
            file_1 = analyzer.open_file()
            analyzer.count_letter(file_1)
            file_1 = analyzer.open_file()
            analyzer.word_frequency(file_1)
            file_1 = analyzer.open_file()
            analyzer.letter_frequency(file_1)

        else:
            print("Control, control, you must learn control! You can only choose from the menu.")
        
        input("\nPress enter to continue...")

if __name__ == "__main__":
    main()
