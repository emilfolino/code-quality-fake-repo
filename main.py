"""
main functions that calls all defined functions
in marvin module
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#16:22 100%

import re
import marvin
import inventory
import emission_functions



marvin_image = r"""
               _._
           __.{,_.).__
        .-"           "-.
      .'  __.........__  '.
     /.-'`___.......___`'-.\
    /_.-'` /   \ /   \ `'-._\
    |     |   '/ \'   |     |
    |      '-'     '-'      |
    ;                       ;
    _\         ___         /_
   /  '.'-.__  ___  __.-'.'  \
 _/_    `'-..._____...-'`    _\_
/   \           .           /   \
\____)         .           (____/
    \___________.___________/
      \___________________/
     (_____________________)
"I`m not fat, I`m festively plump!"
"""
bag = []
def main():
    """
    Main function
    """

    while True:
        print(marvin_image)
        print("Hi I'm Adam. I know it all. What can I do you for?")
        print("1) Present yourself to the entity.")
        print("2) Celcius till Fahrenheit conversion")
        print("3) Ordmultiplicering")
        print("4) Summa och medel")
        print("5) Make a s-tt-rrr-iiii-nnnnn-gggggg")
        print("6) Isogram ")
        print("7) Jamfora tal ")
        print("8) Randomize string")
        print("9) Get the acronym")
        print("10) Mask string ##")
        print("11) Find all indexes of a char in string")
        print("12) Search for country")
        print("13) Show emission change for a country")
        print("14) Show all data for a country")
        print("E1) Total CO2/country")
        print("E2) CO2/Capita")
        print("E3) CO2/Area")
        print("q) Quit.")
        print("Try out my new 'inv' comamnds! ")
        choice = input("---->>  ")

        if choice == "1":
            marvin.greet()

        elif choice == "q":
            break

        elif choice == "2":
            marvin.celcius_to_farenheit()

        elif choice == "3":
            marvin.word_manipulation()

        elif choice == "4":
            marvin.sum_and_average()

        elif choice == '5':
            marvin.hyphen_string()

        elif choice == "6":
            marvin.is_isogram()

        elif choice == '7':
            marvin.compare_numbers()

        elif choice == '8':
            random_string = input("Enter the damn string: ")
            print(marvin.randomize_string(random_string))

        elif choice == '9':
            acro_string = input("Enter a string to create an acronym: ")
            print(marvin.get_acronym(acro_string))

        elif choice == '10':
            maske_str = input("Enter a string to do masking: ")
            print(marvin.mask_string(maske_str))

        elif choice == '11':
            BigString = input("Enter the first string: ")
            SubString = input("Enter the sub string: ")
            print(marvin.find_all_indexes(BigString,SubString))
            
        elif choice == '12':
            con = input("Search for a country if that exists..: ")
            try:
                print(emission_functions.search_country(con))
            except ValueError as e:
                print(e)

        elif choice == '13':
            arg_s = input("Enter country, year and year: ")
            lx = arg_s.split(",")
            sonuc = emission_functions.search_country(lx[0])
            try:
                for x in sonuc:
                    print(x +":"+str(emission_functions.get_country_change_for_years(lx[0], lx[1], lx[2])) + "%")
            except ValueError as e:
                print(e)

        elif choice == "14":
            county = input("Enter a country to get info: ")
            # if county[0].islower():
            #     print(emission_functions.get_country_data(county[0].upper()+county[1:]))
            # else:
            #     print(emission_functions.get_country_data(county))
            if county[0].islower():
                emission_functions.print_country_data(emission_functions.get_country_data(county[0].upper()+county[1:]))
            else:
                emission_functions.print_country_data(emission_functions.get_country_data(county))
        
        elif re.match("e1", choice, flags=re.IGNORECASE):
            arama = input("Enter a year and how many max countries to print:  ")
            
            araList = arama.split(" ")
            print("")
            print("List of countries with total CO2 in " +araList[0])
            print("----------------------------")
            emission_functions.arabul(int(araList[0]),int(araList[1]))

        elif re.match("e2", choice, flags=re.IGNORECASE):
            datem = input("Enter a year and number of countries with space-in-between: ")
            datemx = datem.split(" ")
            print("")
            print("List of countries with CO2/Capita in " +datemx[0])
            print("----------------------------")
            if len(datemx) == 1:
                emission_functions.per_cap(int(datemx[0]), None)
            if len(datemx) == 2:
                emission_functions.per_cap(int(datemx[0]), int(datemx[1]))

        elif re.match("e3", choice, flags=re.IGNORECASE):
        
            datem = input("Enter a year and number of countries with space-in-between: ")
            datemx = datem.split(" ")
            print("")
            print("List of countries with CO2/Area in " +datemx[0])
            print("----------------------------")
            if len(datemx) == 1:
                emission_functions.per_area(int(datemx[0]), None)
            if len(datemx) == 2:
                emission_functions.per_area(int(datemx[0]), int(datemx[1]))


        elif choice == "a1":
            marvin.a1_f()

        elif choice == "a2":
            marvin.a2_f()

        elif choice == 'a3':
            marvin.a3_f()

        elif choice == 'a4':
            marvin.a4_f()

        elif choice == "a5":
            marvin.a5_f()

        elif choice == "b1":
            maxPoint = input("Enter the max point: ")
            yourPoint = input("Enter your points: ")
            print(marvin.points_to_grade(maxPoint, yourPoint))

        elif choice == "b2":
            firstStr = input("First String: ")
            secondStr = input("Second String: ")
            thirdStr = input("Third String: ")
            fourthStr = input("Fourth String: ")
            print(marvin.has_strings(firstStr, secondStr, thirdStr, fourthStr))

        elif "inv" in choice:
            com_list = choice.split(" ")

            if len(com_list) == 1:
                inventory.inventory(bag)

            else:
                if com_list[1] == "pick":
                    if len(com_list) == 3:
                        inventory.pick(bag, com_list[2], None)
                    if len(com_list) == 4:
                        inventory.pick(bag, com_list[2], com_list[3])

                elif com_list[1] == "swap":
                    inventory.swap(bag, com_list[2], com_list[3])

                elif com_list[1] == "drop":
                    inventory.drop(bag, com_list[2])

                elif (isinstance(int(com_list[1])) == int):
                    inventory.inventory(bag, com_list[1], com_list[2])


        #9:19 50%
        #9:31 37%

        else:
            print("That is not a valid choice. You can only choose from the menu.")




        input("\n Press enter to continue...")


if __name__ == "__main__":
    print(marvin_image)

    main()
