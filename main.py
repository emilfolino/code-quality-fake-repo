# pylint: disable=C0305, C0114, R1722

import marvin
import emission_functions
"""Marvin import"""
def main():
    """Meny function"""
    while True:
        print(chr(27) + "[2J" + chr(27) + "[;H")
        print(marvin.turtle_image)
        print("Hello, Im the wise turle who never forgets. Please ask me anything")
        print("1) Engage the turle.")
        print("2) Seek knowlegde about Farenheit.")
        print("3) Word multiplier.")
        print("4) Test the turtles math skills.")
        print("5) Find out the numbers worth.")
        print("6) The word expander.")
        print("7) The Isogram finder.")
        print("8) Everyday I'm shuffling.")
        print("9) Anagram detector.")
        print("10) Acronym finder.")
        print("11) List filter.")
        print("12) List countries")
        print("13) Show emission data for countries")
        print("14) Show all data for a country")
        print("E1) Total CO2/Country")
        print("E2) CO2/Capita")
        print("E2) CO2/Area")
        print("inv) The turtles library")
        print("q) Run away in terror.")

        choice = input("-->")

        if choice == "q":
            print("Wise choice you weak mortal")
            break
        elif choice == "1":
            marvin.name()
        elif choice == "2": 
            marvin.farenheit()
        elif choice == "3":
            marvin.multiplier()
        elif choice == "4": 
            marvin.math()
        elif choice == "5": 
            marvin.worth()
        elif choice == "6": 
            marvin.expander()
        elif choice == "7": 
            marvin.isogram()
        elif choice == "8": 
            marvin.suffle()
        elif choice == "9":
            marvin.anagram()
        elif choice == "10":
            marvin.acronym()
        elif choice == "11":
            marvin.lister()
        elif choice == "12":
            try:
                choice = input("Enter search word: ")
                for x in emission_functions.search_country(choice):
                    print(x)
            except ValueError:
                print("Country does not exist!")
        elif choice == "13":
            choice = input("Enter country,year1,year2: ")
            search = choice.split(",")
            if(len(search) == 3):
                emission_functions.get_country_change_for_years(search[0], search[1], search[2])
            elif(len(search) == 2):
                for x in emission_functions.get_country_year_data_megaton(search[0], search[1]):
                    print(x[0], ": ", x[1])           
            else:
                print("Wrong input")
        elif choice == "14":
            choice = input("Country name: ")
            data = emission_functions.get_country_data(choice)
            emission_functions.print_country_data(data)
        elif "inv" in choice: 
            marvin.inv(choice)
        else:
            print("That is not a valid choice. You can only choose from the menu.")
        
        input("\nPress enter to continue...")

if __name__ == "__main__":
    main()
    exit()   


