#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Contains alla functions required for the Marvin program. 
Functions called by the Main function in main.py
"""
import random

def menu():
    """
    Menu function that prints the menu and returns a user selection.
    """
    bob_image = r"""
              __
      _(\    |@@|
     (__/\__ \--/ __
        \___|----|  |   __
            \ }{ /\ )_ / _\
            /\__/\ \__O (__
           (--/\--)    \__/
           _)(  )(_
          `---''---`
    """

    

    print(chr(27) + "[2J" + chr(27) + "[;H")
    print(bob_image)
    print("Hi, I'm Bob. I know it all. What can I do you for?")
    print("1) Present yourself to Bob.")
    print("2) Celsius to Fahrenheit.")
    print("3) Let's play parrot! You say is, I'll repeat it.")
    print("4) Sure I can do math for you!")
    print("5) Repeat letter in word.")
    print("6) Isogram.")
    print("7) Is smaller, bigger or equal.")
    print("8) Randomize String.")
    print("9) Get Acronym.")
    print("10) Mask string.")
    print("11) Find all index.")
    print("12) Search for country.")
    print("13) Show emission change for a country.")
    print("14) Show all data for a country.")
    print("A1) Check if all letter in a word.")
    print("A2) Match brackets.")
    print("q) Quit.")
    print("\n")
    print('Try out my "inv" commands!')
    print("--------------------------")

    choice = input("--> ")
    
    return choice

def bye():
    """
    Prints farwell message
    """
    print("Bye, bye - and welcome back anytime!")

def not_valid():
    """
    Prints a prompt that input is not a valid choice.
    """
    print("Error. That is not a valid choice.")

def press_to_continue():
    """
    Prompts user to "Press enter to continue...".
    """
    input("\nPress enter to continue...")


def greet():
    """
    Asks for user name and prints a greeting.
    """
    name = input("What is your name: ")
    print("\nBob says:\n")
    print("Hello %s - great to meet you!" % name)
    print("What can I do you for?!")

def celcius_to_farenheit():
    """
    Converts Celcius to Farenheit.
    """
    celsius = float(input("What temperature in Celsius do you want to convert to Fahrenheit: "))
    farenheit = round(celsius * 9 / 5 + 32, 2)
    print("That is %s degrees in Fahrenheit" % farenheit)

def word_manipulation():
    """
    Repeats a word the number of times selected.
    """
    word = input("Tell me the word to repeat: ")
    repeat_nr = int(input("And how many times shall I repeat it: "))
    print(multiply_str(word, repeat_nr))

def sum_and_average():
    """
    Adds number together and calculates an average.
    """
    tot_sum = 0
    nr_of_nr = 0
    
    while True:
        user_number = input("What number shall i add together, end with <done>: ")
        
        if user_number == "done":
            break
        
        nr_of_nr += 1
        tot_sum += float(user_number)
    
    average = round(tot_sum / nr_of_nr, 2)
    print(f"The sum of all numbers are {tot_sum} and the average is {average}")

def hyphen_string():
    """
    Distors a word by increasing the number of letters for each letter.
    """
    word_input = input("What word shall I distort: ")
    word_output = ""
    counter = 0
    nr_of_letters = 0
    
    for _ in word_input:
        nr_of_letters +=1
    
    for letter in word_input:
        counter += 1
        
        for _ in range(counter):
            word_output += letter
        
        if counter != nr_of_letters:
            word_output += "-"
    
    print(word_output)       

def is_isogram():
    """
    Checks if word is an Isogram.
    """
    word_input = input("What word shall I check: ")
    isogram = True
    
    used_letters = ""
    
    for letter in word_input:
        
        if letter in used_letters:
            isogram = False
            break
            
        used_letters += letter
    
    if isogram is False:
        print("No match!")
    
    if isogram:
        print("Match!")

def compare_numbers():
    """
    Compares number and tells if less, equal or greater.
    """
    while True:
        first_nr = input("Enter the first number to be compared: ")
        
        if first_nr == "done":
            break
        
        try:
            first_nr = int(first_nr)
            break
        except ValueError:
            print("not a number!")
            continue
        
        if first_nr == "done":
            continue
    
    while True:
        while True:
            second_nr = input("Compare with: ")
            
            if second_nr == "done":
                break
        
            try:
                second_nr = int(second_nr)
                break
            except ValueError:
                print("not a number!")
                continue
        
        if second_nr == "done":
            break
        
        if first_nr < second_nr:
            print("larger!")
            
        if first_nr == second_nr:
            print("same!")
            
        if first_nr > second_nr:
            print("smaller!")
        
        first_nr = second_nr

def compare_letters():
    """
    Checks if all letters in the second word is in the first word.
    """
    word_1 = input("What's the first word: ").lower()
    word_2 = input("What's the second word: ").lower()
    
    all_there = True
    
    for letter in word_2:
        if letter not in word_1:
            all_there = False
            break
    
    if all_there:
        print("Match!")
    
    if all_there is False:
        print("No match!")

def match_brackets():
    """
    Checks how many tims a number needs to be doubled until it contains all numbers from 0 to 9.
    """
    while True:
        check_number = input("What is the starting number: ")
        try:
            check_number = int(check_number)
            break
        except ValueError:
            print("not a number!")
            continue
    
    while True:
        max_times = input("What is the maximum number of doubling: ")
        try:
            max_times = int(max_times)
            break
        except ValueError:
            print("not a number!")
            continue
    double_times = 0
    loop_stop = False
    
    while loop_stop is False:
        
        for i in range(10):
            if str(i) not in str(check_number):
                break
            
            if i == 9:
                print("Answer: " + str(double_times) + " times")
                loop_stop = True
        if loop_stop is True:
            break      
        
        check_number *= 2
        double_times += 1
        
        if double_times == max_times:
            print("Answer: -1 times")
            break

def randomize_string(string):
    """
    Randomize a string and returns the original and the new random string.
    """
    random_string = "".join(random.sample(string, len(string)))
    return string + " --> " + random_string

def get_acronym(string):
    """
    Creates an acronym from string using only uppercase letters.
    """
    acronym = ""
    for letter in string:
        if letter.isupper():
            acronym += letter
    return acronym

def mask_string(string):
    """
    Masks the content of a string except the last 4 characters.
    """
    nr_of_hash = len(string) - 4
    end_string = string[-4:]
    return multiply_str("#", nr_of_hash) + end_string
            

def multiply_str(string, integer):
    """
    Multiplies a string.
    """
    return string * int(integer)

def find_all_indexes(string_a, string_b):
    """
    Finds alla indexes in string_a where string_b appere.
    """
    nr_index = ""
    index = 0
    for i in range(0, len(string_a)):
        if index >= i:
            try:
                index = string_a.index(string_b, index)
                nr_index += str(index) + ","
                index += 1
            except ValueError:
                break
    
    if nr_index != "":
        nr_index = nr_index[:-1]
    return nr_index
