#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
functions for marvin choices
"""
import random

def greet():
    """
    greet
    """
    name = input("What is your name? ")
    print("\nMarvin says:\n")
    print("Hello %s - your awesomeness!" % name)
    print("What can I do for you?!")

def celcius_to_farenheit():
    """
    celsius to fahrenheit
    """
    celsius = input("How many degrees Celsius would you like to convert? ")
    fahrenheit = (float(celsius) * 1.8) + 32
    return print(f"{str(celsius)} degrees Celsius is {str(round(fahrenheit,2))} degrees Fahrenheit.")

def word_manipulation():
    """
    word manipulation
    """
    word  = input("What word would you like to multiply? ")
    antal = input("And how many times would you like to multiply \"" + word +"\"? ")
    # print("Your word multiplied "+ str(antal) + " times looks like this: " + word * int(antal))
    return print(multiply_str(word, antal))

def sum_and_average():
    """
    sum and average
    """
    total = 0
    antal = 0
    not_number = False
    print("Type 'done' when you are done.")
    while not not_number:
        try:
            tal = input("Enter number: ")
            number = float(tal)
            total += float(number)
            antal += 1
        except ValueError:
            print("Not a number")

        if "done" in tal:
            not_number = True

    average = total/antal
    return print(f"The sum is: {str(round(total, 2))}\nThe average is: {str(round(average, 2))}")

def hyphen_string():
    """
    hyphen string
    """
    try:
        word = input("Type a word and I will add dashes & characters to it: ")
        sammansattord = []
        for ordplats, ordchar in enumerate(word):
            sammansattord += ordchar * (ordplats + 1) + "-"

        if sammansattord[-1] == "-":
            sammansattord.pop()

        sammansattord = "".join(sammansattord)
        print(sammansattord)

    except IndexError:
        print("Please type a word.")

def is_isogram():
    """
    is isogram
    """
    word = input("Type a word: ")
    antalbokstäver = 0

    for bokstav in word:
        if (word.count(bokstav) > 1):
            antalbokstäver += 1

    if antalbokstäver == 0:
        return print("Match!")
    return print("No match!")

def compare_numbers():
    """
    compare numbers
    """
    print("Type 2 numbers. Type 'done' when you are done.")
    tal1  = input("Enter the first number: ")
    run = True
    while run:
        if tal1 == "done":
            print("The program will now exit!")
            break
        
        tal2 = input("Enter another number: ")

        if tal2 == "done":
            print("The program will now exit!")
            break

        try:
            if float(tal1) < float(tal2):
                print("larger!")
            elif float(tal1) == float(tal2):
                print("same!")
            elif float(tal1) > float(tal2):
                print("smaller!")
            tal1 = tal2
        except ValueError:
            return print("not a number!")

def randomize_string(randomizedword):
    """
    randomize string
    """
    normalword = randomizedword
    randomizedword = ''.join(random.sample(randomizedword,len(randomizedword)))
    print(f"{normalword} --> {randomizedword}")
    return f"{normalword} --> {randomizedword}"

def get_acronym(acronymarg):
    """
    get acronym
    """
    acronym = ""
    for char in acronymarg:
        if char.isupper():
            acronym += char
    return acronym

def multiply_str(string1, heltal):
    """
    multiply string
    """
    # if string1.isdigit():
    #     print("You need to input a string!")
    #     string1 = str(input("Enter a string: "))

    # elif heltal.isalpha:
    #     print("You need to input an integer!")
    #     heltal = input("Enter an integer: ")

    heltalstring = str(string1) * int(heltal)
    return heltalstring

def mask_string(stringmask):
    """
    mask string
    """
    newstringmask = multiply_str(stringmask, 1)

    if newstringmask != "":
        mask = ""
        masklist = []

        for char in newstringmask:
            masklist.append(char)

        masklist[0:-4] = "#" * len(masklist[0:-4])

        for number in masklist:
            mask += number

    return mask

def find_all_indexes(firststring, indexstring):
    """
    find all indexes
    """

    start = -1
    platser = [] 

    while True:
        try:
            plats = firststring.index(indexstring, start + 1)
        except ValueError:
            print("")
            break
        else:
            platser.append(plats)
            start = plats
    platser = ",".join([str(p) for p in platser])
    return platser

def eua1():
    """
    extrauppgift 1
    """
    print("Please input two words, and I shall compare them to eachother!")
    string1 = input("Word 1: ")
    string2 = input("Word 2: ")
    if string1.lower() in string2.lower() or string2.lower() in string1.lower():
        return ("Match!")
    return ("No match!")

def eua3():
    """
    extrauppgift 3
    """
    letter = input("Type a sentence with tabs for spaces: ")
    if "\t" in letter:
        print(letter.replace("\t", "   "))
        return None
    print("No tabs!")
    return None
