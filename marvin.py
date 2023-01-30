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
    Asks the user for their name and greets them
    """
    name = input("What is your name? ")
    print("\nThe cat says:\n")
    print("Hello %s - MEOWWWWWWWWWWWW!" % name)
    print("What can I do you for?!")


def celcius_to_farenheit():
    """
    Converts celsius to fahrenheit
    """
    temp_c = input("Temperature in C: ")

    try:
        temp_f = round((float(temp_c) * 9 / 5 + 32), 2)
        print(f"{temp_c} Celsius is {temp_f} fahrenheit.")

    except ValueError:
        print("Error! Please enter a number...")

def word_manipulation():
    """
    Repeats a word
    """
    word = input("Please enter a word: ")
    str_multiply = input("How many times do you want the cat to repeat the word? ")

    try:
        print(word * int(str_multiply))

    except ValueError:
        print("Error! Please enter a number...")



def sum_and_average():
    """
    Prints sum of numbers from user input and their average
    """
    sum_of_numbers = 0
    user_inputs = 0
    while True:
        number_input = input("Please enter a number, press 'done' when done: ")

        if number_input == 'done':
            break
        else:
            try:
                sum_of_numbers = sum_of_numbers + float(number_input)
                user_inputs += 1
            except ValueError:
                print("Error! Please insert a number...")

    try:
        int_average = round((sum_of_numbers / user_inputs), 2)

    except ZeroDivisionError:
        int_average= "Can't divide by zero!"

    print(f"The cat calculated the sum of all numbers to {sum_of_numbers} and the average to be {int_average}")


def hyphen_string():
    """
    Takes input from user and adds letters to make it longer
    """
    user_input = input("Please enter a word for the cat: ")
    counter = 0
    new_long_word = ""

    for letter in user_input:
        counter += 1
        new_long_word = (new_long_word + letter * counter) + '-'

    print(new_long_word[:-1])


def is_isogram():
    """
    Checks if a word is an isogram
    """
    user_input = input("Please enter a word: ")
    match = False

    for letter in user_input:
        if user_input.count(letter) > 1:
            match = False
            break
        else:
            match = True

    if match:
        print("Match!")
    else:
        print("No match!")



def compare_numbers():
    """
    Compares two numbers from the user and checks if the latest one is larger than the previous
    """
    flag = True
    previous = None

    while flag:
        user_input = input("Please enter a number, write 'done' to quit: ")

        if user_input == 'done':
            flag = False
            continue
        if previous is None:
            previous = user_input
            user_input = input("Please enter a second number: ")


        try:
            user_input = float(user_input)
            previous = float(previous)

            if user_input > previous:
                print("larger!")
            elif user_input == previous:
                print("same!")
            elif user_input < previous:
                print("smaller!")
            previous = user_input

        except ValueError:
            print("not a number!")


def randomize_string(string):
    """
    Shuffles letters in a string
    """
    numbers = ""
    rand_word = ""

    for i in string:
        try:
            int(i)
            numbers += str(i)
        except ValueError:
            rand_word += i

    l = list(rand_word)
    random.shuffle(l)
    rand_word = ''.join(l)
    rand_word = rand_word + numbers

    return string + " --> " + rand_word


def get_acronym(string):
    """
    Takes all capital letter in a word and returns an acronym
    """
    acronym = ""

    for letter in string:
        if letter.isupper():
            acronym += letter

    return acronym

def multiply_str(string, number):
    """
    Multiplies a string
    """
    multiplied_string = ""

    try:
        multiplied_string = string * int(number)

    except ValueError:
        print("Error! Please enter a number...")

    return multiplied_string

def mask_string(string):
    """
    Masks all the characters in a string except for the last four.
    """
    last_four_characters = ""
    counter = -1

    while counter >= -4:
        last_four_characters = string[counter] + last_four_characters
        counter -= 1

    new_string = string[:len(string) - 4]
    masking = '#'
    masked_string = multiply_str(masking, len(new_string))

    return masked_string + last_four_characters


def find_all_indexes(string, sub_string):
    """
    find all indexes of substring in string
    """
    start = 0
    index_positions = ""
    for _ in string:
        try:
            start = int(string.index(sub_string, start)) + 1
            index_positions += str(start - 1) + ","
        except ValueError:
            continue

    return index_positions[:-1]

def points_to_grade(max_score, score):
    """
    Calculates a grade based on percentage of max score
    """

    percentage = (int(score) / int(max_score)) * 100
    grade = ""
    if percentage >= 90:
        grade = "A"
    elif percentage >= 80:
        grade = "B"
    elif percentage >= 70:
        grade = "C"
    elif percentage >= 60:
        grade = "D"
    else:
        grade = "F"
    return "score: " + grade

def has_strings(string1, string2, string3, string4):
    """
    Compares if the first string contains the other three strings.
    """
    string_list = [string2, string3, string4]
    counter = 0
    is_match = "No match"
    for i in string_list:
        if string1.startswith(i):
            counter += 1
        elif string1.endswith(i):
            counter += 1
        elif i in string1:
            counter += 1

    if counter == 3:
        is_match = "Match"
    return is_match
