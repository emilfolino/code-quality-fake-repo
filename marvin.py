#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module with functions for marvin options
"""
import random

def greet():
    """
    Menu option 1, tell Marvin your name
    """
    print("\nMarv says:\n")
    name = input("What's your name bro? ")
    print("\nMarv says:\n")
    print(f"{name}, huh? Right on...")

def celcius_to_farenheit():
    """
    Menu option 2, converts celcius to fahrenheit
    """
    print("\nMarv says:\n")
    print("My mama taught be this trick.")
    temp = input("Tell me the temperature in Celcius: ")
    print("\nMarv says:\n")
    print(f"That's {round(float(temp) * 9/5 + 32, 2)} degrees Fahrenheit!! I think...")

def word_manipulation():  # Ersatt med multiply_str
    """
    Menu option 3, multiplies a word a specified time
    """
    print("\nMarv says:\n")
    print("Uuuh... ok...")
    word = input("What you want me to say then? ")
    print("\nMarv says:\n")
    times = int(input("And how many times you want me saying it? "))
    print(multiply_str(word, times))
    print("... Well that was pointless...")

def sum_and_average():
    """
    Menu option 4, calculates sum and average of numbers
    """
    print("\nMarv says:\n")
    print("Yeah I'm crazy about numbers...")
    num = 0
    num_sum = 0
    num_aver = 0
    denom = 0
    while (True):
        if denom == 0:
            num = input("Give me a number or say 'done': ")
        else:
            num = input("Give me another number or say 'done': ")
        if (num == "done"):
            break
        else:
            num = float(num)
            denom += 1
            num_sum += num
            num_aver = num_sum/denom
    print("\nMarv says:\n")
    if denom == 0:
        print("Aaaaw, no numbers for me? Too bad...")
    else:
        print(
            f"Let's see here... eehh.. okay.. the sum of all that iiisss... {round(num_sum,2)}!!")
        print(
            f"and average is... eehhmmm........... {round(num_aver,2)}!!!!!!")
        print("Man... I'm good at this...")

def hyphen_string():
    """
    Menu option 5, ads hyphen between characters and dublicate character as many times as its order in string
    """
    print("\nMarv says:\n")
    print("Huhuhu well that does sound like a funny idea...")
    word = input("What do you want me to say? ")
    times = 0
    max_times = 1
    answer = ""
    for i in word:
        times = max_times
        while times > 0:
            answer += i
            times -= 1
        if i != word[-1]:  # Lägg till "-" förutom efter sista bokstaven
            answer += "-"
        max_times += 1
    print("\nMarv says:\n")
    print(f"{answer}")
    print("Hm... thought it would be funnier...")


def is_isogram():
    """
    Menu option 6, checks if a word is an isogram or not
    """
    print("\nMarv says:\n")
    word = input("Ok, I'll try. Give me a word: ")
    compare = ""
    recurrence = False
    for i in word:
        for j in compare:
            if i == j:
                recurrence = True
        compare += i
    print("\nMarv says:\n")
    if recurrence is False:
        print("Match! Isogram for sure...")
    else:
        print("No match! Man, that's no isogram...")


def compare_numbers():
    """
    Menu option 7, compare two numbers to see if the latter is smaller, bigger och equal
    """
    print("\nMarv says:\n")
    print("Easy, man... ")
    num_previous = float(input("Give me a number: "))
    while(True):
        try:
            num_new = input("Now give me a new number or say 'done': ")
            if num_new == "done":
                break
            else:
                num_new = float(num_new)
                if (num_new > num_previous):
                    print("\nBro, new number is larger!")
                elif (num_new < num_previous):
                    print("\nDude, new number is smaller!")
                else:
                    print("\nNew number is same! Or am or am I going crazy?")
                num_previous = num_new
        except ValueError:
            print("\nThat's not a number! Hehehe... trying to trick me...?")
    print("\nMarv says:\n")
    print("That was fun man...")


def randomize_string(strShuffle):
    """
    Called by menu option 8
    Shuffles the characters in a string and returns the new string
    """
    list_of_characters = list(strShuffle)
    random.shuffle(list_of_characters)
    list_to_str = "".join(list_of_characters)
    str_to_return = f"{strShuffle} --> {list_to_str}"
    return str_to_return

def get_acronym(str_to_acronym):
    """
    Called by menu option 9
    Turns a string into an acronym
    Returns the acronym as a string
    """
    str_to_return = ""
    for i in str_to_acronym:
        if i.isupper():
            str_to_return += i
    return str_to_return

def mask_string(str_to_mask):
    """
    Called by menu option 10
    Masks every digit in a number except the last four
    """
    if len(str_to_mask) > 4:
        str_to_return = multiply_str("#", len(str_to_mask)-4)
    ch_order = 1
    for i in str_to_mask:
        if len(str_to_mask) - ch_order < 4:
            str_to_return += i
        ch_order += 1
    return str_to_return


def multiply_str(str_to_multiply, number_of_times):
    """
    Multiplies a string a specified number of times
    """
    str_to_return = ""
    while number_of_times > 0:
        str_to_return += str_to_multiply
        number_of_times -= 1
    return(str_to_return)

def find_all_indexes(bigstr, substr):
    """
    Called by menu option 11, finds a substrings positions in a string
    """
    start_pos = 0
    str_to_return = ""
    firstSearch = True
    while True:
        try:
            index = bigstr.index(substr, start_pos)
            if firstSearch is False:
                str_to_return += ","
            str_to_return += str(index)
            start_pos = index + 1
            firstSearch = False
        except ValueError:
            break
    return str_to_return

def points_to_grade(max_points, points):
    """
    Menyval b1, omvandlar "procent rätt" till betyg
    """
    points_proportion = int(points)/int(max_points)
    if points_proportion >= 0.9:
        return "score: A"
    if 0.9 > points_proportion >= 0.8:
        return "score: B"
    if 0.8 > points_proportion >= 0.7:
        return "score: C"
    if 0.7 > points_proportion >= 0.6:
        return "score: D"
    return "score: F"

def has_strings(str_big, substr1, substr2, substr3):
    """
    Menyval b2, kollar om substrings är början, en del av och slutet av en string
    """
    if str_big.startswith(substr1) is False:
        return "No match"
    if (substr2 in str_big) is False:
        return "No match"
    if str_big.endswith(substr3) is False:
        return "No match"
    return "Match"



def choice_main_options():
    """
    User decides main choice
    """
    return (input("--> "))
