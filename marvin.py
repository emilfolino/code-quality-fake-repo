#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Functions for marvin
"""
import random
def greet():
    """
    Greets user
    """
    name = input("What is your name? ")
    print("\nMarvin says:\n")
    print("Welcome %s," % name)
    print("Is there anything i can help you with?")

def celcius_to_farenheit():
    """
    Converts Celcius to Fahrenheit
    """
    celsius = float(input("What is your temperature in Celsius: "))
    fahrenheit = round(celsius * 9 / 5 + 32, 2)
    print("\nMarvin says:\n")
    print("Your temperature is equal to: " + str(fahrenheit) + "°F")


def multiply_str(word, number):
    """
    Multiplies a string and print it out

    """ 
    word_number = number * word
    return word_number


def word_manipulation():
    """
    Calls upon function to multiply a string
    """
    user_word = input("Type a word that you would like multiplied: ")
    user_num = int(input("How many times would you like your word to be multiplied: "))
    print(multiply_str(user_word, user_num))

def sum_and_average():
    """
    Lets the user enter number and then adds and calculate the average
    """
    counter = 0
    my_sum = 0
    usr_input = ""
    while usr_input != "done":
        counter += 1
        usr_input = input("Enter a number or type 'done' to calculate current numbers: ")
        if usr_input == "done":
            counter -= 1
            break
        my_sum += round(float(usr_input), 2)
    average = round(my_sum / counter, 2)
    print("\nMarvin says:\n")
    print("The sum is: " + str(round(my_sum, 2)) + " And the average is: " + str(average))


def hyphen_string():
    """
    Manipulates input word with special characters
    """
    add_word = ""
    counter = 0
    word = input("Type a word: ")
    for letter in word:
        counter += 1
        add_word += letter * counter + "-"
    print("\nMarvin says:\n")
    print(add_word[:-1])


def is_isogram():
    """
    Checks if a word is an isogram or not
    """
    word = input("Type a word: ")
    if len(word) == len(set(word)):
        print("\nMarvin says:\n")
        print("Match!")
    else:
        print("\nMarvin says:\n")
        print("No match!")


def compare_numbers():
    """
    Compares input numbers if they are larger, smaller or the same as the previous entered number
    """
    end = ""
    number = float(input("Enter a number: "))
    while end != "done":
        try:
            pre_num = input("Enter a number or type 'done' to exit: ")
            if pre_num == "done":
                break
            if number < float(pre_num):
                print('larger!')
            if number > float(pre_num):
                print('smaller!')
            elif number == float(pre_num):
                print('same!')
            number = float(pre_num)
        except ValueError:
            print('not a number!')

def randomize_string(randomizer):
    """
    Takes a string and then shuffles the order of the letters
    """
    mystring = randomizer
    randomizer = list(randomizer)
    random.shuffle(randomizer)
    randomizer = ''.join(randomizer)
    mystring += " --> " + randomizer
    return mystring


def get_acronym(a_string):
    """
    Creates an acronym for the user when entering name
    """
    acronym = ""
    for letter in a_string:
        if letter.isupper():
            acronym += letter
    return acronym



def mask_string(a_string):
    """
    Masks every character in a string except last 4
    """
    last_four = a_string[-4:]
    word = len(a_string[0:-4])
    number = "#"
    return multiply_str(word, number) + last_four



def find_all_indexes(haystack, needle):
    """
    Finds all occurences of substring in string and prints out the index position of substring
    """
    needle_list = ''
    start = 0
    try:
        if needle in haystack:
            for i in haystack:
                i = haystack.index(needle, start, len(haystack))
                needle_list += str(i) + ","
                start = i + 1
                if start > len(haystack):
                    break
                
    
    except ValueError:
        return needle_list[:-1]
        
    else:
        return needle_list[:-1]
