"""
innehålla kommandoloopen
"""
import analyzer
import menu  

def main():
    """
    Text analysis 
    """
    while True:
        menu.menu()
        choice = input("-->  ")

        if choice == "q":
            print("Bye, bye - and welcome back anytime!")
            with open("last_file_name.txt", "w") as fn:
                fn.write("phil.txt")
            break

        elif choice == "lines":
            print(analyzer.lines())

        elif choice == "words":
            print(analyzer.words())

        elif choice == "letters":
            print(analyzer.letters())
   
        elif choice == "word_frequency":
            print(analyzer.word_frequency())

        elif choice == "letter_frequency":
            print(analyzer.letter_frequency())
            
        elif choice == "all":
            print(analyzer.all_functions())

        elif choice == "change":
            choic = input("Enter filename: ")
            analyzer.change(choic)


        else:
            print("That is not a valid choice. You can only choose from the menu.")

        input("\nPress enter to continue...")


if __name__ == "__main__":
    main()
