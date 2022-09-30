#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
All the functions for the marvin bot.
"""

import random
 
def greet():
    """
    Greets the user
    """
    name = input("What is your name? ")
    print("\nMarvin says:\n")
    print(f"Hello {name} - How can i help you today?")

def celcius_to_farenheit():
    """
    Converts celsius to fahrenheit
    """
    try:
        celsius = float(input("Type a temperature in Celsius and I'll convert it to Fahrenheit. "))
    except ValueError:
        print("Not a valid number.")
    else:
        fahrenheit = round(celsius * 1.8 + 32,2)
        print(fahrenheit)

def sum_and_average():
    """
    Keeps a running sum and average
    """
    running_sum = 0
    iterations = 0
    while True:
        try:
            input_test = input("Insert a number ")
            running_sum += float(input_test)
            iterations+=1
        except ValueError:
            if input_test == "done":
                average = running_sum / iterations
                print(f"The sum of all numbers are {round(running_sum,2)} and the average is {round(average,2)}")
                break

def word_manipulation():
    """
    multiplies words
    """
    word = input("What word would you like me to multiply? ")
    times = input("And how many times? ")
    finalword = multiply_str(word, times)
    
    print(finalword)

def hyphen_string():
    """
    hyphenates a string and each letter is repeated based on it's position
    """
    original_word = input("Input your word: ")
    finalword = ""
    i = 1
    for c in original_word:
        finalword += multiply_str(c,i)
        finalword += "-"
        i+=1
    finalword = finalword[0:len(finalword)-1]
    print(finalword)

def is_isogram():
    """
    checks if a word is an isogram
    """
    possible_isogram = input("Input your word. ")
    is_isograms = True
    for i in range(0, len(possible_isogram)):
        for j in range(i+1, len(possible_isogram)):
            if(possible_isogram[i:i+1] == possible_isogram[j:j+1]):
                is_isograms = False
    if(is_isograms):
        print("Match!")
    else:
        print("No match!")

def compare_numbers(prev_number = 1):
    """
    compares numbers
    """
    if prev_number == "":
        try:
            prev_number = int(input("First you have to set the Comparasion number. "))
        except ValueError:
            print("Not a valid number, number has been set to 0")    

    while(True):
        try:
            input_number = input("Input your number to compare: ")
            input_number = int(input_number)
        except ValueError:
            if input_number == "done":
                return prev_number
            print("not a number!")
        else:
            if prev_number < input_number:
                print("larger!")
            elif prev_number == input_number:
                print("same!")
            else:
                print("smaller!")
            prev_number = input_number

def randomize_string(string):
    """
    randomizes the order of a string
    """
    pick_string = string
    randomized_string = ""

    for _ in range(0, len(string)):
        j = random.randint(0,len(pick_string)-1)  
        randomized_string += pick_string[j:j+1]
        pick_string = pick_string[0:j] + pick_string[j+1:len(pick_string)]

    return string + " --> " + randomized_string

def get_acronym(string):
    """
    takes all Uppercase letters in a string and makes an acronym
    """
    acronym = ""
    for c in string:
        if(c.isupper()):
            acronym += c
    return acronym

def multiply_str(string, times):
    """
    multiplies a string
    """
    return string * times

def mask_string(string):
    """
    Masks a string except for last 4 characters
    """
    final_string = ""
    final_string += multiply_str("#",len(string)-4)
        
    final_string += string[len(string)-4: len(string)]
    return final_string

def find_all_indexes(first_str, second_str):
    """
    finds all indexes of a string in a string
    """
    final_string = ""
    index = 0
    for i in range(0,len(first_str)):
        if i > index:
            try:
                index = first_str.index(second_str, i, len(first_str))
                final_string += str(index) + ","
            except ValueError:
                break
    return final_string[0:len(final_string)-1]

    


def check_if_in():
    """
    check if some letters are all in a string
    """
    all_exist = True
    first_word = input("Input your word to find in. ").lower()
    letters = input("Input your letters to check for. ").lower()
    for c in letters:
        for v in first_word:
            if(c == v):
                break
        else: 
            all_exist = False
            break
    if(all_exist):
        print("Match!")
    else:
        print("No match!")

def multiply_till_complete():
    """
    multiplies a number until all numbers 0 through 9 is in the number or the stop-loss is hit
    """
    try:
        original_number = int(input("Input the number to multiply "))
        stop_loss = int(input("Input your stop loss "))
    except ValueError:
        print("Not valid number!")
    else:
        numbers = "0123456789"
        for i in range(0,stop_loss) :
            confirmed_solution = True
            for j in numbers:
                for k in str(original_number):
                    if(j == k):
                        break
                else:
                    confirmed_solution = False
            if confirmed_solution:
                print(str(i) + " times")
                break
            original_number *= 2
        else:
            print(str(-1) + " times")

def replace_tab_with_space():
    """
    replaces all tabs with 3 spaces
    """
    string_with_tabs = input("input your string ")
    full_string = ""
    for c in string_with_tabs:
        if c == "\t":
            full_string+="   "
        else:
            full_string+=c
    print(full_string)

def name_concatenation():
    """
    concatenates two strings based on where their vowels are
    """
    vokaler = "aeiouy"
    first_name = input("Input the first name ")
    second_name = input("Input the second name ")
    first_shortened = ""
    second_shortened = second_name
    for c in first_name:
        for vokal in vokaler:
            if c == vokal:
                break
        else:
            first_shortened += c
            continue
        break
    ident = 0
    for c in second_name:
        for vokal in vokaler:
            if c == vokal:
                break
        else:
            ident += 1
            continue
        break
    second_shortened = second_shortened[ident:len(second_shortened)]
    print(first_shortened + second_shortened)

def count_score():
    """
    counts the score from a string
    """
    players = []
    scores = []
    scoreCard = input("Type in your scorecard: ")
    for i in range(0, int(len(scoreCard) / 2)):
        player = scoreCard[i*2:i*2+1]
        score = int(scoreCard[i*2+1:i*2+2])
        sub = player.isupper()
        try:
            player_index = players.index(player.lower())
        except ValueError:
            players.append(player.lower())
            if(sub):
                scores.append(score*-1)
            else:
                scores.append(score)
        else:
            if(sub):
                scores[player_index] -= score
            else:
                scores[player_index] += score
    final_string = ""
    curr_index = 0
    for c in players:
        final_string += f"{c} {scores[curr_index]}, "
        curr_index+=1
    final_string = final_string[0:len(final_string) - 2]
    print(final_string)

def points_to_grade(max_points, points):
    """
    Gives grade dependent on score and max score
    """
    
    try:
        percent = (int(points)/int(max_points)) * 100
        variabel = "score: F"
        if(percent >= 90): 
            variabel = "score: A"
        elif(percent >= 80): 
            variabel = "score: B"
        elif(percent >= 70): 
            variabel = "score: C"
        elif(percent >= 60): 
            variabel = "score: D" 
        return variabel
    except TypeError:
        return "score: F"

def has_strings(sa = "", sb = "", sc = "",sd = ""):
    """
    checks if sa begins with sb, contains sc and ends with sd
    """
    try:
        sa.index(sc)
        if(sa.startswith(sb) and sa.endswith(sd)):
            return "Match"
        return "No match"
    except ValueError:
        return "No match"
