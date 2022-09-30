
"""
Abodeh with a simple menu to start up with.
Abodeh doesnt do anything, just presents a menu with some choices.
You should add functinoality to Abodeh.
"""
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import marvin
import inventory
import emission_functions


marvin_image = r"""
      _       _
     (_\     /_)
       ))   ((
     .-^^^^^^^-.  
 /^\/  _.   _.  \/^\
 \(   /__\ /__\   )/
  \,  \o_/_\o_/  ,/
    \    (_)    /
     `-.'==='.-'
      __) - (__   
     /  `~~~`  \
    /  /     \  \
    \ :       ; /
     \|==(*)==|/
      :       :
       \  |  /
     ___)=|=(___
    {____/ \____}

"""



def main():
    """
    Its an eternal loop, until q is pressed.
    It should check the choice done by the user and call a appropriate
    function.
    """
    bagpack = []
    while True:
        print(chr(27) + "[2J" + chr(27) + "[;H")
        print(marvin_image)
        print("Hi, I'm Abodeh.Im here to help you, What can I help you today?")
        print("1) Present yourself to Abodeh.")
        print("2) Convert Celsius to Fahrenheit.")
        print("3) Print many word game.")
        print("4) Let me help you with math.")
        print("5) copy many letters.")
        print("6) Isogram.")
        print("7) Lets play number game.")
        print("8) randomize string.")
        print("9) get_acronym.")
        print("10) mask_string.")
        print("11) find all indexes")
        print("12) find the country !!")
        print("13) country and year.")
        print("14) country data")
        print("q) Quit.")

        choice = input("Try my new inv commend ")

        if choice == "q":
            print("Come back anytime im alweys here ^_^ ")
            break

        elif choice == "1":
            marvin.greet()

        elif choice == "2" :
            marvin.celcius_to_farenheit()
            
        elif choice == "3" : 
            word1 = input("Enter a word : ")
            number1 = input("how many times? ")
            print(marvin.multiply_str(word1,number1))

        elif choice == "4" : 
            marvin.sum_and_average()

        elif choice == "5" : 
            marvin.hyphen_string()

        elif choice == "6":
            marvin.is_isogram()

        elif choice == "7" :
            marvin.compare_numbers()
        
        elif choice == "8":
            s = input("Entre a word: ")
            print(marvin.randomize_string(s))
        
        elif choice == "9" :
            str7 = input("Write a word : ")
            print(marvin.get_acronym(str7))

        elif choice == "10":
            a_string = input("Enter a number : ")
            print(marvin.mask_string(a_string))
            

        elif choice == "11":
            str23 = input("Write the text : ")
            str45 = input("what are you looking for ? ")
            print(marvin.find_all_indexes(str23,str45))
        
        elif "inv pick" in choice :
            input_pick = choice.split(" ")
            if input_pick[2] in bagpack :
                print("Already have it in my bagpack.")
            else:
                if len(input_pick) == 4 :
                    str_1 = input_pick[2]
                    str_2 = input_pick[3]
                    print(inventory.pick(bagpack,str_1,str_2))
                else :
                    str_1 = input_pick[2]
                    str_2 = len(bagpack)
                    print(inventory.pick(bagpack,str_1,str_2))
        elif "inv drop" in choice :
            input_drop = choice.split(" ")
            if len(input_drop) <= 2:
                print("Error item not found")
            else :
                str_1 = input_drop[2]
                print(inventory.drop(bagpack,str_1))
        elif "inv swap" in choice :
            input_swap = choice.split(" ")
            if len(input_swap) == 4 :
                str_1 = input_swap[2]
                str_2 = input_swap[3]
                print(inventory.swap(bagpack,str_1,str_2))
            else : 
                print("Error something went wrong")
        elif "inv" in choice :
            print(inventory.inventory(bagpack))
        
        elif choice == "12":
            try:
                search_word = input("What country are you looking for ? ")

                print(emission_functions.search_country(search_word))
            except ValueError:
                print ("Country does not exist!")
            

        elif choice == "13" :
            try: 
                input_country_year = input("Write country and year : ")
                the_list = input_country_year.split(",")
                input_country = the_list[0]
                if len(the_list) <= 1 :
                    print("Error please write a year!")
                elif len(the_list) == 3 :
                    input_year = the_list[1]
                    input_year_two = the_list[2]
                    str_24 = emission_functions.get_country_change_for_years(input_country,input_year,input_year_two)
                    print(f"{input_country}:{str_24}%")
                else :
                    input_year = the_list[1]
                    print(emission_functions.get_country_year_data_megaton(input_country,input_year))
            except ValueError:
                print("Wrong year!")
        elif choice == "14":
            try:
                input_get = input("Enter a country for info : ") 
                data = emission_functions.get_country_data(input_get)
                print(emission_functions.print_country_data(data))
            except ValueError:
                print("Error")
        else: 
            print("That is not a valid choice. You can only choose from the menu.")

        input("\nPress enter to continue...")

if __name__ == "__main__": 
    main()
