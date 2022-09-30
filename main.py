#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Marvin v2
"""
import marvin as m
import inventory as i
import emission_functions as ef

botname = "Donald"
marvin_image = """
                 ,;;;;;,.
                !!!!!!!!!!>;.
               !!!!!!!!!!!!!!!;;.
          _. - !!!!!!!!!!!!!!!!!!!;;,. ;;!!!!!!;;;.
       . '     !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!;
      '     .- `!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!>
    '     ,'    <!!!!!!!!!!'''''''''''!!!!!!!!!!!!!!!'
  .'     -      `!!!!!!' ----<!!!!!!>;.`'!!!!!!!!!!!!
 /  ,  .'         `!!!',nMMMn.`!!!!!!!!!, `!!!!!!!!!
/.-'; /            `',dMMMMMMMb.``'__``''!><``'!!!'
    (/             .dMMMP"'""4MMn`MMMMMMnn.`MM.`'
    '        ,,,xn MMM",ndMMb,`4MMMMMMMMMMMMM(*.
              ,JMBJMM',MMMMMMMn`MMMMMMMMMMMMMMx       ,ccccocdd$$$$$hocc
            ,M4MMnMM',MMMMMMMMMMMMMMMMMMMMMMMMMb     ,$$P""'''.,;;;,. ?$F
           "  dMMMMMdMMMMMMMMMMMMMMMMMMMMMMMMMMMB   ,$P <!!!!!!!!!!!! d$'
             dMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMP ,dP",!!!!!!!!!!!!! d$'
             MMMMMMMMMMC(ummn)?MMMMMMMMP",,"4MMP,c$".!!!!!!!!!!!!!',dP'
            ;MMMP4MMMMMMMPPPPPPPMMMMM",c$$$$c`",$P',!!!!!!!!!!!!!',$P
            `",nmdMMMMP" .,,,.  "MMP.d$$$$$P',$$",!!!!!!!!!!!!!',cP"
            dMMMMMMMMbxdMMMMMMPbnd",$$$$$$Lc$P",<!!!!!!!!!!!!',c$F
            ",ccc,""MMMMMMCcccnMP z$$$$$$$$$".!!!!!!!!!!!!!',c$P'
            ,$$P?$$c`4MMMMMMMMM".$$$$$$$$P" <!!!!!!!!!!!'.,dP"
            `$F,c "?$c,."TTT",cc$$$$$$P".: ;!!!!!!!!''.zd$P"
             `hd$c"$$$$$$$$$$$$$$$P"' .:: ;!!!!!''.,c$P""
              `$$$h.""???$$$P??""  .:.:   ',,,cr??""
                ?$$$.`!>;;;;, `.:::: ;..`""CC,
                 "?$$c.`!!!!!!> `::: !!!!!;."*c,
                   "?$$c`'!!!!!!; `' !!!!!!!;."?$c,
                     "?$$c`'!!!!!!!>;!!!!!!!!!!,`?$h,.
                       `"$$c,`'!!!!!!!!!!!!!!!!!!>,`"?$c,
                          `"?$c.`'!!!!!!!!!!!!!!!!!!!,."??hc,
                              ""?hc,`''!!!!!!!!!!!!!!!'',c$"
                                  "?$$cc,,````''''',,cc$P"
                                      ""??$$$$$$$$$??"'
                                           ``""'
"""

def main():
    """Main function"""
    menu = """
    Hi, I'm %s. Quack quack. What would you like to do?
    1) A short introduction of myself
    2) Convert a value in Celsius to Fahrenheit
    3) Multiply a word
    4) Calculate the sum of a series of numbers
    5) Increasingly repeat letters of a word
    6) Check if a word is an isogram
    7) Check larger or smaller numbers
    8) Randomize string
    9) Create acronym
    10) Mask string
    11) Find all indexes of a substring in a string
    B1) Points to grade
    B2) Has strings
    12) Search for countries
    13) Country emissions
    14) Print country data
    e1) List countries by most emissions
    e2) List emissions per capita
    e3) List emissions per land
    q) Quit

    Try out my inv commands!
    -------------
    """
    backpack = []
    while True:
        print(chr(27) + "[2J" + chr(27) + "[;H") #Clears terminal
        print(marvin_image)
        print(menu % botname)
        choice = input("--> ")

        if choice == "q":
            print("Bye, bye - and welcome back anytime!")
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
            string = input("Enter a string to randomize: ")
            print(m.randomize_string(string))
        elif choice == "9":
            string = input("Enter string to generate acronym for: ")
            print(m.get_acronym(string))
        elif choice == "10":
            string = input("Enter string to mask: ")
            print(m.mask_string(string))
        elif choice == "11":
            string = input("Enter main string: ")
            subString = input("Enter substring to search for: ")
            print(m.find_all_indexes(string, subString))
        elif choice in ("b1", "B1"): #Same as choice == "b1" or choice == "B1"
            maxPoints = input("Enter max possible points: ")
            points = input("Enter your points: ")
            print(m.points_to_grade(int(maxPoints), int(points)))
        elif choice in ("b2", "B2"):
            string = input("Enter a string: ")
            prefix = input("Enter the first part of the string: ")
            middle = input("Enter the middle part of the string: ")
            end = input("Enter the end of the string: ")
            print(m.has_strings(string, prefix, middle, end))

        # Inv section
        elif choice.startswith("inv pick"):
            choiceList = choice.split(" ")
            if len(choiceList) == 3:
                i.pick(backpack, choiceList[2])
            elif len(choiceList) == 4:
                i.pick(backpack, choiceList[2], choiceList[3])
            else:
                print("Syntax error. Use: inv pick [item] [index](optional) \nTry again..")
        elif choice.startswith("inv drop"):
            choiceList = choice.split(" ")
            if len(choiceList) == 3:
                i.drop(backpack, choiceList[2])
            else:
                print("Syntax error. Use: inv drop [item] \nTry again..")
        elif choice.startswith("inv swap"):
            choiceList = choice.split(" ")
            if len(choiceList) == 4:
                i.swap(backpack, choiceList[2], choiceList[3])
            else:
                print("Syntax error. Use: inv swap [item1] [item2] \nTry again..")
        elif choice.startswith("inv"):
            choiceList = choice.split(" ")
            if len(choiceList) == 3:
                i.inventory(backpack, choiceList[1], choiceList[2])
            elif len(choiceList) == 1:
                i.inventory(backpack)
            else:
                print("Syntax error. Use: inv <start> <stop> OR just 'inv' \nTry again..")

        # Kmom05
        elif choice == "12":
            string = input("Search for country name: ")
            try:
                print(ef.search_country(string))
            except ValueError as e:
                print(e)
        elif choice == "13":
            string = input("Country,year1,year2: ")
            stringList = string.split(",")
            try:
                if len(stringList) == 3:
                    change_em = ef.get_country_change_for_years(stringList[0], stringList[1], stringList[2])
                    print(stringList[0] + ":" + str(change_em) + "%")
                else:
                    print("Syntax error. Use: [Country],[year1],[year2] \nTry again..")
            except ValueError as e:
                print(e)
        elif choice == "14":
            string = input("Country: ")
            ef.print_country_data(ef.get_country_data(string))
        # Extra
        elif choice == "e1":
            string = input("Year and num results(optional): ")
            stringList = string.split(" ")
            if len(stringList) == 1:
                ef.emission_top(string)
            elif len(stringList) == 2:
                ef.emission_top(stringList[0], int(stringList[1]))
            else:
                print("Syntax error. Use: [year] [result_num](optional) \nTry again..")
        elif choice == "e2":
            string = input("Enter year num results(optional): ")
            stringList = string.split(" ")
            if len(stringList) == 1:
                ef.emission_top_capita(string)
            elif len(stringList) == 2:
                ef.emission_top_capita(stringList[0], int(stringList[1]))
            else:
                print("Syntax error. Use: [year] [result_num](optional) \nTry again..")
        elif choice == "e3":
            string = input("Enter year num results(optional): ")
            stringList = string.split(" ")
            if len(stringList) == 1:
                ef.emission_top_land(string)
            elif len(stringList) == 2:
                ef.emission_top_land(stringList[0], int(stringList[1]))
            else:
                print("Syntax error. Use: [year] [result_num](optional) \nTry again..")

        else:
            print("That is not a valid choice. You can only choose from the menu.")
        input("\nPress enter to continue...")

if __name__ == "__main__":
    main()
