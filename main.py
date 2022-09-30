
"""
marvin menu program

    """
import marvin
import inventory
import emission_functions
backpack = []
"""
import functions for marvin

    """
def main():
    """
main function

    """
    marvin_image = r"""
             ______/ ________ \______
           _/      ____________      \_
         _/____________    ____________\_
        /  ___________ \  / ___________  \
       /  /XXXXXXXXXXX\ \/ /XXXXXXXXXXX\  \
      /  /############/    \############\  \
      |  \XXXXXXXXXXX/ _  _ \XXXXXXXXXXX/  |
    __|\_____   ___   //  \\   ___   _____/|__
    [_       \     \  X    X  /     /       _]
    __|     \ \                    / /     |__
    [____  \ \ \   ____________   / / /  ____]
         \  \ \ \/||.||.||.||.||\/ / /  /
          \_ \ \  ||.||.||.||.||  / / _/
            \ \   ||.||.||.||.||   / /
             \_   ||_||_||_||_||   _/
               \     ........     /
                \________________/
    
    """

    while True:
        print(chr(27) + "[2J" + chr(27) + "[;H")
        print(marvin_image)
        print("Hi, I'm Marvin. I know it all. What can I do you for?")
        print("1) Present yourself to Marvin.")
        print("2) Celcius to Farenheit converter")
        print("3) You say it, ill repeat it")
        print("4) Need help with math?")
        print("5) Repeat letters in a word")
        print("6) Isogram")
        print("7) Larger, smaller or equal ?")
        print("8) Randomize")
        print("9) Acronyms")
        print("10) Mask input")
        print("11) Index")
        print("12) Search country")
        print("13) emission difference")
        print("14) country data")
        print("inv pick...")
        print("inv drop...")
        print("inv swap...")
        print("inv")
    
        print("q) Quit.")
        

        choice = input("--> ")

        if choice == "q":
            print("Bye, bye - and welcome back anytime!")
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
            word_input = input("Write a word: ")
            print(marvin.randomize_string(word_input))

        elif choice == "9": 
            name_input = input("Write a name: ")
            print(marvin.get_acronym(name_input))  

        elif choice== "10":
            string_input = input("Skriv in ditt nummer: ")
            print(marvin.mask_string(string_input))

        elif choice == "11":
            string = input("Skriv bokstäver: ")
            char_index =  input("skriv index som ska hittas: ") 
            print(marvin.find_all_indexes(string,char_index))
        
        elif "inv pick" in choice:
            commandlist = choice.split(" ")
            item = commandlist[2]
            try:
                pos = int(commandlist[3])
            except (IndexError, ValueError, TypeError):
                pos = -1
            inventory.pick(backpack,item,pos)
        
        elif choice == "inv":
            inventory.inventory(backpack)
        
        elif "inv drop" in choice:
            commandlist = choice.split(" ")
            item = commandlist[2]
            inventory.drop(backpack,item)
        
        elif "inv swap" in choice:
            commandlist = choice.split(" ")
            item = commandlist[2]
            item2 = commandlist[3]
            inventory.swap(backpack,item, item2)

        elif choice == "12":
            search_word = input("search: ")
            try:
                print(emission_functions.search_country(search_word))
            except ValueError:
                print("Country does not exist!")

        elif choice == "13":
            country = input("country: ")
            part = country.split(",")
            country = part[0]
            year1 = part[1]
            year2 = part[2]
            try:
                print(country+":"+str(emission_functions.get_country_change_for_years(country, year1, year2))+"%")
            except ValueError:
                print("Wrong year!")

        elif choice == "14":
            country_name = input("Country: ")
            data = emission_functions.get_country_data(country_name)
            emission_functions.print_country_data(data)

        else:
            print("That is not a valid choice. You can only choose from the menu.")
        
        input("\nPress enter to continue...")

if __name__ == "__main__":
    main()
