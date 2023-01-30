#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
functions for Marvin
"""
import random

def greet():    #1
    """
    val 1
    Marvin says Hi
    """
    name = input("What is your name? ")
    print("\nMarvin says:\n")
    print(f"Hello {name} - Live long and prosper!")
    print("What can I do for you?")

def celcius_to_farenheit(): #2
    """
    val 2
    convert celsius to farenheit
    output with 2 decimals
    """
    fahrenheit = 0
    celsius = input("°C : ")
    try:
        celsius = float(celsius)
    except ValueError:
        print("That was not a number.")
    else:
        fahrenheit = round(celsius*9/5 + 32, 2)
        print(f"{celsius} °C equals {fahrenheit} °F.")

def word_manipulation():#3
    """
    val 3
    manipulate a word
    new word = word multiplied with a number
    """
    word = input("Word : ")
    number = input("Number : ")
    # multiplied_word = ""
    try:
        number = int(number)
    except ValueError:
        print("The number needs to be an integer")
    else:
        print(f"{multiply_str(word, number)}")
    #     for _ in range(number):
    #         multiplied_word += word
    #     print(f"{multiplied_word}")

def sum_and_average():  #4
    """
    val 4
    add all numbers. output in str with 2 decimals
    """
    sum_numbers = 0
    average = 0
    n_numbers = 0
    while True:
        number = input("Number : ")
        if number != "done":
            try:
                number = float(number)
            except ValueError:
                print("\nThat is not a number.")
                continue
            else:
                sum_numbers += number
                n_numbers += 1
        else:
            average = round(sum_numbers/n_numbers, 2)
            sum_numbers = round(sum_numbers, 2)
            print(
                f"The sum of all numbers is {sum_numbers} and the "
                f"average is {average}.")
            break

def hyphen_string():    #5
    """
    val 5
    increase each letter in string by 1. separate eith "-"
    """
    new_word = ""
    nr_of_letters = 0
    word = input("Word : ")
    for letter in word:
        nr_of_letters += 1
        for _ in range(nr_of_letters):
            new_word += letter
        new_word += "-"
    new_word = new_word[:-1]
    print(f"New word : {new_word}")

def is_isogram():   #6
    """
    val 6 isogram
    """
    not_isogram = False
    word = input("Word : ")
    iso_word = word
    for letter in word:
        iso_word = iso_word[1:]
        if letter in iso_word:
            not_isogram = True
            break
    if not_isogram:
        print("No match!")
    else:
        print("Match!")

def compare_numbers():  #7
    """
    val 7 output "larger", "same", or "smaller" compared to previous value
    """
    previous_input = ""
    current_input = ""
    while True:
        current_input = input("\nnr : ")
        if current_input == "done":
            break
        else:
            try:
                previous_input = float(current_input)
            except ValueError:
                print("not a number!")
                continue
            else:
                break
    while isinstance(previous_input, float):
        current_input = input("\nnr : ")
        if current_input == "done":
            break
        else:
            try:
                current_input = float(current_input)
            except ValueError:
                print("not a number!")
                continue
            if current_input < previous_input:
                print("smaller!")
            elif current_input > previous_input:
                print("larger!")
            else:
                print("same!")
        previous_input = current_input

def randomize_string(word): #8
    """
    val 8 make a word into a random string
    """
    original = word
    random_word = ""
    a= ""
    while len(word) > 0:
        a = random.choice(word)
        random_word += a
        word = word.replace(a, "", 1)
    return f"{original} --> {random_word}"

def get_acronym(text):  #9
    """
    val 9 make an acronym
    """
    acronym = ""
    for i in text:
        if i.isupper():
            acronym += i
    return acronym

def mask_string(text):  #10
    """
    val 10 hide string with ###
    """
    i_split = len(text) - 4
    new_text2 = text[i_split:]
    new_text = multiply_str("#", i_split)
    return f"{new_text}{new_text2}"
    # ------- note to self. läs hela uppgiften innan du börjar-------------
    # mask = ""
    # for i in range(len(text) - 4):
    #     mask = text[i]
    #     text = text.replace(mask, "#", 1)
    # return text

def multiply_str(word, multi):  #10 and 3
    """
    val 10/3 multiply word with multi. return new string
    """

    new_word = ""
    for _ in range(multi):
        new_word += word
    return new_word

def find_all_indexes(text, sub_text): #11
    """
    val 11 list all indexes of sub_text in text separated with ","
    """
    indexes = ""
    i = 0
    while len(sub_text) <= len(text[i:]):
        try:
            i = text.index(sub_text, i)
            indexes += f"{i},"
            i += 1
        except ValueError:
            break
    if i > 0:
        indexes = indexes[:-1]
    return indexes

def points_to_grade(max_score, your_score): # b1
    """
    val b1 calculate grade
    """
    score = int(your_score) / int(max_score)
    grade = ""
    if score < 0.6:
        grade = "F"
    elif score < 0.7:
        grade = "D"
    elif score < 0.8:
        grade = "C"
    elif score < 0.9:
        grade = "B"
    else:
        grade = "A"
    return f"score: {grade}"

def has_strings(str1, str2, str3, str4):    #b2
    """
    val b2 compare strings
    """
    if str1.startswith(str2) and str1.endswith(str4) and str3 in str1:
        is_match = "Match"
    else:
        is_match = "No match"
    return is_match

def compare_strings():  #a1
    """
    val a1 compare if string1 is in string2
    """

    letters_match = False
    word = input("First word : ")
    test_word = input("second word :")
    for letter in test_word:
        if letter not in word:
            print("No match!")
            break
        else:
            letters_match = True
    if letters_match:
        print("Match!")

def square_add():   #a2
    """
    val a2 multiply by 2 and see if all nr exists
    """
    numbers_str = "1234567890"
    all_nr_exist = False
    start_value = input("\nnr : ")
    max_multi = input("\nnr : ")
    n_multi = 0
    nr_to_check = ""
    while True:
        try:
            start_value = int(start_value)
            max_multi = int(max_multi)
        except ValueError:
            print("\nOnly integers allowed.")
            break
        for _ in range(max_multi):
            nr_to_check = str(start_value)
            for char in numbers_str:
                if  char in nr_to_check:
                    all_nr_exist = True
                else:
                    all_nr_exist = False
                    start_value = start_value * 2
                    n_multi += 1
                    break   # first False == no match
            if all_nr_exist:
                print(f"Answer: {n_multi} times")
                break
        if not all_nr_exist:
            print("Answer: -1 times")
        break

def replace_tab():  #a3
    """
    val a3 replace "tab" with "   "
    """

    user_sentence = input("\nType something : ")
    new_sentence = user_sentence.replace("\t", "   ")
    print(new_sentence)

def brangelina():   #a4
    """
    val a4 Concat 2 names -> brad + angelina -> brangelina
    """
    vowels = "aeiouy"
    new_first_name = ""
    new_second_name = ""
    first_name_vowel = []
    second_name_vowel = []
    first_name = input("\nFirst name : ")
    second_name = input("\nSecond name : ")
    for letter in vowels:
        pos_first = first_name.find(letter)
        if pos_first >= 0:
            first_name_vowel.append(pos_first)
    for letter in vowels:
        pos_second = second_name.find(letter)
        if pos_second >= 0:
            second_name_vowel.append(pos_second)
    first_name_vowel.sort()
    second_name_vowel.sort()
    new_first_name = first_name[:first_name_vowel[0]]
    new_second_name = second_name[second_name_vowel[0]:]
    print(f"{new_first_name}{new_second_name}")

def player_score(): #a5
    """
    val a5 see how many points a player gets
    """

    msg1 = input("input: ")
    msg2 = msg1
    scoreboard = ""
    
    for letter in msg1:
        score = 0
        if letter.isalpha():
            x = letter.lower()
            while x in msg2: 
                pos1 = msg2.find(x)
                score += int(msg2[pos1 + 1])
                msg2 = msg2.replace(x, "", 1)
                msg2 = msg2.replace(msg2[pos1], "", 1)
            while x.upper() in msg2:
                pos2 = msg2.find(x.upper())
                score -= int(msg2[pos2 + 1])
                msg2 = msg2.replace(x.upper(), "", 1)
                msg2 = msg2.replace(msg2[pos2], "", 1)
            if not letter.lower() in scoreboard:   
                scoreboard += f"{letter.lower()} {score}, "
    print(scoreboard[:-2])
