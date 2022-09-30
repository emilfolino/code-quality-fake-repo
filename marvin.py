#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Marvin with a simple menu to start up with.
Marvin doesnt do anything, just presents a menu with some choices.
You should add functinoality to Marvin.
"""

import random

def greet():
    """
    Greet the user
    """
    name = input("What is your name? ")
    print("\nMarvin says:\n")
    print("Tjena mors %s - your awesomeness!" % name)
    print("What can I do you for?!")

def celcius_to_farenheit():
    """
    Convert celsius too farenheit
    """
    celsius = input("How many degrees celsius do you want too convert? ")
    fahrenheit = round(9 * float(celsius) / 5 + 32, 2)
    print("\nMarvin says:\n")
    print(str(celsius) + "°C, that is " + str(fahrenheit) + "°F.")

def word_manipulation():
    """
    Multiply a string
    """
    word = input("What word do you want to multiply? ")
    times = int(input("How many times do you want too multiply the word? "))
    result = multiply_str(word, times)
    print("\nMarvin says:\n")
    print(result)

def sum_and_average():
    """
    Get sum and avrage from numbers
    """
    result = 0
    amount = 0
    avrage = 0
    while True:
        number = input("Give me a number or type 'done' if you have no more numbers. ")
        if number == "done":
            break
        else:
            result += float(number)
            amount += 1
    if amount != 0:
        avrage = round(result/amount, 2)
    result = round(result, 2)
    print("\nMarvin says:\n")
    print("The sum of all numbers are " + str(result) + " and the avrage is " + str(avrage))

def hyphen_string():
    """
    Multiply characters
    """
    word = input("Give me a word. ")
    new_word = ""
    for i in range(1, len(word)+1):
        if i == 1:
            new_word = word[0]
        else:
            new_word += "-" + word[i-1] * i
    print("\nMarvin says:\n")
    print(new_word)

def is_isogram():
    """
    Check if string is isogram
    """
    word = input("Give me a word. ")
    isMatch = True
    for count1, value1 in enumerate(word):
        for count2, value2 in enumerate(word):
            if count1 != count2:
                if value1 == value2:
                    isMatch = False
                    break
    print("\nMarvin says:\n")
    if isMatch is True:
        print("Match!")
    else:
        print("No match!")

def compare_numbers():
    """
    Check if number is larger, same or smaller
    """
    current_num = 0
    while True:
        inp = input("Give me a number or type 'done' too stop. ")
        if inp == "done":
            break
        else:
            try:
                if current_num == 0:
                    current_num = float(inp)
                else:
                    new_num = float(inp)
                    if new_num > current_num:
                        print("\nMarvin says:\n")
                        print("larger!\n")
                    elif new_num == current_num:
                        print("\nMarvin says:\n")
                        print("same!\n")
                    else:
                        print("\nMarvin says:\n")
                        print("smaller!\n")
                    current_num = new_num
            except ValueError:
                print("not a number!")

def randomize_string(w):
    """
    Randomize order of letters in a string
    """
    old_word = w
    new_word = ""
    while w != "":
        r = random.randrange(0, len(w))
        new_word += w[r]
        w = w[:r] + w[r+1:]
    return old_word + " --> " + new_word

def get_acronym(w):
    """
    Get acronym from a string
    """
    big_letters = ""
    for i in w:
        if i.isupper() is True:
            big_letters += i
    return big_letters

def mask_string(p):
    """
    Mask every letter except the last 4 in a string
    """
    p = multiply_str("#", len(p)-4) + p[len(p)-4:] 
    return p

def multiply_str(w, i):
    """
    Mulstiply a string
    """
    return w * i

def find_all_indexes(w, c):
    """
    Find index of the searched string in a string
    """
    indexes = ""
    for i in range(0, len(w)):
        try:
            w.index(c, i, i+len(c))
            if indexes == "":
                indexes += str(i)
            else:
                indexes += "," + str(i)
        except ValueError:
            pass
    return indexes
