#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""this program holds the menu and function calling"""
import marvin
import inventory
import emission_functions

#marvin_image = r"""
 #
 ##
 ###
  ####
   #####
   #######
    #######
    ########
    ########
    #########
    ##########
   ############
 ##############
################
 ################
   ##############
    ##############                                              ####
    ##############                                           #####
     ##############                                      #######
     ##############                                 ###########
     ###############                              #############
     ################                           ##############
    #################      #                  ################
    ##################     ##    #           #################
   ####################   ###   ##          #################
        ################  ########          #################
         ################  #######         ###################
           #######################       #####################
            #####################       ###################
              ############################################
               ###########################################
               ##########################################
                ########################################
                ########################################
                 ######################################
                 ######################################
                  ##########################      #####
                  ###  ###################           ##
                  ##    ###############
                  #     ##  ##########
                            ##    ###
                                  ###
                                  ##
                                  #

#"""

myList = []

def main():
    """
    Its an eternal loop, until q is pressed.
    It should check the choice done by the user and call a appropriate
    function.
    """
    while True:
        print(chr(27) + "[2J" + chr(27) + "[;H")
        #print(marvin_image)
        print("Hi, I'm Batbot. I might look scary but I am sweet as sugar. Can I be at your service?")
        print("1) Present yourself to Batbot.")
        print("2) Batbot transforms celcius to Farenheit")
        print("3) Batbot will multiply your word")
        print("4) Batbot will take in number and calculate the average")
        print("5) Batbot will add an extra character for every separated character")
        print("6) Batbot will check if your word is a isogram")
        print("7) Batbot will say larger. smaller or same for your number")
        print("8) Batbot will randomize a string")
        print("9) Batbot will create an Acronym for you")
        print("10) Batbot will mask your string for you")
        print("11) Batbot will get indexes for you")
        print("12) Get countries in database: ")
        print("13) Get difference between country emission")
        print("14) Get collected data for country")
        print("q) Quit.")

        print("\n\nTry out my 'inv' commands \n-------------------------\n")

        choice = input("--> ")

        if choice == "q":
            print("BOOOOO!!! See you another time!")
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
            string = input("Enter a string to randomzie: ")
            string2 = marvin.randomize_string(string)
            print(string2)

        elif choice == "9":
            string = input("Enter string to create Acronym: ")
            string = marvin.get_acronym(string)
            print(string)

        elif choice == "10":
            string = input("Enter string to create mask string: ")
            string = marvin.mask_string(string)
            print(string)

        elif choice == "11":
            string1 = input("Enter string to get indexes: ")
            string2 = input("enter what letter you seek: ")
            string = marvin.find_all_indexes(string1, string2)
            print(string)

        elif choice == "12":
            search_word = input("Type the country your looking for: ")
            try:
                emission_functions.search_country(search_word)
            except(ValueError):
                print("Country does not exist!")

        elif choice == "13":
            try:
                country,year1,year2 = input("What country and two years?: ").split(",")
                emission_dif = emission_functions.get_country_change_for_years(country, year1, year2)
                print(country + ":" + str(round(emission_dif,2)) + "%")

            except(ValueError):
                print("Wrong year!")

        elif choice == "14":
            country = input("What country to get data: ")
            dictionary = emission_functions.get_country_data(country)
            emission_functions.print_country_data(dictionary)




        elif choice == "inv":
            inventory.inventory(myList)

        elif "pick" in choice:
            command = choice.split()
            if len(command) > 3:
                inventory.pick(myList, command[2], int(command[3]))
            else:
                inventory.pick(myList, command[2])

        elif "drop" in choice:
            command = choice.split()
            item = command[2]
            inventory.drop(myList, item)

        elif "swap" in choice:

            command = choice.split()
            fItem = command[2]
            sItem = command[3]
            inventory.swap(myList, fItem, sItem)





    else:
        print("That is not a valid choice. You can only choose from the menu.")



if __name__ == "__main__":
    main()
