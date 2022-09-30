"""
main.py for marvin3
"""

import marvin as m
import inventory as inv
import emission_functions as emi

marvin_image = r"""
                                    _
                                ,-"" "".
                              ,'  ____  `.
                            ,'  ,'    `.  `._
   (`.         _..--.._   ,'  ,'        \    \
  (`-.\    .-""        ""'   /          (  M _M
 (`._  `-"" ,._             (            `-(   \
 <_  `     (  <`<            \              `-._\
  <`-       (__< <           :
   (__        (_<_<          ;
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""

bag = []

def main():
    """ main """
    while True:
        print(chr(27) + "[2J" + chr(27) + "[;H")
        print(marvin_image)
        print(
    """Sup i'm Groos. I know e v e r y t h i n g.... What can I help you with?
    1) Present yourself to Groos.
    2) Convert Celsius to Farenheit.
    3) Make Groos repeat some words.
    4) Groos does simple addition.
    5) Repeat letters in a word.
    6) isogram check.
    7) Smaller? The same? Or bigger?!.
    8) Randomise string!
    9) Get Acronym.
    10) Mask string.
    11) Find all indexes in a string.
    12) Search for a country.
    13) Compare emissions.
    14) Print Country data.

    Inventory commands are still here!

    q) Quit.""")

        choice = input("--> ")

        inv_choice = choice.split()

        if choice == "q":
            print("Bye, bye - and welcome back anytime!")
            bag.clear()
            break

        elif choice == "1":
            m.greet()

        elif choice == "2":
            m.celcius_to_farenheit()

        elif choice == "3":
            m.word_manipulation()

        elif choice == "4":
            m.sum_and_average()

        elif choice == "5":
            m.hyphen_string()

        elif choice == "6":
            m.is_isogram()

        elif choice == "7":
            m.compare_numbers()

        elif choice == "8":
            s = input("Write a string and ill shuffle it: ")
            print(m.randomize_string(s))

        elif choice == "9":
            s = input("Achronym maker: ")
            print(m.get_acronym(s))

        elif choice == "10":
            s = input("Give me a string, preferably longer than 4 characters: \n")
            print(m.mask_string(s))

        elif choice == "11":
            s = input("Give me a string: ")
            s2 = input("Give me a character that exists in the string: ")
            print(m.find_all_indexes(s,s2))

        # Marvin 4 uppgifter
        elif choice == "12":
            s = input("Type country name: ")
            try:
                li = emi.search_country(s)
                print("I found these countries: " + ", ".join(li))
            except ValueError:
                print("Country does not exist!")

        elif choice == "13":
            s = input("'Country,year1,year2' (only 1990, 2005, 2017): ")
            s = s.split(",")

            if len(s) == 3:
                try:
                    x = emi.get_country_change_for_years(s[0], s[1], s[2])
                    print(s[0] + ":" + str(x) + "%")
                except ValueError:
                    print("Wrong year!")
            else:
                print("Wrong syntax")

        elif choice == "14":
            country = input("Name a country: ")
            try:
                data = emi.get_country_data(country)
                emi.print_country_data(data)
            except KeyError:
                print("Country does not exist!")

        #Inventory (lite o-effektiv)
        elif inv_choice[0] == "inv":
            if len(inv_choice) == 4:
                #4 arguments
                if inv_choice[1] == "pick":
                    inv.pick(bag, inv_choice[2], inv_choice[3])
                elif inv_choice[1] == "swap":
                    inv.swap(bag, inv_choice[2], inv_choice[3])
            elif len(inv_choice) == 3:
                #3 arguments
                if inv_choice[1] == "pick":
                    inv.pick(bag, inv_choice[2])
                elif inv_choice[1] == "drop":
                    inv.drop(bag, inv_choice[2])
            elif len(inv_choice) == 1:
                #1 argument
                inv.inventory(bag)


        #No option Check
        else:
            print("That is not a valid choice. You can only choose from the menu.")

        input("\nPress enter to continue...")

if __name__ == "__main__":
    main()
