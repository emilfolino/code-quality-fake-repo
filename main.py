"""
main file 
"""

from menu import showMenu
import analyzer


def main():
    """
    Take users input and give a proper result
    """
    while True:
        showMenu()
        choice = input("#")
        if choice == "q":
            break
        elif choice == "lines":
            print(analyzer.count_lines())
        elif choice == "words":
            print(analyzer.count_words())
        elif choice == 'letters':
            print(analyzer.count_letters())
        elif choice == "word_frequency":
            print(analyzer.word_frequency())
        elif choice == "letter_frequency":
            print(analyzer.letters_frequency())
        elif choice == "all":
            print(analyzer.all_analyses())
        elif choice == "change":
            file = input("Enter filename: ")
            analyzer.changeSelectedFile(file)
        else:
            print("Invalid Input!")

        input("\nPress Enter to continue")


if __name__ == "__main__":
    main()
