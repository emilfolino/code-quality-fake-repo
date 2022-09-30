"""
this file is only for displaying the menue imported from menue
"""
import menu
import analyzer


def main():
    """
    the main file that outputs the answers
    """
    while True:
        menu.chioses()
        inp = input("--> ")

        if inp == "q":
            break

        elif inp == "lines":
            print(analyzer.lines())

        elif inp == "words":
            print(analyzer.words()[0])

        elif inp == "letters":
            print(analyzer.letters()[0])

        elif inp == "word_frequency":
            analyzer.word_frequency()

        elif inp == "letter_frequency":
            analyzer.letter_frequency()

        elif inp == "all":
            analyzer.alla()

        elif inp == "change":
            analyzer.change()


if __name__ == "__main__":
    main()
