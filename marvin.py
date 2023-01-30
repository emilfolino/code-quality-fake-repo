"""
marvin functions

    """
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random

def greet():
    """
greet function

    """
    name = input("What is your name? ")
    print("\nMarvin says:\n")
    print("Greetings Master %s!" % name)
    print("Your wish is my command!")

def celcius_to_farenheit():
    """
celcius to farenheit conversion function

    """
    print("Skriv en tempuratur i Celcius")
    celcius = input("Ange din temperatur (C):")
    farenheit = round(float(celcius)* 9 / 5 + 32, 2)
    print(str(farenheit))

def word_manipulation():
    """
Word manipulation function 

    """
    word = input("Give me a word!")
    word_repeater = input("How many times should i repeat myself? ")
    print(multiply_str(word, word_repeater))

def sum_and_average():
    """
Sums inputs and shows the avrage of said inputs

    """
    total = 0
    input_count = 0
    while True:
        numberinput = input("Write a number to add or write done to se result: ")
        if "done" in numberinput:
            print("The sum of all the numbers is "
            + str(round(total,2))+ "and the average is "
            + str(round(total/input_count,2)))

            break

        total += round(float(numberinput),2)
        input_count += 1

def hyphen_string():
    """
hyphen string function

    """
    final_str =""
    letter_count = 0
    word_input = input("write a word!: ")

    for letters in word_input:
        letter_count += 1
        letter_times = letters * int(letter_count)
        final_str += letter_times + "-"
        
    final_str = final_str.rstrip("-")
    print(final_str)

def is_isogram():
    """
Shows if word is an isogram or not

    """
    word_input = input("Write in a word: ")
    for lettercount in word_input:
        isogram = bool(word_input.count(lettercount) > 1)
        if isogram is True:
            break

    if isogram is True:
        print("No match!")
    else:
        print("Match!")
        
def compare_numbers():
    """
compares numbers

    """
    previous_value = 0
    word_input = input("Write a number: ")
    previous_value = word_input
    
    while True:

        try:
            word_input = input("Write a number: ")

            if "done" in word_input:
                break

            if float(previous_value) > float(word_input):
                print("smaller!")
            elif float(previous_value) < float(word_input):
                print("larger!")
            else:
                print("same!")

            previous_value = word_input    

        except(ValueError):
            print("not a number!")
            continue

def randomize_string(word_input):
    """
Randomizes input

    """
    
    newstring = ""
    result = word_input + " --> " + newstring.join(random.sample(word_input,len(word_input)))
    return result        

def get_acronym(name_input):
    """
Shows acronym of given input

    """
    acronyms = ""
    for char in name_input:
        if char.isupper():
            acronyms += char
    return acronyms

def multiply_str(string,heltal):
    """
multiplies string with int

    """
    multipliceradstr = string*int(heltal)
    return multipliceradstr

def mask_string(string_input):
    """
hides input exept the last 4 digits 

    """
    return (multiply_str("#",len(string_input)-4)+string_input[-4:])

def find_all_indexes(string,char_index):
    """
find index of given input

    """
    start_pos = 0
    str_result = ""
    char = 0
    try:
        
        while char <= len(string):
            if char == 0:
                char_pos = string.index(char_index,start_pos, len(string))
                start_pos = char_pos + 1 
                char += 1
                str_result += str(char_pos)
            else:
                char_pos = string.index(char_index,start_pos, len(string))
                start_pos = char_pos + 1 
                char += 1
                str_result += "," + str(char_pos)

            
        #str_result = str_result[:-1]
        # Detta funkade inte för någon anledning

        return str_result

    except ValueError:
        return str_result
        
