#pylint: disable-all

"""
huvud gränsnittet för programmet
"""
import menu
import analyzer

def main():
    """
    Main funktionen som ska starta programmet
    """
    menu.printMenu()
    choice = input("-->")
    fileName = "phil.txt"

    while True:
        if choice == "lines":
            print(analyzer.countLines(fileName))
        elif choice == "words":
            print(analyzer.countWords(fileName))
        elif choice == "letters":
            print(analyzer.countLetters(fileName))
        elif choice == "word_frequency":
            analyzer.word_frequency(fileName)
        elif choice == "letter_frequency":
            analyzer.letter_frequency(fileName)
        elif choice == "all":
            print(analyzer.countLines(fileName))
            print(analyzer.countWords(fileName))
            print(analyzer.countLetters(fileName))
            analyzer.word_frequency(fileName)
            analyzer.letter_frequency(fileName)
        elif choice == "change":
            fileName = input("Enter file name:")
        elif choice == "q":
            break

        print("\n\n")
        menu.printMenu()
        choice = input("-->")

if __name__ == "__main__":
    main()
