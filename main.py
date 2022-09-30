"""
mainfilen för textanalysprogrammet
"""
import menu
import analyzer
def main():
    """
    mainfunktionen för textanalysprogrammet som körs om __name__ == "__main__"
    """

    analyzer.read_file()
    while True:
        menu.print_menu()
        choice = input("make a choice:\n")
        if choice == "lines":
            n_lines, lines = analyzer.lines()
            print(n_lines, lines)
            #input(text_for_continue)

        elif choice == "words":
            n_words, words = analyzer.words()
            print(n_words, words)
            #input(text_for_continue)

        elif choice == "letters":
            n_letters, letters = analyzer.letters()
            print(n_letters, letters)
            #input(text_for_continue)

        elif choice == "word_frequency":
            sorted_tup_words = analyzer.word_frequency()
            analyzer.dict_printer(sorted_tup_words, analyzer.words()[0])
            #input(text_for_continue)

        elif choice == "letter_frequency":
            sorted_tup_letters = analyzer.letter_frequency()
            analyzer.dict_printer(sorted_tup_letters, analyzer.letters()[0])
            #input(text_for_continue)

        elif choice == "all":
            analyzer.print_all()
            #input(text_for_continue)

        elif choice == "change":
            analyzer.change()
            #input(text_for_continue)

        elif choice == "q":
            #input("I see... after all my effort you're leaving, great. Thx...")
            break

        else:
            print("You can only choose options from the menu... of course...")
            #input("Press enter for another try")




if __name__ == "__main__":
    main()
