#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Marvin main menu
"""

import marvin
import inventory
import emission_functions

def main():
    """
    The-turkey-that-can-do-many-things program
    """
    marvin_image = r"""
                               ,+*^^*+___+++_
                          ,*^^^^              )
                       _+*                     ^**+_
                     +^       _ _++*+_+++_,         )
         _+^^*+_    (     ,+*^ ^          \+_        )
        {       )  (    ,(    ,_+--+--,      ^)      ^\
       { (@)    } f   ,(  ,+-^ __*_*_  ^^\_   ^\       )
      {:;-/    (_+*-+^^^^^+*+*<_ _++_)_    )    )      /
     ( /  (    (        ,___    ^*+_+* )   <    <      \
      U _/     )    *--<  ) ^\-----++__)   )    )       )
       (      )  _(^)^^))  )  )\^^^^^))^*+/    /       /
     (      /  (_))_^)) )  )  ))^^^^^))^^^)__/     +^^
    (     ,/    (^))^))  )  ) ))^^^^^^^))^^)       _)
     *+__+*       (_))^)  ) ) ))^^^^^^))^^^^^)____*^
     \             \_)^)_)) ))^^^^^^^^^^))^^^^)
      (_             ^\__^^^^^^^^^^^^))^^^^^^^)
        ^\___            ^\__^^^^^^))^^^^^^^^)\\
             ^^^^^\uuu/^^\uuu/^^^^\^\^\^\^\^\^\^\
                ___) >____) >___   ^\_\_\_\_\_\_\)
               ^^^//\\_^^//\\_^       ^(\_\_\_\)
                 ^^^ ^^ ^^^
    """

    bag = [] #my inventory list

    while True:
        print(chr(27) + "[2J" + chr(27) + "[;H")
        print(marvin_image)
        print("Hi, I'm Malle. Why do you wake me from my slumber?")
        print("1) Introduce yourself to the mighty turkey.")
        print("2) Change a temperature from Celcius to Fahrenheit.")
        print("3) You want me to give you a word multiple times? Alright.")
        print("4) Feed me numbers and I will tell you what they make.")
        print("5) Let me add letters to words for you.")
        print("6) I'll check if the word is an isogram if you choose this option.")
        print("7) Want me to tell you what number is the largest?")
        print("8) Randomize a string.")
        print("9) Make an acronym.")
        print("10) Hide a string.")
        print("11) Find all indexes.")
        print("12) Search for a country.")
        print("13) Change in emissions for a country.")
        print("14) All info about a country.")
        print("a1) I'll check if some letters exist in a word.")
        print("a2) Multiply a number by 2 until it contains all numbers, and recieve the amount of times.")
        print("a3) Replace tab with blankspace.")
        print("a4) Mash up names.")
        print("a5) Count points via a string of letters and numbers.")
        print("b1) Turn points to a grade.")
        print("b2) Check if certain strings are in a string.")
        print("q) Say goodbye")

        choice = input("--> ")

        if choice == "q":
            marvin.quits()
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
            string = input("What word do you want to randomize?: ")
            print(marvin.randomize_string(string))
        elif choice == "9":
            string = input("Give me the name you want to make an acronym for: ")
            print(marvin.get_acronym(string))
        elif choice == "10":
            string = input("What string do you want to mask?: ")
            print(marvin.mask_string(string))
        elif choice == "11":
            wholeString = input("Give me a string: ")
            partString = input("Give me part of that string: ")
            print(marvin.find_all_indexes(wholeString, partString))
        elif choice == "12":
            searchWord = input("What country? ")
            try:
                print(emission_functions.search_country(searchWord))
            except ValueError:
                print("Country does not exist!")
        elif choice == "13":
            inputString = input("Give me country, year1, and year2. ")
            inputList = inputString.split(",")
            try:
                (print(inputList[0] + ":" + str(emission_functions.get_country_change_for_years
                (inputList[0], inputList[1], inputList[2])) + "%"))
            except ValueError as err:
                print(err)
        elif choice == "14":
            try:
                country_name = input("What country would you like info on? ")
                data = emission_functions.get_country_data(country_name)
                emission_functions.print_country_data(data)
            except ValueError as err:
                print(err)

    #Extras

        elif choice == "a1":
            marvin.a1()
        elif choice == "a2":
            marvin.a2()
        elif choice == "a3":
            marvin.a3()
        elif choice == "a4":
            marvin.a4()
        elif choice == "a5":
            marvin.a5()
        elif choice == "b1":
            maxPoints = input("What is the max amount of points? ")
            points = input("What is the amount of points? ")
            print(marvin.points_to_grade(maxPoints, points))
        elif choice == "b2":
            fullString = input("What's the full string? ")
            startString = input("Check if it starts with: ")
            middleString = input("Check if it has: ")
            endString = input("Check if it ends with: ")
            print(marvin.has_strings(fullString, startString, middleString, endString))

    #Inventory

        elif "inv pick" in choice:
            choiceList = choice.split()
            thing = " ".join(choiceList[2:])
            place = ""
            if choiceList[-1].isnumeric():
                place = choiceList[-1]
                thing = " ".join(choiceList[2:-1])
            bag = inventory.pick(bag, thing, place)

        elif "inv drop" in choice:
            choiceList = choice.split()
            thing = " ".join(choiceList[2:])
            bag = inventory.drop(bag, thing)

        elif "inv swap" in choice:
            choiceList = choice.split()
            thing1 = choiceList[2]
            thing2 = choiceList[3]
            bag = inventory.swap(bag, thing1, thing2)

        elif choice == "inv" or "inv " in choice:
            choiceList = choice.split()
            start = 0
            stop = len(bag)
            if len(choiceList) == 3:
                start = choiceList[1]
                stop = choiceList[2]
            inventory.inventory(bag, start, stop)

        else:
            print("That is not a valid choice. You can only choose from the menu.")

        input("\nPress enter to continue...")

if __name__ == "__main__":
    main()
