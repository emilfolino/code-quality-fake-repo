#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Marvin with a simple menu to start up with.
Marvin doesnt do anything, just presents a menu with some choices.
You should add functinoality to Marvin.
"""

import random

def multiply_str(string_10_string, string_10_number):
    """A function multiplying a string with a given number."""
    output = string_10_string * string_10_number
    return output

def greet():
    """A function which greets the user."""
    name = input("What is your name? ")
    print("\nMarvin says:\n")
    print("Hello %s - your awesomeness!" % name)
    print("What can I do you for?!")

def celcius_to_farenheit():
    """A function which converts temp from Celcius to Farenheit."""
    temp_c = float(input("Tell me the temperature around you, in Celcius, and I will convert it to Farenheit...: "))
    temp_f = float(round((temp_c * 9 / 5 + 32), 2)) 
    print("\nMarvin says:\n")
    print("The temperature is " + str(temp_f) + " Farenheit.")

def word_manipulation():
    """A function using the multiply_str-function."""
    input_3_1 = input("Give me a word: ")
    input_3_2 = int(input("Now, give me a number: "))

    output = multiply_str(input_3_1, input_3_2)
    print("Watch this magic: " + str(output))

def sum_and_average():
    """A function which gives us a sum and an average."""    
    sum_input = float(0)
    input_4 = ""
    counter = 0
    while input_4 != "done":
        input_4 = input("Give me a number or tell me 'done' when you're done! ")
        try:
            sum_input += float(input_4)
            counter += 1
        except ValueError:
            if input_4 != "done":
                print("Only numbers, please!")

    output_uppg4_sum = round(sum_input, 2)
    output_uppg4_average = round(float(sum_input) / float(counter), 2)
        
    print("The sum of all numbers are " + str(output_uppg4_sum) + \
    " and the average is " + str(output_uppg4_average))


def hyphen_string():
    """A function which changes the apparance of the given word."""    
    string_inp = ""
    counter = 1
    string_inp = input("\nGive me a word! \n")
    string_new= ""
    for letter in string_inp:
        if counter > 1:
            string_new += "-"
        string_new += letter * counter
        counter += 1
    print(string_new)

def is_isogram():
    """A function which creates an isogram."""    
    string_inp = ""
    string_inp = input("\nGive me a word! \n")
    string_inp = string_inp.lower()
    if string_inp.isdigit():
        print("No numbers, please!")
    
    else: 
        answer = "Match!"

    for letter in string_inp: 
        if string_inp.count(letter) > 1:
            answer = "No match!"
    
    print(answer)

def only_numbers(input_7):
    """ Funktion som testar om input-värdet är en integer (används i menyval 7)"""
    try: 
        int(input_7)
        return True
    except ValueError:
        print("not a number!")
        return False

def compare_numbers():
    """A function which compare numbers."""
    counter = 0
    previous  = 0
    current = 0

    while current != "done": 
        current = input("Give me a number or tell me 'done' when you're done! ")
        
        if current == "done": 
            break

        if not only_numbers(current):
            continue
        
        while counter == 0: 
            counter += 1
        
        previous = current
    
        while counter >= 1:
            current = input("\nGive me a new number or tell me 'done' when you're done! \n")
            if current == "done": 
                break
            if not only_numbers(current):
                continue
            
            if int(current) > int(previous):
                print("larger!")
                counter += 1
            elif int(current) < int(previous):
                print("smaller!")
                counter += 1
            else: 
                print("same!")
                counter += 1
            
            previous = current

def randomize_string(string):
    """A function which changes our string to a randomized one."""
    char_list = []
    #random_char_string = ""
    for char in string:
        char_list.append(char)

    random.shuffle(char_list)

    output = string + " --> " + ''.join(char_list)

    print(output)
    return output

def get_acronym(string_9):
    """A function which gives an acronym."""
    upper_string = ""
    for letter in string_9:
        if letter.isupper():
            upper_string += letter

    print(upper_string)
    return upper_string 

def mask_string(string_10_string):
    """A function masking all characters except the last four."""
    string_10_number = len(string_10_string[:-4])
    
    output = multiply_str("#", string_10_number)
    output += string_10_string[- 4:]

    print(output)
    return output

def find_all_indexes(string_11_a, string_11_b):
    """A function which finds all indexes."""
    start = 0
    output = ""
    counter = 0

    try:
        while counter < len(string_11_a):
            index = string_11_a.index(string_11_b, start)
            start = index + 1
            counter += 1
            if output:
                output += ","
        
            output += str(index)

        print(output)
        return output

    except ValueError:
        print(output)
        return output
