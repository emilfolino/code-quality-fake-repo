#Project by Croyse

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Funktioner för main.py
'''

import random

def greet():
    '''
    Hälsar välkommen
    '''
    name = input("What is your name? ")
    print(f"{name}? Such a inspiring name, son.")

def celcius_to_farenheit():
    '''
    Omvandla celsius till fahrenheit
    '''
    temp = float(input("Do you want me to help you convert, son? Let me help. Insert celius: "))
    fahrenheit = float(temp * 9 / 5 + 32)
    round_off = (round(fahrenheit, 2))
#avrundar till 2 decimaler
    print(f"{temp} Celsius is {round_off} fahrenheit, son.")

def word_manipulation():
    '''
    Printa ett ord flera gånger
    '''
    word = str(input("What word do you think off? "))
    times = int(input("How many times have you thought about it? "))
    return print(multiply_str(word, times))

def sum_and_average():
    '''
    Räknar ut summan och medelvärdet av de siffror du matar in
    '''
    summarize = 0
    counter = 0
    while True:
        number = input("Please give me a number, son. When you feel satisfied, please write 'done'. ")
        if number == "done":
            break
            
        summarize += float(number)
        counter += 1
        average = round(summarize / counter, 2)
    print(f"Son. The sum of all numbers are {summarize} and the average is {average}.")

def hyphen_string():
    '''
    Lägger till "+1" och "-" för varje bokstav
    '''
    word = input("Tell me a word, son. ")
    string = ""
    value = 1

    for char in word:
        if len(word) > value:
            string += char * value + "-"
            value += 1
        else:
            string += char * value
            print(string)

def is_isogram():
    '''
    Kollar om det är ett isogram
    '''
    string = input("Give me a word, son and I will tell you if it is a isogram. ")
        
    for char in string:
        if string.count(char) > 1:
            answer = False
            break
        else:
            answer = True
     
    if answer is True:
        print("Match!")
    else:
        print("No match!")

def compare_numbers():
    '''
    Jämför storlek på tal
    '''
    start_value = input("Give me a value, son!: ")
    new_value = ""
    while True:
        new_value = input(f"Enter a new value, son or type 'done' to quit. Your old value is {start_value}.")
        if new_value == 'done':
            print("Good job, son. ") 
            break
        try: 
            new_value = float(new_value)

            if float(start_value) < float(new_value):
                print("larger!")
                
            elif float(start_value) > float(new_value):
                print("smaller!")

            else:
                print("same!")
            start_value = new_value
        except ValueError:
            print("not a number!")

def randomize_string(string):
    '''
    Kastar om bokstäver
    '''
    word = []
    for char in string:
        word.append(char)
        random.shuffle(word)

    return string + " --> " + "".join(word)

def get_acronym(akronym):
    '''
    Fixar ett akronym
    '''
    strings = ""

    for letter in akronym:
        if letter.isupper() is True:
            strings += letter
    
    return strings

def mask_string(secret):
    '''
    Sträng maskering
    '''
    return multiply_str("#", len(secret) -4) + secret[len(secret) -4 : None]

def multiply_str(x,y):
    '''
    Multiplicerar strängar
    '''
    a_string = x * int(y)
    return a_string


def find_all_indexes(string1, string2):
    '''
    Hittar index
    '''
    index = 0
    the_result = ""

    try:
        while index < len(string1):
            index = string1.index(string2, index + 1)
            the_result += "," + str(index)
    
    except ValueError:
        pass
    
    if len(the_result) > 0:
        return the_result[1:]
    return the_result
