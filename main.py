"""
Main
"""
import menu

def main():
    """
    Main
    """
    while True:
        menu.menuchoices()

        choice = input("--> ")

        

        if choice == "q":
            menu.quit_program()
            break

        elif choice == "lines":
            menu.frequency(choice)
        
        elif choice == "words":
            menu.frequency(choice)

        elif choice == "letters":
            menu.frequency(choice)

        elif choice == "word_frequency":
            menu.word_frequency(choice)

        elif choice == "letter_frequency":
            menu.word_frequency(choice)

        elif choice == "all":
            menu.all_analysis()
        
        elif choice == "change":
            menu.textfile = menu.change()
            print(f"Chosen textfile is now changed to {menu.textfile}")
            

        else:
            menu.wrongchoice()
    
        input("Press enter to continue...")

if __name__ == "__main__":
    main()
