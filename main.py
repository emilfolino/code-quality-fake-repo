"""
Main program for Marvin
"""

import analyzer
import menu

def main():
    """
    Something
    """
    file_1 = "phil.txt"

    while True : 
        input_1 = input("Write menu to see options : ")

        if input_1.lower() == "change":
            file_1 = analyzer.change()
        
        elif input_1.lower() == "menu": 
            print(menu.menu_funktion())

        elif input_1.lower() == "lines":
            print(analyzer.lines(file_1))

        elif input_1.lower() == "letters":
            print(analyzer.letters(file_1))

        elif input_1.lower() == "words":
            print(analyzer.words(file_1))

        elif input_1.lower() == "letter_frequency":
            print(analyzer.letter_frequency(file_1))

        elif input_1.lower() == "word_frequency":
            print(analyzer.word_frequency(file_1))

        elif input_1.lower() == "all":
            print(analyzer.print_all(file_1))
            
        elif input_1.lower() == "q" :
            break

        elif len(input_1.lower()) == 0 :
            print("vaild choice")
        
if __name__ == "__main__":
    main()
