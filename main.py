"""
Marvin with a simple menu to start up with.
Marvin doesnt do anything, just presents a menu with some choices.
You should add functinoality to Marvin.
"""
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
import marvin
import inventory
import emission_functions

marvin_image = r"""
   ___  _____    
 .'/,-Y"     "~-.  
 l.Y             ^.           
 /\               _\_      "Doh!"   
i            ___/"   "\ 
|          /"   "\   o !   
l         ]     o !__./   
 \ _  _    \.___./    "~\  
  X \/ \            ___./  
 ( \ ___.   _..--~~"   ~`-.  
  ` Z,--   /               \    
    \__.  (   /       ______) 
      \   l  /-----~~" /      
       Y   \          / 
       |    "x______.^ 
       |           \    
       j            Y
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
        print("Hi, I'm Homer. What can I Do for you?")
        print("1) Present yourself to Homer.")
        print("2) Let Homer convert celsius to fahrenheit.")
        print("3) Let homer Multiply a word (x) amount of times. ")
        print("4) Enter any amount of numbers and get the sum and average of all the numbers. ")
        print("5) Enter a word. ")
        print("6) Is your word an isogram?")
        print("7) Are the numbers larger, smaller or the same?")
        print("8) Shuffle a string.")
        print("9) Get an acronym")
        print("10) Mask everything but the last 4 digits. ")
        print("11) Find indexes. ")
        print("12 Search for a country. ")
        print("13 See country emission change between 1990 - 2017.")
        print("14 Get all data from a country of choice.")
        print("inv pick) Pick an item to put in your backpack. ")
        print("inv drop) Remove an item from your backpack. ")
        print("inv swap) Swap to items in your backpack. ")
        print("q) Quit.")

        choice = input("--> ")

        if choice == "q":
            print("Bye, bye - and welcome back anytime!")
            break

        elif choice == "1":
            marvin.greet("name")

        elif choice == "2":
            marvin.celsius_to_fahrenheit("ctf")

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
            str1 = list(input("Shuffle this string"))
            random.shuffle(str1)
            print("".join(str1))


        elif choice == "9":
            acronym = marvin.get_acronym(input("Enter a word with CAPS in it: "))
            print(acronym)



        elif choice == "10":
            masked = marvin.mask_string(input("Enter a number with more then 4 digits: "))
            masked2 = marvin.multiply_str("#", masked)
            masked3 = masked + masked2
            print(masked3)



        elif choice == "11":
            a = input("Enter a string: ")
            b = input("Enter another string: ")
            print(marvin.find_all_indexes(a, b))



        elif "inv pick" in choice:
            backpack_list = choice.split(" ")
            item = backpack_list[2]
            if len(backpack_list) == 4:
                backpack = inventory.pick(backpack, item, backpack_list[3])
            else:
                inventory.pick(backpack, item)


        elif "inv swap" in choice:
            backpack1 = backpack_list[2:]
            backpack1 = choice.split(" ")
            print(backpack_list)
            item1 = backpack1[2]
            item2 = backpack1[3]
            inventory.swap(backpack, item1, item2)


        elif "inv drop" in choice:
            backpack_list = choice.split(" ")
            item = backpack_list[2]
            inventory.drop(backpack, item)



        elif "inv" in choice:
            inventory.inventory(backpack)


        elif choice == "12":
            search_word = input("Enter a part of/or the full name of a country: ")
            try:
                countries_list = emission_functions.search_country(search_word)
                results_string = "The following countries were found: " + ", ".join(countries_list)
                print(results_string)
            except ValueError:
                print("Country does not exist!")


        elif choice == "13":
            inp = input("Enter a country and year (1990, 2005, 2017): ")
            try:
                our_list = inp.split(",")
                inp_country = our_list[0]
                if len(our_list) <= 1:
                    print("Wrong year!")
                if len(our_list) == 3:
                    inp_year = our_list[1]
                    inp_year2 = our_list[2]
                    shorterword = emission_functions.get_country_change_for_years(inp_country, inp_year, inp_year2)
                    print(f"{inp_country}:{shorterword}%")
                else:
                    inp_year = our_list[1]
                    print(emission_functions.get_country_year_data_megaton(inp_country, inp_year))
            except ValueError:
                print("Wrong year!")


        elif choice == "14":
            country_name = input("Enter country: ")
            data = emission_functions.get_country_data(country_name)
            emission_functions.print_country_data(data)

        else:
            print("That is not a valid choice. You can only choose from the menu.")

        input("\nPress enter to continue...")

if __name__ == "__main__":
    main()
