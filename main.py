"""
The main file that runs the program. Contains main() which runs the menu options.
"""
import analyzer
import menu

def main():
    """
    The main function that runs the menu and calls for functions when an option is entered. 
    If the option does not exist, it prints an error message, then asks for an input again.
    """
    file_to_analyze = "phil.txt"
    while True:
        print("menu) Show the menu.")
        print("q) Close the program.")
        print()
        menuChoice = input("What do you want to do? ")
        if menuChoice == "menu":
            menu.menu()
        elif menuChoice == "lines":
            print(analyzer.lines(file_to_analyze))
        elif menuChoice == "words":
            print(len(analyzer.words(file_to_analyze)))
        elif menuChoice == "letters":
            print(len(analyzer.letters(file_to_analyze)))
            print(analyzer.letters(file_to_analyze))
        elif menuChoice == "word_frequency":
            print(analyzer.word_frequency(file_to_analyze))
        elif menuChoice == "letter_frequency":
            print(analyzer.letter_frequency(file_to_analyze))
        elif menuChoice == "all":
            alldict = analyzer.alloftheabove(file_to_analyze)
            print(alldict["lines"])
            print(alldict["words"])
            print(alldict["letters"])
            print(alldict["word_frequency"])
            print(alldict["letter_frequency"])
        elif menuChoice == "change":
            change_to_file = input("What file would you rather analyze? ")
            file_to_analyze = change_to_file
                
        elif menuChoice == "q":
            break

        else:
            print("That is not a valid choice!")
        
        input("Press any key to continue... ")
if __name__ == "__main__":
    main()
