"""
Main file for program.
"""
import menu
import analyzer
def main():
    """
    Main function for program.
    """
    file_name = "phil.txt"
    while True:
        menu.menu()
        choice = input("--> ")

        if choice == "q":
            print("Bye, bye - and welcome back anytime!")
            break

        elif choice == "change":
            file_name = input("Enter filename: ")

        elif choice == "lines":
            print(analyzer.count_lines(file_name))

        elif choice == "words":
            print(analyzer.count_words(file_name))

        elif choice == "letters":
            print(analyzer.count_letters(file_name))

        elif choice == "word_frequency":
            word_freq = analyzer.word_frequency(file_name)
            for i in range(7):
                print(word_freq[i])

        elif choice == "letter_frequency":
            letter_freq = analyzer.letter_frequency(file_name)
            for i in range(7):
                print(letter_freq[i])

        elif choice == "all":
            word_freq = analyzer.word_frequency(file_name)
            letter_freq = analyzer.letter_frequency(file_name)

            print(analyzer.count_lines(file_name))
            print(analyzer.count_words(file_name))
            print(analyzer.count_letters(file_name))
            for i in range(7):
                print(word_freq[i])
            for i in range(7):
                print(letter_freq[i])

        else:
            print("That is not a valid choice. You can only choose from the menu.")
        input("\nPress enter to continue...")

if __name__ == "__main__":
    main()
