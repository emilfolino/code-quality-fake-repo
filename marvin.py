#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Functions till marvin
"""
import random

def greet():
    """
    greet
    """
    name = input("What is your name? ")
    print("\nMarvin says:\n")
    print("Hello %s ,I'm Marvin the allknowing computer!" % name)
    print("What knowledge do you seek?")
    
def celcius_to_farenheit():
    """
    celcius_to_farenheit
    """
    print("Write a temperature in celsius and I shall show you what it is in farenheit ")
    temp = float(input())
    farenheit = ((float(temp) * 9/5) + 32)
    print("\nMarvin says:\n")
    print("This is the temperature in farenheit!")
    print(round(farenheit, 2))

def word_manipulation():
    """
    word_manipulation
    """
    print("\nMarvin says:\n")
    word_for_multiplication = input("What word would you like multiplied? ")
    number_of_multiplications = int(input("And how many times would you like it multiplied? "))
    for i in range(number_of_multiplications):
        print(str(word_for_multiplication), end = "")
        #pylint klagade på att i inte används men den behövs för for loopen inte ska sluta funka
    i = ""
    print(i)

def sum_and_average():
    """
    sum_and_average
    """
    print("\nMarvin says:\n")
    numbers = 0
    not_done = True
    print("Ah looking for the avrage are we? ")
    print("type 'done' when you want the result. ")
    number = input("Please enter the first number. ")
    amount_of_numbers = 0

    while not_done:
        try:
            float(number)
        except ValueError: 
            print("Type a valid number or done please! ")
            number = 0
        else:
            print(number)
            numbers += float(number)
            amount_of_numbers += 1
            average = numbers/amount_of_numbers
            number = input("What is the next number? ")
        
        if number == "done" and number.isalpha():
            not_done = False
            result = round(average,2)
            numbers = round(numbers, 2)
            print("Sum of all numbers = " + str(numbers) + " and the avrage of all numbers " + str(result))
            break

def hyphen_string():
    """
    hyphen_string
    """
    print("\nMarvin says:\n")
    print("Hello I will be extending any word you might have!")
    amount_of_letters = 1
    for word in input():
        print(amount_of_letters * word + "-", end = "")
        amount_of_letters += 1

def is_isogram():
    """
    is_isogram
    """
    print("\nMarvin says:\n")
    print("Hello it would seem that you want to check if a word is a isogram. ")
    word = input("Please type your word. ")
    not_duplicates = True
    match = False
    chosen_word = ""
    for character in word:
        if character in chosen_word:
            not_duplicates = False
        else:
            chosen_word = chosen_word + character
        if not_duplicates:
            match = False
        else:
            match = True
            break
    if match is True:
        print("No match!")
        print("\nResults are in\n")
        print("it´s not a Isogram")
    elif match is False:
        print("Match!")
        print("\nResults are in\n")
        print("it´s a Isogram!")

def compare_numbers():
    """
    compare_numbers
    """
    print("\nMarvin says:\n")
    number = 0
    not_done = True
    print("Hello I will tell you if your numbers are higher or lower. ")
    print("Dont forget to type done when you are done. ")
    number = input("Please enter the first number. ")
    if number.isalpha():
        print("not a number!")
        number = input("Please enter the first number. ")
    while not_done:
        if number == "done" and str.isalpha:
            not_done = False
            break
        number2 = input("Now please enter your other number. ")
        if number2 == "done" and str.isalpha:
            not_done = False
            break
        if number2.isalpha():
            print("not a number!")
            number2 = float(input("Now please enter your other number. "))
        if float(number) < float(number2):
            print("larger!")
        elif float(number) == float(number2):
            print("same!")
        if float(number) > float(number2):
            print("smaller!")
        number = number2

def randomize_string(string):
    """
    randomize_string
    """
    text = list(string)
    random.shuffle(text)
    result = ''.join(text)
    print(string + " --> " + result)
    return string + " --> " + result

def get_acronym(string):
    """
    get_acronym
    """
    newString = ""
    for char in string:
        if char.isupper():
            newString += char
    print(newString)
    return newString

def mask_string(string):
    """
    mask_string
    """
    answer = multiply_str('#',(len(string) - 4))+string[-4:]
    print(answer)

    return answer

def multiply_str(string, number):
    """
    multiply_str
    """
    multiString = string * int(number)
    return multiString

def find_all_indexes(string, Find):
    """
    find_all_indexes
    """
    try:
        index = 0
        answer = ""
        while index < len(string):
            index = string.find(Find, index)
            if index == -1:
                answer = answer[:-1]
                print(answer, end = "")
                return answer
            answer += str(index) + ","
            index += 1
            
        if index == len(string):
            answer = answer[:-1]
            print(answer, end = "")
            return answer
        
    except ValueError:
        print("There was a ValueError!")
        return None
