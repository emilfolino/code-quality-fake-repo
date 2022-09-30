"""
Main program
"""

import menu
import analyzer

def main():
    """
    Analyze text
    """
    file = "phil.txt"

    while True:

        menu.printMenu()

        choice = input("What do you want to do? ").lower()
        item = analyzer.openFile(file)

        if choice in ("q"):
            break
        
        elif choice == "lines":
            print(analyzer.countLines(item))

        elif choice == "words":
            print(analyzer.countWords(item))
        
        elif choice == "letters":
            print(analyzer.countLetters(item))

        elif choice == "word_frequency":
            print(analyzer.wordFrequency(item))
        
        elif choice == "letter_frequency":
            print(analyzer.letterFrequency(item))
        
        elif choice == "all":
            print(analyzer.runAll(item))
        
        elif choice == "change":
            file = input("What file would you like to change to? ")
            input("Press enter to continue.")

        else:
            print("That's not an option, try again!")
        
        print("Press enter to continue.")

if __name__ == "__main__":
    main()
