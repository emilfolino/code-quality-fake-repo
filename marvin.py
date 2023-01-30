#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Functions for marvin in kmom03
"""

import random
last_num = ""

def meImage():
    """
    Holds ascii-image
    """
    return r"""
                _
            /\\_\_.-----.___  _.._
                / _    _      \//   \
                / /      \       Y--  |
                |  /\  /\        \ __/
    ___________| _*/__*/_        \_
    /   \\      +----.    ____      \_
    \    ||           \__/ / /        \
    +---+/               / /        /\\
    \ \                / /       _/
    '-+----._____,---' /      -'  \
        \___________--'            \
                /                     \
                /                       \
    """



def greet():
    """
    Function for greeting with name from input
    """
    name = input("What is your name? ")
    print("\nMarvin says:\n")
    print("Hello there %s - nice to meet you!" % name)
    print("What can I do you for?!")



def celcius_to_farenheit():
    """
    Converts celsius to farenheit
    """
    celsius = float(input("What is the temperature in celsius? "))
    farenheit = celsius * 9 / 5 + 32
    farenheit_rounded = round(farenheit, 2)
    print(f"{celsius} celsius would be {farenheit_rounded} farenheit.")


def word_manipulation():
    """
    Takes a string from input and multiplies it by the number from the second input
    """
    multiply_string = input("What word should i repeat? ")
    multiply_number = input(f"How many times would you like {multiply_string} to be repeated? ")
    multiply_str(multiply_string, multiply_number)
    print(multiply_str(multiply_string, multiply_number))




def sum_and_average():
    """
    Adds numbers together until "done" is entered, then presents the total and the median value
    """
    math_num = 0
    math_sum = 0
    math_amount = 0
    
    print("Keep giving me numbers and i will sum them up for you. Write 'done' when you're happy.")
    
    while True:
        math_num = input("Hit me! ")
        if str(math_num) == "done":
            break
        math_sum = float(math_sum)
        math_num = float(math_num)
        math_sum += math_num
        math_amount += 1
        math_divided = math_sum / math_amount

    print(f"The total is {round(math_sum, 2)} and the median value is {round(math_divided, 2)}!")



def hyphen_string():
    """
    Takes a word from input, for each letter the letter is multiplied by +1
    """
    repeat_word = input("What word should i work my magic on? ")
    repeated_word = ""
    i = 0
    while i < len(repeat_word):
        if i != 0:
            repeated_word += "-"
        repeated_word = str(repeated_word) + repeat_word[i] * (i + 1)
        i += 1
    print(repeated_word)



def is_isogram():
    """
    Calculates if a word from input is an isogram
    """
    isogram_word = input("Type a word to check if it's an Isogram! ")
    isogram_word = isogram_word.lower()
    letter_list = []
    isogram_result = "Match!"
    for letter in isogram_word:
        if letter in letter_list:
            isogram_result = "No match!"
        letter_list.append(letter)
    print(isogram_result)



def compare_numbers():
    """
    Compares numbers from input to determine if each number is smaller, the same or larger than the previous
    """
    print("Write me some numbers and I'll let you know if its bigger or smaller than the last number! ")
    while True:
        global last_num
        current_num = input("Hit me! --> ")
        if current_num == "done":
            break
        if last_num == "":
            last_num = int(current_num)
            current_num = input("Enter another number --> ")
        try:
            current_num = int(current_num)
            if current_num > last_num:
                print(f"{current_num} is larger!")
                last_num = current_num
            elif current_num < last_num:
                print(f"{current_num} is smaller!")
                last_num = current_num
            else:
                print(f"{current_num} and {last_num} are the same!")
                last_num = current_num
        except ValueError:
            print(f"{current_num} is not a number!")





def randomize_string(randomize_input):
    """
    Takes a word from input and randomizes each character
    """
    randomize_word = list(randomize_input)
    random.shuffle(randomize_word)
    randomize_word = "".join(randomize_word)
    #randomize_result = print(f"{randomize_input} --> {randomize_word}")
    return f"{randomize_input} --> {randomize_word}"



def get_acronym(acronym_input):
    """
    Creates a acronym from each capital letter in input string
    """
    acronym = ""
    for char in acronym_input:
        if char.isupper():
            acronym += char
    return acronym



def mask_string(mask_string_input):
    """
    Masks everything but the 4 last character in input string with "#"
    """
    multiply_string = "#"
    multiply_number = len(mask_string_input[:-4])
    multiply_str(multiply_string, multiply_number)
    masked_string = multiply_str(multiply_string, multiply_number) + mask_string_input[-4:]
    return masked_string



def multiply_str(multiply_string, multiply_number):
    """
    Takes a string from input and multiplies it by the number from the second input
    """
    return multiply_string * int(multiply_number)



def find_all_indexes(sentence, sub_sentence):
    """
    Finds all indexes from the first string, searching for the second string
    """
    index_result = ""
    i = 0
    while i < len(sentence):
        try:
            i = sentence.index(sub_sentence, i)
            index_result += str(i) + ","
            i += 1
        except ValueError:
            break
    return index_result[:-1] 
