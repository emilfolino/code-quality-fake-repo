#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Module for main.py that includes functions for Marvin
"""

import random

# FUNCTIONS FOR MARVIN1 #


def greet():
    """
    Greets the user
    """
    name = input("And what might you be called? ")
    print("\nElky says:\n")
    print("Pfft... %s - what are you doing in my forest?" % name)
    print("Why are you here?!")


def celcius_to_farenheit():
    """
    Converts celcius to fahrenheit
    """
    try:
        celsius = float(input(
            "Ah, so you're american, I see. Please enter a temperature in celsius: \n"))
        fahrenheit = round((1.8 * celsius + 32), 2)
        print("{} celsius is {} fahrenheit. Are you happy now?".format(
            celsius, fahrenheit))
    except ValueError:
        print('No, no, no! You must enter a temperature, NUMBERS my friend!')


def word_manipulation():
    """
    Multiplies a word based on user input
    """
    multiplied_word = input('Please enter a word to multiply: \n')
    try:
        multiplication_factor = int(
            input("Now please enter a number and watch the magic.\n"))
        final_multiplied_word = multiply_str(
            multiplied_word, multiplication_factor)
        print(final_multiplied_word)
    except ValueError:
        print('No dummy! I said a NUMBER. Moooose!')


def sum_and_average():
    """
    Calculates sum and avg of user inputs
    """
    total = 0
    count = 0
    while True:
        number_input = input(
            'Please enter a(nother) number (write "done" to calculate sum and avg): ')
        if number_input == 'done':
            break
        try:
            total += float(number_input)
            count += 1
        except ValueError:
            print('Please input a number.')
    if count:
        total = round(total, 2)
        average = round(total / count, 2)
        print("Seems like you've had enough fun. The sum of all numbers was {} and the average was {}".format(
            total, average))


def hyphen_string():
    """
    Makes a string all weird.
    """
    hyphenword_input = input(
        'Please enter a word and watch some naughty business: \n')
    counter = 1
    s = ''
    hyphen = '-'
    for char in hyphenword_input:
        char *= counter
        s += char + hyphen
        counter += 1
    s = s[:-1]
    print(s)


def is_isogram():
    """
    Checks if a word is an isogram.
    """
    isogram_input = input(
        "Please enter a word to determine whether it is an isogram: \n")
    s = ''
    message = True

    for letter in isogram_input:
        if letter in s:
            message = False
        s += letter
    if not message:
        print('No match!')
    else:
        print('Match!')


def compare_numbers():
    """
    Compares numbers and outputs whether 
    the most recent input is smaller, larger or equal to the previous.
    """
    second_number_input = None
    done = False
    try:
        first_number_input = float(input('Please enter a number: \n'))
    except ValueError:
        print('not a number!')

    while not done:
        try:
            first_number_input = float(first_number_input)
            second_number_input = input('Please enter a(nother) number: \n')
            if second_number_input == 'done':
                done = True
                continue
            second_number_input = float(second_number_input)
        except ValueError:
            print('not a number!')
        else:
            if second_number_input > first_number_input:
                print('larger!')
            elif second_number_input == first_number_input:
                print('same!')
            elif second_number_input < first_number_input:
                print('smaller!')
            first_number_input = second_number_input


def string_match():
    """
    Checks if all letters in sub_string are in main_string
    """
    message = True
    main_string = input('Please enter a string. \n')
    sub_string = input('Please enter the string to compare to. \n')

    for letter in sub_string:
        if letter not in main_string:
            message = False
        elif letter in main_string:
            main_string = main_string.replace(letter, "")
    if message:
        print('Match!')
    else:
        print('No match!')


def zeronine_multiply():  # change this function to something better
    """
    Gets a set number of tries to multiply a number by 2 in order to get
    a number that includes all numbers between 0-9. Outputs the number of tries.
    """
    number_input = int(input('Please enter a number to check: \n'))
    amount_of_tries = int(input('Please enter the amount of tries: \n'))
    counter = 0
    while amount_of_tries >= 0:
        number_in_list = True
        for nr in range(10):
            if str(nr) not in str(number_input):
                number_in_list = False
        if not number_in_list and amount_of_tries == 0:
            counter = -1
            break
        elif not number_in_list:
            number_input *= 2
            counter += 1
            amount_of_tries -= 1
        else:
            break
    print('Answer: {} times.'.format(counter))


def tab_to_space():
    """
    Converts tabs in a string to three spaces.
    """
    inp = input('Input a string: ')
    word = ''
    for letter in inp:
        if letter == '\t':
            letter = '   '
        word += letter
    print(word)


def brangelina():
    """
    Combines two strings (names) into a cheesy hollywood couple name, such as brangelina. 
    """
    vowels = ["a", "e", "i", "o", "u", "y"]
    first_name = input('Please enter a name: \n')
    second_name = input('Please enter another name: \n')
    index = 0
    index_two = 0

    for char in first_name:
        if char in vowels:
            first_sliced_name = first_name[:index]
            break
        index += 1
    for letter in second_name:
        if letter in vowels:
            second_sliced_name = second_name[index_two:]
            break
        index_two += 1
    full_name = first_sliced_name + second_sliced_name
    print(full_name)


def point_system():
    """
    Calculates points for different players based on a string.
    Small letters give the points that the integer after it holds, 
    big letters remove it. 
    """
    point_string = input('Input a string: ')  # "a2b4A5s3B1"
    final_str = ""
    used_letters = ""
    lowercase = point_string.lower()

    for letter in lowercase:
        result = 0
        if letter in used_letters or letter.isdigit():
            continue
        used_letters += letter
        for i, char in enumerate(point_string):
            if char == letter:
                result += int(point_string[i+1])
            elif char == letter.upper():
                result -= int(point_string[i+1])
        final_str += letter + " " + str(result) + ", "
    print(final_str[:-2])

# FUNCTIONS FOR MARVIN2 #


def randomize_string(nonrandom_string):
    """
    Shuffles characters in a string
    """
    charlist = []
    for char in nonrandom_string:
        charlist.append(char)
    random.shuffle(charlist)
    joined = ''.join(charlist)
    return f'{nonrandom_string} --> {joined}'


def get_acronym(acronym_string):
    """
    Creates an acronym based on a string.
    """
    acronym = ""
    for c in acronym_string:
        if c.isupper():
            acronym += c
    return acronym


def mask_string(unmasked_string):
    """
    Masks a string except for the last 4 chars
    """
    last_four = unmasked_string[-4:]
    multiply = len(unmasked_string[:-4])
    masked_string = multiply_str('#', multiply) + last_four
    return masked_string


def multiply_str(multipled_string, multi_factor):
    """
    Multiplies a string
    """
    return multipled_string * multi_factor


def find_all_indexes(main_i_string, sub_i_string):
    """
    Finds all index places in a main string compared to sub string.
    """
    start = 0
    indexed = ""
    try:
        while start < len(main_i_string):
            find_index = main_i_string.index(sub_i_string, start)
            indexed += str(find_index) + ','
            start = find_index + 1
    except ValueError:
        return indexed.rstrip(',')
    return indexed.rstrip(',')

# FUNCTIONS FOR EXTRA ASSIGNMENTS NEW MARVIN #


def points_to_grade(max_points, score):
    """
    Scoring system!
    """
    try:
        max_points = int(max_points)
        score = int(score)
        if score < 0 or score > max_points:
            return 'Please enter positive numeric values.'
    except ValueError:
        return 'Please enter positive numeric values.'

    if score >= (0.9*max_points):
        grade = 'A'
    elif score >= (0.8*max_points):
        grade = 'B'
    elif score >= (0.7*max_points):
        grade = 'C'
    elif score >= (0.6*max_points):
        grade = 'D'
    else:
        grade = 'F'

    return f'score: {grade}'


def has_strings(string_main, string_start, string_contain, string_end):
    """
    Compares first string with the following three ones.
    """
    output = "No match"
    if (string_main.startswith(string_start) and
        string_contain in string_main and
            string_main.endswith(string_end)):
        output = "Match"
    return output
