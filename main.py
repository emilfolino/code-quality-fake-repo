#
#Mainen
#

"""A dummy docstring."""

import marvin
import inventory
import emission_functions

def main():
    """A dummy docstring."""
    backpack = []
    while True:
        """
Marvin with a simple menu to start up with.
Marvin doesnt do anything, just presents a menu with some choices.
You should add functinoality to Marvin.
"""

        """
        Its an eternal loop, until q is pressed.
        It should check the choice done by the user and call a appropriate
        function.
        """
        print("Hi, I'm Marvin. I know it all. What can I do you for?")
        print("1) Present yourself to Marvin.")
        print("2) Wanna convert celcius to Fahrenheit?.")
        print("3) ordmultiplicering.")
        print("4) Summa n medelvärde.")
        print("5) Ordförlängaren.")
        print("6) Isogram-kollen.")
        print("7) large-small.")
        print("8) Kastar runt bokstäverna.")
        print("9) Skapar en akronym.")
        print("10) Multiplicerar och hashar.")
        print("11) find all indexes.")
        print("a1) Bokstavsjämförare")
        print("inv pick) inv pick")
        print("inv) visa hela inventoryn")
        print("inv drop) Kasta något")
        print("inv swap) byt något")
        print("12")
        print("13")
        print("14")
        print("q) Quit.")

        choice = input("--> ")
        #Skapar listan för ryggsäcken
        if choice == "q":
            result = marvin.quitter()
            if result:
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
            result = input("input word")
            print (marvin.randomize_string(result))
        elif choice == "9":
            result = input("Vad du vill akronyma")
            print (marvin.get_acronym(result))
        elif choice == "10":
            result = input("Skriv in ditt ord")
            print(marvin.mask_string(result))
        elif choice == "11":
            result = input("strängen")
            result1 = input("hitta index")
            print(marvin.find_all_indexes(result, result1))
        elif choice in ("A1","a1"):
            marvin.first_second()
        elif ("inv pick") in choice:
            x = choice.split(" ")
            the_thing = x[2]
            try:
                pos = x[3]
            except IndexError:
                pos = ""
            inventory.pick(backpack, the_thing, pos)
            print(backpack)

        elif choice in ("inv"):
            y = choice.split(" ")
            try:
                start = y[1]
                stop = y[2]
                inventory.inventory(backpack, start, stop)
            except IndexError:
                start = ""
                stop = ""
                inventory.inventory(backpack, start, stop)
        elif ("inv drop") in choice:
            y = choice.split(" ")
            saken = y[2]
            inventory.drop(backpack, saken)
        elif ("inv swap") in choice:
            y = choice.split(" ")
            saken = y[2]
            right = y[3]
            inventory.swap(backpack, saken, right)

        elif choice == "12":
            land_ord = input("vad söker du efter?")
            try:
                x = emission_functions.search_country(land_ord)
                print(x)
            except ValueError as e:
                print(str(e))

        elif choice == "13":
            land_ord = input("land, year,year")
            l = land_ord.split(",")
            try:
                p = emission_functions.get_country_change_for_years(l[0], l[1], l[2])
                print(l[0] + ":" + str(p) + "%")
            except ValueError as e:
                print(str(e))

        elif choice == "14":
            land_ord = input("vad söker du efter?")
            try:
                data = emission_functions.get_country_data(land_ord) 
                emission_functions.print_country_data(data)
            except ValueError as e:
                print(str(e))
        elif choice == "e1":
            land_ord = input("år, antal")
            y = land_ord.split(" ")
            try:
                data = emission_functions.high_emission(y[0], y[1])
                print(data)
            except ValueError as e:
                print(str(e))

        else:
            marvin.not_valid_choice()

        input("\nPress enter to continue...")


if __name__ == "__main__":
    main()
