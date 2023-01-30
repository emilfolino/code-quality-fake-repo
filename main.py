"""
Marvin with a simple menu to start up with.
Marvin doesnt do anything, just presents a menu with some choices.
main file that imports and runs code from the file marvin.py
"""
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import marvin
import inventory
import emission_functions

def main():
    """
    Its an eternal loop, until q is pressed.
    It should check the choice done by the user and call a appropriate
    function.
    """
    marvin_image = r"""
                      ,/{}
                    ,/  {|
                ,,,/    {|,
          __--~~        {| ~-,
    __--~~              {     `\
                            ,__ \
                           `,\{),\,
                          __-~  `_ ~-_
                       _-~        ~~-_`~-_
                      '               `~-_`~-__
                      `,                  `~-\_|
                       `,      _-----___    _,'
                       / /--__  ~~--__  `~,~
                        /     ~~--__  ~-',
                       /            ~~--'
    """
    backpack = []
    while True:
        print(chr(27) + "[2J" + chr(27) + "[;H")
        print(marvin_image)
        print("Hi, I'm Wolferz. I am a wolf and I live up on the mountains.")
        print("1) Present yourself to Wolferz.")
        print("2) Return degrees in Celsius to Fahrenheit.")
        print("3) Multiply a given word x number of times.")
        print("4) Return sum and average value.")
        print("5) Return a hyphen string. ")
        print("6) Check if a word is an isogram.")
        print("7) Check if number is larger, smaller or same than the other number.")
        print("8) Randomize a string.")
        print("9) Turn a string into an acronym.")
        print("10) Replace string with a masked version.")
        print("11) Find all indexes where substring exists in string.")
        print("12) Search for country.")
        print("13) Show emission change for a country.")
        print("14) Show all data for a country.")
        print("q) Quit.")
        print("")
        print('You can also try my "inv" commands.')
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
            string = input("Enter a string: ")
            print(marvin.randomize_string(string))

        elif choice == "9":
            string = input("Enter a string: ")
            print(marvin.get_acronym(string))

        elif choice == "10":
            string = input("Enter a string: ")
            print(marvin.mask_string(string))

        elif choice == "11":
            string = input("Enter a string: ")
            substring = input("Enter a substring: ")
            print(marvin.find_all_indexes(string, substring))

        elif choice == "12":
            country = input("Enter a country or part of a country name: ")
            try:
                found_countries = emission_functions.search_country(country)
                print("Following countries were found:", ", ".join(found_countries))
            except ValueError:
                print("Country does not exist!")

        elif choice == "13":
            string = input("Enter a country, year and year: ")
            try:
                lst = string.split(",")
                print(lst[0] + f":{emission_functions.get_country_change_for_years(lst[0],lst[1],lst[2])}%")
            except ValueError:
                print("Wrong year!")

        elif choice == "14":
            country = input("Enter a country: ")
            country_dict = emission_functions.get_country_data(country)
            emission_functions.print_country_data(country_dict)

        elif "inv pick" in choice:
            choice_in_list = choice.split(" ")
            if len(choice_in_list) == 4:
                backpack = inventory.pick(backpack, choice_in_list[2], choice_in_list[3])
            else:
                backpack = inventory.pick(backpack, choice_in_list[2])

        elif choice == "inv":
            inventory.inventory(backpack)

        elif "inv drop" in choice:
            choice_in_list = choice.split(" ")
            backpack = inventory.drop(backpack, choice_in_list[2])

        elif "inv swap" in choice:
            choice_in_list = choice.split(" ")
            backpack = inventory.swap(backpack, choice_in_list[2], choice_in_list[3])

        else:
            print("That is not a valid choice. You can only choose from the menu.")

        input("\nPress enter to continue...")

if __name__ == "__main__":
    main()
