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


asciimage = r"""
       ___,---.__          /'|`\          __,---,___
    ,-'    \`    `-.____,-'  |  `-.____,-'    //    `-.
  ,'        |           ~'\     /`~           |        `.
 /      ___//              `. ,'          ,  , \___      |
|    ,-'   `-.__   _         |        ,    __,-'   `-.    |
|   /          /\_  `   .    |    ,      _/\          \   |
\  |           \ \`-.___ \   |   / ___,-'/ /           |  /
 \  \           | `._   ` \  |  //'   _,' |           /  /
  `-.\         /'  _ `---'' , . ``---' _  `\         /,-'
     ``       /     \    ,='/ \`=.    /     \       ''
             |__   /|\_,--.,-.--,--._/|\   __|
             /  `./   \`\ |  |  | /,//' \,'   |
            /   /     ||--+--|--+-/-|     \   |
           |   |     /'\_\_\ | /_/_/`\     |   |
            \   \__, \_     `~'     _/ .__/   /
             `-._,-'   `-._______,-'   `-._,-'
"""

def main():

    """
    Its an eternal loop, until q is pressed.
    It should check the choice done by the user and call a appropriate
    function.
    """
    invlist = []
        
    while True:
        print(chr(27) + "[2J" + chr(27) + "[;H")
        print(asciimage)
        print("I am Aamon, the lord of the underworld. What do you want?")
        print("1) Tell who you are to Aamon.")
        print("2) Ask what the temperature is from celsius to fahrenheit")
        print("3) Tell Aamon a word and he will repeat it the nuber of time you say")
        print("4) Enter three numbers and get both the sum and the avrage")
        print("5) Pick a word and I will add another letter depending on the lenght of the word")
        print("6) Pick a word and I will check if it is a isogram")
        print("7) Check if a number is lower or higher or the same")
        print("8) Give me a word and i will randomize it")
        print("9) Give me a word and i will give you a short version of your word")
        print("10) Give me a word and i will mask it")
        print("11) Give me a word and a letter and i will show the position of the letters")
        print("12) Search for country")
        print("13) Difference between emission between two years")
        print("14) Prints all info about country")
        print("q) Leave Aamon.")
        print("\n\n")
        print("Try my inv command")
        choice = input("--> ")
        
        
        if choice == "q":
            print("I will see you again mortal!")
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
            strrand = input("Enter a string to randomize: ")
            print(marvin.randomize_string(strrand))
        elif choice == "9":
            akro = input("Give me a word: ")
            print(marvin.get_acronym(akro))
        elif choice == "10":
            mask = input("Give me a word: ")
            print(marvin.mask_string(mask))
        elif choice == "11":
            inde = input("Give me a word: ")
            indelet = input("Give me a letter: ")
            print(marvin.find_all_indexes(inde, indelet))
        
        elif "inv" in choice:
            chooser = choice.split()
            try:
                posit = chooser[3]
            except IndexError:
                posit = ""
            if "pick" in choice:
                inventory.pick(invlist, chooser[2], posit)
                    
            elif "drop" in choice:
                inventory.drop(invlist, chooser[2])

            elif "swap" in choice:
                invlist = inventory.swap(invlist, chooser[2], chooser[3])
                
                
            elif choice == "inv":
                inventory.inventory(invlist)
            
            else:
                print("Sorry not a command, try")
        
        elif choice == "12":
            searchcountry = input("Typa a country or a part of one to see if it exists: ")
            try:
                emission_functions.search_country(searchcountry)
            except ValueError:
                print("Country does not exist!")
        elif choice == "13":
            try:
                country1, year1, year2 = input("Type a country, a year and another year: ").split(",")
                try:
                    print(country1 + ":" + str(emission_functions.get_country_change_for_years(country1, year1, year2))
                     + "%")
                except ValueError:
                    print("Wrong year!")
                

            except ValueError:
                print("Not enough values, try again")

        elif choice == "14":
            countrydt = input("Type a country: ")
            cdt = emission_functions.get_country_data(countrydt)
            emission_functions.print_country_data(cdt)
        else:
            print("\nAamon says:\n")
            print("That is not the right question to ask mortal!!!")
        input("\nPress enter to continue...")

if __name__ == "__main__":
    main()    
        
        