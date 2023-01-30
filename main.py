""" this is main"""
import analyzer
import menu

def main():
    """ Main function """
    while True:
        menu.ShowMenu()
        choice = input()
        if choice == "q":
            break
        elif choice == "lines":
            print(analyzer.AmountLines(analyzer.ReadFile()))
        elif choice == "words":
            print(len(analyzer.AmountWordFromString(analyzer.ReadFile())))
        elif choice == "letters":
            print(analyzer.CountLettersInList(
                analyzer.ListOfChars(analyzer.ReadFile())))
        elif choice == "word_frequency":
            print(analyzer.word_frequency())
        elif choice == "letter_frequency":
            print(analyzer.letter_frequency())
        elif choice == "all":
            print(analyzer.all_Analyzes())
        elif choice == "change":
            analyzer.ChangeFile(input())


if __name__ == '__main__':
    main()
