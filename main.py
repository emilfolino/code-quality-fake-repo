"""
All functions to marvin
"""

import inventory
import marvin
import emission_functions

marvin_image = r"""
     ·___·
    |o   o|
     \ ' /
      |¯| 
 /¯|¯¯¯|¯ ¯|¯\
 | |___|___| |
 | |\__|__/| |
 |_| |_|_| |_|
  ¥  |_|_|  ¥
   /¯|···|¯\
   | |   | |
   |_|   |_|
   |¯|   |¯|
   | |   | |
   |_|   |_|
   / \   / \
  (>.<) (>.<)
"""


def main():
    """
    startar marvin chatbot
    """
    backpack_list:list = []
    invstarter = "inv"

    while True:
        print(chr(27) + "[2J" + chr(27) + "[;H")
        print(marvin_image)
        print("Hi, I'm Marvin. I know it all. What can I do you for?")
        print("1) Present yourself to Marvin.")
        print("2) Temperature converter")
        print("3) Word multiplier")
        print("4) Number adder")
        print("5) Word enhancer :)")
        print("6) Isogram checker")
        print("7) Bigger,smaller or same")
        print("8) Random string")
        print("9) Acronym maker")
        print("10) String masker")
        print("11) Index finder")
        print("12) Country searcher")
        print("13) Country emission")
        print("14) Country info")
        print("b1) Grade checker")
        print("b2) String checker")
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
            og_string = input("Enter a string to randomize\n")
            print(marvin.randomize_string(og_string))

        elif choice == "9":
            string = input("Type something!\n")
            print(marvin.get_acronym(string))

        elif choice == "10":
            number_string = input("Type some numbers and I shall"
                                " mask all digits except the last four!\n")
            print(marvin.mask_string(number_string))

        elif choice == "11":
            string1 = input("Type something\n")
            find_me = input("Type something you want to find the index of!\n")
            print(marvin.find_all_indexes(string1,find_me))
        
        elif choice == "12":
            try:
                country_search = input("What country are you looking for?")
                str_of_countries = ", ".join(map(str,emission_functions.search_country(country_search)))
                print("Following countries were found : " + str_of_countries)
            except ValueError as e:
                print(str(e))
        
        elif choice == "13":
            try:
                country_emissions = input("Type in a country, a year and a second year "
                "Example: (Sweden,2005,2017)"
                " (years to pick from: 1990, 2005, 2017)\n")
                arguments_country_emission = country_emissions.split(",")
                print(arguments_country_emission[0] + ":"+ str(emission_functions.get_country_change_for_years
                (arguments_country_emission[0],
                arguments_country_emission[1],
                arguments_country_emission[2])) + "%")
            except ValueError as e:
                print(str(e))
            except TypeError as d:
                print(str(d))
            except IndexError:
                print("You did not type anything or missed one or two arguments!")

        elif choice == "14":
            country_info = input("Type a country you want info about!\n")
            try:
                emission_functions.print_country_data(emission_functions.get_country_data(country_info))
            except TypeError as x:
                print(str(x))
            

        elif choice == "b1":
            max_points = input("please type in the maximum points you could get\n")
            your_points = input("please type in your points\n")
            print(marvin.points_to_grade(max_points,your_points))

        elif choice == "b2":
            print("This is a string checker! First you type the string you want to check, "
                "then the string you think it starts with, then something the string contins "
                "and finally the thing it ends with!")
            string = input("Type something\n")
            string_first = input("Type something\n")
            string_contain = input("Type something\n")
            string_end = input("Type something\n")
            print(marvin.has_strings(string, string_first, string_contain, string_end))

        
        elif choice.startswith(invstarter):
            object1 = choice.split()
            if "pick" in choice:
                try:
                    inventory.pick(backpack_list ,object1[2], object1[3])
                except IndexError:
                    inventory.pick(backpack_list ,object1[2])
            elif "drop" in choice:
                inventory.drop(backpack_list, object1[2])
            elif "swap" in choice:
                try:
                    inventory.swap(backpack_list, object1[2], object1[3])
                except IndexError:
                    print("error: You did not write anything after swap or only wrote one object")
            else:
                try:
                    inventory.inventory(backpack_list, object1[1], object1[2])
                except IndexError:
                    inventory.inventory(backpack_list)
            


        else:
            print("That is not a valid choice. You can only choose from the menu.")

        input("\nPress enter to continue...")


    

if __name__ == "__main__":
    main()
    