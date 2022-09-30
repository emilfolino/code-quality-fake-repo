"""Dotline"""

import analyzer
import menu

def main():
    """Dotstring"""
    while True:
        menu.menu()

        choice = input("--> ")

        if(choice.lower() == "lines"):
            print(analyzer.count_lines())

        elif(choice.lower() == "words"):
            print(analyzer.count_words())

        elif(choice.lower() == "letters"):
            print(analyzer.count_letters())

        elif(choice.lower() == "word_frequency"):
            analyzer.word_frequency()

        elif(choice.lower() == "letter_frequency"):
            analyzer.letter_frequency()
        
        elif(choice.lower() == "all"):
            analyzer.allData()

        elif(choice.lower() == "change"):
            analyzer.change_file()

        elif(choice.lower() == "q"):
            break

        else:
            menu.invalidChoice()
        
        menu.pressEnter()

if __name__ == "__main__":
    main()
