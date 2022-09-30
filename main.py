#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Analys av texter
"""

# import av de moduler som behövs
import menu
import analyzer

def main():
    """
    Huvudprogram för statistik
    """
    # standardvald fil
    filename = "phil.txt"
    data_dict = analyzer.init_incoming_data(filename)
    if data_dict is None:
        print("fil går ej att läsa")
        input("\nPress enter to confirm...")
        
    # Evig loop, tills 'q' anges på skärmen
    while True:
        # 'break' avslutar loopen helt, inte bara detta varv
        # yttersta loopen = exekveringen avslutas
        menu.menu()
        choice = input("--> ")

        if choice == "q":
            print()
            print("Tack för idag, välkommen åter!")
            break

        if choice == "lines":
            print(analyzer.lines(data_dict["dict_lines"]))

        elif choice == "words":
            print(analyzer.words(data_dict["dict_words"]))

        elif choice == "letters":
            print(analyzer.letters(data_dict["dict_letters"]))

        elif choice == "word_frequency":
            calc_data = analyzer.word_frequency(data_dict["dict_words"])
            analyzer.output(calc_data)

        elif choice == "letter_frequency":
            calc_data = analyzer.letter_frequency(data_dict["dict_letters"])
            analyzer.output(calc_data)

        elif choice == "all":
            to_print = analyzer.execute_all(data_dict)
            analyzer.output(to_print)

        elif choice == "change":
            filename = analyzer.change()
            temp_dict = analyzer.init_incoming_data(filename)
            if temp_dict is not None:
                data_dict = temp_dict

        else:
            # felaktigt menyval
            print()
            print("Felaktigt val, du kan enbart välja från ovanstående meny.")

        input("\nPress enter to continue...")

# används vid test av enbart denna modul
# exekveras inte när modulen importeras till annan fil
if __name__ == "__main__":
    main()
