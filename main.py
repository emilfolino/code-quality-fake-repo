# Filen main.py skall enbart innehålla kommandoloopen, tänk while-loopen i marvin, 
# och använda sig av modulerna analyzer och menu för att lösa uppgiften. 
# Koden ska ligga i en funktion som heter main. Glöm inte if __name__ == "__main__" i main.py 
# för att starta programmet.
"""
Main analyzer loop
"""

import analyzer
import menu

def main():
    """
    Main analyzer loop
    """
    file_name = "phil.txt"
    while True:
        print(chr(27) + "[2J" + chr(27) + "[;H")
        print(menu.start(file_name))
        choice = input('What can I do for you? ')

        if choice == 'q':
            print('Bye, have a good day!')
            break
        elif choice == "lines":
            print(f'There are {analyzer.line_count(file_name)} lines in {file_name}.')

        elif choice == "words":
            print(f'There are {analyzer.word_count(file_name)} words in {file_name}.')

        elif choice == "letters":
            print(f'There are {analyzer.letter_count(file_name)} letters in {file_name}.')

        elif choice == "word_frequency":
            analyzer.word_frequency(file_name)
        
        elif choice == "letter_frequency":
            analyzer.letter_frequency(file_name)

        elif choice == "all":
            analyzer.do_everything(file_name)

        elif choice == "change":
            inp = input('Enter which file to change to: ')
            file_name = inp
        
        else:
            print("Not valid! Choose from the menu, please!")

        input('\nPress any button to continue...')

if __name__ == "__main__":
    main()
