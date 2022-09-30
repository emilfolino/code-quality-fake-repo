"""
Marvin with a simple menu to start up with.
Marvin doesnt do anything, just presents a menu with some choices.
You should add functinoality to Marvin.
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import marvin
import inventory
import emission_functions





marvin_image = r"""
  /\ ___ /\
 (  o   o  )
  \  >#<  /
  /       \
 /         \       ^
|           |     //
 \         /    //
  ///  ///   --


"""

def main ():
    """
    Its an eternal loop, until q is pressed.
    It should check the choice done by the user and call a appropriate
    function.
    """
    backpack = []

    while True:
        print(chr(27) + "[2J" + chr(27) + "[;H")
        print(marvin_image)
        print("Hi, I'm Marvin. I know it all. What can I do you for?")
        print("1) Present yourself to Marvin.")
        print("2) Celsius to Fahrenheit.")
        print("3) Wordgame!")
        print("4) Sum and average.")
        print("5) Letters")
        print("6) Isogram")
        print("7) Larger or smaller")
        print("8) Randomize string")
        print("9) Get acronym")
        print("10) Mask string")
        print("11) Find all indexes")
        print("12) Search country")
        print("13) Emission change between the years 1990, 2005, 2017")
        print("14) Print country data")
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

        elif choice == "8":
            user_str = input("Enter a string to randomize: ")
            print(marvin.randomize_string(user_str))

        elif choice == "9":
            input_str = input("Marvin says: Enter a string: ")
            print(marvin.get_acronym(input_str))

        elif choice== "10":
            inp_str= input("Marvin ask for a string: ")
            print(marvin.mask_string(inp_str))

        elif choice== "11":
            str1= input("Marvin ask for a string: ")
            str2= input("Enter a substring to search for: ")
            print(marvin.find_all_indexes(str1, str2))

        elif choice == "12":
            try:
                input_data =input("Enter a country: ")
                print(emission_functions.search_country(input_data))

            except ValueError as e:
                print(str(e))

        elif choice == "13":
            try:
                inp_str= input("Enter a comma separated string containing a country and two years: ")
                inp_list = inp_str.split(",")

                answer= emission_functions.get_country_change_for_years(inp_list[0], inp_list[1], inp_list[2])
                print(f"{inp_list[0]}:{answer}%")

            except ValueError as e:
                print(str(e))

        elif choice=="14":
            inp_country =input("Enter a country: ")
            dict_co = emission_functions.get_country_data(inp_country)

            emission_functions.print_country_data(dict_co)



        elif choice.startswith("inv"):
            if choice == "inv":
                inventory.inventory(backpack)

            else:
                list_choice= choice.split()

                if "pick" in choice:

                    try:
                        pos= int(list_choice[3])
                        backpack= inventory.pick(backpack, list_choice[2],pos)
                    except IndexError:
                        backpack= inventory.pick(backpack, list_choice[2])

                elif "drop" in choice:
                    backpack= inventory.drop(backpack,list_choice[2])


                elif "swap" in choice:
                    backpack= inventory.swap(backpack,list_choice[2], list_choice[3])



        else:
            print()
            print("Ah Ah Ah, You didn´t say the magic word! (You can only choose from the menu)")

        input("\nPress enter to continue...")

if __name__ == "__main__":
    main()
