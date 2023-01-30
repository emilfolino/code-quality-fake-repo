"""Main"""

import marvin
import inventory
import emission_functions


inv = []

def main():
    """Main Function"""
    global inv 


    while True:
        choice = marvin.menu_choice()
        
        if choice[0] == "q":
            break

        elif choice[0] == "1":
            marvin.greet()
            marvin.press_enter_to_continue()

        elif choice[0] == "2":
            marvin.celcius_to_farenheit()
            marvin.press_enter_to_continue()

        elif choice[0] == "3":
            marvin.word_manipulation()
            marvin.press_enter_to_continue()
        
        elif choice[0] == "4":
            marvin.sum_and_average()
            marvin.press_enter_to_continue()
        
        elif choice[0] == "5":
            marvin.hyphen_string()
            marvin.press_enter_to_continue()
        
        elif choice[0] == "6":
            marvin.is_isogram()
            marvin.press_enter_to_continue()
        
        elif choice[0] == "7":
            marvin.compare_numbers()
            marvin.press_enter_to_continue()    
        
        elif choice[0] == "a1":
            marvin.contains_letters()
            marvin.press_enter_to_continue()

        elif choice[0] == "8":
            rand_string = input("Enter a string to randomize: ")
            print(marvin.randomize_string(rand_string))
            marvin.press_enter_to_continue()

        elif choice[0] == "9":
            acronym_string = input("Enter a phrase to extract an acronym: ")
            print(marvin.get_acronym(acronym_string))
            marvin.press_enter_to_continue()

        elif choice[0] == "10":
            unmasked_str = input("Enter a string to mask: ")
            print(marvin.mask_string(unmasked_str))
            marvin.press_enter_to_continue()

        elif choice[0] == "11":
            index_str = input("Enter a string: ")
            index_sub_str = input("Enter a sub-string of your previous input: ")
            
            print(marvin.find_all_indexes(index_str, index_sub_str))
            marvin.press_enter_to_continue()

        elif choice[0] == "inv":
            if len(choice) == 1:
                inventory.inventory(inv, 0, len(inv))
            elif choice[1].isdigit() and choice[2].isdigit():
                inventory.inventory(inv, choice[1], choice[2])

            elif choice[1] == "pick":
                if len(choice) == 4:
                    inv = inventory.pick(inv, choice[2], choice[3])
                elif len(choice) == 3:
                    inv = inventory.pick(inv, choice[2])
            
            elif choice[1] == "drop":
                inv = inventory.drop(inv, choice[2])
                
            elif choice[1] == "swap" and len(choice) == 4:
                inv = inventory.swap(inv, choice[2], choice[3])

            else:
                print("That is not a valid inventory command, try again")

            marvin.press_enter_to_continue()

        elif choice[0] == "12":
            search_word = input("Enter a string to search using: ")
            try :
                found_countries = emission_functions.search_country(search_word)
                foundcountries_str = ""
                for i in found_countries:
                    foundcountries_str += f"{i},"
                print(f"Following countries were found: {foundcountries_str[:-1]}")

            except ValueError :
                print("Country does not exist!")

            marvin.press_enter_to_continue()

        elif choice[0] == "13":
            (country, year1, year2) = input(
                "Enter the country and 2 years you wish to compare is a CSV list: ").split(",")
            try :
                co2_change = emission_functions.get_country_change_for_years(country, year1, year2)
                print(f"{country}:{co2_change}%")
            except ValueError:
                print("Wrong year!")
            marvin.press_enter_to_continue()

        elif choice[0] == "14":
            country_input = input("Input: ")
            emission_functions.print_country_data(emission_functions.get_country_data(country_input))
            marvin.press_enter_to_continue()
        
        elif choice[0] == "e1":
            sort_co2 = input("Enter a year and how many countries to list: ").split()
            if len(sort_co2) == 2:
                emission_functions.sorted_co2(sort_co2[0], sort_co2[1])
            else:
                emission_functions.sorted_co2(sort_co2[0])
            marvin.press_enter_to_continue()

        elif choice[0] == "e2":
            sort_per_capita = input("Enter a year and how many countries to list: ").split()
            if len(sort_per_capita) == 2:    
                emission_functions.sorted_per_capita(sort_per_capita[0], sort_per_capita[1])
            else:
                emission_functions.sorted_per_capita(sort_per_capita[0])

            marvin.press_enter_to_continue()

        elif choice[0] == "e3":
            sort_land = input("Enter a year and how many countries to list: ").split()
            if len(sort_land) == 2:    
                emission_functions.sorted_land(sort_land[0], sort_land[1])
            else:
                emission_functions.sorted_land(sort_land[0])

            marvin.press_enter_to_continue()    

        elif not choice[0].isdigit() or int(choice[0]) > 14:
            print("That is not a valid choice. You can only choose from the menu.")
            marvin.press_enter_to_continue()





if __name__ == "__main__":
    main()
