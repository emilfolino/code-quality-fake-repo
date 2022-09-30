#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Marvin with a simple menu to start up with.
Marvin doesnt do anything, just presents a menu with some choices.
You should add functinoality to Marvin.
"""


import marvin
import inventory
import emission_functions

marvin_image = r"""
               _/       \_
              / |       | \
             /  |__   __|  \
            |__/((o| |o))\__|
            |      | |      |
            |\     |_|     /|
            | \           / |
             \| /  ___  \ |/
              \ | / _ \ | /
               \_________/
                _|_____|_
           ____|_________|____
          /                   \
"""

"""
Its an eternal loop, until q is pressed.
It should check the choice done by the user and call a appropriate
function.
"""

def main():
    """
    Main menu
    """
    backpack = []
    while True:
        print(chr(27) + "[2J" + chr(27) + "[;H")
        print(marvin_image)
        print("Hi, I'm Marvin. I know it all. What can I do you for?")
        print("1) Present yourself to Marvin.")
        print("2) Turn Celsius into fahrenheit")
        print("3) Wordmultiplier")
        print("4) Sum and average calculator")
        print("5) Wordmanipulator")
        print("6) Isogram-checker")
        print("7) Smaller or larger")
        print("8) Word-randomizer")
        print("9) Turn name into acronym")
        print("10) Mask input")
        print("11) Find all indexes")
        print("12) Search for countries")
        print("13) Show emission change for a country")
        print("14) Show all data for a country")
        print("q) Quit.")

        choice = input("--> ")

        if choice == "q":
            print("Bye, bye - and welcome back anytime!")
            break

        elif choice == "1":
            marvin.greet()

        elif choice == "2":
            marvin.celcius_to_farenheit()

        elif choice == "3":
            marvin.word_manipulation()

        elif choice == "4":
            marvin.sum_and_average()


        elif choice == "5":
            marvin.hyphen_string()


        elif choice == "6":
            marvin.is_isogram()


        elif choice == "7":
            marvin.compare_numbers()

        elif choice == "8":
            usr_string = input("Type something: ")
            print(marvin.randomize_string(usr_string))

        elif choice == "9":
            usr_string = input("Type your full name: ")
            print(marvin.get_acronym(usr_string))

        elif choice == "10":
            user_string = input("Type something: ")
            print(marvin.mask_string(user_string))
            

        elif choice == "11":
            user_string = input("Type a string: ")
            user_string2  = input("Type a substring: ")
            print(marvin.find_all_indexes(user_string, user_string2))
            
        elif "inv pick" in choice:
            choice_list = choice.split()
            if len(choice_list) < 3:
                argument = None
            else:
                argument = choice_list[2]
            if len(choice_list) > 3:
                position = int(choice_list[-1])
            else:
                position = None
            backpack = inventory.pick(backpack, argument, position)

        elif choice == "inv":
            inventory.inventory(backpack)
            
        elif "inv drop" in choice:
            choice_list = choice.split()
            if len(choice_list) > 3:
                print("Error: too many items entered try again.")
            argument = choice_list[2]
            backpack = inventory.drop(backpack, argument)

        elif "inv swap" in choice:
            choice_list = choice.split()
            argument = choice_list[2]
            other = choice_list[3]
            backpack = inventory.swap(backpack, argument, other)

        elif choice == "12":
            user_search = input("Search for country: ")
            try:
                print(emission_functions.search_country(user_search))
            except ValueError:
                print("Country does not exist!")
        
        elif choice == "13":
            user_search = input("Enter country, year and year: ")
            search_list = user_search.split(',')
            country = search_list[0]
            year1 = search_list[1]
            year2 = search_list[2]
            try:
                print(country + ":" + str(emission_functions.get_country_change_for_years(country, year1, year2)) + "%")
            except ValueError:
                print("Wrong year!")
            
        elif choice == "14":
            user_input = input("Enter country: ")
            data = emission_functions.get_country_data(user_input)
            emission_functions.print_country_data(data)





    

        else:
            print("That is not a valid choice. You can only choose from the menu.")

        input("\nPress enter to continue...")

if __name__ == "__main__":
    main()
