"""Main code for analyzer"""
import menu
import analyzer


def main():
    """Main program loop"""
    file = "phil.txt"
    while True:
        choice = menu.menu()
        if choice == "lines":
            print(analyzer.lines(file))
        elif choice == "words":
            print(analyzer.words(file))
        elif choice == "letters":
            print(analyzer.letters(file))
        elif choice == "word_frequency":
            print(analyzer.word_frequency(file))
        elif choice == "letter_frequency":
            print(analyzer.letter_frequency(file))
        elif choice == "all":
            print(analyzer.lines(file))
            print(analyzer.words(file))
            print(analyzer.letters(file))
            print(analyzer.word_frequency(file))
            print(analyzer.letter_frequency(file))
        elif choice == "change":
            file = str(input("Enter file name: "))
        elif choice == "q":
            break
        input("Press anything to continue")


if __name__ == "__main__":
    main()
