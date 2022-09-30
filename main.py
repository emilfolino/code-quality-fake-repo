#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Marvin with a simple menu to start up with.
Marvin doesnt do anything, just presents a menu with some choices.
You should add functinoality to Marvin.
"""
import emission_functions
import marvin
import inventory

barvin_image = r"""
    ·___·
   |o   o|
    \ ' /
     |¯| 
/¯|¯¯¯|¯ ¯|¯¯¯\¯\
| |___|___| |
| |\__|__/| |
|_| |_|_| |_|
 ¥  |_|_|  ¥
  /¯|···|¯\
  | |   | |
  |_|   |_|
  |¯|   |¯|
  | |   | |
  |_|   |_|
  / \   / \
 (>.<) (>.<)

"""

"""
Its an eternal loop, until q is pressed.
It should check the choice done by the user and call a appropriate
function.
"""


def main():
    """
    The Marvin (Barvin) program
    """
    backpack = []
    while True:
        print(chr(27) + "[2J" + chr(27) + "[;H")
        print(barvin_image)
        print("Hi, I'm Barvin. I know it all. What can I do you for?")
        print("1) Present yourself to Barvin.")
        print("2) Celsius to Fahrenheit.")
        print("3) Repeat words. ")
        print("4) Do math. ")
        print("5) Repeat letters in word. ")
        print("6) Isogram. ")
        print("7) Smaller, bigger or equal?. ")
        print("8) Shuffle a word. ")
        print("9) Get an acronym. ")
        print("10) Mask a string. ")
        print("11) Find index. ")
        print("a1) Characters in word. ")
        print("a2) Number 0-9. ")
        print("a3) Tab = 3 spaces. ")
        print("a4) Concatenate names. ")
        print("b1) Points to grade. ")
        print("b2) Has strings. ")
        print("12) Search for country. ")
        print("13) Difference in emission. ")
        print("14) Get data for country. ")
        print("q) Quit. ")

        choice = input("--> ")
        # menyval q
        if choice == "q":
            print("Bye, bye - and welcome back anytime!")
            break
        # menyval 1
        elif choice == "1":
            marvin.greet()
        # menyval 2
        elif choice == "2":
            marvin.celcius_to_farenheit()
        # menyval 3
        elif choice == "3":
            marvin.word_manipulation()
        # menyval 4
        elif choice == "4":
            marvin.sum_and_average()
        # menyval 5
        elif choice == "5":
            marvin.hyphen_string()
        # menyval 6
        elif choice == "6":
            marvin.is_isogram()
        # menyval 7
        elif choice == "7":
            marvin.compare_numbers()
        # menyval 8
        elif choice == "8":
            marvin.randomize_string(input("Enter a word or sentence: "))
        # menyval 9
        elif choice == "9":
            marvin.get_acronym(input("Enter a text: "))
        # Menyval 10
        elif choice == "10":
            marvin.mask_string(input("Enter a string: "))
        # menyval 11
        elif choice == "11":
            print(marvin.find_all_indexes(input("String: "), input("String: ")))
        # menyval a1
        elif choice == "a1":
            marvin.check_letters()
        # menyval a2
        elif choice == "a2":
            marvin.number_0_to_9()
        # menyval a3
        elif choice == "a3":
            marvin.tab_to_spaces()
        # menyval a4
        elif choice == "a4":
            marvin.name_concatenator()
        # menyval b1
        elif choice == "b1":
            print(marvin.points_to_grade(input("Enter the maximum points --> "), input("Enter your points --> ")))
        # menyval b2
        elif choice == "b2":
            answer = marvin.has_strings(input("Enter a string: "), input("Begins with: "),
                                        input("Is included: "), input("Ends with: "))
            print(answer)
        elif choice.startswith("inv pick"):
            choice_list = choice.split(" ")
            try:
                pick_index = int(choice_list[3])
            except (IndexError, ValueError):
                try:
                    inventory.pick(backpack, choice_list[2])
                except IndexError:
                    print("No item to pick ")
            else:
                inventory.pick(backpack, choice_list[2], pick_index)
        elif choice == "inv":
            inventory.inventory(backpack)
        elif choice.startswith("inv drop "):
            inventory.drop(backpack, choice)
        elif choice.startswith("inv swap "):
            swap_var = inventory.str_to_list(choice)
            inventory.swap(backpack, swap_var[2], swap_var[3])
        elif choice == "12":
            search = input("Enter a country name or parts of it: ")
            try:
                print(emission_functions.search_country(search))
            except ValueError:
                print("Country does not exist! ")
        elif choice == "13":
            country_years = input("Enter: Country,year1,year2: ")
            country_year1_year_2 = country_years.split(",")
            try:
                year1 = country_year1_year_2[1]
                year2 = country_year1_year_2[2]
                country = country_year1_year_2[0]
                print(f"{country_year1_year_2[0]}:"
                      f"{emission_functions.get_country_change_for_years(country, year1, year2)}% ")
            except (ValueError, IndexError):
                print("Wrong year!")
        elif choice == "14":
            to_print = emission_functions.get_country_data(input("Enter a country: "))
            emission_functions.print_country_data(to_print)
        input("Press enter to continue: ")


if __name__ == "__main__":
    main()
