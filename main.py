 #!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Marvin with a simple menu to start up with.
Marvin doesnt do anything, just presents a menu with some choices.
You should add functinoality to Marvin.
"""
import marvin
import inventory
import emission_functions

MarvinImg = (r'''
           .---.     .---.
          ( -o- )---( -o- )
          ;-...-`   `-...-;
         /                 \
        /                   \
       | /_               _\ |
       \`'.`'"--.....--"'`.'`/
        \  '.   `._.`   .'  /
     _.-''.  `-.,___,.-`  .''-._
    `--._  `'-._______.-'`  _.--`
        /                 \
        /.-'`\   .'.   /`'-.\
       `      '.'   '.'
''')



def main():
    """
    Main Function That Runs
    The Program
    """
    Value = 'q' , 'Q'
    Choice = ""
    ryggsäcken = []

    while True:
        #print(chr(27) + "[2J" + chr(27) + "[;H")        
        print(MarvinImg)
        print("1, Present Yourself To Magmus 9000, Yes My Name Is Magmus 9000")
        print("2, Convert Celcius To Fahrenhit")
        print("3, Spam A Word x Amount Of Times")
        print("4, Calculate Average")
        print("5, Turn A Text String Into A Magic Trick!")
        print("6, Try IF Your Word Is AN ISOGRAM!")
        print("7, Compare Numbers!")
        print("8, Shuffle A WORD!!!")
        print("9, Show My Acronym!")
        print("10, Mask Your Text")
        print("11, Find Index")
        print("12, Search For A Country By Word")
        print("13, Compare Utsläpp Mellan Två År")
        print("14, Skriv Ut Country Data Information")
        
        
        
        print("(q / Q ) - Quit")
        
        Choice = input("--> ")
        
        if Choice in Value:
            print("Oh, well, ill see you soon again!")
            break
                            
        elif Choice == "1":
            marvin.greet()
        
        elif Choice == "2":
            marvin.celcius_to_farenheit()
        
        elif Choice == "3":
            marvin.word_manipulation()
            
        elif Choice == "4":
            marvin.sum_and_average()
        
        elif Choice == "5":
            marvin.hyphen_string()

        elif Choice == "6":
            marvin.is_isogram()

        elif Choice == "7":
            marvin.compare_numbers()
            
        elif Choice == "8":
            string = input("Enter a string to randomize: ")
            print(marvin.randomize_string(string))
        
        elif Choice == "9":
            acronym = input("Skriv En Text Där Varje Ord Börjar Med Ett Stort Bokstav: ")
            print(marvin.get_acronym(acronym))
                
        elif Choice == "10":
            TextWrite = input("Skriv ett flertal siffror du vill maskera utan de 4 sista: ")
            print(marvin.mask_string(TextWrite))
            
        elif Choice == "11":
            FirstArgument = input("Write Your First Argument: ")
            SecondArgument = input("Write Your Second Argument: ")
            print(marvin.find_all_indexes(FirstArgument, SecondArgument))

        elif Choice.startswith('inv pick'):
            SplitChoice = Choice.split(" ")
            item = SplitChoice[2]
            try:
                position = int(SplitChoice[3])
                ryggsäcken = inventory.pick(ryggsäcken, item , position)
            except IndexError:
                ryggsäcken = inventory.pick(ryggsäcken, item)

        elif Choice.startswith('inv drop'):
            SplitChoice = Choice.split(" ")
            ItemDrop = SplitChoice[2]
            inventory.drop(ryggsäcken, ItemDrop)

        elif Choice.startswith('inv swap'):
            SplitChoice = Choice.split(" ")
            itemswap1 = SplitChoice[2]
            itemswap2 = SplitChoice[3]
            inventory.swap(ryggsäcken, itemswap1, itemswap2)

        elif Choice.startswith('inv'):
            inventory.inventory(ryggsäcken)

        elif Choice == "12":
            Ordet = input("Provide A Word: ")
            try:
                print(emission_functions.search_country(Ordet))
            except ValueError:
                print("Country does not exist!")

        elif Choice == "13":
            Ordet = input("Ange Land Och Year ")
            try:
                SplitChoice = Ordet.split("," , 3)
                Printen = emission_functions.get_country_change_for_years(
                    SplitChoice[0], 
                    SplitChoice[1], 
                    SplitChoice[2]
                )
                print(f"{SplitChoice[0]}:{Printen}%")

            except ValueError:
                print("Wrong year!")

        elif Choice == "14":
            Ordet = input("Ange Ett Land: ")
            emission_functions.print_country_data(emission_functions.get_country_data(Ordet))
        
        else:
            print("Felaktigt val, du kan enbart välja från ovanstående meny.")
        input("tyck enter för att fordsätta") 


if __name__ == "__main__":
    main()
    