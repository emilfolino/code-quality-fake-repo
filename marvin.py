#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
functions for marvin choices
"""
import random

def greet():
    """
    greet
    """
    name = input("What is your name? ")
    print("\nMarvin says:\n")
    print("Hello %s - your awesomeness!" % name)
    print("What can I do you for?!")

def celcius_to_farenheit():
    """
    celsius to fahrenheit
    """
    celsius = float(input("Give me the degrees in Celsius\n"))
    fahrenheit = round(celsius * 9 /5 + 32, 2)
    print("That's " + str(fahrenheit) + " Fahrenheit")

def word_manipulation():
    """
    word manipulation
    """
    word = input("Type a word ")
    word_multiply = input("Now type a number ")
    try:
        if word_multiply != "0":
            print(multiply_str(word,word_multiply))
        else:
            print("0 is not a valid number")
    except ValueError:
        print("Not a number")

def sum_and_average():
    """
    sum and average
    """
    total_sum = 0.0
    total = 0.0
    average = 0.0
    new_number = 0.0
    number = ""
    while(number != "done"):
        number = input("Type a number to continue or type 'done' to end ")
        try:
            new_number = float(number)
            total_sum += new_number
            total += 1
            average = round(total_sum / total, 2)
        except ValueError:
            if number == "done":
                print("Done! ")
                break
            else:
                print("not a number")
                continue
    print("The sum of all numbers is " + str(total_sum) + " and the average is " + str(average))

def hyphen_string():
    """
    hyphen string
    """
    counter_word = 0 #Used as 2 counters for index + times multiplied 
    new_word = ""
    first_word = input("Type a word to continue or type 'done' to exit\n")
    for _ in range(len(first_word)):
        new_word += first_word[counter_word] * (counter_word + 1) + "-"
        counter_word += 1
    print(new_word[:-1])

def is_isogram():
    """
    isogram
    """
    isogram_word = input("Type a word, and I will check if it's an isogram\n")
    count_isogram = 0
    for _ in range(len(isogram_word)):
        if(isogram_word[count_isogram] in isogram_word[count_isogram + 1:]):
            print("No match!")
            break
        elif count_isogram == len(isogram_word) -1:
            print("Match!")
        count_isogram += 1

def compare_numbers():
    """
    compare numbers
    """
    big_number = None
    number_input = ""
    while number_input != "done":
        if big_number is None:
            number_input = input("Give me a number to start with ")
            try:
                big_number = int(number_input)
            except ValueError:
                print("not a number!")
                continue
        number_input = input("Give me another number ")
        try:
            if int(number_input) > big_number:
                print("larger!")
                big_number = int(number_input)
            elif int(number_input) < big_number:
                print("smaller!")
                big_number = int(number_input)
            elif int(number_input) == big_number:
                print("same!")
                big_number = int(number_input)
        except ValueError:
            print("not a number!")

def compare_character():
    """
    compare characters
    """
    string1 = input("Give me a string\n")
    string2 = input("Now give me a second string\n")
    count_string = 0
    letters = ""
    true_false = True
    for letter in string2:
        if string2[count_string] in string1:
            letters += letter
            if letters.count(letter) > string1.count(letter):
                print("No match!")
                true_false = False
                break
        else:
            print("No match!")
            true_false = False
            break
        count_string +=1
    if true_false is True:
        print("Match!")


def multiply_by_two():
    """
    multiply by two
    """
    base_number = int(input("Give a number to multiply "))
    multiply_number = int(input("How many times should it try to multiply? "))
    total_number = base_number
    times = 0
    y = 0
    check = False
    for _ in range((multiply_number)):
        for _ in range(10):
            if str(y) in str(total_number):
                check = True
                y += 1
            else: 
                check = False
                break
        if check is True:
            print("Answer: " + str(times) + " times")
            break
        y = 0
        total_number *= 2
        times += 1
    if check is False:
        print("Answer: -1 times")

def replace_tab():
    """
    replace tab
    """
    tab_word = input("Type some text with a tab in it\n")
    new_tab_word = ""
    for symbol in tab_word:
        if symbol == "\t":
            new_tab_word += "   "
        else:
            new_tab_word += symbol
    print(new_tab_word)

def new_name():
    """
    new name
    """
    vocal = "aeiouy"
    name1 = input("Give me a name ")
    name2 = input("Give me a second name ")
    name_combined = ""
    count_name = 0
    for _ in range(len(name1)):
        if name1[count_name] not in vocal:
            name_combined += name1[count_name]
        else:
            break
        count_name += 1
    count_name = 0
    for _ in range(len(name2)):
        if name2[count_name] in vocal:
            name_combined += name2[count_name:]
            break
        count_name +=1
    print(name_combined)

def player_score():
    """
    player score
    """
    score = input("Give me a string of letters and numbers ex.'a2b4A5s3B1\n")
    lowercase = "abcdefghijklmnopqrstuvwxyz"
    uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    new_lower = ""
    new_upper = ""
    c_score = 0
    scoreboard = ""
    lett = ""
    list_score = []


    for value in score:
        if value in lowercase:
            new_lower += value + score[c_score+1]
        elif value in uppercase:
            new_upper += value + score[c_score+1]
        c_score +=1
    c_score = 0
    new_upper = new_upper.lower() # makes all letters lowercase 

    for value in new_lower:
        if new_lower[c_score] in lowercase: # make sure i only check for letters and not numbers
            lett = new_lower[c_score]
            if lett in list_score: #Check if the letter has already been added to the list
                list_index = list_score.index(lett)
                list_score[list_index+1] = str(int(list_score[list_index+1]) + int(new_lower[c_score+1]))
            else:
                list_score.append(lett)
                list_score.append(new_lower[c_score+1])
        c_score +=1

    c_score = 0
    for value in new_upper:
        if new_upper[c_score] in lowercase: # .lower before so have to check lowercase instead of uppercase
            lett = new_upper[c_score]
            if lett in list_score:
                list_index = list_score.index(lett)
                list_score[list_index+1] = str(int(list_score[list_index+1]) - int(new_upper[c_score+1]))
            else:
                list_score.append(lett)
                list_score.append(str(0 - int(new_upper[c_score+1])))
        c_score +=1
    c_score = 0 # resuing c_score
    for value in list_score:
        if value in lowercase:
            scoreboard += value + " " + list_score[c_score+1] + ", "
        c_score +=1
    scoreboard = scoreboard[:-2]
    print(scoreboard)

def randomize_string(word):
    """
    randomize string
    """
    new_word = ""
    full_word = word
    while full_word != "":
        i = random.randint(0,len(full_word) - 1)
        new_word += full_word[i]
        full_word = full_word[:i] + full_word[i+1:]
    return f"{word} --> {new_word}"

def get_acronym(word):
    """
    get acronym
    """
    new_word = ""
    for letter in word:
        if letter.isupper():
            new_word += letter
    return new_word

def multiply_str(string,number):
    """
    multiply string x times
    """
    return string * int(number)

def mask_string(word):
    """
    mask string
    """
    new_word = multiply_str("#", len(word) - 4) + word[-4:]
    return new_word

def find_all_indexes(str1,str2):
    """
    find all indexes
    """
    new_word = ""
    counter = 0
    for _ in range(len(str1) - 1):
        try:
            index = str1.index(str2,counter)
            new_word += str(index) +","
            counter = index + 1
        except ValueError:
            break
    return new_word[:-1]

def points_to_grade(max_points,points):
    """
    points to grade
    """
    grade = ""

    try:
        percent = float(int(points) / int(max_points)) * 100
        if percent < 60:
            grade = "F"
        elif percent < 70:
            grade = "D"
        elif percent < 80:
            grade = "C"
        elif percent < 90:
            grade = "B"
        else:
            grade = "A"
    except ValueError:
        print("Not a number")
    return "score: " + grade

def has_strings(str1,str2,str3,str4):
    """
    check if string in string
    """
    if str1.startswith(str2) and str3 in str1 and str1.endswith(str4):
        return "Match"
    return "No match"
