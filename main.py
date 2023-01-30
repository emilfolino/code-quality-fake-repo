"""
Chat bot
"""
#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import marvin
import inventory
import emission_functions
"""
Marvin with a simple menu to start up with.
Marvin doesnt do anything, just presents a menu with some choices.
You should add functinoality to Marvin.
"""

marvin_image = r"""
             _/|    _   |\_
           _/_ |   _|\\ | _\
         _/_/| /  /   \|\ |\_\_
       _/_/  |/  /  _  \/\|  \_\_ 
     _/_/    ||  | | \o/ ||    \_\_
    /_/  | | |\  | \_ V  /| | |  \_\
   //    ||| | \_/   \__/ | |||    \\
  // __| ||\  \          /  /|| |__ \\
 //_/ \|||| \/\\        //\/ ||||/ \_\\
///    \\\\/   /        \   \////    \\\
|/      \/    |    |    |     \/      \|
              /_|  | |_  \
             ///_| |_||\_ \
             |//||/||\/||\|             
              / \/|||/||/\/              
                /|/\| \/       
"""
def main():
    """
    Its an eternal loop, until q is pressed.
    It should check the choice done by the user and call a appropriate
    function.
    """
    bag = []

    while True:
        print(chr(27) + "[2J" + chr(27) + "[;H")
        print(marvin_image)
        print("Hi, I'm Basel. Chose what you find it intersting?")
        print("1) Present yourself to Marvin.")
        print("2) Convert from Celsius to Fahrenheit.")
        print("3) Multiple a word you enter by the number you want.")   
        print("4) The sum and arithmetic average of given numbers.")   
        print("5) Type a string to get a new string with repeated letters in row.")   
        print("6) Type a word to check if it an isogram.")            
        print("7) Enter tow numbers to check which of them is larger.")
        print("8) Enter a word to get it shuffled.")
        print("9) Enter a word to get the acronym.")
        print("10) Enter a string or number to get all characters except tha last 3 replaced with '#'.")
        print("11) Enter tow string to get the indexes of the second string of the first one.")
        print("12) Search for country.")
        print("13) Show emession change for a country.")
        print("14) Show all data for a country.")
        print("q) Quit.")

        choice = input("--> ")

        if choice == "q":
            print("Bye, bye - and welcome back anytime!")
            break

        elif choice == "1":
            marvin.greet()
        
        elif choice == "2" :
            marvin.celcius_to_farenheit()

            
        elif choice == "3":
            marvin.word_manipulation()
        
        elif choice == "4":
            marvin.sum_and_average()
    

        elif choice == "5":
            
            marvin.hyphen_string()
        
        elif choice == "6":
            marvin.is_isogram()


        elif choice == "7" :

            marvin.compare_numbers()

        
        elif choice == "8" :
            word = input("Enter a word: ")
            print(marvin.randomize_string(word))
        
        
        elif choice == "9" :
            word = input("Enter a word: ")
            short_cut = marvin.get_acronym(word)
            print(short_cut)

        
        elif choice == "10" :
            word = input("Enter a number: ")
            print(marvin.mask_string(word))
            
        
        elif choice == "11" :
            string = input("Enter the first string: ")
            sub_string = input("Enter the substring: ")
            print(marvin.find_all_indexes(string, sub_string))
            
        
        
        elif "inv pick" in choice:
            element_index = choice.split(" ")
            element = element_index[2]
            try:
                index = int(element_index[3])
            except IndexError:
                index = -1
            inventory.pick(bag,element,index)
        
        
        elif choice == "inv":
            inventory.inventory(bag)

        
        elif "inv drop" in choice:
            
            get_unwanted = choice.split(" ")
            unwanted = get_unwanted[2]
            inventory.drop(bag,unwanted)


        elif "inv swap" in choice:
            get_elements = choice.split(" ")
            first_element = get_elements[2]
            second_element = get_elements[3]
            
            inventory.swap(bag,first_element,second_element)

        elif choice == "12":
            search_word = input("Enter the name of the country: ")
            try:
                print(emission_functions.search_country(search_word))
            except ValueError:
                print("Country does not exist!")


        elif choice == "13":
            country_year = input("Enter the name,year:")
            get_inputs = country_year.split(",")
            country = get_inputs[0]
            year1 = get_inputs[1]
           
            year2 = get_inputs[2]
           
            try:
                print(country+":"+str(emission_functions.get_country_change_for_years(country,year1,year2))+"%")
            except ValueError:
                print("Wrong year!")
            
            
            
        elif choice == "14":
            country_name = input("Enter the name of a country: ")
            try:
                
                data = emission_functions.get_country_data(country_name)
                
                
                emission_functions.print_country_data(data)

                
                
            
            except ValueError:
                print(country_name , "does not exist!")

           
        else:
            print("That is not a valid choice. You can only choose from the menu.")

        input("\nPress enter to continue...")

if __name__ == "__main__":
    main()    
