#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Functions for our Phoenix chatbot
"""
import random


def multiply_str(word, number):
    """
    function to multiply strings
    """
    repeated_word = ""
    for _ in range(number):
        repeated_word += word
     
    return repeated_word

def greet():
    """
    choice 1. function for greeting the user 
    """
    name = input("Present yourself to Phoenix: ")
    print("\nPhoenix says:\n")
    print("Hello %s - looking...allright." % name)
    print("What can Phoenix do for you ?!")

def celcius_to_farenheit():
    """
    choice 2. function for converting celsius to fahrenheit
    """
    print("You want to convert celsius to fahrenheit?! but why...?")
    print("Allright, I'll do it")
    temp_celsius = float(input("Type in temperature in celsius: "))
    temp_fahrenheit = round((temp_celsius*9/5)+32, 2)
    print("Done! %s celsius is %s fahrenheit" % (str(temp_celsius), str(temp_fahrenheit)))

def word_manipulation():
    """
    choice 3. function to call for a function to multiply an inputed word from user
    """
    word = input("Your word: ")
    number = int(input("How many times to repeat it?: "))
    silly_word = multiply_str(word, number)

    return print("Your silly word is: %s" % silly_word)


def sum_and_average():
    """
    choice 4. function to find sum and mean value of all numbers inputed by user
    """
    sum_numbers = 0
    counter = 0
    while True:
        digit_or_done = (input("Type in a digit, to start, or done to finish calculations: "))
        if digit_or_done == "done":
            break
        else:
            sum_numbers += float(digit_or_done)
            sum_numbers = round(sum_numbers, 2)
            counter += 1
            mean_value = round(sum_numbers / counter, 2)
    print("Your total sum is %s and your mean value is %s " % (str(sum_numbers), str(mean_value)))

def hyphen_string():
    """
    choice 5. function to multiply every letter in a word by its position
    """
    counter = 1
    word = input("Type in your word: ")
    new_word = ""
    for i in word:
        new_word += i * counter + "-"
        counter += 1
        new_word2 = new_word.rstrip("-")
    print("Words fun version: %s" % new_word2)

def is_isogram():
    """
    choice 6. function to define if a word is an isogram or not
    """
    word = input("Your word: ")
    word2 = word.replace("-", "").replace(" ", "").lower()
    if len(word2) == len(set(word2)):
        print("Match!")

    else:
        print("No match!")

def compare_numbers():
    """
    choice 7. function to find if the latter users input is larger, smaller, or the same as users previous input
    """
    previous = 0
    current = 0
    while True:
        number = input("Type in number, or 'done': ")

        if number == "done":
            print("We are done here, wooosh")
            break
        else:
            
            try:
                current = int(number)
                if previous:
                    if current > previous:
                        print("larger!")
                    elif current < previous:
                        print("smaller!")
                    else:
                        print("same!")
            except ValueError:
                print("%s is not a number!" % number)
        previous = current

def randomize_string(original_string):
    """
    choice 8. Function to randomize character positions in a string given by user
    """
    character_list = list(original_string)
    random.shuffle(character_list)
    randomized_string = "".join(character_list)
    return original_string + " --> " + randomized_string

def get_acronym(comp_name):
    """
    choice 9. Function to build an acronym our of a string given by a user
    """
    acronym = ""
    for char in comp_name:
        if char.isupper():
            acronym += char

    return acronym
    

def mask_string(characters):
    """
    choice 10. Function to change all characters except last four into "#"
    """
    number = 1
    masked_string = multiply_str(characters, number)
    masked_string = ("#" * (len(masked_string) - 4))
    last_four_characters = characters[-4:]
    masked_multiplied_string = masked_string + last_four_characters
    return masked_multiplied_string


def find_all_indexes(text, x):
    """
    choice 11. Function to find all indexes of a given argument in a string
    """
    indexes = ""
    start = 0
    while True:
        try:
            found = text.index(x, start)
            start = found + 1
            indexes += str(found) + ","
        except ValueError:
            break   
    indexes_2 = indexes.rstrip(",")

    return indexes_2

def points_to_grade(max_points, your_points):
    """
    choice b1. Function to convert given amount of points into a grade based off of maximum points given by users \
    all the numbers are given by user, gradescale is implemented by Phoenix.
    """

    grade = int(your_points) / int(max_points)

    if grade >= 0.9:
        score = ("score: A")
    elif grade >= 0.8:
        score = ("score: B")
    elif grade >= 0.7:
        score = ("score: C")
    elif grade >= 0.6:
        score = ("score: D")
    else:
        score = ("score: F")

    return score
