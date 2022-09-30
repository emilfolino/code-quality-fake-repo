"""This file contains the main loop to run the Marvin program."""

import marvin
import inventory
import emission_functions
"""Functions for all menu options."""

marvin_image = r"""
                __________
         ______/ ________ \______
       _/      ____________      \_
     _/____________    ____________\_
    /  ___________ \  / ___________  \
   /  /XXXXXXXXXXX\ \/ /XXXXXXXXXXX\  \
  /  /############/    \############\  \
  |  \XXXXXXXXXXX/ _  _ \XXXXXXXXXXX/  |
__|\_____   ___   //  \\   ___   _____/|__
[_       \     \  X    X  /     /       _]
__|     \ \                    / /     |__
[____  \ \ \   ____________   / / /  ____]
     \  \ \ \/||.||.||.||.||\/ / /  /
      \_ \ \  ||.||.||.||.||  / / _/
        \ \   ||.||.||.||.||   / /
         \_   ||_||_||_||_||   _/
           \     ........     /
            \________________/
"""

"""
Its an eternal loop, until q is pressed.
It should check the choice done by the user and call a appropriate
function.
"""



def main():
    """The main loop of the program. Asks for a user selection and then
    runs the approriate function."""
    invList = []
    while True:
        print(chr(27) + "[2J" + chr(27) + "[;H")
        print(marvin_image)
        print("Hi, I'm Darwin. I know it all. What can I do you for?")
        print("1) Present yourself to Darwin.")
        print("2) Convert Celsius to Farenheit.")
        print("3) Print a word a number of times.")
        print("4) Calculate the sum and average of multiple numbers.")
        print("5) Print every letter of a word an increasing number of times")
        print("6) Check if a word is an isogram.")
        print("7) Compare number to previous number.")
        print("8) Randomize a string.")
        print("9) Create an acronym.")
        print("10) Mask a string.")
        print("a1) Check if every letter in a string i in another string.")
        print("a2) Double a number until it contains every digit 0-9.")
        print("a3) Replaces tabs in string with spaces.")
        print("a4) Combine two names.")
        print("a5) Calculate points for players based on string.")
        print("b1) Calculate a grade based on points.")
        print("b2) Compare four strings.")
        print("Emission functions:")
        print("12) Search for countries in data.")
        print("q) Quit.")

        print('Try out my "inv" commands!')
        choice = str(input("--> "))

        if choice == "q":
            marvin.quit_program()
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
        
        elif choice == "a1":
            marvin.compare_strings()

        elif choice == "a2":
            marvin.double_number_check()
    
        elif choice == "a3":
            marvin.replace_tabs()

        elif choice == "a4":
            marvin.combine_names()
        
        elif choice == "a5":
            marvin.calculate_points()

        elif choice == "8":
            string = input("Enter a string to randomize: ")
            print(marvin.randomize_string(string))

        elif choice == "9":
            string = input("Enter a string to get an acronym:")
            print(marvin.get_acronym(string))

        elif choice == "10":
            string = input("Enter a string to mask:")
            print(marvin.mask_string(string))
        
        elif choice == "11":
            string1 = input("Enter your first string:")
            string2 = input("Enter a second string which is contained in the first:")
            print(marvin.find_all_indexes(string1,string2))

        elif choice == "b1":
            max_points = int(input("What's the point maximum?"))
            your_points = int(input("How many points did you get?"))
            print(marvin.points_to_grade(max_points,your_points))

        elif choice == "b2":
            first = input("Enter your first string:")
            second = input("Enter your second string:")
            third = input("Enter your third string:")
            fourth = input("Enter your fourth string:")
            print(marvin.has_strings(first,second,third,fourth))

        # Funktioner kmom04
        
        elif choice.startswith("inv pick"):
            invChoice = choice.replace("inv pick ","")
            print(invChoice)
            if " " in invChoice:
                invChoiceSplit = invChoice.split(" ")
                invItem = invChoiceSplit[0]
                invPos = int(invChoiceSplit[1])
                invList = inventory.pick(invList,invItem,invPos)
            else: 
                invList = inventory.pick(invList,invChoice)
        
        elif choice.startswith("inv drop"):
            invChoice = choice.replace("inv drop ","")
            invList = inventory.drop(invList,invChoice)
        
        elif choice.startswith("inv swap"):
            invChoice = choice.replace("inv swap ","")
            invChoiceSplit = invChoice.split(" ")
            invList = inventory.swap(invList,invChoiceSplit[0],invChoiceSplit[1])
        
        elif choice == "inv":
            inventory.inventory(invList)

        elif choice.startswith("inv"):
            invChoice = choice.replace("inv ","")
            invChoiceSplit = invChoice.split(" ")
            inventory.inventory(invList,invChoiceSplit[0],invChoiceSplit[1])

        #Funktion kmom05
        elif choice == "12":
            search_word = input("Enter your search word:")
            try:
                emission_functions.search_country(search_word)
            except ValueError:
                print("Country does not exist!")
        
        elif choice == "13":
            change_input = input("Input your data in this format: country,year1,year2")
            split_input = change_input.split(",")
            try:
                change_result = emission_functions.get_country_change_for_years(*split_input)
                print(split_input[0] + ":" + str(change_result) + "%")
            except ValueError:
                print("Wrong year!")

        elif choice ==  "14":
            userInput = input("Input your country:")
            emission_functions.get_and_print_country_data(userInput)

        elif choice == "e1":
            userInput = input("Input a year and amount:")
            splitInput = userInput.split(" ")
            emission_functions.print_emissions_for_year(*splitInput)

        elif choice == "e2":
            userInput = input("Per capita. Input a year and amount:")
            splitInput = userInput.split(" ")
            emission_functions.print_emissions_for_year_per_capita(*splitInput)

        elif choice == "e3":
            userInput = input("Per area. Input a year and amount:")
            splitInput = userInput.split(" ")
            emission_functions.print_emissions_for_year_per_area(*splitInput)

        else:
            print("That is not a valid choice. You can only choose from the menu.")

        input("\nPress enter to continue...")

if __name__ == "__main__":
    main()
