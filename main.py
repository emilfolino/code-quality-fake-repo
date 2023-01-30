#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Phoenix with a simple menu to start up with.
Phoenix doesn't do anything, just presents a menu with some choices.
You should add functionality to Phoenix.
ASCII art by : Christian Koehler
"""
import inventory

import marvin

import emission_functions


bag = []

Phoenix = r"""
             _/|       |\_
            /  |       |  \
           |    \     /    |
           |  \ /     \ /  |
           | \  |     |  / |
           | \ _\_/^\_/_ / |
           |    --\//--    |
            \_  \     /  _/
              \__  |  __/
                 \ _ /
                _/   \_   
               / _/|\_ \  
                /  |  \   
                 / v \
"""


def main():
    """
    Its an eternal loop, until q is pressed.
    It should check the choice done by the user and call a appropriate
    function.
    """
    while True:
        print(chr(27) + "[2J" + chr(27) + "[;H")
        print(Phoenix)
        print("Greetings! Im Phoenix, I've just been hatched and ready to help you!")
        print("Warning: I'm flamable...")
        print("""
    1) Present yourself to Phoenix. 
    2) Convert celsius to fahrenheit.
    3) Let me repeat after your, as many times as you wish.
    4) Do a little math for you.
    5) Have fun with words.
    6) Is that word an isogram or not?
    7) Is that number larger, smaller, or same?
    8) Shuffle letters in your word or sentence.
    9) Create your own, exclusive acronym!
    10) Make a secret funny sentence or number.
    11) Find what you are looking for in a sentence.
    b1) Convert your points into grade.
    12) Get country data
    13) Compare C02 emission in a country in two different years
    14) Retrieve full data on a chosen country
    q) Quit.
    

    I've got new 'inv' commands, try them out!
    """)
        choice = input("Choose wisely: ")

        if choice == "q":
            print("Flying away, but I'll come back when you'll need me.")
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

            original_string = input("Type in a string that you want to shuffle: ")

            print(marvin.randomize_string(original_string))

        elif choice == "9":

            comp_name = input("Type in a sentence you want to have and acronym for: ")
            print(marvin.get_acronym(comp_name))

        elif choice == "10":
            characters = input("Type in a word or any characters: ")

            print(marvin.mask_string(characters))

        elif choice == "11":

            text = input("Type in any string: ")
            x = input("Type in symbols you want to find indexes of in a string: ")
            print(marvin.find_all_indexes(text, x))

        elif choice == "b1":   

            max_points = input("Type in maximum points: ")
            your_points = input("Type in your points: ")
            print(marvin.points_to_grade(max_points, your_points))

        elif choice == "inv":

            inventory.inventory(bag)
            

        elif "inv pick" in choice:

            arguments = choice.split(" ")
            item = arguments[2]
            index = None
            if len(arguments) == 4:
                index = arguments[3]

            inventory.pick(bag, item, index)


        elif "inv swap" in choice:

            arguments = choice.split(" ")
            item1 = arguments[2]
            item2 = arguments[3]
            inventory.swap(bag, item1, item2)


        elif "inv drop" in choice:
            arguments = choice.split(" ")
            item = arguments[2]
            inventory.drop(bag, item)

        elif choice == "12":

            country_name = input("Name of the country: ")
            try:
                country_list = emission_functions.search_country(country_name)
                print("Following countries were found : " + ", ".join(country_list))
            except ValueError:
                print("Country does not exist!")


        elif choice == "13":
            arguments = input("Type in country and two different years that you want to compare: ")
            arguments_2 = arguments.split(",")
            years = ['1990', '2005', '2017']
            country = arguments_2[0]
            year_1 = arguments_2[1]
            year_2 = arguments_2[2]

            try:
                if year_1 not in years or year_2 not in years:
                    raise ValueError
                print(country + ":" + str(emission_functions.get_country_change_for_years(country, year_1, year_2))\
 + "%")

            except ValueError:
                print("Wrong year!")
                

        elif choice == "14":
            country = input("Which country's data you would like to retrieve?: ")
            chosenc = country.title()
            data = emission_functions.get_country_data(chosenc)
            emission_functions.print_country_data(data)

        else:
            print("I don't know everything, I just know what I know...")

        input("\nPress enter to continue...")

if __name__ == "__main__":
    main()
