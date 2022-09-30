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
      ___       ___
     [___] /~\ [___]          
     |ooo|.\_/.|ooo|
     |888||   ||888|
    /|888||   ||888|\
  /_,|###||___||###|._\
 /~\  ~~~ /[_]\ ~~~  /~\
(O_O) /~~[_____]~~\ (O_O)
     (  |       |  )
    [~` ]       [ '~]
    |~~|         |~~|
    |  |         |  |
   _<\/>_       _<\/>_
  /_====_\     /_====_\
"""

"""
Its an eternal loop, until q is pressed.
It should check the choice done by the user and call a appropriate
function.
"""

def main():
    """
    Marvin kmom03
    """
    bagpack = []
    while True:
        print(chr(27) + "[2J" + chr(27) + "[;H")
        print(marvin_image)
        print("Hi, I'm V8. I know it all. What can I do you for?")
        print("1) Present yourself to V8.")
        print("2) Convert the temperature from celsius to Fahrenheit.")
        print("3) Lets play parrto! You say it, will repeat it.")
        print("4) Calculate the sum and the mean of numbers.")
        print("5) Change a string to another form.")
        print("6) Isogram: Check if a string does not contain repeated letters.")
        print("7) Comparing between numbers.")
        print("8) Shuffle a word.")
        print("9) Check anagram.") 
        print("10) Create acronym.") 
        print("11) Mask characters.")  
        print("12) Search for country.") 
        print("13) Show emission change for a countr.")
        print("14) Show all data for a country.")
        print("q) Quit.\n\n\n")

        choice = input("Try out my \"inv\" commands!\n-----------\n--> ")

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
            word = input("Enter a word: ")
            print(marvin.randomize_string(word))

        elif choice == "9":
            char = input("Enter a sting: ")
            print(marvin.get_acronym(char))
 
        elif choice == "10":
            string = input("Enter a string: ")
            print(marvin.mask_string(string))

        elif choice == "11":
            str1 = input("Enter a string: ")
            index_str1 = input("Enter a index: ")
            print(marvin.find_all_indexes(str1, index_str1))

        elif "inv pick" in choice:
            print_list = bagpack
            choice_list = choice.split()
            try:
                choice_string = choice_list[2]
                if len(choice_list) == 4:
                    choice_index = int(choice_list[3])
                    inventory.pick(print_list, choice_string, choice_index)
                else:
                    choice_index = None
                    inventory.pick(print_list, choice_string, choice_index)
            except IndexError:
                print("Error: You did not wrait anything after (inv pick)")


        elif "inv drop" in choice:
            choice_list = choice.split()
            if len(choice_list) >= 3:
                word = choice_list[2]
                print_list = bagpack
                inventory.drop(print_list, word)
            else:
                print("Error")


        elif "inv swap" in choice:
            choice_list = choice.split()
            position1 = choice_list[2]
            position2 = choice_list[3]
            inventory.swap(bagpack, position1, position2)
        
        elif choice.startswith("inv"):
            inventory.inventory(bagpack)

        elif choice == "12":
            try:
                search_word = input("Enter country, year and year: ")
                emission_functions.search_country(search_word)
            except ValueError as e:
                print(str(e))

        elif choice == "13":
            vals = input("Enter country, year and year: ")
            if "," in vals:
                vals = vals.split(",")
            else:
                vals = vals.split()
            try:
                if len(vals) == 2:
                    country = vals[0]
                    year1 = vals[1]
                    print(emission_functions.get_country_year_data_megaton(country, year1))

                elif len(vals) == 3:
                    country = vals[0]
                    year1 = vals[1]
                    year2 = vals[2]
                    emission_functions.get_country_change_for_years(country, year1, year2)
            except ValueError as e:
                print(str(e))

        elif choice == "14":
            country_name = input("Enter country: ")
            get_data = emission_functions.get_country_data(country_name)
            emission_functions.print_country_data(get_data)
        else:
            print("That is not a valid choice. You can only choose from the menu.")

        input("\nPress enter to continue...")

if __name__ == "__main__":
    main()
