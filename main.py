
"""
Marvin with a simple menu to start up with.
Marvin doesnt do anything, just presents a menu with some choices.
You should add functinoality to Marvin.
"""

import marvin
import inventory
import emission_functions

"""
Its an eternal loop, until q is pressed.
It should check the choice done by the user and call a appropriate
function.
"""

def main():
    """
    A new main function to run marvin
    """

    bag = []
    while True:
        print(chr(27) + "[2J" + chr(27) + "[;H")
        print(marvin.marvin_image)
        print("Hej, Mitt namn är Elvis, Hur kan jag stå till tjänst?")
        print("1) Presentera dig själv.")
        print("2) Celsius till fahrenheit")
        print("3) Multiplicera ord")
        print("4) Summa och medelvärde")
        print("5) Bokstavsförökning")
        print("6) Kolla efter isogram")
        print("7) Större eller mindre")
        print("8) Kasta om en sträng")
        print("9) Skapa en akronym")
        print("10) Maskera en sträng")
        print("11) Hitta alla index")
        print("12) Sök efter ett land")
        print("13) Sök på länders utsläpp")
        print("14) Skriv ut information om ett land") 
        print("q) Avsluta.")


        choice = input("Välj en av menyerna: ")
        if choice == "q":
            print("Bye bye")
            break

        elif choice == "1":
            marvin.greet()

        elif choice == "2":
            marvin.celsius_to_fahrenheit()

        elif choice == "3":
            word = input("Skriv ett ord: ")
            number = input("Skriv ett nummer: ")
            print(marvin.multiply_str(word, number))
        
        elif choice == "4":
            marvin.sum_and_average()
        
        elif choice == "5":
            marvin.hyphen_string()

        elif choice == "6":
            marvin.is_isogram()

        elif choice == "7":
            marvin.compare_numbers()

        elif choice == "8":
            random_str = input("Skriv något här: ")
            print(marvin.randomize_string(random_str))

        elif choice == "9":
            acro = input("Skriv in en sträng: ")
            print(marvin.get_acronym(acro))

        elif choice == "10":
            word = input("Skriv ett ord: ")
            print(marvin.mask_string(word))

        elif choice == "11":
            index1 = input("Skriv en sträng: ")
            index2 = input("Skriv en substräng: ")
            print(marvin.find_all_indexes(index1, index2))

        elif choice.startswith("inv pick"):
            choice = choice.split(" ")
            if len(choice) == 3:
                item = choice[2]
                indx = len(bag)
                bag = inventory.pick(bag, item, indx)

            elif len(choice) == 4:
                item = choice[2]
                indx = int(choice[3])
                bag = inventory.pick(bag, item, indx)

        elif choice == "inv":
            inventory.inventory(bag)

        elif choice.startswith("inv drop"):
            choice = choice.split(" ")
            item = choice[2]
            bag = inventory.drop(bag, item)

        elif choice.startswith("inv swap"):
            choice = choice.split(" ")
            item1 = choice[2]
            item2 = choice[3]
            bag = inventory.swap(bag, item1, item2)

        elif choice == "12":
            search = input("Sök efter ett land: ")
            try:
                print(emission_functions.search_country(search))
            except ValueError as e:
                print(str(e))

        elif choice == "13":
            
            search_year = input("Sök efter land och år 1990, 2005 eller 2017: ")
            search_year = search_year.split(",")
            try:
                if len(search_year) == 2:
                    print(emission_functions.get_country_year_data_megaton(search_year[0], search_year[1]))
                elif len(search_year) == 3:
                    print(search_year[0] + ":" + str(emission_functions.get_country_change_for_years(
                        search_year[0], search_year[1], search_year[2])) + "%")
            except ValueError as e:
                print(str(e))

        elif choice == "14":
            search = input("Sök efter ett land: ")
            get_data = emission_functions.get_country_data(search)
            emission_functions.print_country_data(get_data)

        else:
            print("That is not a valid choice. You can only choose from the menu.")

        input("\nPress enter to continue...")

if __name__ == "__main__":
    main()
