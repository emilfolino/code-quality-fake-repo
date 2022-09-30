
"""
Marvin with a simple menu to start up with.
Marvin doesnt do anything, just presents a menu with some choices.
You should add functinoality to Marvin.
"""

import marvin
import inventory
import emission_functions

Anna_image = r"""
⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠛⠛⠛⠋⠉⠈⠉⠉⠉⠉⠛⠻⢿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⡿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⢿⣿⣿⣿⣿
⣿⣿⣿⣿⡏⣀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣤⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿
⣿⣿⣿⢏⣴⣿⣷⠀⠀⠀⠀⠀⢾⣿⣿⣿⣿⣿⣿⡆⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿
⣿⣿⣟⣾⣿⡟⠁⠀⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣷⢢⠀⠀⠀⠀⠀⠀⠀⢸⣿
⣿⣿⣿⣿⣟⠀⡴⠄⠀⠀⠀⠀⠀⠀⠙⠻⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⣿
⣿⣿⣿⠟⠻⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠶⢴⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⣿
⣿⣁⡀⠀⠀⢰⢠⣦⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⣿⣿⣿⣿⣿⡄⠀⣴⣶⣿⡄⣿
⣿⡋⠀⠀⠀⠎⢸⣿⡆⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⠗⢘⣿⣟⠛⠿⣼
⣿⣿⠋⢀⡌⢰⣿⡿⢿⡀⠀⠀⠀⠀⠀⠙⠿⣿⣿⣿⣿⣿⡇⠀⢸⣿⣿⣧⢀⣼
⣿⣿⣷⢻⠄⠘⠛⠋⠛⠃⠀⠀⠀⠀⠀⢿⣧⠈⠉⠙⠛⠋⠀⠀⠀⣿⣿⣿⣿⣿
⣿⣿⣧⠀⠈⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠟⠀⠀⠀⠀⢀⢃⠀⠀⢸⣿⣿⣿⣿
⣿⣿⡿⠀⠴⢗⣠⣤⣴⡶⠶⠖⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡸⠀⣿⣿⣿⣿
⣿⣿⣿⡀⢠⣾⣿⠏⠀⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⠉⠀⣿⣿⣿⣿
⣿⣿⣿⣧⠈⢹⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⣿⣿
⣿⣿⣿⣿⡄⠈⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣴⣾⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣦⣄⣀⣀⣀⣀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡄⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
"""

"""
Its an eternal loop, until q is pressed.
It should check the choice done by the user and call a appropriate
function.
"""


def main():
    """
    The main function of main.py and marvin.py
    """
    while True:
        print(chr(27) + "[2J" + chr(27) + "[;H")
        print(Anna_image)
        print("I - Anna - know all. What do you want?")
        print("1) Present yourself to Anna")
        print("2) Ask Anna for help with temperature")
        print("3) Ask Anna to say one word multiple times")
        print("4) Ask Anna for an average")
        print("5) Ask Anna to spell a word poorly")
        print("6) Ask Anna if a word is an isogram")
        print("7) Ask Anna to teach about the numbers")
        print("8) Ask Anna to randomize sentance")
        print('9) Ask Anna to "acronym" sentance')
        print("10) Ask Anna to hide all but 4 characters")
        print("11) Ask Anna to find instances of repeating characters")
        print("12) Ask Anna to search for country")
        print("13) Ask Anna to show emission chnage for a country")
        print("q) Quit.\n")

        choice = list(map(str, input("--> ").split()))

        if choice[0] == "q":
            print("\nLeave already")
            break

        elif choice[0] == "1":
            marvin.greet()

        elif choice[0] == "2":
            marvin.celcius_to_farenheit()

        elif choice[0] == "3":
            marvin.word_manipulation()

        elif choice[0] == "4":
            marvin.sum_and_average()

        elif choice[0] == "5":
            marvin.hyphen_string()

        elif choice[0] == "6":
            marvin.is_isogram()

        elif choice[0] == "7":
            marvin.compare_numbers()

        elif choice[0] == "8":
            randomize = input(
                "Tell I - Anna - what sentence you need randomized --> ")
            print(marvin.randomize_string(randomize))

        elif choice[0] == "9":
            acronym = input("I - Anna - can acronym --> ")
            print(marvin.get_acronym(acronym))

        elif choice[0] == "10":
            mask = input("I - Anna - can mask your pin number --> ")
            print(marvin.mask_string(mask))

        elif choice[0] == "11":
            string = input("I - Anna - need your string --> ")
            search = input("What do you need me - Anna - to seek? --> ")
            print(marvin.find_all_indexes(string, search))

        elif choice[0] == "12":
            search_request = input("Enter country name or part of country name to see if exists --> ")
            try:
                search_result = emission_functions.search_country(search_request)
                print(emission_functions.nice_list_print(search_result))
            except ValueError:
                print("\nCountry does not exist!\n")

        elif choice[0] == "13":
            try:
                emission_request = input("Enter country, year and year --> ")
                rr = emission_functions.read_emission_request(emission_request)
                emission_result = emission_functions.get_country_change_for_years(rr[0], rr[1], rr[2])
                print(emission_functions.print_emission_request(rr[0], emission_result))
            except ValueError:
                print("\nWrong year!\n")

        elif choice[0] == "14":
            country = input("Enter country --> ")
            emission_functions.print_country_data(emission_functions.get_country_data(country))

        elif choice[0] == "inv":
            try:
                if choice[1] == "pick" and choice[2]:
                    try:
                        inventory.pick(backpack, choice[2], choice[3])
                    except IndexError:
                        inventory.pick(backpack, choice[2])
                elif choice[1] == "drop" and choice[2]:
                    inventory.drop(backpack, choice[2])
                elif choice[1] == "swap" and choice[2]:
                    inventory.swap(backpack, choice[2], choice[3])
            except IndexError:
                inventory.inventory(backpack)

        else:
            print("That is not a valid choice. You can only choose from the menu.")

        input("\nPress enter to continue...")

backpack = []

if __name__ == "__main__":
    main()
