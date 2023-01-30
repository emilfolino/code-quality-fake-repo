"""
Marvin with a simple menu to start up with.
Marvin doesnt do anything, just presents a menu with some choices.
You should add functinoality to Marvin.
"""
import menu
import analyzer

def main():
    """
    Its an eternal loop, until q is pressed.
    It should check the choice done by the user and call a appropriate
    function.
   """
    while True:
        menu.menu()
        choice = input("--> ")

        if choice == "q":
            print("Bye, bye - and welcome back anytime!")
            break

        elif choice == "lines":
            print(analyzer.lines())
        elif choice == "words":
            print(analyzer.Words()) 
        elif choice == "letters":
            print(analyzer.Letters()) 
        elif choice == "word_frequency":
            data = analyzer.word_frequency()
            keyList = list(data[0].keys())
            valueList = list(data[0].values())
            textToShow = ''
            index = 0
            for _ in range(7):
                textToShow = textToShow + f'{keyList[index]}: {valueList[index]} |'\
                    f' {round( int(valueList[index]) / data[1] * 100, 1)}%\n'
                index += 1
            print(textToShow)
        elif choice == "letter_frequency":
            l_Data = analyzer.letter_frequency()
            letter_key = list(l_Data[0].keys())
            letter_value = list(l_Data[0].values())
            lettersToShow = ''
            l_index = 0
            for _ in range(7):
                lettersToShow = lettersToShow + f'{letter_key[l_index]}: {letter_value[l_index]} |'\
                    f' {round(int(letter_value[l_index]) / l_Data[1] * 100, 1)}%\n'
                l_index += 1
            print(lettersToShow)
        elif choice == "all":
            analyzer.All()
        elif choice == "change":
            analyzer.change()

    
        else:
            print("That is not a valid choice. You can only choose from the menu.")

        input("\nPress enter to continue...")
    
if __name__ == "__main__":
    main()
