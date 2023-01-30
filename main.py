"""
Prints out menu options and uses funtions from the module 'marvin'
"""
import marvin
import inventory
import emission_functions



marvin_image = r"""
             8888888888888
          88888o8888888o88888
        888o88888888o8888o88888
      888888888888o88888888888888
     8888o88             888888888
    88888888             88888o888
    8888888              888888o888
   888888                 8o8888888
  88 888 ,*8888o, ,o8888*, 8888 88 8
 8888888 '`(0))`~ ~`((0)`' 8888888 8
 8888888l  `'` `; ;` `'`   88888888 8
  88 8888       ; d;       8888888 88
  8888888       ( 7,       8888 888  8
 88888888      @@@@@@      888888888 8
 8 88888o   ,@@@@@@@@@, , o8888888  88
88888888`o  @@;~^~^~;@@ 0;`8 8888888
8888 88 8`v    `@@@`    o`88888 888 8
88888888  `;,        ,;o`8 88888888 8
 8 8888     `o,  ,;,;o` 888888 88 8
 8888 88      ``'''`     88 8888888 8
88888888                  8 8888 8888
8888888                    88  888888
                                888888
                                888888

"""


def pressEnterToContinue():
    """
    Called often after completing a menu option
    """
    input("\nMarv wants you to press enter to continue...")


def main():
    """
    Prints out menu options
    """
    bag = []
    while True:
        print(chr(27) + "[2J" + chr(27) + "[;H")
        print(marvin_image)
        print("Zup, I'm Marv. I know it all worth knowing. What can I do you for?")
        print("1) Present yourself to Marv.")
        print("2) Ask Marv about temperature in Fahrenheit.")
        print("3) Ask Marv to repeat something")
        print("4) Ask Marv to get sum and average")
        print("5) Ask Marv to say something s-ll-ooo-wwww-llll-yyyyyy")
        print("6) Ask Marv to decide if a word is an isogram")
        print("7) Ask Marv if a number is bigger than the previous")
        print("8) Ask Marv to shuffle a word")
        print("9) Ask Marv to create an acronym")
        print("10) Ask Marv to mask parts of a number")
        print("11) Ask Marv about a substrings positions in string")
        print("12) Ask Marvin to search country names")
        print("13) Ask Marvin to check a countries pollution change")
        print("14) Ask Marvin about a country")
        print("b1) Ask Marvin what grade you've got")
        print("b2) Ask Marvin about strings content")
        print("e1) Ask Marvin to list worst CO2 pollution countries in the world")
        print("Commands: inv, inv pick, inv drop, inv swap, inv 'startindex' 'endindex'")
        print("q) Quit.")

        choice = marvin.choice_main_options()

        if choice == "q":
            print("Anytime dude!")
            break

        elif choice == "1":
            marvin.greet()
            pressEnterToContinue()

        elif choice == "2":
            marvin.celcius_to_farenheit()
            pressEnterToContinue()

        elif choice == "3":
            marvin.word_manipulation()
            pressEnterToContinue()

        elif choice == "4":
            marvin.sum_and_average()
            pressEnterToContinue()

        elif choice == "5":
            marvin.hyphen_string()
            pressEnterToContinue()

        elif choice == "6":
            marvin.is_isogram()

        elif choice == "7":
            marvin.compare_numbers()

        elif choice == "8":
            print("\nMarv says:\n")
            strShuffle = input("What do you want me to shuffle bro? ")
            print(marvin.randomize_string(strShuffle))
            print("\nCrazy dude!\n")
            pressEnterToContinue()

        elif choice == "9":
            print("\nMarv says:\n")
            toAcronymite = input("No prob, what do you want me to acronymite? ")
            print(marvin.get_acronym(toAcronymite))
            print("\nSounds waaay to formal bro!")
            pressEnterToContinue()

        elif choice == "10":
            print("\nMarv says:\n")
            str_to_mask = input(
                "Tell me a number and I'll mask everything except the last four digits: ")
            print(marvin.mask_string(str_to_mask))
            print("\nDon't get into problems now...")
            pressEnterToContinue()

        elif choice == "11":
            print("\nMarv says:\n")
            bigstr = input("No prob! Tell med the string: ")
            substr = input("Alright, now tell me the substring: ")
            print(marvin.find_all_indexes(bigstr, substr))
            pressEnterToContinue()

        elif choice == "12":
            print("\nMarv says:\n")
            print("I loooove geography!")
            try:
                result = emission_functions.search_country(input("Search on : "))
                result_str = ", ".join(result) # Gör om lista till sträng
                print(f"I found these countries: {result_str}.")
            except ValueError as e:
                print(e)
            pressEnterToContinue()

        elif choice == "13":
            print("\nMarv says:\n")
            print("Oooh geography AND mathematics.. Bring it on...")
            splitted_input = input("Type in format 'country,year1,year2': ").split(",")

            country = splitted_input[0]
            year1 = splitted_input[1]
            year2 = splitted_input[2]
            try:
                print(f"{country}:{emission_functions.get_country_change_for_years(country, year1, year2)}%")
            except ValueError as e:
                print(e)
            pressEnterToContinue()

        elif choice == "14":
            print("\nMarv says:\n")
            print("I'll tell you everything I know, man...'")
            facts = emission_functions.get_country_data(input("Tell me a country: "))
            if facts == "Country does not exist!":
                print(facts)
            else:
                emission_functions.print_country_data(facts)
            pressEnterToContinue()


        elif choice == "b1":
            print("\nMarv says:\n")
            print("Don't belive in grades but alright...\n")
            max_point = input("Tell me the maximum points: ")
            points = input("Mhm,. now tell me your points: ")
            print(marvin.points_to_grade(max_point, points))
            pressEnterToContinue()

        elif choice == "b2":
            print("\nMarv says:\n")
            print("Easy dude...\n")
            str_big = input("Tell me a string ")
            substr1 = input("Now tell me a substring: ")
            substr2 = input("Ok, another: ")
            substr3 = input("Aha, and a third one: ")
            print(f"{marvin.has_strings(str_big, substr1, substr2, substr3)}")
            pressEnterToContinue()

        elif choice == "e1":
            print("\nMarv says:\n")
            print("Depressing if you ask me...")
            splitted_input = input("Type in year and length of list in format 'year,length': ").split(" ")

            year = splitted_input[0]
            length = splitted_input[1]

            try:
                emission_functions.worst_countries(year, length)
            except ValueError as e:
                print(str(e))

            pressEnterToContinue()

        elif "inv pick" in choice:
            splitted_choice = choice.split()
            try:
                inventory.pick(bag, splitted_choice[2], splitted_choice[3])
            except IndexError:
                inventory.pick(bag, splitted_choice[2])

            pressEnterToContinue()

        elif "inv drop" in choice:
            splitted_choice = choice.split()
            inventory.drop(bag, splitted_choice[2])
            pressEnterToContinue()

        elif "inv swap" in choice:
            splitted_choice = choice.split()
            inventory.swap(bag, splitted_choice[2], splitted_choice[3])
            pressEnterToContinue()

        elif "inv" in choice:
            splitted_choice = choice.split()
            if len(splitted_choice) == 3:
                inventory.inventory(bag, splitted_choice[1], splitted_choice[2])
            elif len(splitted_choice) == 2:
                inventory.inventory(bag, splitted_choice[1])
            else:
                inventory.inventory(bag)
            pressEnterToContinue()


        else:
            print("What? Didn't catch that part...")
            pressEnterToContinue()

if __name__ == "__main__":
    main()
