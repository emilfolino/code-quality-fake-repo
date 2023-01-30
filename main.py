""" this is main"""
import marvin
import inventory
import emission_functions as eFunc

myBackpack = []

def main():
    """ Main function """
    
    # while True:
    #     eFunc.GetIdByName("Sweden")
    global myBackpack
    while True:
        marvin.menu()
        try:
            choice = input("--> ")
        except ValueError as e:
            print(e.__cause__, e.__annotations__)
            print("Choose a option")
            continue
        lista = inventory.SplitInputIntoList(choice)
        print(lista)

        if choice == "13":
            print("Type a country")
            string = input("--> ")
            lista = inventory.SplitInputIntoList(string)
            try:
                print(eFunc.get_country_change_for_years_str(
                    lista[0], lista[1], lista[2]))
            except Exception:
                print("Wrong year!")
        elif choice == "14":
            print("Type a country")
            string = input("--> ")
            eFunc.print_country_data(eFunc.get_country_data(string))
        elif choice == "12":
            try:
                print("Search for a country")
                string = input("--> ")
                print(eFunc.search_country(string))
            except ValueError:
                print("Country does not exist!")
        elif "inv" in lista and "pick" in lista:
            if len(lista) == 3:
                myBackpack = inventory.pick(myBackpack, lista[2])
            elif len(lista) == 4:
                myBackpack = inventory.pick(myBackpack, lista[2], lista[3])
        elif "inv" in lista and "drop" in lista:
            if len(lista) == 3:
                myBackpack = inventory.drop(myBackpack, lista[2])
        elif "inv" in lista and "swap" in lista:
            if len(lista) == 4:
                myBackpack = inventory.swap(myBackpack, lista[2], lista[3])
        elif choice == "inv":
            inventory.inventory(myBackpack)
        elif choice == 'q':
            marvin.goodbye()
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
            print("Type a string")
            string = input("--> ")
            print(marvin.randomize_string(string))
        elif choice == "9":
            print("Type a string")
            string = input("--> ")
            print(marvin.get_acronym(string))
        elif choice == "10":
            print("Type a string")
            string = input("--> ")
            print(marvin.mask_string(string))
        elif choice == "11":
            print("Type a string")
            string1 = input("--> ")
            print("Type another string")
            string2 = input("--> ")
            print(marvin.find_all_indexes(string1, string2))
        else:
            print("That is not a valid choice. You can only choose from the menu.")
        input("\nPress enter to continue...")
        continue


if __name__ == '__main__':
    main()
