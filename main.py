#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Marvin with a simple menu to start up with.
Marvin doesnt do anything, just presents a menu with some choices.
You should add functinoality to Marvin.
"""

import marvin 
import inventory as inv
import emission_functions as em_func
marvin_image = r"""
              .andAHHAbnn.
           .aAHHHAAUUAAHHHAn.
          dHP^~"        "~^THb.
    .   .AHF                YHA.   .
    |  .AHHb.              .dHHA.  |
    |  HHAUAAHAbn      adAHAAUAHA  |
    I  HF~"_____        ____ ]HHH  I
   HHI HAPK""~^YUHb  dAHHHHHHHHHH IHH
   HHI HHHD> .andHH  HHUUP^~YHHHH IHH
   YUI ]HHP     "~Y  P~"     THH[ IUP
    "  `HK                   ]HH'  "
        THAn.  .d.aAAn.b.  .dHHP
        ]HHHHAAUP" ~~ "YUAAHHHH[
        `HHP^~"  .annn.  "~^YHH'
         YHb    ~" "" "~    dHF
          "YAb..abdHHbndbndAP"
           THHAAb.  .adAHHF
            "UHHHHHHHHHHU"
              ]HHUUHHHHHH[
            .adHHb "HHHHHbn.
     ..andAAHHHHHHb.AHHHHHHHAAbnn..
.ndAAHHHHHHUUHHHHHHHHHHUP^~"~^YUHHHAAbn.
  "~^YUHHP"   "~^YUHHUP"        "^YUP^"
       ""         "~~"
"""


def main():
    """
    Its an eternal loop, until q is pressed.
    It should check the choice done by the user and call a appropriate
    function.
    """

    bag = []

    while True:
        print(chr(27) + "[2J" + chr(27) + "[;H")
        print(marvin_image)
        print("How do you do, I'm Marvin. I know it all. What can I do for you?")
        print("1) Present yourself to Marvin")
        print("2) Convert Celsius to Fahrenheit")
        print("3) Word multiplication")
        print("4) Sum and average")
        print("5) Letter multiplication by position")
        print("6) Check isogram")
        print("7) Numbers game")
        print("8) Randomize string")
        print("9) Acronym")
        print("10) Mask string")
        print("11) Find all indexes")
        print("12) Search countries")
        print("13) Country change in pollution by year")
        print("14) Print country data")
        print("a1) Check letters in word")
        print("a2) Multiplications by 2 before number contains all 10 digits")
        print("a3) Replace tabs with spaces")
        print("a4) Portmanteau a name")
        print("a5) Count points")
        print("b1) Points to grade")
        print("b2) Check if string contains substring")
        print("e1) Print top emitters")
        print("e2) Print top emitters per capita")
        print("e3) Print top emitters per area")
        print("inv) Print inventory of bag")
        print("inv pick) Pick up an item and put in bag\nuse syntax \"pick item position(optional)\"")
        print("inv swap) Swap position of two items in the bag\nuse syntax \"swap item item\"")
        print("inv drop) Dropan item from the bag\nuse syntax \"drop item\"")

        print("q) Quit.")

        choice = input("--> ")
        choice = choice.lower()

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
            input_string = input("Enter a string to randomize:\n-->")
            print(marvin.randomize_string(input_string))

        elif choice == "9":
            input_string = input("Please enter a string with uppercase letters to acronymise:\n-->")
            print(marvin.get_acronym(input_string))

        elif choice == "10":
            input_string = input("Please enter a string to be masked:\n-->")
            print(marvin.mask_string(input_string))

        elif choice == "11":
            input_string1 = input("Please enter a string:\n-->")
            input_string2 = input("Please enter a string which is a substring of the last string:\n-->")

            print(marvin.find_all_indexes(input_string1, input_string2))
        
        elif choice == "12":
            input_string1 = input("Please enter your search:\n-->")

            try:
                print("Following countries were found: " + ', '.join(em_func.search_country(input_string1)))
            except ValueError as e:
                print(str(e))
        
        elif choice == "13":
            input_string1 = input("Please enter country and" 
                                " years you want to compare separated by comma:\n-->")
            input_list = input_string1.split(',')
            if len(input_list) == 3:
                try:
                    print(input_list[0] + ":" + \
                        str(em_func.get_country_change_for_years(input_list[0], input_list[1], input_list[2])) +"%")
                except ValueError as e:
                    print(str(e))
            else:
                print("Error: please enter a valid command.")
        
        elif choice == "14":
            input_string1 = input("Please enter a country:\n-->")
            try:
                em_func.print_country_data(em_func.get_country_data(input_string1))
            except ValueError as e:
                print(str(e))

        elif choice == "e1":
            input_string1 = input("Please enter a year and number of countries:\n-->")
            input_list = input_string1.split(' ')
            try:
                if len(input_list) == 2:
                    em_func.print_top_emitters(input_list[0], int(input_list[1]))
                elif len(input_list) == 1:
                    em_func.print_top_emitters(input_list[0])
                else:
                    print("Error: please enter a valid command.")
            except ValueError as e:
                print(str(e))

        elif choice == "e2":
            input_string1 = input("Please enter a year and number of countries:\n-->")
            input_list = input_string1.split(' ')
            try:
                if len(input_list) == 2:
                    em_func.print_emission_per_capita(input_list[0], int(input_list[1]))
                elif len(input_list) == 1:
                    em_func.print_emission_per_capita(input_list[0])
                else:
                    print("Error: please enter a valid command.")
            except ValueError as e:
                print(str(e))

        elif choice == "e3":
            input_string1 = input("Please enter a year and number of countries:\n-->")
            input_list = input_string1.split(' ')
            try:
                if len(input_list) == 2:
                    em_func.print_emission_per_area(input_list[0], int(input_list[1]))
                elif len(input_list) == 1:
                    em_func.print_emission_per_area(input_list[0])
                else:
                    print("Error: please enter a valid command.")
            except ValueError as e:
                print(str(e))

        elif choice == "a1":
            marvin.check_letters_in_word()
        
        elif choice == "a2":
            marvin.all_digits()

        elif choice == "a3":
            marvin.replace_tab_with_spaces()

        elif choice == "a4":
            marvin.portmanteau_name()

        elif choice == "a5":
            marvin.count_points()

        elif choice == "b1":
            max_points = input("Please enter max points:\n-->")
            points = input("Please enter your points:\n-->")
            print(marvin.points_to_grade(max_points, points))

        elif choice == "b2":
            str1 = input("Please enter 1st string:\n-->")
            str2 = input("Please enter 2nd string:\n-->")
            str3 = input("Please enter 3d string:\n-->")
            str4 = input("Please enter 4th string:\n-->")
            print(marvin.has_strings(str1, str2, str3, str4))

        elif choice.startswith("inv pick "):
            list1 = choice.split()
            try:
                if len(list1) > 3:
                    bag = inv.pick(bag, list1[2], list1[3])
                else:
                    bag = inv.pick(bag, list1[2])    
            except IndexError:
                print("Error: no item given. Please type in an item to put in the bag")


        elif choice.startswith("inv swap "):
            list1 = choice.split()
            try:
                bag = inv.swap(bag, list1[2], list1[3])
            except IndexError:
                print("Error: Please enter two items to be swapped")

        elif choice.startswith("inv drop "):
            list1 = choice.split()
            try:
                bag = inv.drop(bag, list1[2])
            except IndexError:
                print("Please enter an item to be dropped.")

        elif choice.startswith("inv"):
            list1 = choice.split()
            try:
                if(list1[0] == 'inv'):
                    if len(list1) > 2:
                        inv.inventory(bag, list1[1], list1[2])
                    elif len(list1) > 1:
                        inv.inventory(bag, list1[1])  
                    else:
                        inv.inventory(bag)    
                else:
                    print("Error: please enter a valid command")

            except ValueError:
                print("Error: please enter a valid command")

        else:
            print("That is not a valid choice. You can only choose from the menu.")

        input("\nPress enter to continue...")


if __name__ == "__main__":
    main()
