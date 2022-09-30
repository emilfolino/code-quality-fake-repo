#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
Marvin functions. A collection of functions that main.py will call when selected
from the menu.
"""


# from math import trunc
import random as rnd


def greet():
    """
    Simple greet function, takes name as input and writes greeting msg
    """
    name = input("What is your name? ")
    print("\nMarvin says:\n")
    print(
        f"Hello {name} - I come in peace, take me to your leader "
        f"(or pick a choice below...)")
    print("What can I do for you?!")


def celcius_to_farenheit():
    """
    Celsius to Farenheit converter. input C output F
    """
    temp_celsius = float(
        input("Enter the temperature in degree Celsius: "))
    temp_farenheit = round((temp_celsius * 9 / 5) + 32, 2)
    print(f"The temperature is {temp_farenheit} degree Farenheit")


def word_manipulation():
    """
    Word repeater, input word as string and multiplication factor as int
    Output is word * factor
    """
    word = input("Enter your word of choice: ")
    number = int(input(
        "How many times would you like Marvin to repeat the word? "))
    print(multiply_str(word, number))


def sum_and_average():
    """
    Arithmetic function. Takes numbers as input and calculates sum and average
    Output sum and avg
    """
    sum_numbers = 0
    average = 0
    counter = 0
    input_number = input(
        "Enter your first number, type 'done' at any time to quit: ")

    while input_number != "done":
        counter += 1
        sum_numbers += float(input_number)
        average = sum_numbers / counter
        input_number = input("Enter next number, 'done' to quit. ")

    print("The sum is {sum_numbers} and the average is {average}".format(
        sum_numbers=round(sum_numbers, 2), average=round(average, 2)))


def hyphen_string():
    """
    String manipulator. Takes string as input and multiples each letter with
    its index in the input string, separated by -*index
    """
    input_string = input("Enter your string: ")
    output_string = ""
    factor = 1

    for i, char in enumerate(input_string):
        if i != len(input_string) - 1:
            output_string += char * factor + "-"
            factor += 1
        else:
            output_string += char * factor
            factor += 1

    print(output_string)


def is_isogram():
    """
    String comparison. Takes a string as ionput and checks wether it is an
    isogram. Outputs result of comparison
    """
    input_word = input("Enter your word: ")
    times_in_word = 0
    word_length = 0

    for char in input_word:
        word_length += 1
        for char2 in input_word:
            if char == char2:
                times_in_word += 1

    if times_in_word > word_length:
        print("No match!")
    else:
        print("Match!")


def compare_numbers():
    """
    Number comparison with try/except. Takes two numbers as input and compares
    them, keeps taking a new number until exit parameter is given. Outputs
    result of each comparison
    """
    num_one = input("Enter the first number, 'done' to quit: ")
    num_two = ""

    while num_one != "done":

        try:
            int(num_one)
        except ValueError:
            print("not a number!")
            num_one = input("Enter the first number, 'done' to quit: ")
            continue
        num_one = int(num_one)
        num_two = input("Enter a new number, 'done' to quit: ")

        if num_two != "done":
            try:
                int(num_two)
            except ValueError:
                print("not a number!")
                continue
            num_two = int(num_two)
            if num_two < num_one:
                print("smaller!")
            elif num_two == num_one:
                print("same!")
            else:
                print("larger!")
            num_one = num_two
        else:
            num_one = num_two


def randomize_string(my_string):
    """
    String function, takes string as arg, randomizes the chars and returns them
    as string
    """
    my_string_copy = my_string
    rand_string = ""

    while len(rand_string) < len(my_string):
        rand_index = rnd.randint(0, len(my_string_copy) - 1)
        rand_string += my_string_copy[rand_index]
        my_string_copy = str.replace(my_string_copy, my_string_copy[rand_index],
                                     "", 1)

    return f"{my_string} --> {rand_string}"


def get_acronym(my_string):
    """
    String function, searches string given as arg for uppercase letters and
    combines appends them to a new string.
    Returns new string
    """
    string_upper = ""
    for char in my_string:
        if char.isupper():
            string_upper += char

    return string_upper


def mask_string(my_String):
    """
    String function, takes string as arg and returns it with all but the
    last 4 chars replaced with #
    """
    return multiply_str("#", len(my_String) - 4) + my_String[-4:]


def multiply_str(my_string, factor):
    """
    String function, takes string and int as args, returns string * arg as new
    string
    """
    return my_string * factor


def find_all_indexes(my_string, my_other_string):
    """
    String function, takes two strings as arguments where string 2 must be a
    substring of string a. Produces the indexes of each instance of b in a.
    Returns string of indexes
    """
    index_counter = 0
    index_string = ""
    out_string = ""

    while True:
        try:
            char_pos = my_string.index(my_other_string, index_counter)
        except ValueError:
            break
        index_string += str(char_pos) + ","
        index_counter = char_pos + len(my_other_string)

    for i in range(0, len(index_string) - 1):
        out_string += index_string[i]

    return out_string


def string_comparison():
    """
    String comparison. Takes two strings as input and checks if all the letters
    in the second string can be found in the first
    Output is result of comparison
    """
    string1 = input("Enter first string: ")
    string2 = input("Enter second string: ")
    string3 = ''
    # char_counter = 0
    # string2_length = 0

    for char in string2:
        if char in string1:
            string3 += char

    if string3 == string2:
        print("Match!")
    else:
        print("No match!")


def times_to_all():
    """
    Arithmetics and comparison. Takes a number and a counter as input.
    Multiplies the number with 2 until every number 0-9 can be found.
    Runs for counter times, output number of tries until success
    """
    number = input("Enter a number: ")
    tries = int(input("How many tries does Marvin have? "))
    check_nums = "0123456789"

    for i in range(tries):
        number_check = 0
        for num in check_nums:
            if num in str(number):
                number_check += 1
        if number_check == 10:
            print(f"Answer: {i} times")
            break
        elif i == tries - 1:
            print("Answer: -1 times")
        number = int(number) * 2


def tab_to_spaces():
    """
    String converter. Takes a string as input and convers any tabs to 3*space
    Output converted string
    """
    string1 = input("Enter a string: ")
    string2 = ''

    for char in string1:
        if char != '\t':
            string2 += char
        else:
            string2 += ' ' * 3

    print(string2)


def combine_names():
    """
    String conversion. Takes two names as input and combines them. First name
    is read until first vowel and second name is read from first vowel.
    output combined name
    """
    name1 = input("Enter first name: ")
    name2 = input("Enter second name: ")
    new_name = ""
    breakpoint_char = "a e i o u y"

    for i, char in enumerate(name1):
        if char in breakpoint_char:
            new_name += name1[:i]
            break

    for i, char in enumerate(name2):
        if char not in breakpoint_char:
            new_name += name2[i-1:]
            break

    print(new_name)


def string_to_scores():
    """
    Takes a string as input. Separates chars and digits. Tracks a char and
    calculates the score for given char.
    """
    in_str = input("Enter string: ")
    tmp_str = ""
    out_str = ""

    for i, char in enumerate(in_str):

        if char.isalpha() and char.lower() not in tmp_str:

            tmp_str += char.lower()

            char_tracker = char

            char_score = 0

            for j in range(i + 1, len(in_str)):

                if in_str[j].isnumeric() and char_tracker == char.lower():

                    char_score += int(in_str[j])

                elif in_str[j].isnumeric() and char_tracker == char.upper():

                    char_score -= int(in_str[j])

                elif in_str[j].isalpha():

                    char_tracker = in_str[j]

            tmp_str += str(char_score)

    for i, char in enumerate(tmp_str):
        if char.isalpha():
            out_str += char + " "
        elif char == "-":
            out_str += char
        elif char.isnumeric() and i != len(tmp_str) - 1:
            out_str += char + ", "
        else:
            out_str += char
    print(out_str)


def points_to_grade(max_score, my_Score):
    """
    Artithmetic function, takes two strings as args, compares them as integers,
    second relative the first (e.g. int2/int1) and returns grade from table.
    Return string
    """
    grade = ""

    score = (int(my_Score) / int(max_score)) * 100

    if score < 60:
        grade = "F"
    elif score < 70:
        grade = "D"
    elif score < 80:
        grade = "C"
    elif score < 90:
        grade = "B"
    else:
        grade = "A"

    return f"score: {grade}"


def has_strings(string_1, string_2, string_3, string_4):
    """
    String function, takes 4 strings as args. Compares strings 2-4 with string 1
    Comparison is true if string_1 starts with string_2, contains string_3 and
    ends with string_4.
    Return string
    """

    try:
        string_1.index(string_3)
    except ValueError:
        return "No match"
    if string_1.startswith(string_2) and string_1.endswith(string_4):
        return "Match"

    return "No match"
