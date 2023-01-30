"""Modul som anropar funktioner"""
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import marvin
import inventory
import emission_functions
import emission_data

"""
Marvin with a simple menu to start up with.
Marvin doesnt do anything, just presents a menu with some choices.
You should add functinoality to Marvin.
"""
bag =[]

def main ():
    """chattrobot som kan svara på frågor"""
    marvin_image = r"""
            .--.
    ::\`--._,'.::.`._.--'/::::
    ::::.  ` __::__ '  .::::::
    ::::::-:.`'..`'.:-::::::::
    ::::::::\ `--' /::::::::::

    """

    """
    Its an eternal loop, until q is pressed.
    It should check the choice done by the user and call a appropriate
    function.
    """
    
    while True:
        print(chr(27) + "[2J" + chr(27) + "[;H")
        print(marvin_image)
        print("Hi, I'm Yoda. I know it all. Your path you must decide.")
        print("1) Present yourself to Yoda.")
        print("2) Convert Celsius to Fahrenheit")
        print("3) Your favorite word")
        print("4) All about the numbers")
        print("5) Transforming words")
        print("6) I know all about isograms")
        print("7) Big or small")
        print("8) Random words")
        print("9) Akronym create")
        print("10) Strings and masks")
        print("11) Index")
        print("12) Search for country")
        print("13) Show emission change for a country")
        print("14) Show all data for a country")
        print("q) Quit.")
        
        choice = input("--->: ")
            
            


        if choice == "q":
            print("Farewell")
            break

        elif choice == "1":
            marvin.greet()

        elif choice == "2":
            marvin.celcius_to_farenheit()

        elif choice == "3":
            marvin.word_manipulation()

        #Summa och medel: Marvin ska fråga efter tal tills du skriver “done” 
        # och sedan ska Marvin skriva ut en sträng som skall innehålla summan och medelvärdet för dessa tal.
        #  Avrunda dina värden till två decimaler. Exempel #

        elif choice == "4":
            marvin.sum_and_average()
            
        
        # Marvin ska fråga efter en sträng och skriva ut en ny
        # sträng där varje karaktär har ökat med +1 och är separerad med “-“. 

        elif choice == "5":
            marvin.hyphen_string()

        #Menyval 6: Gör så Marvin kan kolla om ett ord är ett isogram. 
        # Ett ord är ett isogram om det inte innehåller några återupprepande bokstäver, 
        # både i följd och icke i följd. Det är OK om den är case-sensitive, a != A. 

        elif choice == "6":
            marvin.is_isogram()

        # Frågar efter tal och för varje tal angivet så ska Marvin skriva ut “larger!”
        #  om det nya talet är större, “smaller!” om mindre
        #Första gången = 2 tal
        # Om inget tal = not a number!"
        elif choice == "7":
            marvin.compare_numbers()

        elif choice == "8":
            for_random_word = input("Enter a string to randomize: ")
            rand = marvin.randomize_string(for_random_word)
            print(rand)

        elif choice == "9":
            input_word = input("Give me a string: ")
            new_word = marvin.get_acronym(input_word)
            print(new_word)

        elif choice == "10":
            string = input("Give me numbers for your password: ")
            news_word = marvin.mask_string(string)
            print(news_word)

        elif choice == "11":
            long_word = input("Give me a sentence")
            short_word = input("Give me someting from the sentence")

            new_word1 = (marvin.find_all_indexes(long_word, short_word))
            print(new_word1)
        


        elif choice == "12":
            search_word = input("give me a country to se if its in my list: ")
            list_1 = []
            try:
                list_1 = emission_functions.search_country(search_word)
                print(list_1)
            except ValueError:
                print("Country does not exist!")

            

        elif choice == "13":
            try:
                input_1 = input("Give me a country and two years: ")
                checking_variables = input_1.split(",")
                country = checking_variables[0]
                number_of_inputs = len(checking_variables)
                if country == "":
                    raise ValueError("You have to write something!")
                try:
                    if number_of_inputs == 3:
                        year1 = checking_variables[1]
                        year2 = checking_variables[2]
                        change_in_gas = emission_functions.get_country_change_for_years(country, year1, year2)
                        print(str(country) + ":" + str(change_in_gas) + "%")

                    else:
                        raise ValueError("Wrong year!")

                except Exception:
                    print("Wrong year!")
                    
    
            except ValueError:
                print("Wrong year!")
            

                
            




        elif choice == "14":
            country = input("What country?")
            
            try:
                if country in emission_data.country_data:
                    final_result = 0
                    final_result = emission_functions.get_country_data(country)
                    emission_functions.print_country_data(final_result)
                    
                    
                else:
                    print("Wrong country!")

            except ValueError:
                print("Country does not exist!")

            

        elif "inv pick" in choice:
            try:
                new_inv = choice.split()
                new_inv1 = new_inv[2]
                try:
                    rand = new_inv[3]
                except IndexError:
                    pass
                insert_list = "".join(new_inv1)
                
                inventory.pick(bag, insert_list, rand = -1)
            except TypeError:
                print("Sorry, not working in list " + str(bag))
            except IndexError:
                print("Sorry, not working in list " + str(bag))
                

        elif "inv drop" in choice:
            try:
                inventory.drop(bag, choice)
            except IndexError:
                print("Error, the backpack is " + str(bag))
            except TypeError:
                print("Error, the backpack is " + str(bag))

        
            
        elif "inv swap" in choice:
            try:
                new_inv = choice.split()
                word1 = new_inv[2]
                word2 = new_inv[3]
                inventory.swap(bag, word1, word2)
            
            except IndexError:
                print("Error, the backpack is " + str(bag) + word1 + word2 + " is non-existing")
            except TypeError:
                print("Error, the backpack is " + str(bag) + word1 + word2 + " is non-existing")

        elif choice == "inv":
            try:
                if str(choice) == str("inv"):
                    inventory.inventory(bag)
                else:
                    print("Error, not valid " + str(bag))
            except TypeError:
                print("Error, the backpack is " + str(bag) + " is non-existing")
        
        else:
            continue

        input("\nPress enter to continue...")

if __name__ == "__main__":
    try:
        main()
    except ValueError:
        print("Wrong year!")
