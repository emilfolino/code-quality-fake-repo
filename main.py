"""
The main program
"""

import analyzer
import menu

def main():
    """
    the main loop of the program
    """
    file_name = "phil.txt"
    while(True):
        menu.print_menu()
        choice = input("--> ")
        
        if choice == "lines":
            text_list = analyzer.get_file_list(file_name)
            print(len(text_list))
        elif choice == "words":
            words_count = analyzer.get_word_count(file_name)
            print(words_count)
        elif choice == "letters":
            letter_count = analyzer.get_letter_count(file_name)
            print(letter_count)
        elif choice == "word_frequency":
            analyzer.get_word_frequency(file_name)
        elif choice == "letter_frequency":
            analyzer.get_letter_frequency(file_name)
        elif choice == "all":
            analyzer.everything(file_name)
        elif choice == "change":
            file_name = input("What's the name of the file? ")
        elif choice in ("quit", "q"):
            print("Bye! :)")
            break
        else:
            print("That's not a valid command!")

        input("\nPress enter to continue...")

if __name__ == "__main__":
    main()
