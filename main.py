#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
this is marvin 3.0

in the new patch notes
* marvin now comes equiped with a bag that you can store and remove items from
"""

import marvin
import inventory
import emission_functions 
from emission_functions import get_country_change_for_years


def main():
    """
    the first print sektion that asks the user for a input on what task
    """
    temp_rygga = []
      

    while True:
        print(chr(27) + "[2J" + chr(27) + "[;H")
        print(marvin.marvin_image)
        print("Hi, I'm Marvin. I know it all. What can I do you for?")
        print("I think you ought to know I'm feeling very depressed.")
        print("1) Present yourself to Marvin.")
        print("q) Quit.")
        print("2) for celsius to fahrenheit")
        print("f) for fahrenheit to celsius")
        print("3) for multiplikation of a string")
        print("4) sum an avrage")
        print("5) where every letter in a word is progresivly expanded")
        print("6) is isogram")
        print("7) larger or smaler")
        print("a1) if all letters can be found i two strings")
        print("a2) how many times do we nead to multiply x to have all num 0-9 in it")
        print("a3) type backslash t and it will be convertet to a tab")
        print("a4) concatunate last and first name")
        print("a5) score talying system")
        print("8) randomize a string")
        print("9) get acronym")
        print("10) hide first part")
        print("11) find index")
        print("inv) inventory")
        print("inv pick) add a item to the bag")
        print("inv drop) remove a item from the bag")
        print("inv swap) swap to items in the bag")
        print("12) search country")
        print("13) landets förändrade utsläpp")
        print("14) land information")




        choice = input("--> ")
        print("Here I am, brain the size of a planet, and they tell me " + str(choice) + " ... great")


    #the user will  be direkted to diffrent funktions depending on what task. this is an infinit loop
        if choice == "q":
            print("\nBye, bye - and welcome back anytime!")
            print("Now I lay me down to sleep")
            print("Try to count electric sheep")
            print("Sweet dream wishes you can keep")
            print("How I hate the night")
            break

        elif choice == "1":
            marvin.greet()


        elif choice == "2":
            marvin.celcius_to_farenheit()

        elif choice == "f":
            marvin.f_converter()
            
        elif  choice == "3":
            marvin.word_manipulation()

        elif choice == "4":
            marvin.sum_and_average()

            
        elif choice == "5":
            marvin.hyphen_string() 
            
        elif choice == "6":
            marvin.is_isogram()


        elif choice == "7":
            marvin.compare_numbers()


        elif choice == "a1":
            marvin.a1_funk()

        elif choice == "a2":
            marvin.a2_funk()


        elif choice == "a3":
            marvin.a3_funk()
            
            

        elif choice == "a4":
            marvin.a4_funk()
            

        elif choice == "a5": 
            marvin.a5_funk()
            
        elif choice == "8":
            inputt = input("enter a string: ")
            print(marvin.randomize_string(inputt))

        elif choice == "9":
            inp = input("enter a string: ")
            print(marvin.get_acronym(inp))

        elif choice == "10":
            statment = input("--> ")
            print(marvin.mask_string(statment))

        elif choice == "11":
            string = input("the strung: ")
            sub_string = input("the supstring: ")
            print(marvin.find_all_indexes(string, sub_string))

        elif choice[:8] == "inv pick":
            ch = choice.split()
            if len(ch) >= 4:
                ryggan = inventory.pick(temp_rygga, ch[2], ch[3])
            else:
                ryggan = inventory.pick(temp_rygga, ch[-1])
            temp_rygga = ryggan

        elif choice[:8] == "inv drop":
            ch = choice.split()
            ryggan = inventory.drop(temp_rygga, ch[2])
            temp_rygga = ryggan

        elif choice[:8] == "inv swap":
            ch = choice.split()
            ryggan = inventory.swap(temp_rygga, ch[2], ch[3])
            temp_rygga = ryggan

        elif choice[:3] == "inv":
            ch = choice.split()
            try:
                inventory.inventory(temp_rygga, ch[1], ch[2])
            except IndexError:
                inventory.inventory(temp_rygga)
        
        elif choice == "12":
            try:
                choice = input("serch for a contrie: ")
                print(emission_functions.search_country(choice))
            except ValueError as e:
                print(e)



        elif choice == "13":
            choice = input("enter a contry year and year: ")
            try:
                out = get_country_change_for_years(choice.split(",")[0], choice.split(",")[1], choice.split(",")[2])
                print(str(choice.split(",")[0]) + ":" + str(out)  + "%")
            except KeyError as k:
                print(k)
            except ValueError as v:
                print(v)
     

        elif choice == "14":  
            choice = input("enter the contrie: ")
            try:               
                emission_functions.print_country_data(emission_functions.get_country_data(choice))
            except IndexError:
                print("invalid input")


        else:
            print("That is not a valid choice. I wish you'd just tell me a valid ")
            print("choice rather trying to engage my enthusiasm because I haven't got one.")

        input("\nPress enter to continue...")




if __name__ == "__main__":
    main()
