#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Functions for marvin
"""
from random import randint

def greet():
    """() => print
    prints a welcome message
    """
    name = input("What is your name? ")
    print("\nCat says:\n")
    print("Hello %s - your awesomeness!" % name)
    print("What can I do you for?!")

def celcius_to_farenheit():
    """() => print
    converts celsius to farenheit.
    prints the result.
    """
    fahrenheit_conversion = 9/5
    fahrenheit_constant = 32
    celsius = ""
    while celsius == "":
        try: 
            celsius = float(input("What's the temp in celsius?"))
            print(f"{round(celsius, 2)} Celsius is the same as \
                {round(celsius * fahrenheit_conversion + fahrenheit_constant, 2)} fahrenheit.")
        except ValueError:
            print("Celsius should be a number")

def word_manipulation():
    """() => print
    prints the string multiplied n times.
    """
    word = input("Give me a word!") + "\n"
    while True:
        try:
            number_times = int(input("How many times should I repeat it?"))
            break
        except ValueError:
            print("I'll only multiply the word if you give me a number!")     
    print(multiply_str(word, number_times))   

def sum_and_average():
    """() => print
    prints the sum and average.
    """
    number_in = []
    done = False
    while not done:
        current_number = input("Enter a number or, if done, enter 'done': ")
        if current_number == "done":
            done = True
        try:
            number_in.append(float(current_number))
        except ValueError:
            print("Enter a number or, if done, enter 'done'.")
    print(f"The sum of all numbers are {sum(number_in)} and the average is \
        {round(sum(number_in)/len(number_in), 2)}.")

def hyphen_string():
    """() => print
    prints the string but the character is written n times. 
    where n == character index.
    """
    word = input("write a word: ")
    new_string = ""
    for index, letter in enumerate(word):
        new_string += f"{multiply_str(letter, index + 1)}-"
    print(new_string)

def is_isogram():
    """() => print
    checks if the word is an isogram
    prints the result.
    """
    word = input("Check if the word is an isogram: ")
    is_match = "Match!"
    for index, letter in enumerate(word):
        if letter in word[(index + 1):]:
            is_match = "No match!"
    print(is_match)

def compare_numbers():
    """() => print
    checks if the 2nd number is < or > or == the 1st number.
    prints the result.
    """
    prev_number = ""
    next_number = input("Enter a number: ")
    while next_number != "done":
        try:
            next_number = int(next_number)
            if prev_number:
                if next_number > prev_number:
                    print("larger!")
                elif next_number < prev_number:
                    print("smaller!")
                else:
                    print("same!")
            prev_number = next_number
        except ValueError:
            print("not a number!")
        next_number = input("Enter a number: ")

def chars_in_string():
    """() => print
    checks if the second string is found in the first.
    prints the result.    
    """
    first_string = input("first string: ")
    second_string = input("second string: ")
    all_char_in_string = True
    for letter in second_string:
        if letter not in first_string:
            all_char_in_string = False
    if all_char_in_string:
        print("Match!")
    else: 
        print("No match!")

def all_digits_in_number():
    """() => print
    prints the number of times a number have to be multiplied by 2
    for it to contain all numbers from 0-9.
    """
    message = "Answer: -1 times"
    control_numbers = "0123456789"
    numbers_valid = False
    while not numbers_valid:
        try:
            check_number = int(input("Enter a number: "))
            limit = int(input("How many times should i try? "))
            numbers_valid = True
        except ValueError:
            print("Not a number. Try again!")

    for num_times in range(limit):
        all_numbers_in = True
        for number in control_numbers:
            if number not in str(check_number):
                all_numbers_in = False
                break
        if all_numbers_in:
            message = f"Answer: {num_times} times"
            break
        check_number *= 2
    print(message)

def string_to_tabs():
    """() => print
    prints a string with spaces instead of tabs.
    """
    string_with_tabs = input("Skriv något: ")
    new_string = ""

    for letter in string_with_tabs:
        if letter == "\t":
            new_string += "   "
        else:
            new_string += letter

    print(new_string)

def vowels_in_name():
    """() => print
    concatentes two strings. All letters from the first string until the character is a vowel. 
    And all letters from the 2nd string from the first vowel found.
    """
    vowels = "aeiouy"
    name_one = input("Första namnet: ")
    name_two = input("Andra namnet: ")
    #Om det ej finns några vokaler i namn ett sparas hela name_one.
    concat_names = name_one
    for index, letter in enumerate(name_one):
        if letter in vowels:
            concat_names = name_one[0:index]
            break
    for index, letter in enumerate(name_two):
        if letter in vowels:
            concat_names += name_two[index:]
            break
    print(concat_names)

def long_word():
    """() => print
    prints points given to player. Player is known by letter
    and points given follows letter. If char is uppercase
    player gets the point otherwise looses same points.
    """
    long_string = input("en lång sträng! ")
    output = ""
    for letter in long_string:
        value = 0
        if letter.lower() not in output and letter.isalpha():
            for index_two, letter_two in enumerate(long_string):
                if letter.lower() == letter_two.lower():
                    if letter_two.islower():
                        value += int(long_string[index_two+1:index_two + 2])
                    else:
                        value -= int(long_string[index_two+1:index_two + 2])       
            if output:
                output += f", {letter.lower()} {value}"
            else: 
                output = f"{letter.lower()} {value}"
    print(output)  

def randomize_string(string):
    """(string) => string
    returns string with all characters in random order

    ("Borde inte bli samma igen") => "Borde inte bli samma igen --> eel gn rtm dBmibo saiiane"
    """
    new_string = ""
    left_of_string = string
    while len(new_string) != len(string):
        rand_num = randint(0, len(left_of_string) -1)
        new_string += left_of_string[rand_num]
        left_of_string = left_of_string[0:rand_num:] + left_of_string[rand_num +1::]
        
    return f"{string} --> {new_string}"

def get_acronym(string):
    """(string) => string
    returns a string with all uppercase letters (an acronym) from the input string
    """
    acronym = ""
    for letter in string:
        if letter.isupper():
            acronym += letter
    return acronym

def multiply_str(string, multiplier):
    """(string, number) => string
    returns the string multiplied n (multiplier) times.
    """
    return string * multiplier

def mask_string(string):
    """(string) => string
    returns the string with all but the last 4 letters masked
    """
    new_string = multiply_str("#", len(string) - 4)
    for i in range(len(string) - 4, len(string)):
        new_string += string[i]
    return(new_string)

def find_all_indexes(string, string_to_find):
    """(string, string) => string
    returns a string with all the indexes of the characters from string_to_find in string
    """
    current_index = 0
    all_indexes = ""
    while True:
        try: 
            current_index = string.index(string_to_find, current_index)
            if all_indexes:
                all_indexes += ","
            all_indexes += str(current_index)
            current_index += 1
        except ValueError:
            return all_indexes

def points_to_grade(max_points, points):
    """(int, int) => string
    returns your grade based on points/max_points.
    """
    # Ska man hantera felaktiga parametrar i funktionen eller kan den förvänta sig 
    # att alla parametrar är ok? 
    try:
        points = int(points)
        max_points = int(max_points)
    except ValueError:
        return "Can't set grades if you don't provide the correctly."
    score = points / max_points
    if score >= 0.9:
        grade = "A"
    elif score >= 0.8:
        grade = "B"
    elif score >= 0.7:
        grade = "C"
    elif score >= 0.6:
        grade = "D"
    else:
        grade = "F"
    return f"score: {grade}"

def has_strings(string, string_starts_with, string_contains, string_ends_with):
    """(string, string, string, string) => string
    checkes if 1st string starts with 2nd string, contains 3rd string and ends with 4th string.
    returns Match or No match
    """
    is_ok = string.startswith(string_starts_with) and \
        string_contains in string and \
        string.endswith(string_ends_with)
    return "Match" if is_ok else "No match"
    

if __name__ == "__main__":
    print(has_strings("anagram", "ana" , "agr", "aam"))
    print(points_to_grade(100, 59))
