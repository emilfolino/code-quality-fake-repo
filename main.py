"""
Importerar marvin
Importerar inventory
Importerar emission_functions
"""
import marvin
import inventory
import emission_functions
backpack = []
def main():    
    """
    Its an eternal loop, until q is pressed.
    It should check the choice done by the user and call a appropriate
    function.
    """
    while True:
        print(marvin.bulldog_ai())
        print("Welcome. I am SiriTheBulldog The Master of the Universe!! How can I help you today?\n") 
        print("1.Your presentation to me")
        print("2.Celcius to Fahrenheit") 
        print("3.RepeatGame")
        print("4.Math")
        print("5.Letter repeat")
        print("6.Isogram") 
        print("7.Smaller, bigger or equal")
        print("8.Randomize String")
        print("9.Get acronym")
        print("10.Mask string")
        print("11.Find all indexes")
        print("12. Find Country")
        print("a1.Word Search")
        print("a2.DoubleNumber")
        print("a3.ReplaceTab")
        print("a4.NameAdding")
        print("a5.ScoreTable")
        print("q. Quit")

        choice = input()            
        if choice == "1":
            marvin.greet()
        if choice == "2":
            marvin.celcius_to_farenheit()
        if choice == "3":
            marvin.word_manipulation()
        if choice == "4":
            marvin.sum_and_average(0,0)
        if choice == "5":
            marvin.hyphen_string()
        if choice == "6":
            marvin.is_isogram()
        if choice == "7":
            marvin.compare_numbers()
        if choice == "8":
            string = input("Enter a string to randomize: ")
            print(marvin.randomize_string(string))
        if choice == "9":
            print(marvin.get_acronym(input("Write names with capital letters:\n")))
        if choice =="10":
            num = input("Write the numbers:\n")
            print(marvin.mask_string(num))
        if choice =="11":
            search1 = input("Please enter a string")
            search2 = input("Please enter search char")
            print(marvin.find_all_indexes(search1, search2))
        if choice == "12" :
            search_word = input("What country are you looking for?")
            try:
                pollution = emission_functions.search_country(search_word)
                print(str(pollution))
            except ValueError:
                print("Country does not exist!")
        if choice == "13":
            hv = input("Enter Country and Year")
            hv = hv.split(',')
            try:
                print(hv[0]+":"+str(emission_functions.get_country_change_for_years(hv[0], int(hv[1]), int(hv[2])))+"%")
            except ValueError:
                print("Wrong year!")
        if choice == "14":
            country = input("Choose a country\n")
            country = country.capitalize()
            try:
                emission_functions.print_country_data(emission_functions.get_country_data(country))
            except ValueError:
                print("Country does not exist!")
        if choice == "a1":
            marvin.word_match()
        if choice == "a2":
            marvin.number_searching()
        if choice == "a3":
            marvin.tab_replace()
        if choice == "a4":
            marvin.vocal_count()
        if choice == "b1":
            score = float(input("Write the scorenumber:"))
            print(marvin.points_to_grade(score))
        if "inv pick" in choice:            
            x = choice.split()
            if len(x) <= 3:
                inventory.pick(backpack, x[2])                
            else:
                inventory.pick(backpack, x[2], int(x[3]))                               
        if "inv drop" in choice:
            x = choice.split()
            inventory.drop(backpack, x[2])
        if "inv swap" in choice:
            x = choice.split()
            inventory.swap(backpack, x[2], x[3])
        if choice == "inv":
            inventory.inventory(backpack)               
        if choice == "q":
            print("Bye!")
            break
        else:
            print("Please choose in the list")

if __name__ == "__main__":
    main()
