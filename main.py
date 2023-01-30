"""main file for running the marvin bot"""
import marvin as calls
import inventory as inv
import emission_functions as emfu

backpack = []

def main():
    """
    Its an eternal loop, until q is pressed.
    It should check the choice done by the user and call a appropriate
    function.
    """
    while True:
        print(chr(27) + "[2J" + chr(27) + "[;H")
        print(calls.marvin_image)
        print("Hi, I'm Snoop. I know it all. What can I do you for?")
        print("1) Present yourself to Marvin.")
        print("2) Convert Celsius to Fahrenheit.")
        print("3) word-multiplication")
        print("4) sum and medel*")
        print("5) hphen a string")
        print("q) Quit.")

        choice = input("--> ")

        if choice == "q":
            print("Bye, bye - and welcome back anytime!")
            break

        elif choice == "1":
            calls.greet()

        elif choice == "2":
            calls.celcius_to_farenheit()

        elif choice == "3":
            calls.word_manipulation()
        
        elif choice == "4":
            calls.sum_and_average()

        elif choice == "5":
            calls.hyphen_string()
        
        elif choice == "6":
            calls.is_isogram()
    
        elif choice == "7":
            calls.compare_numbers()

        elif choice == "8":
            choice8 = input("Enter a string to randomize: ")
            print(calls.randomize_string(choice8))

        elif choice == "9":
            choice9 = input("Enter a string to acronymize?: ")
            print(calls.get_acronym(choice9))

        elif choice == "10":
            choice10 = input("Enter a string to mask: ")
            print(calls.mask_string(choice10))

        elif choice == "11":
            choice11a = input("Enter a string to indexize: ")
            choice11b = input("Enter the substring to use ofr the indexzation: ")

            print(calls.find_all_indexes(choice11a, choice11b))
        elif choice == "12":
            
            choice12 = input("Enter a country to search for: ")
            try:
                print(emfu.search_country(choice12))
            except ValueError:
                print("Country does not exist!")
        elif choice == "13":
            l = input("Enter country,year,year: ").split(",")
            try:
                print(l[0] + ":" + str(emfu.get_country_change_for_years(l[0], l[1], l[2])) + "%")
            except ValueError:
                print("Wrong year!")
        elif choice == "14":
            choice14 = input("Enter a country to access the data for: ")
            emfu.print_country_data(emfu.get_country_data(choice14))
        #inventory stuff
        elif "inv pick" in choice:
            pickl = choice.split()
            picka = pickl[2]
            if len(pickl) == 4:
                pickb = pickl[3]
                inv.pick(backpack, picka, pickb)
            else:
                inv.pick(backpack, picka)
        elif choice == "inv":
            inv.inventory(backpack)
        elif "inv drop" in choice:
            dropl = choice.split()
            dropItem = dropl[2]
            inv.drop(backpack, dropItem)
        elif "inv swap" in choice:
            swapl = choice.split()
            swap1 = swapl[2]
            swap2 = swapl[3]
            inv.swap(backpack, swap1, swap2)
        else:
            print("That is not a valid choice. You can only choose from the menu.")

        input("\nPress enter to continue...")

if __name__ == '__main__':
    main()
    