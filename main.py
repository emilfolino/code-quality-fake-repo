"""
Main module of the marvin program
"""
import marvin

import inventory

import emission_functions

marvin_image = r"""
	
           ,-.
       ,--' ~.).
     ,'         `.
    ; (((__   __)))
    ;  ( (#) ( (#)
    |   \_/___\_/|
   ,"  ,-'    `__".
  (   ( ._   ____`.)--._        _
   `._ `-.`-' \(`-'  _  `-. _,-' `-/`.
    ,')   `.`._))  ,' `.   `.  ,','  ;
  .'  .     `--'  /     ).   `.      ;
 ;     `-        /     '  )         ;
 \                       ')       ,'
  \                     ,'       ;
   \               `~~~'       ,'
    `.                      _,'
      `.                ,--'
        `-._________,--'

"""

def main():
    """
    main loop of the program
    """
    backpack = []
    while True:
        print(chr(27) + "[2J" + chr(27) + "[;H")
        print(marvin_image)
        print("Hi, I'm Patric, Oh , I mean Quack quack.")
        print("1) Present yourself to Patric.")
        print("2) Celius to fahrenheit.")
        print("3) Multiply a word")
        print("4) Sum and average of numbers.")
        print("5) Increase characters by +1 and seperate with -")
        print("6) Check if a word is an isograms.")
        print("7) Larger or Smaller?")
        print("8) Randomize a string.")
        print("9) Get an acronym of a word.")
        print("10) Mask a string.")
        print("11) Indexify a word.")
        print("-----------------------------------------------------")
        print("12) Search for nations in carbon-list")
        print("13) Look up a nations difference in emissions")
        print("14) Search for a nations emission data")
        print("-----------------------------------------------------")
        print("a1) Check if characters are present in a word.")
        print("a2) Double a value until every number is present.")
        print("a3) Replace tab with three spaces.")
        print("a4) Combine two words into a new and imoroved name.")
        print("a5) Count points to different players.")
        print("-----------------------------------------------------")
        print("b1) Turn points into grade.")
        print("b2) Check if three string are in one word.")
        print("-----------------------------------------------------")
        print("e1) Get the amount of emissions of nations")
        print("e2) Get the amount of emissions per capita")
        print("e3) Get the amount of emissions per area")
        print("---------------")
        print("\n" + "q) Quit. \n")

        choice = input("--> ")

        #kmom02-03
        if choice == "q":
            print("Bye, bye - and welcome back anytime!")
            break
        if choice == "1":
            marvin.greet()
        elif choice== "2":
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
            inp = input("What word would you like to randomize? ")
            print(marvin.randomize_string(inp))
        elif choice == "9":
            inp = input("What word would you like to acronymize? ")
            print(marvin.get_acronym(inp))
        elif choice == "10":
            inp = input("What string would you like to mask?")
            print(marvin.mask_string(inp))
        elif choice == "11":
            inp1 = input("What word would you like to indexify? ")
            inp2 = input("What character would you like to index with? ")
            print(marvin.find_all_indexes(inp1,inp2))

        #Kmom 05    
        elif choice == "12":
            country = input("What would you like to search? ")
            try:
                tmp_list = emission_functions.search_country(country)
                tmp_string = ""
                for country in tmp_list:
                    tmp_string += f"{country}, "
                tmp_string = tmp_string[:-2]
                print(f"Following countries were found: {tmp_string}")
            except ValueError:
                print("Country does not exist!")
        elif choice == "13":
            inp = input("Write in following format: Country,Year,Year ")
            inp = inp.split(",")
            try:
                value = emission_functions.get_country_change_for_years(inp[0], int(inp[1]), int(inp[2]))
                print(f"{inp[0]}:{value}%")
            except ValueError as e:
                print(str(e))
        elif choice == "14":
            inp = input("What country would you like to examine? ")
            country_data = emission_functions.get_country_data(inp)
            emission_functions.print_country_data(country_data)

        #Extra assignments
        elif choice == "a1":
            marvin.word2_in_word()
        elif choice == "a2":
            marvin.multiply_x_times()
        elif choice == "a3":
            marvin.spaces_to_tab()
        elif choice == "a4":
            marvin.combine_names()
        elif choice == "a5":
            marvin.pointsheet_to_players()
        elif choice == "b1":
            max_pts = float(input("What was the maximum amount of points in the test? "))
            user_pts = float(input("What was your points? "))
            print(marvin.points_to_grade(max_pts, user_pts))
        elif choice == "b2":
            word = input("What is the full word? ") 
            inp_1 = input("First part: ")
            inp_2 = input("Second part: ")
            inp_3 = input("Third part: ")
            print(marvin.has_strings(word, inp_1, inp_2, inp_3))
        elif choice == "e1":
            inp = input("What year would you like to examine? ")
            inp = inp.split(" ")
            try:
                emission_functions.get_multiple_countries(int(inp[0]), int(inp[1]))
            except IndexError:
                emission_functions.get_multiple_countries(int(inp[0]))
            except ValueError as e:
                print(str(e))
        elif choice == "e2":
            inp = input("What year would you like to examine? ")
            inp = inp.split(" ")
            try:
                emission_functions.get_emission_per_capita(int(inp[0]), int(inp[1]))
            except IndexError:
                emission_functions.get_emission_per_capita(int(inp[0]))
            except ValueError as e:
                print(str(e))
        elif choice == "e3":
            inp = input("What year would you like to examine? ")
            inp = inp.split(" ")
            try:
                emission_functions.get_emission_per_area(int(inp[0]), int(inp[1]))
            except IndexError:
                emission_functions.get_emission_per_area(int(inp[0]))
            except ValueError as e:
                print(str(e))
        
                
        #Marvins Backpack
        elif choice.startswith("inv"):
            choice = choice.split(" ")
            if len(choice) == 1:
                inventory.inventory(backpack)
            elif choice[1].lstrip("-").isdigit() and choice[2].lstrip("-").isdigit():
                inventory.inventory(backpack, choice[1], choice[2])
            elif choice[1] == "pick":
                if len(choice) == 3:
                    backpack = inventory.pick(backpack, choice[2])
                else:
                    backpack = inventory.pick(backpack, choice[2], int(choice[3]))
            elif choice[1] == "drop":
                backpack = inventory.drop(backpack, choice[2])
            elif choice[1] == "swap":
                backpack = inventory.swap(backpack, choice[2], choice[3])
                
        else:
            print("That is not a valid choice. You can only choose from the menu.")

        input("\nPress enter to continue...")

if __name__ == "__main__":
    main()
