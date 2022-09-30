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
                    /^\/^\
                  _|__|  O|
         \/     /~     \_/ \
          \____|__________/  \
                 \_______      \
                         `\     \                 \
                           |     |                  \
                          /      /                    \
                         /     /                       \
                       /      /                         \ \
                      /     /                            \  \
                    /     /             _----_            \   \
                   /     /           _-~      ~-_         |   |
                  (      (        _-~    _--_    ~-_     _/   |
                   \      ~-____-~    _-~    ~-_    ~-_-~    /
                     ~-_           _-~          ~-_       _-~
                        ~--______-~                ~-___-~
"""
def main():

    """
    Its an eternal loop, until q is pressed.
    It should check the choice done by the user and call a appropriate
    function.
    """
    backpack = []
    while True:
        print(chr(27) + "[2J" + chr(27) + "[;H")
        print(marvin_image)
        print("Hi, I'm Marvin. Nice to meet you.")
        print("1) Let me know something about you")
        print("2) Let's convert Celsius to Fahrenheit")
        print("3) Word multiplier")
        print("4) Sum and average of numbers")
        print("5) Longer words")
        print("6) Isogram")
        print("7) Larger or smaller")
        print("a1) String in string")
        print("a2) Times containing numbers ")
        print("a3) Space instead of tab")
        print("a4) Name together")
        print("a5) Player points")
        print("8) randomize word")
        print("9) get acronym")
        print("10) mask string")
        print("11) find all indexes")
        print("b1) points to grade")
        print("b2) string in string")
        print("inv pick) add item to backpack")
        print("inv drop) remove item from backpack")
        print("inv swap) swap places of two items")
        print("inv) check items in backpack, or (inv start stop) for items in that range")
        print("12) Search country")
        print("13) Change years")
        print("14) Data per country")
        print("e1) Co2 emission per country")
        print("e2) emission per capita")
        print("e3) emission per country area")
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

        elif choice == "a1":
            marvin.compare_character()

        elif choice == "a2":
            marvin.multiply_by_two()

        elif choice == "a3":
            marvin.replace_tab()

        elif choice == "a4":
            marvin.new_name()

        elif choice == "a5":
            marvin.player_score()

        elif choice == "8":
            word = input("Enter a string to randomize: ")
            print(marvin.randomize_string(word))

        elif choice == "9":
            word = input("Enter a string to create a new acronym ")
            print(marvin.get_acronym(word))

        elif choice == "10":
            word = input("Enter a word to mask ")
            print(marvin.mask_string(word))

        elif choice == "11":
            word1 = input("Enter a word ")
            word2 = input("Enter a letter or text that is in the first word ")
            print(marvin.find_all_indexes(word1,word2))

        elif choice == "b1":
            max_points = input("Give me max points ")
            points = input("Give me your points ")
            print(marvin.points_to_grade(max_points,points))

        elif choice == "b2":
            str1 = input("Give me a string ")
            str2 = input("Give me a string ")
            str3 = input("Give me a string ")
            str4 = input("Give me a string ")
            print(marvin.has_strings(str1,str2,str3,str4))

        elif choice.startswith("inv pick "):
            inv_list = choice.split(" ")
            new_inv_list = inv_list[2:]
            print(len(new_inv_list))
            if len(new_inv_list) > 1:
                copy_backpack = inventory.pick(backpack,new_inv_list[0],int(new_inv_list[1]))
                backpack = copy_backpack[:]
            else:
                copy_backpack = inventory.pick(backpack,new_inv_list[0])
                backpack = copy_backpack[:]

        
        elif choice.startswith("inv drop "):
            inv_list = choice.split(" ")
            new_inv_list = inv_list[2:]
            inventory.drop(backpack,new_inv_list[0])

        elif choice.startswith("inv swap "):
            inv_list = choice.split(" ")
            new_inv_list = inv_list[2:]
            new_backpack = inventory.swap(backpack,new_inv_list[0],new_inv_list[1])
            backpack = new_backpack[:]


        elif choice.startswith("inv"):
            inv_list = choice.split(" ")
            new_inv_list = inv_list[:]
            if len((new_inv_list)) == 1:
                inventory.inventory(backpack)
            else:
                inventory.inventory(backpack,new_inv_list[1],new_inv_list[2])

        elif choice == "12":
            try:
                search_word = input("Search for a country ")
                print(emission_functions.search_country(search_word))
            except ValueError as e:
                print(str(e))

        elif choice == "13":
            try:
                string = input("Give me a country,first year,second year ")
                new_string = string.split(",")
                country = new_string[0]
                year1 = new_string[1]
                year2 = new_string[2]
                print(country + ":" + str(emission_functions.get_country_change_for_years(country,year1,year2)) + "%")
            except ValueError as e:
                print(str(e))

        elif choice == "14":
            c_name = input("Give me a country")
            c_data = emission_functions.get_country_data(c_name)
            emission_functions.print_country_data(c_data)

        elif choice == "e1":
            try:
                year = input("Give me a year, add a number if you want ex : 1990 10 with a space between ")
                list_year = year.split(" ")
                if len(list_year) > 1:
                    print(emission_functions.co2_order(list_year[0],list_year[1]))
                else:
                    print(emission_functions.co2_order(list_year[0]))
            except ValueError as e:
                print(e)

        elif choice == "e2":
            try:
                year = input("Give me a year, add a number if you want ex : 1990 10 with a space between ")
                list_year = year.split(" ")
                if len(list_year) > 1:
                    print(emission_functions.get_emission_capita(list_year[0],list_year[1]))
                else:
                    print(emission_functions.get_emission_capita(list_year[0]))
            except ValueError as e:
                print(e)

        elif choice == "e3":
            try:
                year = input("Give me a year, add a number if you want ex : 1990 10 with a space between ")
                list_year = year.split(" ")
                if len(list_year) > 1:
                    print(emission_functions.get_emission_area(list_year[0],list_year[1]))
                else:
                    print(emission_functions.get_emission_area(list_year[0]))
            except ValueError as e:
                print(e)


        else:
            print("That is not a valid choice. You can only choose from the menu.")
        input("\nPress enter to continue...")

if __name__ == "__main__":
    main()
