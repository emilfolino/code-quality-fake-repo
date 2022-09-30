#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
meny
"""
def menu():
    """
    Skriver ut menyn, vilka val som kan göras
    """
    # 'CONTROL_L' innehåller kod för att rensa skärmen
    # dvs 'skjuter upp' alla tidigare kommandon, utom synhåll
    CONTROL_L = chr(27) + "[2J" + chr(27) + "[;H"

    # skriver ut meny
    print(CONTROL_L)
    print()
    print("lines) Räkna antal rader")
    print("words) Räkna antal ord")
    print("letters) Räkna antal bokstäver")
    print("word_frequency) Visa de 7 vanligaste orden")
    print("letter_frequency) Visa de 7 vanligaste bokstäverna")
    print("all) Gör allt ovanstående")
    print("change) Byt fil")
    print()
    print("q) Avsluta.")

# används vid test av enbart denna modul
# exekveras inte när modulen importeras till annan fil
if __name__ == "__main__":
    menu()
