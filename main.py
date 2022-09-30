#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
This is the Marvin chatbot version 2
"""

import marvin
import inventory
import emission_functions

def main():
    """ The main function. This is where the loop happens! """
    print(chr(27) + "[2J" + chr(27) + "[;H")
    print("                     Marv-inu is approaching, please make room for Marv-inu!")
    print("<----------------- Your terminal window needs to be at least this wide (100 chars) ----------------->")
    pre_menu_choice = marvin.press_enter()
    menu_text = "Hello, I'm Marv-inu the friendly doggo! I'm a good boi, I know many things! What do you want to do? \n"
    marvinu_bag = []
    run_marvinu = True

    while run_marvinu:
        pre_menu_flag = False
        if pre_menu_choice: # Om pylint försöker välja något i menyn innan menyn visas
            choice = pre_menu_choice
            pre_menu_choice = ""
            pre_menu_flag = True

        else:
            marvin.redraw_marvinu()
            print(menu_text)
            marvin.show_menu()

            choice = input("\n--> ")
            # redraw_marvinu("")

        if choice == "q":
            run_marvinu = marvin.quit_marvinu()

        elif choice == "1": # Present yourself to Marv-inu
            marvin.greet()

        elif choice == "2": # Convert temperatures
            marvin.celcius_to_farenheit()

        elif choice == "3": # Repeat words
            marvin.word_manipulation()

        elif choice == "4": # Calculate sum and average
            marvin.sum_and_average()

        elif choice == "5":
            marvin.hyphen_string()

        elif choice == "6":
            marvin.is_isogram()

        elif choice == "7":
            marvin.compare_numbers()

        elif choice == "a1":
            marvin.check_chars()

        elif choice == "a2":
            marvin.double_number()

        elif choice == "a3":
            marvin.replace_tabs()

        elif choice == "a4":
            marvin.combine_names()

        elif choice == "a5":
            marvin.count_points()

        elif choice == "a6":
            marvin.think_of_a_number()



        elif choice == "8":
            marvinu_input_request = "Give me a string and I'll randomize it for you!"
            marvinu_input_error_message = "Write a string of text please!"
            input_type = "string"
            string_to_randomize = marvin.get_user_input(marvinu_input_request, marvinu_input_error_message, input_type)
            marvinu_message = marvin.randomize_string(string_to_randomize)
            marvin.redraw_marvinu(marvinu_message)

        elif choice == "9":
            marvinu_input_request = "Write a String with Initial Capitals!"
            marvinu_input_error_message = "Write a String of Text with Initial Capitals Please!"
            input_type = "upper_lower"
            string_to_acronymize = marvin.get_user_input(marvinu_input_request, marvinu_input_error_message, input_type)
            marvinu_message = marvin.get_acronym(string_to_acronymize)
            marvin.redraw_marvinu(marvinu_message)


        elif choice == "10":
            marvinu_input_request = "Give me a string and I'll mask it all except the last 4 characters!"
            marvinu_input_error_message = "Write a string of text please!"
            input_type = "string"
            string_to_mask = marvin.get_user_input(marvinu_input_request, marvinu_input_error_message, input_type)
            marvinu_message = marvin.mask_string(string_to_mask)
            marvin.redraw_marvinu(marvinu_message)


        elif choice == "11":
            marvinu_input_request = "Give me a string of text!"
            marvinu_input_error_message = "Write a string of text please!"
            input_type = "string"
            string_to_search = marvin.get_user_input(marvinu_input_request, marvinu_input_error_message, input_type)

            marvinu_input_request = "Type one or more characters, "
            marvinu_input_request += "and I'll tell you at where they occur in your string of text!"
            marvinu_input_error_message = "Give me one or more characters please!"
            input_type = "string"
            chars_to_find = marvin.get_user_input(marvinu_input_request, marvinu_input_error_message, input_type)
            marvinu_message = marvin.find_all_indexes(string_to_search, chars_to_find)
            if not marvinu_message:
                marvinu_message = f"I can't find any {chars_to_find} in {string_to_search}!"
            marvin.redraw_marvinu(marvinu_message)

        elif choice == "12":
            marvinu_input_request = "Give me a string of text "
            marvinu_input_request += "and I'll find any countries whose names contain that string!"
            marvinu_input_error_message = "Write a string of text please!"
            input_type = "string"
            search_word = marvin.get_user_input(marvinu_input_request, marvinu_input_error_message, input_type)
            try:
                search_results = emission_functions.search_country(search_word)
                marvinu_message = ", ".join(search_results)
                marvin.redraw_marvinu(marvinu_message)
            except ValueError as ve:
                marvin.redraw_marvinu(ve)

        elif choice == "13":
            marvinu_input_request = "Choose a country and two years to compare, like this: Country,YYYY,YYYY"
            marvinu_input_error_message = "Write a comma separated string with a country and two years please!"
            input_type = ("comma_separated_string", 3)
            search_string = marvin.get_user_input(marvinu_input_request, marvinu_input_error_message, input_type)
            search_array = [stringpart.strip() for stringpart in search_string.split(",")]
            try:
                years_change = emission_functions.get_country_change_for_years(
                    search_array[0], search_array[1], search_array[2])
                marvinu_message = f"{search_array[0]}:{years_change}%"
                marvin.redraw_marvinu(marvinu_message)
            except ValueError as felmeddelande:
                marvin.redraw_marvinu(felmeddelande)

        elif choice == "14":
            marvinu_input_request = "Choose a country and I'll give you the emission data!"
            marvinu_input_error_message = "Write a comma separated string with a country and two years please!"
            input_type = ("string")
            search_string = marvin.get_user_input(marvinu_input_request, marvinu_input_error_message, input_type)
            try:
                country_data = emission_functions.get_country_data(search_string)
                emission_functions.print_country_data(country_data)
            except ValueError as felmeddelande:
                marvin.redraw_marvinu(felmeddelande)

        elif choice == "b1":
            marvinu_input_request = "What was the maximum score on the test?"
            marvinu_input_error_message = "Only numbers please! How many points was the max score?"
            input_type = "posint"
            max_score = marvin.get_user_input(marvinu_input_request, marvinu_input_error_message, input_type)

            marvinu_input_request = "How many points did you get?"
            marvinu_input_error_message = "Only numbers please! How many points did you get?"
            input_type = "number"
            your_points = marvin.get_user_input(marvinu_input_request, marvinu_input_error_message, input_type)
            marvinu_message = marvin.points_to_grade(max_score, your_points)
            marvin.redraw_marvinu(marvinu_message)

        elif choice == "b2":
            marvinu_input_request = "Give me a string of text!"
            marvinu_input_error_message = "Type some text please!"
            input_type = "string"
            string_1 = marvin.get_user_input(marvinu_input_request, marvinu_input_error_message, input_type)

            marvinu_input_request = "Give me another string of text!"
            string_2 = marvin.get_user_input(marvinu_input_request, marvinu_input_error_message, input_type)

            marvinu_input_request = "More! Give me another one!"
            string_3 = marvin.get_user_input(marvinu_input_request, marvinu_input_error_message, input_type)

            marvinu_input_request = "Yum! Just one more please!"
            string_4 = marvin.get_user_input(marvinu_input_request, marvinu_input_error_message, input_type)

            marvinu_message = marvin.has_strings(string_1, string_2, string_3, string_4)
            marvin.redraw_marvinu(marvinu_message)

        elif choice == "e1":
            marvinu_input_request = "Tell me what year of emissions to examine!"
            marvinu_input_request += "\n  If you want to limit the number of countries to list, write that number too!"
            marvinu_input_error_message = "Year (and number of countries to list) please!"
            input_type = "string"
            user_input_string = marvin.get_user_input(marvinu_input_request, marvinu_input_error_message, input_type)
            user_input_list = user_input_string.split(" ")
            year = user_input_list[0]
            try:
                limit = int(user_input_list[1])
            except IndexError:
                limit = None
            except ValueError:
                limit = ""

            try:
                emission_toplist = emission_functions.get_emission_toplist(year, limit)
            except ValueError as felmeddelande:
                marvin.redraw_marvinu(felmeddelande)
            except TypeError:
                felmeddelande = "Only numbers please!"
                marvin.redraw_marvinu(felmeddelande)
            if emission_toplist:
                marvin.redraw_marvinu(emission_functions.items_to_clean_str(emission_toplist))


        elif choice == "e2":
            marvinu_input_request = "Tell me what year of emissions to examine!"
            marvinu_input_request += "\n  If you want to limit the number of countries to list, write that number too!"
            marvinu_input_error_message = "Year (and number of countries to list) please!"
            input_type = "string"
            user_input_string = marvin.get_user_input(marvinu_input_request, marvinu_input_error_message, input_type)
            user_input_list = user_input_string.split(" ")
            year = user_input_list[0]
            try:
                limit = int(user_input_list[1])
            except IndexError:
                limit = None
            except ValueError:
                limit = ""

            try:
                emission_per_capita_list = emission_functions.get_emission_per_capita_list(year, limit)
                marvin.redraw_marvinu(emission_functions.items_to_clean_str(emission_per_capita_list))
            except ValueError as felmeddelande:
                marvin.redraw_marvinu(felmeddelande)
            except IndexError:
                felmeddelande = "Only numbers please!"
                marvin.redraw_marvinu(felmeddelande)


        elif choice[:3] == "inv":

            inv_list = choice.split()

            try:
                inv_start = int(inv_list[1])
                inv_end = int(inv_list[2])
            except (ValueError, IndexError):
                inv_start = ""
                inv_end = ""

            if len(inv_list) == 1:
                inventory.inventory(marvinu_bag)
            elif len(inv_list) == 3 and inv_start and inv_end:
                inventory.inventory(marvinu_bag, inv_list[1], inv_list[2])

            elif len(inv_list) in [3, 4, 5] and inv_list[1] in ["pick", "drop", "swap"]:
                try:
                    marvinu_bag = getattr(inventory, inv_list[1])(marvinu_bag, inv_list[2], inv_list[3], inv_list[4])
                except (IndexError, TypeError):
                    try:
                        marvinu_bag = getattr(inventory, inv_list[1])(marvinu_bag, inv_list[2], inv_list[3])
                    except (IndexError, TypeError):
                        marvinu_bag = getattr(inventory, inv_list[1])(marvinu_bag, inv_list[2])

            elif len(inv_list) == 2 and inv_list[1] in ["pick", "drop", "swap"]:
                marvinu_message = f"I can't {inv_list[1]} anything if you don't tell me what to {inv_list[1]}!"
                marvin.redraw_marvinu(marvinu_message)
            elif len(inv_list) < 6:
                marvinu_message = f"{inv_list[1]}? What's that?"
                marvin.redraw_marvinu(marvinu_message)
            else:
                marvinu_message = "Whoa! Too many words!"
                marvin.redraw_marvinu(marvinu_message)

        elif choice: # If user input is not menu option

            if not pre_menu_flag: # If menu has not yet been displayed
                menu_text = "Marv-inu says:\n What? No, choose something from the menu! \n"
            continue

        else: # If user presses enter with no input when the menu is displayed
            menu_text = "Marv-inu says:\n Choose something from the menu please! \n"
            continue

        if choice and choice != "q": # After every menu option except q
            menu_text = "Marv-inu says:\n That was fun! What do you want to do now? \n"
            pre_menu_choice = marvin.press_enter()


if __name__ == "__main__":
    main()
