"""
Main doc of Marvin. Welcome.
"""

import marvin
import inventory
import emission_functions

elky_image = r"""
 _________
< Mooose! >
 ---------
  \
   \   \_\_    _/_/
    \      \__/
           (oo)\_______
           (__)\       )\/\
               ||----w |
               ||     ||
"""

"""
Its an eternal loop, until q is pressed.
It should check the choice done by the user and call a appropriate
function.
"""


def main():
    """
    Main loop that runs the whole marvin program.
    """

    backpack = []

    while True:
        print(chr(27) + "[2J" + chr(27) + "[;H")
        print(elky_image)
        print("Hi, I'm Elky. I am the king of the forest. Waddup, dawg?")
        print("1) Present yourself to Elky.")
        print("2) Convert celsius to fahrenheit.")
        print("3) Multiply a word!")
        print("4) Get the sum and average of some numbers!")
        print("5) Make a string all weird...")
        print("6) Check if a word is an isogram.")
        print("7) Compare numbers. Are they bigger, same or smaller?")
        print("8) Shuffle characters in a string.")
        print("9) Create an acronym from a string.")
        print("10) Mask a string.")
        print("11) Find all indexes.")
        print("12) Search for a country.")
        print("13) Search for emission data for a country.")
        print("14) Print all data relevant to a country.")
        print("a1) Check if a string only contains letters from another string.")
        print(
            "a2) Check how many times a number has to be multiplied by two to include [0..9].")
        print("a3) Convert tabs to three spaces in a string.")
        print("a4) Make a cool celebrity couple name.")
        print("a5) Check points of players based on a string.")
        print("b1) Check your fake grades!")
        print("b2) Check if a string starts with, ends with and contains other strings.")
        print("e1) Print top CO2 offender for a year.")
        print("e2) Print top CO2 offenders per capita for a year.")
        print("e3) Print top CO2 offenders per area for a year.")
        print("q) Quit.")

        choice = input("--> ")

        if choice == "q":
            print("Bye, bye - and welcome back anytime!")
            break

        # CALLS FUNCTIONS FOR MARVIN1

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

        elif choice == "a1":
            marvin.string_match()

        elif choice == "a2":
            marvin.zeronine_multiply()

        elif choice == "a3":
            marvin.tab_to_space()

        elif choice == "a4":
            marvin.brangelina()

        elif choice == "a5":
            marvin.point_system()

        # CALLS FUNCTIONS FOR NEW MARVIN

        elif choice == "8":
            nonrandom_string = input("Enter a string to randomize: \n")
            print(marvin.randomize_string(nonrandom_string))

        elif choice == "9":
            acronym_string = input("Enter a string to acronymize! \n")
            print(marvin.get_acronym(acronym_string))

        elif choice == "10":
            unmasked_string = input("Enter a string to mask: \n")
            print(marvin.mask_string(unmasked_string))

        elif choice == "11":
            main_i_string = input("Please enter the main string: \n")
            sub_i_string = input("Please enter the sub-string: \n")
            print(marvin.find_all_indexes(main_i_string, sub_i_string))

        # CALLS FUNCTIONS FOR EXTRA ASSIGNMENTS NEW MARVIN #

        elif choice == "b1":
            max_points = input('What was the maximum amount of points? \n')
            score = input("Please enter your score. \n")
            print(marvin.points_to_grade(max_points, score))

        elif choice == "b2":
            string_main = input('Please enter the first (main) string: \n')
            string_start = input(
                'Please enter a string to check if the main string starts with it: \n')
            string_contain = input(
                'Please enter a string to see if the main string contains it: \n')
            string_end = input(
                'Please enter a string to see if the main string ends with it: \n')
            print(marvin.has_strings(string_main,
                  string_start, string_contain, string_end))

        # CALLS FUNCTIONS FOR MARVIN 3

        elif choice.startswith('inv pick'):
            split_choice = choice.split(" ")
            item = split_choice[2]
            try:
                position = split_choice[3]
                backpack = inventory.pick(backpack, item, position)
            except IndexError:
                backpack = inventory.pick(backpack, item)

        elif choice.startswith('inv drop'):
            split_choice = choice.split(" ")
            item = split_choice[2]
            backpack = inventory.drop(backpack, item)

        elif choice.startswith('inv swap'):
            split_choice = choice.split(" ")
            item1 = split_choice[2]
            item2 = split_choice[3]
            backpack = inventory.swap(backpack, item1, item2)

        elif choice.startswith('inv'):
            # inventory.inventory(backpack)
            split_choice = choice.split(" ")
            try:
                start = split_choice[1]
                end = split_choice[2]
                inventory.inventory(backpack, start, end)
            except IndexError:
                inventory.inventory(backpack)
        
        # CALLS FUNCTIONS FOR MARVIN 4

        elif choice == "12":
            search_word = input('Enter your search term: ')
            try:
                print(emission_functions.search_country(search_word))
            except ValueError as e:
                print(str(e))

        elif choice == "13":
            emission_diff_inp = input('Enter a country and two years in csv: ')
            split_emission_diff_inp = emission_diff_inp.split(",")
            
            country = split_emission_diff_inp[0]
            year1 = split_emission_diff_inp[1]
           
            if len(split_emission_diff_inp) > 2:
                try:
                    year2 = split_emission_diff_inp[2]
                    print(f'{country}:{emission_functions.get_country_change_for_years(country, year1, year2)}%')
                except ValueError as er:
                    print(str(er))
            else:
                try:
                    print(emission_functions.get_country_year_data_megaton(country, year1))
                except ValueError as er:
                    print(str(er))

        elif choice == "14":
            country_input = input('Please enter a country: ')
            emission_functions.print_country_data(emission_functions.get_country_data(country_input))

        # CALLS FUNCTIONS FOR MARVIN4 EXTRA ASSIGNMENTS

        elif choice == "e1":
            co2_input = input('Please enter a year and amount of countries: ')
            split_co2_input = co2_input.split(' ')
            year = split_co2_input[0]
            amount = int(split_co2_input[1])
            emission_functions.ordered_co2_emissions(year, amount)

        elif choice == "e2":
            capita_input = input('Please enter a year and amount of countries: ')
            split_capita_input = capita_input.split(' ')
            year = split_capita_input[0]
            try:
                amount = int(split_capita_input[1])
                emission_functions.emissions_per_capita(year, amount)
            except IndexError:
                emission_functions.emissions_per_capita(year)

        elif choice == "e3":
            area_input = input('Please enter a year and amount of countries: ')
            split_area_input = area_input.split(' ')
            year = split_area_input[0]
            try: 
                amount = int(split_area_input[1])
                emission_functions.emissions_per_area(year, amount)
            except IndexError:
                emission_functions.emissions_per_area(year)

        else:
            print("That is not a valid choice. You can only choose from the menu.")

        input("\nPress enter to continue...")


if __name__ == "__main__":
    main()
