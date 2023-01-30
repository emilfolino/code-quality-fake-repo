#Project by Croyse

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Funktioner som kör programmet
'''

import emission_functions
import inventory
import marvin


marvin_image = r"""
      o   o
       )-(
      (O O)
       \=/
      .-"-.
     //\ /\ \ 
  _ // / \ \ \_
  =./ {,-.} \.= 
      || ||
      || ||    
    __|| ||__  
   `---" "---'

"""


def main():
    '''
    Gör så att programmet funkar
    '''
    backpack_list = []


    print(marvin_image)
    print("Hello and welcome! My name is Bob. What question are you seeking an answer for, son?")    
    print("1) Present yourself to Bob, son.")
    print("2) Do you need help to convert celsius to fahrenheit, son?")
    print("3) Have something on your mind, son?")
    print("4) Do you need help with your math, son? Let me help you.")
    print("5) Give me a word, son and watch this.")
    print("6) Want to know if it a isogram, son?")
    print("7) Want to know if something is smaller or bigger, son?")
    print("8) Let me shuffle a word, son.")
    print("9) Do you want help with acronyms, son?")
    print("10) Do you want me to mask your text, son?")
    print("11) Let med help you find the index, son.")
    print("12) Do you want to search for some countries, son?")
    print("13) Want to see the difference for emission between two years in a country in, son?")
    print("14) Want to see some data for a country, son?")
    print("q) Quit.")

    print("Try out my 'inv' commands, son!")

    while True: 
        choice = input("--> ")

    #om man vill avsluta programmet.    
        if choice in ('q', 'Q'):
            print("Are you already leaving, son?")
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
            string = input("Input something you want me to shuffle, son: ")
            print(marvin.randomize_string(string))


        elif choice == "9":
            akronym = input("Let me help you make a acronym, son. ")
            print(marvin.get_acronym(akronym))


        elif choice == "10":
            secret = input("Input a number, son. Every number except the last 4 will be protected. ")
            print(marvin.mask_string(secret))

    
        elif choice == "11":
            Argument_one = input("Input your first argument, son: ")
            Argument_two = input("Input your second argument, son: ")
            print(marvin.find_all_indexes(Argument_one, Argument_two))

        elif choice == "12":
            search_word = input("Want to check what countries exists? Enter a country or some letters, son. ")
            try:
                print(emission_functions.search_country(search_word))
            except ValueError:
                print("Country does not exist!")

        elif choice == "13":
            country = input("Enter a country and 2 years, to see the difference, son. ")
            split = country.split("," , 3)
            try:
                print(split)
                print(split[0] + ":" + 
                str(emission_functions.get_country_change_for_years(split[0], split[1], split[2])) + "%")
            except ValueError:
                print("Wrong year!")

        elif choice == "14":
            country_info = input("Enter a country, son. ")
            emission_functions.print_country_data(emission_functions.get_country_data(country_info))

        elif choice.startswith("inv pick"):
            splitting = choice.split(" ")
            thing = splitting[2]
            try:
                index = splitting[2]
                backpack_list = inventory.pick(backpack_list, thing, index)
            except ValueError:
                backpack_list = inventory.pick(backpack_list, thing)

        elif choice.startswith("inv drop"):
            splitting = choice.split(" ")
            the_dropped_thing = splitting[2]
            inventory.drop(backpack_list, the_dropped_thing)

        elif choice.startswith("inv swap"):
            splitting = choice.split(" ")
            thing1 = splitting[2]
            thing2 = splitting[3]
            inventory.swap(backpack_list, thing1, thing2)

        elif choice.startswith("inv"):
            inventory.inventory(backpack_list)

        else:
            print("That is not valid. Choose a valid option, son.")

            
if __name__ == "__main__":
    main()  
     