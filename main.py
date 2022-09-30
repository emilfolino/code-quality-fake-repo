#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Main function that runs the Marvin program
"""
import marvin
import inventory
import emission_functions

bag = []

def main():
    """
    Its an eternal loop, until q is pressed.
    It should check the choice done by the user and call a appropriate
    function.
    """
    while True:
        choice = marvin.menu()
        

        if choice == "q":
            marvin.bye()
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
            input_string = input("Enter a string to randomize: ")
            print(marvin.randomize_string(input_string))

        elif choice == "9":
            input_string = input("Enter a string with some uppercase letters to make an acronym of: ")
            print(marvin.get_acronym(input_string))
        
        elif choice == "10":
            input_string = input("Enter a string to mask: ")
            print(marvin.mask_string(input_string))

        elif choice == "11":
            input_string_a = input("Enter the first string: ")
            input_string_b = input("Enter the second string: ")
            print(marvin.find_all_indexes(input_string_a, input_string_b))

        elif choice == "12":
            input_string = input("Search for country: ")
            try:
                print("Following countries were found: " + ", ".join(emission_functions.search_country(input_string)))
            except ValueError as error:
                print(str(error))

        elif choice == "13":
            try:
                input_string = input("Search for emission change(country,year1,year2)\
                    (Year must be either 1990, 2005 or 2017): ")
                country, year1, year2 = input_string.split(",")
                print(country + ":" + str(emission_functions.get_country_change_for_years(country, year1, year2)) + "%")
            except ValueError as error:
                print(str(error))

        elif choice == "14":
            try:
                input_string = input("Search for country: ")
                data = emission_functions.get_country_data(input_string)
                emission_functions.print_country_data(data)
            except ValueError as error:
                print(str(error))

        elif choice in ("A1", "a1"):
            marvin.compare_letters()

        elif choice in ("A2", "a2"):
            marvin.match_brackets()

        elif choice.startswith("inv"):
            if choice == "inv":
                inventory.inventory(bag)

            elif choice.startswith("inv pick"):
                choice = choice.replace("inv pick ", "")
                choice_array = choice.split(" ")
                if len(choice_array) < 2:
                    inventory.pick(bag, choice_array[0])
                else:
                    inventory.pick(bag, choice_array[0], choice_array[1])

            elif choice.startswith("inv swap"):
                choice = choice.replace("inv swap ", "")
                choice_array = choice.split(" ")
                inventory.swap(bag, choice_array[0], choice_array[1])

            elif choice.startswith("inv drop"):
                choice = choice.replace("inv drop ", "")
                inventory.drop(bag, choice)
                

            else:
                marvin.not_valid()

        else:
            marvin.not_valid()

        marvin.press_to_continue()

if __name__ == "__main__":
    main()
