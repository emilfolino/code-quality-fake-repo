"""
Main file to run our analyzer programm
"""
import menu
import analyzer



def main():
    """
    Main programm that will run the programm using functions from the analyzer modul
    """

    text_file = "phil.txt"

    while True:

        menu.menu_showcase()

        choice = input("What would you like to do?: ")

        if choice == "letters":
            print(analyzer.letters(text_file))


        elif choice == "words":
            print(analyzer.words(text_file))

        elif choice == "lines":
            print(analyzer.lines(text_file))

        elif choice == "all":
            print(analyzer.lines(text_file))
            print(analyzer.words(text_file))
            print(analyzer.letters(text_file))
            print(analyzer.word_frequency(text_file, analyzer.words(text_file)))
            print(analyzer.letter_frequency(text_file, analyzer.letters(text_file)))

        elif choice == "change":
            new_file = input("Name of the new file: ")
            text_file = new_file
            print(f"Text file to handle has been changed to {new_file}")

        elif choice == "word_frequency":
            total_words = analyzer.words(text_file)
            print(analyzer.word_frequency(text_file, total_words))

        elif choice == "letter_frequency":
            total_letters = analyzer.letters(text_file)
            print(analyzer.letter_frequency(text_file, total_letters))

        elif choice == "q":
            break

        else:
            print("Dont know what to do")

        input("\nEnter to continue")


if __name__ == '__main__':
    main()
