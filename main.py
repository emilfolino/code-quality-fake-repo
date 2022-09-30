"""
Main menu for choices in analyzer
"""
import analyzer
import menu





def main():
    """
    Function for main menu
    """
    filename = "phil.txt"
    while True:
        menu.menu()
        inp = input("--> ")

        if inp == "q":
            print("Welcome back any time!")
            break
        elif inp == "change":
            filename = input("Enter new filename: ")
        elif inp == "lines":
            print(analyzer.count(inp, filename))
        elif inp == "words":
            print(analyzer.count(inp, filename))
        elif inp == "letters":
            print(analyzer.count(inp, filename))
        elif inp == "word_frequency":
            analyzer.frequency(inp, filename)
        elif inp == "letter_frequency":
            analyzer.frequency(inp, filename)
        elif inp == "all":
            analyzer.print_all(filename)
        else:
            print("That is not a valid choice. You can only choose from the menu.")
        input("\n Press Enter if you want more!")













if __name__ == "__main__":
    main()
