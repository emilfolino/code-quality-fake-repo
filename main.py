#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Mr Marvin svarar på frågor via ett menyprogram
"""

# import av de moduler som behövs
import marvin
import inventory
import emission_functions as em_func


marvin_image = r"""
                             
        ________________    
        |  ___________  |  
        | |           | |   
        | |   0   0   | |  
        | |     -     | |   
        | |   \___/   | |  
        | |___     ___| |  
        |_____|\_/|_____|  
          ____|/ \|____
         / *********** \      
        / ************* \  
        ------------------  

"""
def main():
    """
    huvudprogrammet för Mr Marvin:
    while-loop som hela tiden ligger och väntar på input
    """
    # 'CONTROL_L' innehåller kod för att rensa skärmen
    # dvs 'skjuter upp' alla tidigare kommandon, utom synhåll
    CONTROL_L = chr(27) + "[2J" + chr(27) + "[;H"

    # listan 'bag_list' motsvarar Mr Marvins ryggsäck
    bag_list = []

    # Evig loop, tills 'q' anges på skärmen
    # ska ligga i main-funktionen
    while True:
        print(CONTROL_L)
        print(marvin_image)
        print("Det här är Mr Marvin. Vad vill du ha hjälp med?")
        print()
        print("1) Presentera mig för Mr Marvin.")
        print("2) Omvandla Celcius till Fahrenheit.")
        print("3) Ordmultiplicering.")
        print("4) Summa och medel.")
        print("5) Upprepa bokstäver.")
        print("6) Checka isogram.")
        print("7) Högre eller lägre.")
        print("8) Kasta om bokstäver (randomize).")
        print("9) Skapa akronym.")
        print("10) Sträng-maskering.")
        print("11) Hitta alla index.")
        print("12) Sök länder.")
        print("13) Beräkna utsläpp för angivet land.")
        print("14) Visa info om angivet land.")
        print("a1) Sök matchande tecken i två strängar")
        print("a2) Dubblera siffror")
        print("a3) Ersätt 'tab' med mellanslag")
        print("a4) Slå ihop två namn")
        print("a5) Räkna poäng per spelare")
        print("b1) Betygs-sättning")
        print("b2) Analysera ett ord")
        print()
        print("q) Avsluta.")

        choice = input("--> ")

        # 'break' avslutar loopen helt, inte bara detta varv
        # yttersta loopen = exekveringen avslutas
        if choice == "q":
            print()
            print("Tack för idag, välkommen åter!")
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
            word_in = input("skriv in ett ord: ")
            print()
            print(marvin.randomize_string(word_in))
        
        elif choice == "9":
            word_in = input("skriv in ett ord som akronymen skapas från: ")
            print()
            print(marvin.get_acronym(word_in))
        
        elif choice == "10":
            word_in = input("skriv in ett ord att undersöka: ")
            print()
            print(marvin.mask_string(word_in))
        
        elif choice == "11":
            search_str = input("skriv in ett ord att undersöka: ")
            wanted_str = input("vilket ord ska hittas: ")
            print()
            print(marvin.find_all_indexes(search_str, wanted_str))
        
        elif choice == "12":
            search_str = input("skriv landets namn, eller skriv del av namn: ")
            print()
            try:
                result_list = em_func.search_country(search_str)
                result_str = ", ".join(result_list)
                print(f"Following countries were found: {result_str}")
            except ValueError as error_message:
                print(str(error_message))

        elif choice == "13":
            search_str = input("ange land och två årtal: ")
            print()
            search_list = search_str.split(",")
            country = search_list[0]
            year1 = search_list[1]
            year2 = search_list[2]
            try:
                change_result = em_func.get_country_change_for_years(country, year1, year2)
                print(f"{country}:{change_result}%")
            except ValueError as error_message:
                print(str(error_message))

        elif choice == "14":
            country = input("ange land: ")
            print()
            country_dict = em_func.get_country_data(country)
            em_func.print_country_data(country_dict)

        elif choice == "a1":
            marvin.a1()

        elif choice == "a2":
            marvin.a2()

        elif choice == "a3":
            marvin.a3()

        elif choice == "a4":
            marvin.a4()

        elif choice == "a5":
            marvin.a5()

        elif choice == "b1":
            max_point = input("max antal poäng: ")
            given_point = input("dina poäng: ")
            print()
            print(marvin.points_to_grade(max_point, given_point))

        elif choice == "b2":
            total_string = input("ord att analysera: ")
            start = input("vad ska ordet börja med: ")
            middle = input("vilken teckensekvens måste förekomma: ")
            stop = input("vad ska ordet sluta med: ")
            print()
            print(marvin.has_strings(total_string, start, middle, stop))
        
        elif choice.startswith("inv"):
            if (choice.startswith("inv pick")
            or choice.startswith("inv swap")
            or choice.startswith("inv drop")):
                bag_list = inventory.handle_choice(bag_list, choice)
            else:
                choice_list = choice.split(" ")
                if len(choice_list) == 1:
                    inventory.inventory(bag_list)
                else:
                    start = choice_list[1]
                    stop = choice_list[2]
                    inventory.inventory(bag_list, start, stop)

        else:
            # felaktigt menyval
            print()
            print("Felaktigt val, du kan enbart välja från ovanstående meny.")

        input("\nPress enter to continue...")

# används vid test av enbart denna modul
# exekveras inte när modulen importeras till annan fil
if __name__ == "__main__":
    main()
