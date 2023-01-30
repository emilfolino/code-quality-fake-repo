#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
    För att avsluta programmet
'''

import random



def quitter():
    '''
    För att avsluta programmet
    '''
    print("Bye, bye - and welcome back anytime!")
    return True

def greet():
    '''
    Hälsar på användaren
    '''
    name = input("What is your name? ")
    print("\nMarvin says:\n")
    print("Hello %s - i am awesomeness!" % name)
    print("What do you want?!")

def celcius_to_farenheit():
    '''
    Förvandlar celsius to farenheit
    '''
    print("Wanna convert celcius to Fahrenheit? ")
    temp = float(input("Celcius:"))
    temp = temp * 1.8 + 32
    print("Farhenheit: " + str(round(temp,2)))

def word_manipulation():
    '''
    Dubblerar ordet
    '''
    ord1 = input("ordet")
    times = int(input("gånger"))
    print("ordmultipliceraren? ")
    ord1 = multiply_str(ord1, times)
    print(ord1)

def sum_and_average():
    '''
    Räknar ut summa och medelvärde
    '''
    print("Summa n medelvärde? Skriv done när du är klar ")
    talen = []
    num = 0
    räknare = 0
    while True:
        tal = input("tal")
        if tal != "done":
            talen.append(tal)
        else:
            break
    for x in talen:
        num = num + float(x)
        räknare = räknare + 1
        avarage = num / räknare
        avarage = round(avarage, 2)
    print( "The sum of all numbers are " + str(num) + " and the avarage is " + str(avarage) )

def hyphen_string():
    '''
    Förlänger ordet med bokstäver
    '''
    print("Ordförlängaren")
    förläng = 0
    jäm_ord1 = input("Ord: ")
    ord1 = ""
    for x in jäm_ord1:
        förläng = förläng + 1
        x = x * förläng
        ord1 = ord1 + "-" + x
    print(ord1)

def is_isogram():
    '''
    Kollar om ordet är ett isogram
    '''
    print("Isogram-kollen ")
    ord1 = input("Ord:")
    räknare = 0
    ord_upper = ord1.upper()
    print(ord_upper)
    for x in ord_upper:
        if ord_upper.count(x) > 1:
            räknare = räknare + 1
        elif ord_upper.isnumeric():
            resultat = "No match!"
    if räknare > 1:
        resultat = "No match!"
    else:
        resultat = "Match!"
    print(resultat)

def compare_numbers():
    '''
    jämför siffror
    '''
    num = None
    while True:
        tal = ""
        tal = input("Nummer:")
        if tal == "done":
            break
        else:
            try:
                tal = float(tal)
                while num is None and isinstance(tal, float):
                    try:
                        num1 = float(input("skriv jämförelsetalet: "))
                        num = tal
                        tal = num1
                    except ValueError:
                        print("not a number!")
                if tal < num:
                    print("smaller!")
                    num = tal
                    print(str(num) + "s" + str(tal))
                elif tal > num:
                    print("larger!")
                    num = tal
                    print(str(num) + "s" + str(tal))
                else:
                    print("same!")
                    print(str(num) + "s" + str(tal))
            except ValueError:
                print("not a number!")

def first_second():
    '''
    Jämför
    '''
    ord1 = input("första ordet")
    ord2 = input("andra ordet")
    ord1 = ord1.lower()
    ord2 = ord2.lower()
    match = 0
    for x in ord2:
        if x in ord1:
            match = match + 1
            if match == len(ord2):
                print("Match!")
        else:
            nomatch = 1
            if nomatch > 0:
                print("No match!")
                break

def randomize_string(result):
    '''
    Shufflar bokstäverna i strängen
    '''
    new_word = ""
    random_list = []
    for x in result:
        random_list.append(x)
    random.shuffle(random_list)
    for x in random_list:
        new_word = new_word + x
    return result + " --> " +new_word

def get_acronym(result):
    '''
    Tar fram en akronym av dom stora bokstäverna
    '''
    akro = ""
    for x in result:
        if x.isupper():
            akro = akro + x
    return akro

def mask_string(result):
    '''
    Byter ut alla bokstäver förutom dom fyra sista till #
    '''
    akro = len(result)
    counter = 0
    four_last = ""
    gånger = akro - 4
    for x in result:
        counter = counter + 1
        if counter <= akro - 4:
            pass
        else:
            four_last = four_last + x
    gånger = multiply_str("#", gånger)
    gånger = gånger + four_last
    return gånger

def multiply_str(ord1, times):
    '''
    multiplicerar ordet med times
    '''
    try:
        times = int(times)
        ord12 = ord1 * times
        return(ord12)
    except ValueError:
        ord12 = ord1
        return(ord12)

def find_all_indexes(first_str, second_str):
    '''
    Hittar index för secon_str i first_str
    '''
    counter = 0
    answer = ""
    for x in range(0, len(first_str)):
        try:
            x = first_str.index(second_str, counter)
            counter = x + 1
            answer = answer + str(x) + ","
        except ValueError:
            break

    if x == 0:
        x = ""
    return answer[:-1] 

def not_valid_choice():
    '''
    För att avsluta programmet
    '''
    print("That is not a valid choice. You can only choose from the menu.")
