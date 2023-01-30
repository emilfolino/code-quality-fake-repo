#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Marvin functions
"""

import random

def print_menu():
    """Skriver ut meny"""
    marvin_image = r"""
    ---------------------------------------
        .-.
       (@ @)
      \ \-/   Hi, I'm Marvin. I know it all.
       \/ \
        \ /\  What can I do for you?
        _H_ \
    ---------------------------------------
    """
    print(chr(27) + "[2J" + chr(27) + "[;H")
    print(marvin_image)
    # print("1) Present yourself to Marvin.")
    # print("2) Transform temperature in Celsius to Farenheit.")
    # print("3) Print a word x times.")
    # print("4) Sum and mean.")
    # print("5) Expand string.")
    # print("6) Check if isogram.")
    # print("7) Larger, smaller or same.")
    # print("8) Randomize word.")
    # print("9) Acronym creator.")
    # print("10) Mask string.")
    # print("11) Find all indexes.")
    print("12) Countries in 'country_data'.")
    print("13) Emission difference.")
    print("14) Country info.")
    # print("a1 Check if characters exist.")
    # print("a2 Double.")
    # print("a3 Replace tab.")
    # print("a4 Implode name.")
    # print("a5 Count points.")
    # print("b1 Points to grade.")
    # print("b2 Has strings.")
    print("e1 Emission per country.")
    print("b2 Emission per capita.")
    print("b2 Emission per area.")
    print("q) Quit." + "\n\n"
    "Also try my inv commands for my bag; inv, inv pick, inv drop, inv swap")

def greet():
    """ Hälsar på dig """
    name = input("What is your name? ")
    print("\nMarvin says:\n")
    print("Hello %s!" % name)
    print("What can I do for you?")


def celcius_to_farenheit():
    """Räknar om grader, C till F """
    x = True
    while x:
        tempC = input("Please give a temperature in Celsius: ")
        try:
            tempF = float(tempC) * 9/5+32
            x = False
        except ValueError:
            print("\nPlease answer with a number.\n")
            continue
    tempF_r = round(tempF, 2)
    print("\nMarvin says:\n")
    print("The temperature in Farenheit is %s." % tempF_r)
    print("What can I do for you?")


def word_manipulation():
    """Skriver ett ord flera ggr"""
    x = True
    while x:
        word = input("Please give a word: ")
        try:
            number = int(input("How many times shall I print the word? "))
            x = False
        except ValueError:
            print("That was not a number")
            continue
    print("\nMarvin says:\n")
    new_word = multiply_str(word, number)
    print(new_word)
    print("What can I do for you?")

def sum_and_average():
    """Beräknar summa och medelvärde"""
    sum_numbers = 0
    counter = 0
    number = 0

    while True:
        number = input("Give a number:") # Obs, svaret är en sträng - måste omvandlas
        if (number == "done"):
            break
        else:
            try:
                sum_numbers += float(number)
            except ValueError:
                print("That was not a number")
                continue
            counter+=1

    mean = float(sum_numbers) / counter
    sum_r = round(sum_numbers, 2)
    mean_r = round(mean, 2)
    print("\nMarvin says:\n")
    print("The sum of the numbers is " + str(sum_r) + " and the mean is " + str(mean_r) + ".")
    print("What can I do for you?")

def hyphen_string():
    """ Bindestreck i ord"""
    word = input("Please give a word: ")

    print("\nMarvin says:\n")
    new_word = ""
    counter = 1
    for letter in word:
        new_word += letter*counter + "-"
        counter+=1
    print(new_word[0:len(new_word)-1])

    print("What can I do for you?")

def is_isogram():
    """Kollar om ord är isogram"""
    word = input("Please give a word: ")

    print("\nMarvin says:\n")

    counter = 0
    iso = False

    type(counter)
    type(len(word))

    for letter in word:
        for another_letter in word[counter+1: len(word)]:
            if letter == another_letter:
                iso = True
        counter+=1

    if iso:
        print("No match! - Not Isogram - contains reoccurring letters")
    else:
        print("Match! - Isogram - no reoccurring letters")

    print("What can I do for you?")

def compare_numbers():
    """Kollar om nummer är större/mindre/samma"""
    while True:
        try:
            number = float(input("Please give a number: "))
            break
        except ValueError:
            print("That was not a number!")
            continue

    while True:
        new_number = input("Please give another number: ")
        if (new_number == "done"):
            break
        else:
            try:
                new_number = float(new_number)
            except ValueError:
                print("That was not a number")

        if new_number > number:
            print("larger!")
        elif new_number < number:
            print("smaller!")
        else:
            print("same!")

        number = new_number


    print("What can I do for you?")


def letters_in_word():
    """ Kollar om alla bokstäver i ord1 finns i ord2"""
    word1 = input("String: ")
    word2 = input("String2: ")

    counter = 0
    for letter2 in word2:
        for letter1 in word1:
            if letter2 == letter1:
                counter+=1

    if counter >= len(word2):
        print("Match!")
    else:
        print("No match!")


def a2():
    """?"""
    #     number = input("Number: ")
    #     times = input("Times: ")

    #     counter = 0
    #     for time in range(times):
    #         check = time*number
    #         for x in range(0, 10):
    #             for numb in range(0, 10):
    #                 if x == numb:
    #                     counter+=1
    #             if counter == 

    #                 counter+=1
        
    #     if counter >= len(word2):
    #         print("Match!")
    #     else:
    #         print("No match!")


def randomize_string(word):
    """ Slumpar bokstäverna i ett ord"""
    new_word = ""
    length = len(word)
    tempword = word

    for i in range(length):
        rand = random.randint(0, length-i-1)
        new_word += word[rand:rand+1]
        word = word[:rand] + word[rand+1:]

    return tempword + " --> " + new_word

def get_acronym(string):
    """ Tar fram en akronym"""
    acro = ""
    for letter in string:
        if letter.isupper() is True:
            acro += letter
    if (acro != ""):
        return acro
    return "No acronym could be created"

def mask_string(string):
    """Maskerar en sträng med #"""
    chars = string[-4:]
    length = len(string)-4
    b = "#"
    new_word = multiply_str(b, length)
    new_word = new_word + chars
    return new_word

def multiply_str(a, b):
    """Multiplicerar en sträng"""
    new_word = ""
    b = int(b)
    for _ in range(b):
        new_word += a
    return new_word

def find_all_indexes(string1, string2):
    """Hittar index"""
    new_string = ""

    for i in range(len(string1)):
        try:
            if (string1.index(string2, i) == i):
                new_string += str(i) + ","
        except ValueError:
            continue
    new_string = new_string[0:-1]
    return new_string

def points_to_grade(string1, string2):
    """Räknar om poäng till betyg"""
    while True:
        try:
            string1 = int(string1)
            break
        except ValueError:
            print("Ange maxpoäng som en siffra!")

    while True:
        try:
            string2 = int(string2)
            break
        except ValueError:
            print("Ange dina poäng som en siffra!")

    perc = string2/string1*100

    if (perc >= 90):
        return "score: A"
    if (perc >= 80):
        return "score: B"
    if (perc >= 70):
        return "score: C"
    if (perc >= 60):
        return"score: D"
    if (perc < 60):
        return "score: F"

def has_strings(string1, string2, string3, string4):
    """ Kollar om sträng ingår"""
    if (string1.startswith(string2) and
        string3 in string1 and
        string1.endswith(string4)):
        return "Match"
    return "No match"
