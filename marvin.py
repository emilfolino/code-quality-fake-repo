'''module with functions for the marvin program'''
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random

"""
Marvin with a simple menu to start up with.
Marvin doesnt do anything, just presents a menu with some choices.
You should add functinoality to Marvin.
"""

marvin_image = r"""
      \_/
     (* *)
    __)#(__
   ( )...( )(_)
   || |_| ||//
>==() | | ()/
    _(___)_
   [-]   [-]
"""

"""
Its an eternal loop, until q is pressed.
It should check the choice done by the user and call a appropriate
function.
"""

print(chr(27) + "[2J" + chr(27) + "[;H")
print(marvin_image)
print("Hi, I'm Marvin. I know it all. What can I do you for?")
def greet():
    '''present yourself to Marvin'''
    name = input("What is your name? ")
    print("\nMarvin says:\n")
    print("Hello %s - it's an honour to assist you" % name)
    print("What can I do you for?!")

def celcius_to_farenheit():
    '''converts celcius to farenheit'''
    temp = float(input("Enter a temperature in celsius: "))
    #omvandlar till farenheit
    temp = temp * 9 / 5 + 32
    print("Fahrenheit:",round(temp, 2))

def word_manipulation(): 
    '''manipulates a word'''
    word = input("Enter a word: ")
    number = input("Enter a number: ")
    print(multiply_str(word, number))

def sum_and_average():
    '''calculates sum and avarage'''
    total_sum = 0
    avarage = 0
    counter = 0

    while True:
        user_input = input("Enter a number: ")
        counter += 1
        
        if user_input == "done":
            break
        else:
            number = float(user_input)
            total_sum = total_sum + number
            avarage = float(total_sum/counter)

    print("\nSum: " + str(round(total_sum, 2)) + "\nAvarage: " + str(round(avarage, 2)))

def hyphen_string():
    '''hyphens a string'''
    word = input("Enter a word: ")
    counter = 1
    new_word = ""
    for letter in word:
        new_word = new_word + letter * counter + "-"
        counter += 1
    print(new_word[:-1])

def is_isogram():
    '''checks if a word is a isogram'''
    user_input = input("Enter a word: ")
    word = user_input.lower()    
    character_list = []
    match = "Match!"

    for char in word:
        if char in character_list:
            match = "No match!"
            break
        else:
            character_list.append(char)
    print(match)

def compare_numbers():
    '''compares numbers'''
    number1 = input("Enter a number: ")

    while True:
        number2 = input("Enter a number: ")
        if number2 == "done":
            break
        else:
            try:
                if int(number1) < int(number2):
                    print("larger!")
                elif int(number1) > int(number2):
                    print("smaller!")
                else:
                    print("same!")
                number1 = number2
            except ValueError:
                print("not a number!")

def randomize_string(word):
    '''randomizes letters in a given word'''
    list_of_char = list(word)
    random.shuffle(list_of_char)
    random_word = ''.join(list_of_char)
    result = f"{word} --> {random_word}"
    return result

def get_acronym(word):
    '''creates an acronym for a word'''
    acronym = ""
    for char in word:
        if char.isupper():
            acronym = acronym + char
    return acronym

def multiply_str(arg1, arg2):
    '''multiplies a string(arg1) with a int(arg2)'''
    multiplied_string = str(arg1) * int(arg2)
    return multiplied_string

def mask_string(word):
    '''masks a string with "#"'''
    part1_len = len(word[:-4])
    part2 = word[-4:]

    masked_string = multiply_str("#", part1_len) + part2
    return masked_string

def find_all_indexes(str1, str2):
    '''finds all indexes where str2 is a part of str1'''
    pos_list = []
    pos = 0
    while True:
        try:
            pos = str1.index(str2, pos)
            pos_list.append(pos)
            pos += 1
        except ValueError:
            break
    result = ','.join(str(x) for x in pos_list)
    return result
