#Filen main.py skall enbart innehålla kommandoloopen, tänk while-loopen i marvin, 
#och använda sig av modulerna analyzer och menu för att lösa uppgiften. 
#Koden ska ligga i en funktion som heter main. 
#Glöm inte if __name__ == "__main__" i main.py för att starta programmet.

"""
Chatt thing
"""
import menu
import analyzer

def main():
    """
    Main code
    """
    while True: 

        menu.menuChoice()
        choice = input("--> ")

        if choice == "q":
            print("Ah it would apear you have found the knowledge you were looking for, come back anytime.")
            break

        elif choice == "lines":
            analyzer.Count_lines()
        
        elif choice == "words":
            analyzer.Count_words()

        elif choice == "letters":
            analyzer.Count_letters()

        elif choice == "word_frequency":
            analyzer.word_frequency()

        elif choice == "letter_frequency":
            analyzer.letter_frequency()

        elif choice == "all":
            analyzer.all_functions()

        elif choice == "change":
            analyzer.change_file()

        else:
            print("That is not a valid choice. You can only choose from the menu.")

        input("\nPress enter to continue...")


if __name__ == "__main__":
    main()
