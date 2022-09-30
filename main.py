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
      ,     ,
     (\____/)
      (_oo_)
        (O)
      __||__    \/
   []/______\[] /
   / \______/ \/
  /    /__\
 /\   /____\
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
        print("Hi, I'm Marvin. I know it all. What can I do you for?")
        print("1) Present yourself to Marvin.")
        print("2) Let's convert Celsius to Fahrenheit!")
        print("3) Let's multiply a word!")
        print("4) Let's do maths!")
        print("5) Let's play with words!")
        print("6) Let's do play with words a different way!")
        print("7) Let's compare!")
        print("8) Let's randomize a string!")
        print("9) Let's create an acronym!")
        print("10) Let's mask a string!")
        print("11) Let's find part of a string!")
        print("12) Let's find a country or part of a country!")
        print("13) Let's learn about changes in emssions!")
        print("14) Let's learn about a country!")
        print("a1) Let's check strings!")
        print("a2) Let's double!")
        print("a3) Let's change tabs to spaces!")
        print("a4) Let's ship!")
        print("a5) Let's play a game!")
        print("b1) Let's calculate a grade!")
        print("b2) Let's check strings a different")
        print("e1) Let's look up CO2 emissions!")
        print("e2) Let's look up CO2 emissions per capita!")
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
            string = input("Enter a string to randomize: ")
            print(marvin.randomize_string(string))


        elif choice == "9":
            string = input("Enter a string: ")
            print(marvin.get_acronym(string))

        
        elif choice == "10":
            string = input("Enter a string: ")
            print(marvin.mask_string(string))


        elif choice == "11":
            string = input("Enter a string: ")
            part = input("Enter a part: ")
            print(marvin.find_all_indexes(string, part))
        
        ### kmom05 ### 
        elif choice == "12":
            try:
                string = input("Enter a country name or part of country name to search for: ")
                result = emission_functions.search_country(string)
                print(result)
            except ValueError as e:
                print(str(e))

        elif choice == "13":
            try: 
                string = input("To compare, please enter: country,year1,year2 ")
                split_string = string.split(",")
                country = split_string[0]
                year1 = split_string[1]
                year2 = split_string[2]

                result = emission_functions.get_country_change_for_years(country, year1, year2)
                print (f"{country}:{result}%")
            except ValueError as e:
                print(str(e))

        
        elif choice == "14":
            string = input("Enter a country to learn about: ")
            data = emission_functions.get_country_data(string)
            emission_functions.print_country_data(data)
            
        
        elif choice == "e1":
            string = input("Enter a year, and number of countries if wanted: ")
            split_string = string.split()
            if len(split_string) == 2:
                result = emission_functions.sort_countries(split_string[0], int(split_string[1]))
                print(result)
            else: 
                result = emission_functions.sort_countries(split_string[0])
                print(result)
        
        elif choice == "e2":
            string = input("Enter a year, and number of countries if wanted: ")
            split_string = string.split()
            if len(split_string) == 2:
                result = emission_functions.countries_CO2_pc(split_string[0], int(split_string[1]))
                print(result)
            else: 
                result = emission_functions.countries_CO2_pc(split_string[0])
                print(result)
        
        elif choice == "e3":
            string = input("Enter a year, and number of countries if wanted: ")
            split_string = string.split()
            if len(split_string) == 2:
                result = emission_functions.countries_CO2_area(split_string[0], int(split_string[1]))
                print(result)
            else: 
                result = emission_functions.countries_CO2_area(split_string[0])
                print(result)
        
### slut på kmom05 ###

        elif choice == "a1":
            string1 = "" 
            string2 = ""
            
            string1 = input("Enter a word: ")
            string2 = input("Enter a second word: ")
            string1_small = string1.casefold() 
            string2_small = string2.casefold()
            
            print(marvin.check_strings(string1_small, string2_small))

        
        #Jag missade att jag hade missat fallet med alla siffrorna. 
        elif choice == "a2":
            tal = int(input("Enter a number to try: "))
            tal_tries = int(input("Enter number of tries: "))

            print(marvin.number_doubler(tal, tal_tries))

        
        elif choice == "a3":
            string1 = input("Enter a string that contains at least 1 tab: ")
            print(marvin.tab_space(string1))


        elif choice == "a4":
            word1 = input("Enter the first name: ")
            word2 = input("Enter the second name: ")

            print(marvin.ship_names(word1, word2))

        
        elif choice == "a5":
            playerpoints = input("Enter required info: ")
            players = ""
            for letter in playerpoints:
                if letter.isalpha(): # det är en spelare
                    if letter.lower() not in players:
                        players = players + letter.lower()
            result = ""
            for player in players:
                score = 0
                for index, letter in enumerate(playerpoints):
                    if letter == player:
                        score += int(playerpoints[index+1])
                    elif letter == player.upper():
                        score -= int(playerpoints[index+1])
                result = result + player + " " + str(score) + ", "
            result = result.rstrip(", ")

            print(marvin.calc_points(playerpoints)) 


        elif choice == "b1":
            score_max = input("Enter the max score: ") 
            score = input("Enter your score: ")

            print("score: " + marvin.points_to_grade(score_max, score))
        

        elif choice == "b2":
            str1 = input("Enter a word: ")
            str2 = input("Enter a word: ") 
            str3 = input("Enter a word: ") 
            str4 = input("Enter a word: ")  

            print(marvin.has_strings(str1, str2, str3, str4))
        
        ### HÄR BÖRJAR KOD FÖR KMOM04 ###
        elif choice.startswith("inv pick"): 
            inv_pick = choice.split()
            if len(inv_pick) == 3:
                backpack = inventory.pick(backpack, inv_pick[2])
            else:
                backpack = inventory.pick(backpack, inv_pick[2], int(inv_pick[3]))

        elif choice == "inv":
            inventory.inventory(backpack) 

        elif choice.startswith("inv drop"):
            inv_drop = choice.split()
            backpack = inventory.drop(backpack, inv_drop[2])

        elif choice.startswith("inv swap"):
            inv_swap = choice.split()
            backpack = inventory.swap(backpack, inv_swap[2], inv_swap[3])

        elif inventory.check_extra(choice): #för extrauppg
            split_choice = choice.split()
            a = int(split_choice[1])
            b = int(split_choice[2])
            inventory.inventory(backpack, a, b)
        ### HÄR SLUTAR KOD FÖR KMOM04 ###


        else:
            print("That is not a valid choice. You can only choose from the menu.")

        input("\nPress enter to continue...")


if __name__ == "__main__":
    main()
