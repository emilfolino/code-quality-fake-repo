#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Functions for marvin choises
"""

import random


def greet():
    """
    Välkommen med namn
    """
    name = input("What is your name? ")
    print("\nYazan says:\n")
    print("Hello %s - your name is very nice!" % name)
    print("What can I do you for?!")

def celcius_to_farenheit():
    """
    Omvandlig celcius till farenheit
    """
    temperature_value = float(input("Enter a temperature in Celsius:"))
    temperature_value = (temperature_value * 1.8) + 32
    print(round(temperature_value, 2))

def word_manipulation():
    """
    Ord repetering
    """
    string = input("Enter a string: ")
    integer = int(input("Enter an integer: "))
    new_result = multiply_str(string, integer)

    return print(new_result)

def sum_and_average():
    """
    Beräkna summan och meldel
    """
    new_number = []
    while True: 
        in_put = input("Enter numbers until you write “done" ":  ")
        new_number.append(in_put)
        if in_put == "done":
            new_number.remove("done")
            num = [float(x) for x in new_number]
            addition = float(sum(num))
            avrage = float(addition/len(num))
            print("The sum of all numbers are", addition , "and the avrege is", round(avrage, 2))
            break

def hyphen_string():
    """
    hyphen_string
    """
    old_string = input("Enter a string and see what happens: ")
    new_string = ""
    increase_leter = 0
    for i in old_string:
        i = i + (i * increase_leter)
        increase_leter = increase_leter + 1
        new_string += f"{i}-"
    print(new_string[:-1])

def is_isogram():
    """
    is_isogram
    """
    answer = ""
    string = (input("Enter a string: "))
    check_list = []
    for letter in string:
        check_list.append(letter)
        if (check_list.count(letter)) >= 2:
            answer = "No_match!"
            break
        elif check_list.count(letter) != 2:
            continue

    if answer == "No_match!":
        print("No match!")
    else:
        print("Match!")

def compare_numbers():
    """
    compare_numbers
    """
    num1 = int(input("Enter the first number: "))

    while True:
        try:
            num2 = (input("Enter a number, done to quit: "))
            num3 = int(num2)
        except ValueError:
            if str(num2) == "done":
                break
            print("not a number!")
            continue

        if int(num3) > num1:
            print("larger!")
        elif num3 < num1:
            print("smaller!")
        else:
            print("same!")
        num1 = int(num2)

def randomize_string(word):
    """
    randomize_string: slumpa bökstaverna
    """
    save = ""
    new_word = random.sample(word, k=len(word))
    for letter in new_word:
        save += letter
    return (word + " --> " + save)

def get_acronym(char):
    """
    get_acronym: signatur
    """
    save = ""
    for letter in char:
        if letter == letter.upper() and letter.isalpha():
            save += letter
        else:
            continue

    return save

def mask_string(string):
    """
    mask_string: maskera strängen utan de sista fyra
    """
    integer = 1
    new_result = multiply_str(string, integer)
    result = []
    save = ""
    for char in new_result:
        result.append(char)
    
    result[0:-4] = "#"* len(result[0:-4])
    for letter in result:
        save += letter
    return (save)
        
def multiply_str(string, integer):
    """
    multiply_str: multiplisera stängen met ett viss heltal
    """
    string *= integer
    return (string)

def find_all_indexes(str1, index_str1):
    """
    find_all_indexes: hutta index
    """
    save = []
    start = 0
    stop = (str1.count(index_str1))
    answer = ""

    for i in range(start, stop):
        if i != stop:
            try:
                result = str1.index(index_str1, start)
                save.append((result))
                start = 1 + result
                #answer = (*save, sep=",")
            except ValueError:
                print("")
                break

    for char in save:
        answer += (str(char) + ",")
    answer = answer[:-1]

    return (answer)
