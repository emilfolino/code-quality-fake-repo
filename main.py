#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""docstring"""

import marvin as m
import inventory as inv
import emission_functions as ef

def main():
    """
    Marvin with a simple menu to start up with.
    Marvin doesnt do anything, just presents a menu with some choices.
    You should add functinoality to Marvin.
    """

    marvin_inventory = []

    marvin_image = r"""
        .'\   /`.
            .'.-.`-'.-.`.
        ..._:   .-. .-.   :_...
    .'    '-.(o ) (o ).-'    `.
    :  _    _ _`~(_)~`_ _    _  :
    :  /:   ' .-=_   _=-. `   ;\  :
    :   :|-.._  '     `  _..-|:   :
    :   `:| |`:-:-.-:-:'| |:'   :
    `.   `.| | | | | | |.'   .'
        `.   `-:_| | |_:-'   .'
        `-._   ````    _.-'
            ``-------''
    """

    """
    Its an eternal loop, until q is pressed.
    It should check the choice done by the user and call a appropriate
    function.
    """

    while True:
        print(chr(27) + "[2J" + chr(27) + "[;H")
        print(marvin_image)
        print("Hi, I'm Marvin. I know it all. What can I do you for?")
        print("1) Present yourself to Marvin.")
        print("2) Celsius to Fahrenheit.")
        print("3) Let's play parrot! You say it I'll repeat it.")
        print("4) Sure I can do your math for you")
        print("5) Is smaller, bigger or equal.")
        print("6) Isogram")
        print("7) Repeat letters in word")
        print("8) Radnomize string")
        print("9) Acronym")
        print("10) Mask string")
        print("11) Find index")
        print("a1) All char in string: ")
        print("a2) All numbers in: ")
        print("a3) String with tabs")
        print("a4) Vowels")
        print("a5) Long word: ")
        print("b1) Grading")
        print("q) Quit.")

 

        choice = input("--> ")

        if choice == "q":
            print("Bye, bye - and welcome back anytime!")
            break

        elif choice == "1":
            m.greet()

        elif choice == "2":
            m.celcius_to_farenheit()

        elif choice == "3":
            m.word_manipulation()

        elif choice == "4":
            m.sum_and_average()

        elif choice == "5":
            m.hyphen_string()

        elif choice == "6":
            m.is_isogram()
        
        elif choice == "7":
            m.compare_numbers()

        elif choice == "8":
            string = input("Enter a string to randomize: ")
            print(m.randomize_string(string))

        elif choice == "9":
            string = input("Enter a string to get acronym: ")
            print(m.get_acronym(string))

        elif choice == "9":
            string = input("Enter a string to get acronym: ")
            print(m.mask_string(string))

        elif choice == "10":
            string = input("I'll mask the string: ")
            print(m.mask_string(string))

        elif choice == "11":
            string = input("a string and what I should look for: ")
            find_string = input("what to look for: ")
            print(m.find_all_indexes(string, find_string))

        elif choice == "a1":
            m.chars_in_string()

        elif choice == "a2":
            m.all_digits_in_number()

        elif choice == "a3":
            m.string_to_tabs()

        elif choice == "a4":
            m.vowels_in_name()

        elif choice == "a5":
            m.long_word()

        elif choice == "b1":
            try:
                max_points = int(input("max points: "))
                points = int(input("your points: "))
                print(m.points_to_grade(max_points, points))
            except ValueError:
                continue
            
        elif choice == "b2":
            first_string = input("first string: ")
            second_string = input("second string: ")
            third_string = input("third string: ")
            fourth_string = input("fourth string: ")
            print(m.has_strings(first_string,second_string, third_string, fourth_string))
        
        elif choice == "inv":
            inv.inventory(marvin_inventory)

        elif "inv pick" in choice:
            input_command = choice.split()

            if len(input_command) > 3:
                marvin_inventory = inv.pick(marvin_inventory, input_command[2], input_command[-1])
            else:
                marvin_inventory = inv.pick(marvin_inventory,input_command[2])
        
        elif "inv drop" in choice:
            item_to_drop = choice.split()[-1]
            inv.drop(marvin_inventory, item_to_drop)

        elif "inv swap" in choice:
            input_command = choice.split()
            item_one, item_two = input_command[2], input_command[3]
            marvin_inventory = inv.swap(marvin_inventory, item_one,item_two)

        elif choice == "12":
            search_word = input("Enter country name or part of country name to see if it exists: ")
            try:
                print(ef.search_country(search_word))
            except ValueError as e:
                print(e)
        
        elif choice == "13":
            country, from_year, to_year = input("Enter country, year and year: ").split(",")
            try:
                emission_change = ef.get_country_change_for_years(country, from_year, to_year)
                print(f"{country}:{emission_change}%")
            except ValueError as e:
                print(e)
        
        elif choice == "14":
            country = input("Enter country: ")
            data = ef.get_country_data(country)
            ef.print_country_data(data)

        elif choice == "e1":
            input_string = input("What year and how many countries to show? ")
            try: 
                year, limitation = input_string.split(",")
                all_country_emission = ef.get_sorted_emission(year, int(limitation))
            except ValueError:
                year = input_string
                all_country_emission = ef.get_sorted_emission(year)
            ef.print_countires_emission(all_country_emission)

        else:
            print("That is not a valid choice. You can only choose from the menu.")

        input("\nPress enter to continue...")


if __name__ == "__main__":
    main()
