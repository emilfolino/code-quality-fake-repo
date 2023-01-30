#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Main for the marvin chatbot.
"""

import marvin
import emission_functions
import inventory



"""
Its an eternal loop, until q is pressed.
It should check the choice done by the user and call a appropriate
function.
"""
def main():
    """Main method containing structure for program Marvin"""

    # My inventory list
    inventoryStatus = []

    while True:

        choice = marvin.menu_choice()
        words = choice.split()

        if choice == "q":
            marvin.choice_q()
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
            string = input("Enter a string to get akronym: ")
            outputAcronym = marvin.get_acronym(string)
            print(outputAcronym)

        elif choice == "10":
            string = input("Enter a string to mask it: ")
            outputMasked = marvin.mask_string(string)
            print(outputMasked)

        elif choice == "11":
            string1 = input("Enter a string to search in: ")
            string2 = input("Enter the value to find index of: ")
            indexes = marvin.find_all_indexes(string1, string2)
            print(indexes)

        elif choice == "12":
            search_word = input("Search for available data keys type search key word: ")
            try:
                countrySearchList = emission_functions.search_country(search_word)
            except ValueError:
                print("Country does not exist!")
            else:
                print("Following countries were found: " + ", ".join(countrySearchList))

        elif choice == "13":
            search_word = input("Enter country, year and year: ")
            try:
                [country, year1, year2] = search_word.split(",")
            except ValueError:
                print("Wrong input type!")
            else:
                try:
                    emissionChange = emission_functions.get_country_change_for_years(country, year1, year2)
                except KeyError:
                    print("Wrong country!")
                except ValueError:
                    print("Wrong year!")
                else:
                    print(country + ":" +  str(emissionChange) + "%")

        elif choice == "14":
            countryInput = input("Enter country: ")
            data = emission_functions.get_country_data(countryInput)
            emission_functions.print_country_data(data)


        elif "inv" in words:
            inventory.run(words, inventoryStatus)

        else:
            marvin.not_valid()

        marvin.continue_func()

if __name__ == "__main__":
    main()
