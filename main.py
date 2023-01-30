"""This is the main file"""
import re
import marvin
import inventory
import emission_functions


def function_calls(user_choice):
    """Tries to call a function from the Function_calls dictionary"""
    try:
        x = int(user_choice)
    except Exception:
        print('Please choose from the menu...')
    else:
        if x < 8:
            marvin.Function_calls[user_choice]()
        elif x == 8:
            sentence = input('Please enter a string to randomize: ')
            print(marvin.Function_calls[user_choice](sentence))
        elif x == 9:
            sentence = input('Please enter a string: ')
            print(marvin.Function_calls[user_choice](sentence))
        elif x == 10:
            sentence = input('Please enter a string to mask: ')
            print(marvin.Function_calls[user_choice](sentence))
        elif x == 11:
            sequence = input('Please enter a sequence: ')
            subsequence = input('Please enter a subsequence: ')
            print(marvin.Function_calls[user_choice](sequence, subsequence))
        elif 11 < x < 15:
            try:
                result = emission_functions.function_calls(x)
            except ValueError as e:
                print(e)
            else:
                print(result)

def main():
    """ This is the main function. The program starts from here. """
    backpack = []
    state = True
    while state is True:
        print(chr(27) + "[2J" + chr(27) + "[;H")
        print(marvin.Marvin_image)
        print("Hi, I'm Marvin. I know it all. What can I do you for?")
        print("1) Present yourself to Marvin.")
        print("2) Have Marvin help with temp-convertion.")
        print("3) Marvin will multiply your input string")
        print("4) Marvin will calculate the sum and average")
        print("5) Surprise")
        print("6) Check Isogram")
        print("7) Hi-Lo")
        print("8) Randomize string")
        print("9) Get Acronynm")
        print("10) Mask string")
        print("11) Find all indexes")
        print("12) Search for country")
        print("13) Get Emission change")
        print("14) Print country data")
        print("q) Quit.")
        print('\n\nTry out my new "inv" commands')

        user_choice = input("--> ")
        if user_choice == 'q':
            print("Bye, bye - and welcome back anytime!")
            state = False
        elif re.search('^inv( |$)', user_choice):
            backpack = inventory.function_call(backpack, user_choice)
            input("\nPress enter to continue...")
        else:
            function_calls(user_choice)
            input("\nPress enter to continue...")


if __name__ == "__main__":
    main()
