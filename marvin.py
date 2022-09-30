#!/usr/bin/env python3
 
"""
Functions for marvin chatbot to be called in main.py
"""

import random

"""
FUNCTION DEFINITIONS FOR MENU OPTIONS
"""

def multiply_str(input_string, multiplication_number):
    """Takes a string and an integer as arguments, multiplies the string by the number
    and returns the resulting string.
    """

    return input_string * multiplication_number

def greet():
    """Takes a string as input (the name) and prints it out together with a greeting."""

    name = input("What is your name? \n")

    print("\nMarvin says:")
    print("Hello %s - it's a pleasure!" % name)

def celcius_to_farenheit():
    """Takes celsius as input, converts input to float and converts it to fahrenheit, 
    rounded to 2 and then prints out the result. Tests for value error related to input"""

    celsius = input("What amount of degrees do you want to convert?\n-->")

    try:
        fahrenheit = round((float(celsius) * 9 / 5 + 32), 2)
        celsius = round(float(celsius), 2)
        print("\nMarvin says:")
        print(str(celsius) + "C equals " + str(fahrenheit) + "F")

    except ValueError:
        print("Marvin says: \nPlease input a number next time!")

def word_manipulation():
    """Takes a word and a number and multiplies the word by the number, printing out the result."""

    word = input("What is the word you would like to multiply?\n-->")
    number = input("How many times would you like to multiply the word?\n-->")

    try:
        print(multiply_str(word, int(number)))
    except ValueError:
        print("Something went wrong, please try again.")

def sum_and_average():
    """Takes numbers as input in a loop until the user writes, sums and averages the
    numbers and prints out the sums and average. Tries for value error to check if
    user entered a number, if not throws an exception printing a "try again" prompt,
    continuing the loop, or finishing the loop if the user wrote "done"."""

    print("Please write the numbers you would like to sum and average, write done when finished.\n")
    number_list = []

    while True:
        try:
            number_input = input("Write a number or done if finished: ")
            number_list += [float(number_input)]
        except ValueError:
            if(number_input == 'done'):
                break
            else:
                print("That's not an number, try again.")
        
    print   ("The sum of all numbers is " + str(round(sum(number_list), 2)) + 
            " and the average is " + str(round((sum(number_list) / len(number_list)), 2)))

def hyphen_string():
    """Takes a word as input and then multiplies the letters in the word by their
    position in the word, with dashes in between, printing out the resulting string.
    The letters in the input word are multiplied in a for loop using a counter starting 
    at 1 which is incremented by 1 each iteration."""

    word = input("Please write a word:\n")
    multiplied_word = ''
    counter = 1

    for letters in word:
        multiplied_word += letters * counter + "-"
        counter += 1
        
    multiplied_word = multiplied_word[:-1]

    print(multiplied_word)

def is_isogram():
    """Takes a word as input and checks if it is an isogram. If so it prints "Match!",
    if not it prints "No match!". Input word is changed to lowercase and then in a for-loop
    each letter is checked in the word to find whether it's is used more than once. If so
    variable match is set to 0 and loop is broken. After loop the variable match is check 
    if its True or not in a if-else statement, printing "Match!" if true and "No match" if false."""

    word = input("What is the word you want to check?\n-->")
    word = word.lower()
    match = 1

    for letter in word:
        if word.count(letter) > 1:
            match = 0
            break

    if match:
        print("Match!")
    else:
        print("No match!")

def compare_numbers():
    """Takes numbers as input in a nested loop and checks if the number input is larger or smaller than 
    or the same as the previous number, then printing out "larger!", "smaller!" or "same!" This is done
    until the user enters "done", which ends the loop and function. If a user enters a non-numeral string
    other than "done" a message saying "not a number" is shown, continuing the loop."""

    while True:
        try:
            input_str1 = input("Write a number or done if you want to finish:\n-->")
            number1 = float(input_str1)
            while True:
                try:
                    input_str2 = input("Write a number or done if you want to finish:\n-->")
                    number2 = float(input_str2)

                    if number2 > number1:
                        print("larger!\n")
                        number1 = number2

                    elif number2 < number1:
                        print("smaller!\n")
                        number1 = number2
                    else:
                        print("same!\n")
                        number1 = number2

                except ValueError:
                    if(input_str2 == 'done'):
                        break
                    else:
                        print("not a number!\n")
                        continue
                
        except ValueError:
            if(input_str1 == 'done'):
                break

            else:
                print("not a number!\n")
                continue
        break

def check_letters_in_word():
    """Takes two strings as input and checks whether all the characters of the second string are present in the first.
    Then prints "Match! or "No Match!" depending on the result."""

    word = input("Please write the first word:\n-->")
    word = word.lower()
    letters = input("Please write the letters you want to check:\n-->")
    letters = letters.lower()
    letters_in_word = 0

    for letter in letters:
        if letter in word:
            letter_pos = word.find(letter)
            word = word[:(letter_pos)] + word[(letter_pos + 1):]
            letters_in_word += 1

    if letters_in_word == len(letters):
        print("Match!")
    else:
        print("No match!")

def all_digits():
    """Takes two numbers as input and checks how many times the first number has to be multiplied
    with two before it contains all 10 digits. The second input number is the number of times
    the function tries to multiply before "giving up". If a corresponding number is found before
    reaching the limit given in the second input, the number of times multiplied (or iterations)
    is printed. Otherwise -1 is printed. """

    try:
        number1 = int(input("Input the number:\n-->"))
        number2 = int(input("Input amount of times you want to try to multiply:\n-->"))
        number_list = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        match = False
        it_counter = 0

        while (it_counter < number2):
            digit_counter = 0

            for number in number_list:
                if number in str(number1):
                    digit_counter += 1

            if digit_counter == 10:
                match = True
                break
            
            it_counter += 1
            number1 *= 2

        if match:
            print("Answer: " + str(it_counter) + " times")

        else:
            print("Answer: -1 times")

    except ValueError:
        print("Not a number!")


def replace_tab_with_spaces():
    """Takes a string containing tabs and replaces all tabs with 3 spaces."""

    str_with_tab = input("Enter a sentence containing atleast 1 tab:\n-->")
    str_with_tab = str_with_tab.replace("\t", "   ")
    print(str_with_tab)

def portmanteau_name():
    """Takes two names as string inputs and creates a portmanteau by removing the first vowel and any
    subsequent consonants in the first name and any consonants preceeding the first vowel in the second 
    name and then concatenating the two strings."""

    vowels = "aouåeiyäöAOUÅEIYÄÖ"
    name1 = input("Enter the first name:\n-->")
    name2 = input("Enter the second name:\n-->")
    name1_shortened = ''
    name2_shortened = ''

    for letter in name1:
        if letter in vowels:
            name1_shortened = name1[:name1.find(letter)]
            name1_shortened= name1_shortened.lower()
            break

    for letter in name2:
        if letter in vowels:
            name2_shortened = name2[name2.find(letter):]
            name2_shortened= name2_shortened.lower()
            break

    print(name1_shortened + name2_shortened)

def count_points():
    """Takes a string input where the user writes letters and numbers interchangeably.
    For each of these letters points are awarded if lowercase and deducted if uppercase, the amount
    decided by the subsequent number, eg. a5b2A3B1 equals a: 3, b: 1. Each letter is then printed
    together with the respective amount of points"""

    input_string = input("Write a string with letters and digits interchangeably (eg. a2B3A5b6):\n-->")
    alphabet = "aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZåÅäÄöÖ"
    player_point_list = []
    player_letter_list = []

    try:
        for letter in input_string:
            if letter in alphabet and letter.lower() not in player_letter_list:
                player_letter_list.append(letter.lower())
                player_point_list.append(0)
                counter = input_string.find(letter)

                while (counter < len(input_string)):
                    if input_string[counter] == player_letter_list[-1].lower():
                        player_point_list[-1] += int(input_string[counter + 1])

                    elif input_string[counter] == player_letter_list[-1].upper():
                        player_point_list[-1] -= int(input_string[counter + 1])

                    counter += 1

        output_string = ''
        counter = 0

        while counter < len(player_letter_list):
            output_string += player_letter_list[counter] + " " + str(player_point_list[counter]) + ", "
            counter += 1

        print(output_string[:-2])

    except (ValueError, IndexError):
        print("Something went wrong!")


def randomize_string(input_string):
    """Takes a string as an argument and randomizes the letters of the string after converting to 
    a list using random.shuffle. The original string and randomized string are then concatenated
    with " --> " in between, returning the resulting string."""

    random.seed()
    rand_string = list(input_string)
    random.shuffle(rand_string)
    rand_string = ''.join(rand_string)

    return input_string + " --> " + rand_string

def get_acronym(input_string):
    """Takes a string as argument, combines all uppercase letters in the string to an acronym.
    and returns the acronym"""

    acronym = ''
    for letter in input_string:
        if letter.isupper():
            acronym += letter

    return acronym

def mask_string(input_string):
    """Takes a string as an argument, masks all characters except the last 4 with '#' and 
    returns the new string."""
    
    return multiply_str('#', len(input_string[:-4])) + input_string[-4:]

def find_all_indexes(input_string1, input_string2):
    """Takes two strings of which the second string is a substring of the first, 
    finds all the indexes of the 2nd string in the 1st then returns all the indexes
    in a string, separated by a comma. If substring is not present, an empty string is 
    returned. While loop in function is broken by the ValueError thrown by index()
    once no more instances of the substring is found """

    output_string = ''
    start_index = 0

    while True:
        try:
            ind = input_string1.index(input_string2, start_index)
            start_index = ind + len(input_string2)
            output_string += str(ind) + ','
        except ValueError:
            break

    return output_string[:-1]

def points_to_grade(max_points, points):
    """Takes two arguments: max_points and points, calculates the
    percentage of points compared to max_points and then checks
    the percentage and concatenates the string return_str with
    the corresponding grade. The resulting string
    is returned."""

    return_str = 'score: '

    try:
        if float(max_points) != 0:
            if float(points) != 0:
                score_percentage = float(points) / float(max_points) * 100

                if score_percentage >= 90:
                    return_str += 'A'

                elif score_percentage >= 80:
                    return_str += 'B'

                elif score_percentage >= 70:
                    return_str += 'C'

                elif score_percentage >= 60:
                    return_str += 'D'

                else:
                    return_str += 'F'

            else:
                return_str += 'F'

        else:
            return_str = "Max points cannot be 0, please enter a valid number."

    except ValueError:
        return_str = "Points entered are not valid, please try again."    
    
    return return_str



def has_strings(str1, str2, str3, str4):
    """Takes for strings as arguments. The 1st string is checked as to
    whether it starts with the 2nd string, contains the 3d string
    and ends with the 4th string. If so "Match" is returned, else
    "No match" is returned"""

    return_str = ''
    
    if str1.startswith(str2) and str3 in str1 and str1.endswith(str4):
        return_str = "Match"
    else:
        return_str = "No match"
    
    return return_str
