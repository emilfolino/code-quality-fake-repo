"""Ska innehålla koden för att starta programmet"""
import marvin
import inventory
import emission_functions as EF


penguin_image = r"""
             . --- .
           /        \
          |  O  _  O |
          |  ./   \. |
          /  `-._.-'  \
        .' /         \ `.
    .-~.-~/           \~-.~-.
.-~ ~    |             |    ~ ~-.
`- .     |             |     . -'
     ~ - |             | - ~
         \             /
       ___\           /___
       ~;_  >- . . -<  _i~
          `'         `'
"""

def main():
    """Funktion för menyval, kallar på andra funktioner"""  
    bag = []
    while True:
        print(chr(27) + "[2J" + chr(27) + "[;H")
        print(penguin_image)

        # Menyval #
        print("Hi, I'm a penguin. I know it all. What can I do you for?")
        print("1) Present yourself to the penguin.")
        print("2) Convert Celcius to Farenheit")
        print("3) Let's play parrot!")
        print("4) I'll count for you!")
        print("5) Wanna see something annoying?")
        print("6) Have you heard about isograms?")
        print("7) Do you want me to compare numbers?")   
        print("a1) Do you want me to compare strings?")
        print("a2) I can double your value, many times!")
        print("a3) Wanna see me replace tab with spaces?")
        print("a4) Do a Brangelina with any names!")
        print("a5) I can help you count your score!")
        print("8) Let's shuffle a word!")
        print("9) Let's do an acronym!")
        print("10) Let's mask a string!")
        print("11) Find a substring!")
        print("b1) Points to grade")
        print("b2) has_strings")
        print("q) Quit.")
        print(" NEW ")
        print("Try out my 'inv' commands!")
        print("a) inv")
        print("b) inv pick [thing] [position]")
        print("c) inv drop [thing]")
        print("d) inv swap [thing1] [thing2]")
        print(" NEW ")
        print("12) See if the country is in the database")
        print("13) How much the emissions have changed?")
        print("14) See all data for the country")

        choice = input("--> ")

        if choice == "q":
            print("Bye, bye - and welcome back anytime!")
            break

        # Menyval Marvin 1 #
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

        # Extrauppgifter Marvin 1 #
        elif choice == "a1":
            marvin.letter_in_word()

        elif choice == "a2":
            marvin.something()

        elif choice == "a3":
            marvin.replace_tab()

        elif choice == "a4":
            marvin.brangelina()

        elif choice == "a5":
            marvin.game_sum()

        # Menyval Marvin 2 #
        elif choice == "8":
            word = input("Skriv ett ord: ")
            print(marvin.randomize_string(word))

        elif choice == "9":
            sentence = input("Skriv flera ord som börjar med stor bokstav: ")
            print(marvin.get_acronym(sentence))  

        elif choice == "10":
            mask = input("Skriv in nåt att maskera: ")
            print(marvin.mask_string(mask))

        elif choice == "11":
            long = input("Skriv in en sträng: ")
            short = input("Skriv in den substräng du vill hitta: ")
            print(marvin.find_all_indexes(long, short))

        # Extrauppgifter Marvin 2 #
        elif choice == "b1":
            maxpoints = input("Vad är maxpoängen? ")
            points = input("Hur många poäng fick du? ")
            print(marvin.points_to_grade(maxpoints, points))  

        elif choice == "b2":
            compare = input("Skriv in en sträng: ")
            start = input("Kolla om strängen börjar med: ")
            contain = input("Kolla om strängen innehåller: ")
            ends = input("Kolla om strängen slutar med: ")
            print(marvin.has_strings(compare, start, contain, ends))

        # Menyval Marvin 3 #
        #elif choice == "inv":
        #    inventory.inventory(bag)

        elif choice.startswith("inv pick"):
            pick_list = choice.split(" ")
            thing = pick_list[2]
            if len(pick_list) > 3:
                bag = inventory.pick(bag, thing, pick_list[3])
            else:
                bag = inventory.pick(bag, thing)

        elif choice.startswith("inv drop"):
            drop_list = choice.split(" ")
            thing = drop_list[2]
            bag = inventory.drop(bag,thing)


        elif choice.startswith("inv swap"):
            swap_list = choice.split(" ")
            first = swap_list[2]
            second = swap_list[3]
            bag = inventory.swap(bag, first, second)
           
        elif choice.startswith("inv"):
            start = 0
            stop = 0 
            if len(choice) > 3:
                start = int(choice[4])
                stop = int(choice[6])
            inventory.inventory(bag, start, stop)  

        # Marvin kmom05

        elif choice == "12":
            search_word = input("Enter the country name: ")
            try:
                countr = EF.search_country(search_word)
                countries = ", ".join(countr)
                print("Following countries were found: " + countries)
            except ValueError:
                print("Country does not exist!")

                
        elif choice == "13":
            s_word = input("Enter the country,year1,year2. No spaces: ")
            search_word = s_word.split(",")
            country = EF.search_country(search_word[0])[0]
            year1 = search_word[1]
            year2 = search_word[2]
            if year1 not in ["1990","2005","2017"] or year1 not in ["1990","2005","2017"]:
                print("Wrong year!")
            else:
                try:
                    change = EF.get_country_change_for_years(country, year1, year2)
                    print(country + ":" + str(change) + "%")
                except ValueError:
                    print("Wrong year!")
            

        elif choice == "14":
            country = input("Enter the country: ")
            country_dict = EF.get_country_data(country)
            EF.print_country_data(country_dict)

        elif choice == "e1":
            year_number = input("Which year? And how many countries?")
            y_no = year_number.split(" ")
            year = y_no[0]
            no = 1
            if len(y_no) > 1:
                no = int(y_no[1])
            EF.top_emission(year,no)

        elif choice == "e2":
            year_number = input("Which year? And how many countries?")
            y_no = year_number.split(" ")
            year = y_no[0]
            no = -1
            if len(y_no) > 1:
                no = int(y_no[1])
            EF.emission_per_capita(year, no)

        elif choice == "e3":
            year_number = input("Which year? And how many countries?")
            y_no = year_number.split(" ")
            year = y_no[0]
            no = -1
            if len(y_no) > 1:
                no = int(y_no[1])
            EF.emission_per_area(year, no)

        # RÖR EJ:
        else:
            print("That is not a valid choice. You can only choose from the menu.")

        input("\nPress enter to continue...")
    

if __name__ == "__main__":
    main()
