"""
This is a main module.
"""
import menu
import analyzer


def main():
    """
    Main.
    """
    run = True
    while run:
        choice = input("--> ")

        if choice == "lines":
            res = analyzer.count_lines()
            print(res)

        elif choice == "words":
            res = analyzer.count_words()
            print(res)

        elif choice == "letters":
            res = analyzer.count_letters()
            print(res)

        elif choice == "word_frequency":
            res = analyzer.word_frequency()
            analyzer.print_frequency(res, 7)

        elif choice == "letter_frequency":
            res = analyzer.letter_frequency()
            analyzer.print_frequency(res, 7)

        elif choice == "all":
            res = analyzer.count_lines()
            print(res)
            res = analyzer.count_words()
            print(res)
            res = analyzer.count_letters()
            print(res)
            res = analyzer.word_frequency()
            analyzer.print_frequency(res, 7)
            res = analyzer.letter_frequency()
            analyzer.print_frequency(res, 7)

        elif choice == "change":
            new_file = input("File name: ")
            analyzer.set_file(new_file)

        elif choice == "menu":
            menu.print_()

        elif choice == "q":
            run = False


if __name__ == '__main__':
    main()
