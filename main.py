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

lst_inventory = []
marvin_image = r"""
     _
     (_\     /_)
       ))   ((
     .---------.  
 /^\/  _.   _.  \/^\
 \(   /__\ /__\   )/
  \,  \o_/_\o_/  ,/
    \    (_)    /
     `-.'==='.-'
      __) - (__   
     /  `~~~`  \
    /  /     \  \
    \ :       ; /
     \|==(*)==|/
      :       :
       \  |  /
     ___)=|=(___
jgs {____/ \____}
"""

"""
Its an eternal loop, until q is pressed.
It should check the choice done by the user and call a appropriate
function.
"""

def main():
    """The program's main() function."""
    while True:
        print(chr(27) + "[2J" + chr(27) + "[;H")
        print(marvin_image)
        print("Hi, I'm Marvin. I know it all. What can I do you for?")
        print("1) Present yourself to Marvin.")
        print("2) Tell Marvin how hot it is outside today.")
        print("3) Play \"Word-multiplication\" with Marvin.")
        print("4) Give Marvin some numbers.")
        print("5) Give Marvin a string.")
        print("6) Isogram with Marvin.")
        print("7) Advanced wordgame with Marvin.")
        print("8) Shuffle a string with Marvin.")
        print("9) Acronym with Marvin.")
        print("10) Mask a string with Marvin.")
        print("11) Help Marvin find some indexes in a string.")
        print("12) Search for countries with Marvin.")
        print("13) Calculate changes in emissions with Marvin.")
        print("14) Get complete country data with Marvin.")
        print("q) Quit.")

        print("\n" * 2 + "Try out my 'inv' commands!")
        choice = input("--> ")

        if choice == "q":
            marvin.menyval_q()
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
            string = input("Enter a string to randomize: ")
            print(marvin.randomize_string(string)) 

        elif choice == "9":
            string = input("Enter a string to acronym: ")
            print(marvin.get_acronym(string)) 

        elif choice == "10":
            string = input("Enter a string to mask: ")
            print(marvin.mask_string(string)) 

        elif choice == "11":
            string1 = input("Enter the first string: ")
            string2 = input("Enter the second string: ")
            print(marvin.find_all_indexes(string1, string2)) 

        elif choice == "12":
            try:
                string = input("Enter a string: ")
                print("Following countries were found: " + ', '.join(emission_functions.search_country(string)))
            except ValueError as e:
                print(str(e))

        elif choice == "13":
            string = input("Enter a string in this format (country,year1,year2): ")
            string_split = string.split(",")
            if string_split[1] != "1990" and string_split[1] != "2005" and string_split[1] != "2017":
                print("Wrong year!")
            elif string_split[2] != "1990" and string_split[2] != "2005" and string_split[2] != "2017":
                print("Wrong year!")
            else:
                try: 
                    country_change = emission_functions.get_country_change_for_years(
                        string_split[0], string_split[1], string_split[2])
                    print(f"{string_split[0]}:{country_change}%")
                except ValueError as e:
                    print(str(e))

        elif choice == "14":
            string = input("Enter a country: ")
            emission_functions.print_country_data(emission_functions.get_country_data(string))

        elif choice[0:3] == "inv":
            choice_list = choice.split()

            if not (0 <= 1 < len(choice_list)):
                inventory.inventory(lst_inventory)

            elif (0 <= 1 < len(choice_list)) and (choice_list[1] == "pick"):
                if (0 <= 2 < len(choice_list)):
                    item = choice_list[2]
                    if not (0 <= 3 < len(choice_list)):
                        inventory.pick(lst_inventory, item)
                    elif (0 <= 3 < len(choice_list)):
                        index = int(choice_list[3])
                        inventory.pick(lst_inventory, item, index)

            elif (0 <= 1 < len(choice_list)) and (choice_list[1] == "drop"):
                if (0 <= 2 < len(choice_list)):
                    item = choice_list[2]
                    inventory.drop(lst_inventory, item)
                    
            elif (0 <= 1 < len(choice_list)) and (choice_list[1] == "swap"):
                if 0 <= 2 < len(choice_list):
                    item1 = choice_list[2]
                    if 0 <= 3 < len(choice_list):
                        item2 = choice_list[3]
                        inventory.swap(lst_inventory, item1, item2)

        else:
            print("That is not a valid choice. You can only choose from the menu.")

        input("\nPress enter to continue...")


if __name__ == "__main__":            
    main()
