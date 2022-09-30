#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Functions for Kevin.
"""
import random
"""
Importing the standard module 'random' to use the sample function in function
'randomize_string'.
"""

def greet():
    """
    The program is greeting the user.
    """
    name = input("\nWhat is your name? ")
    print("\nKevin says:\n")
    print("Hello %s - your Highness!" % name)
    print("What will you choose next?!")

def celcius_to_farenheit():
    """
    Takes the user input (type float) and converts the float to Fahrenheit
    and rounds it off to two decimal points and prints the new value.
    """
    temp = float(input("\nEnter a temperature in Celsius, please: "))
    tempFarenheit = round(temp * 9 / 5 + 32, 2)
    print("If you want to know, this is your temperature in Fahrenheit: " + str(tempFarenheit))

def word_manipulation():
    """
    Takes input from user and calls the function 'multiply_str' to print the
    user input a given number of times.
    """
    string = input("\nGive me a word, please: ")
    number = int(input("How many times shall I repeat it? "))
    print(multiply_str(string + "\n", number))

def sum_and_average():
    """
    Takes user input (numbers) until user types 'done' and sums the value of all
    inputs and gives the average of all numbers. A while loop is used because
    the number of user inputs is not known.
    """
    amount = 0
    average = 0
    while True:
        number2 = input("\nType done when you want me to do the math for you. Give me a number, please: ")
        if number2 == "done":
            break
        amount += float(number2)
        average += 1
    print("\nThe sum of all numbers are " + str(round(amount, 2)) +
        " and the average is " + str(round(amount/average, 2)))

def hyphen_string():
    """
    Takes user input (string) and creates a new string by iterating the letters
    and adding multiples of the same letter for each index, and each sequence
    of letter/s is put together with a hyphen. At the end the last hyphen is
    removed to 'tidy' the output.
    """
    word = input("\nLet me show you a trick! Give me a word, please: ")
    new_word = ""
    count = 1
    for letter in word:
        for _ in range(count):
            new_word += letter
        count += 1
        new_word += "-"
    new_word = new_word[:-1]
    print(new_word)

def is_isogram():
    """
    Checks if word is isogram, by first converting the input to lowercase
    letters and then iterating, looking for duplicates of the same letter in the
    same word. If duplicates are found it is not an isogram.
    """
    word = input("\nLet's check if your word is an isogram! Give me a word, please: ")
    lower = word.lower()
    string = ""
    isogram = True
    for letter in lower:
        if letter in string:
            isogram = False
        else:
            string += letter
    if isogram:
        print("Match!")
    else:
        print("No match!")

def compare_numbers():
    """
    Functions asks for numbers and compares the latest number to the previous
    one and prints 'smaller', 'larger' or 'same'. The user can break the
    loop by typing 'done'. There is also a try/except statement that checks if
    input is a number.
    """
    current = 0
    previous = 0
    while True:
        user_input = input("\nGive me a number, please: ")
        try:
            previous = int(user_input)
            break
        except ValueError:
            print("not a number!")
    while True:
        user_input = input("\nGive me another number, please: ")
        if user_input == "done":
            break
        try:
            current = int(user_input)
            if current > previous:
                print("larger!")
            elif current < previous:
                print("smaller!")
            elif current == previous:
                print("same!")
            previous = current
        except ValueError:
            print("not a number!")

def randomize_string(user_input):
    """
    Using the function 'sample' from the standard module 'random', the input
    from a user is randomized and added to the output next to the input.
    """
    a = "".join(random.sample(user_input, len(user_input)))
    combined = user_input + " --> " + a
    return combined

def get_acronym(user_input):
    """
    Function creates an acronym by iterating the input and taking the
    uppercase letters to create the new string.
    """
    string = ""
    for letters in user_input:
        if letters.isupper():
            string = "".join((string, letters))
    return string

def multiply_str(string, number):
    "Function to multiply a string a given number of times."
    return string * number

def mask_string(user_input):
    """
    Using the function 'multiply_str' to hide all but the last four characters
    in the given user input. The output presents the partly hidden input.
    """
    part1 = multiply_str("#", len(user_input)-4)
    part2 = user_input[len(user_input)-4:]
    return part1 + part2

def find_all_indexes(string1, string2):
    """
    Function finds all the indeces where string2 is found within string1
    and creates a new string with the indeces comma separated. 
    """
    start = 0
    string3 = ""
    while start <= len(string1):
        try:
            ind = string1.index(string2, start)
            string3 = "".join((string3, str(ind),","))
            start = ind + 1
        except ValueError:
            start = len(string1) + 1
    return string3[:-1]
