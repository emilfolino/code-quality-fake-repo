#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Functions for marvin program
"""

import random


def greet():
    """
    Function for asking for users name
    """
    name = input("What is your name? ")
    print("\nAlf says:\n")
    print("Hello %s - i have a cousin with a similar name!" % name)
    print("What can I do you for?!")

def celcius_to_farenheit():
    """
    Function for celsius to farenheit converter
    """
    celsius = input("Celsius: ")
    try:
        celsius = float(celsius)

        farenheit = celsius * (9/5) + 32
        farenheit = round(farenheit, 2)
        print(str(farenheit))
    except ValueError:
        print("I've heard of numbers on planet earth")

def word_manipulation():
    """
    Function for word manipulation
    """
    word = input("Your word(please something new): ")
    number = input("A number: ")
    try:
        word = str(word)
        number = int(number)

        new_word = multiply_str(word, number)
        print(str(new_word))
    except ValueError:
        print("Not correct!")

def sum_and_average():
    """
    Function for sum and averages
    """
    add = 0
    count = 0

    while True:
        try:
            num = input("number or are you done? ")
            if num == "done":
                break
            num = float(num)
            add += num
            count += 1
        except ValueError:
            print("Wrong answer!")

    average = round(add / count, 2)
    add = round(add, 2)
    print("The sum of all numbers are", str(add), "and the average is",
     str(average))

def hyphen_string():
    """
    Function to spice a word up
    """
    spaceword = input("Give me a funky word: ")
    index = 0
    accu = 1
    empty = ""

    while index < len(spaceword):
        letter = spaceword[index] * accu
        empty += str(letter) + "-"
        index = index + 1
        accu = accu + 1
    print(empty[:-1])

def is_isogram():
    """
    Function to check if word is isogram
    """
    word = input("Give me your holo...isogram: ")
    word = word.lower()
    count = 0

    for i in word:
        count += word.count(i)
    if count == len(word):
        print('Match!')
    else:
        print('No match!')

def compare_numbers():
    """
    Function to compare numbers
    """
    while True:
        num_1 = input("number or done?: ")
        if num_1 == "done":
            break
        else:
            try:
                num_1 = float(num_1)
                break
            except ValueError:
                print("not a number!")
                continue


    while num_1 != "done":
        num_2 = input("number or done?: ")
        if num_2 == "done":
            break
        else:
            try:
                num_2 = float(num_2)
            except ValueError:
                print("not a number!")
                continue

            if float(num_2) > float(num_1):
                print("larger!")
            elif float(num_2) == float(num_1):
                print("same!")
            else:
                print("smaller!")
            num_1 = num_2

def randomize_string(a_string):
    """
    Function to randomize letters in string
    """


    new_string = (''.join(random.sample(a_string,len(a_string))))

    return(a_string + " --> " + new_string)

def get_acronym(name):
    """
    Function to convert string into acronym
    """
    acronym = ""

    for i in name:
        try:
            name = str(name)
        except ValueError:
            print("not a string!")
            break
        if i.isupper():
            acronym += i

    return(acronym)

def mask_string(string):
    """
    Function to mask all but 4 last letters in a string
    """
    last_4 = string[-4:]
    before_4 = string[:-4]
    word = "#"
    num = len(before_4)

    string = multiply_str(word, num) + last_4
    return(string)

def multiply_str(word, num):
    """
    Function to duplicate string * integer
    """

    duplicate = word * num
    return(duplicate)

def find_all_indexes(str_1, str_2):
    """
    Function to compare and find indexes of a substring in another string
    """
    index = 0 - len(str_2)
    index_values = ""

    try:
        while True:
            index = str_1.index(str_2, index + len(str_2))
            index_values += str(index) + ","
    except ValueError:
        pass
    return(index_values[:-1])
