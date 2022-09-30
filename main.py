"""
The "main" module
"""
import analyzer
import menu


def main():
    """
    Main function
    :return:
    """
    filename = "phil.txt"
    while True:
        choice = menu.menu()
        if choice == "q":
            print("Bye bye...")
            break
        elif choice == "lines":
            print(analyzer.lines(filename))
        elif choice == "words":
            print(analyzer.words(filename))
        elif choice == "letters":
            print(analyzer.letters(filename))
        elif choice == "word_frequency":
            print(analyzer.word_frequency(filename))
        elif choice == "letter_frequency":
            print(analyzer.letter_frequency(filename))
        elif choice == "all":
            print(analyzer.do_all(filename))
        elif choice == "change":
            filename = input("--> ")
        else:
            print("Invalid input. ")
        input("Press enter to continue: ")


if __name__ == "__main__":
    main()
