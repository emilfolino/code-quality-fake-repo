#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Here are the menu choices for marvin
"""

import random

def get_integer():
    """
    loops until the user enters a valid integer, then returns the integer
    """
    while True: #loops until a valid integer is given
        try:
            integer = int(input("--> "))
            break
        except ValueError:
            print("Oooops, that's not an integer! Please try again: ")
    return integer

def get_float():
    """
    loops until the user enters a valid float, then returns the float
    """
    while True: #loops until a valid float is given
        try:
            my_float = float(input("--> "))
            break
        except ValueError:
            print("Oooops, that's not a valid number! Please try again: ")
    return my_float

def greet():
    """
    asks for the username and greets the user
    """
    print("What would you like me to call you?")
    name = input("--> ")
    print("Hi %s, it's a pleasure to meet you!" % name)

def celcius_to_farenheit():
    """
    asks for input in Celsius and converts is to Fahrenheit
    """
    print("Excellent! What is the temperature in C?")
    temp_celsius = get_float()
    temp_f = temp_celsius * 9 /5 +32 # converts C to F
    print("The temperature in Fahrenheit is " + str(round(temp_f, 2))) #prints temp in F

def word_manipulation():
    """
    repeats a word a given number of times and concatenates it into one string
    """
    print("What word would you like me to repeat?")
    user_word = input("--> ")
    print("How many times?")
    no_times = get_integer()
    new_word = multiply_str(user_word,no_times)
    print(new_word)

def sum_and_average():
    """
    takes in values until the user writes "done", then calculates the sum and the average
    """
    print("Write as many numbers as you'd like! When you're ready, write 'done'.")
    the_sum = 0 #keeps track of the sum
    no_iterations = 0 #counts the number of values to calculate the average
    while True: #loops until the user writes "done"
        user_input = input("--> ")
        user_input = user_input.upper() 
        """
        changes the word to upper case so that anything will be accepted: 
        done, Done, DONE, DoNe, etc
        """
        if user_input == "DONE":
            break
        else:
            try:
                user_no = float(user_input)
                the_sum += user_no
                no_iterations += 1
            except ValueError:
                print("Oooops, that's not a number! Please try again!")
    the_average = the_sum / no_iterations #calculate the average
    print("The sum of all numbers are " + str(round(the_sum, 2))
            + " and the average is " + str(round(the_average, 2)))

def hyphen_string():
    """
    modifies a word by repeating its letters a number of times corresponding to
    the letter's position and inserting a hyphen between the different letters
    """
    print("What word would you like me to use?")
    user_word = input("--> ")
    new_word = ""
    counter = 1 #counts the position of each letter to know how many times it should be repeated
    for letter in user_word:
        for _ in range (counter): #repeat a number of times equal to the letter's position
            new_word = new_word + letter
        new_word += "-" #add a hyphen after each different letter
        counter += 1
    new_word = new_word[:-1] #remove the last hyphen
    print(new_word)

def is_isogram():
    """
    checks if a word is an isogram, returns "Match!" if it is and "No match!" if not
    """
    is_an_isogram = True
    print("What word would you like me to use?")
    user_word = input("--> ")
    user_word = user_word.upper() #changes the word to upper case so that the programme is not case-sensitive
    for i, letter in enumerate(user_word):
        if letter in user_word[0:i]:
            is_an_isogram = False
            break
    if is_an_isogram:
        print("Match!")
        #print("The word %s is an isogram!" % user_word)
    else:
        print("No match!")
        #print("The word %s is not an isogram!" % user_word)

def compare_numbers():
    """
    Takes a number at a time and compares it to the previous number
    """
    print("Please write the first integer! (or write 'done' to exit)")
    done = False
    while True: #loops until the user writes "done" or inputs an integer as the 1st number
        num1 = input("--> ")
        num1 = num1.upper() #changes to upper case so that "done" is not case-sensitive
        if num1 == "DONE":
            done = True
            break
        else:
            try:
                num1 = int(num1)
                break
            except ValueError:
                print("Oooops, that's not a number! Please try again!")
    while done is False: # if the first number has been given, this loop will keep asking for the second number
        got_number = False
        print("Previous number: " + str(num1) + ". Write the next number: ")
        num2 = input("--> ")
        num2 = num2.upper() #uppercase so that "done" is not case-sensitive
        if num2 == "DONE":
            break
        else:
            try:
                num2 = int(num2)
                got_number = True
            except ValueError:
                print("not a number!    ")
            if got_number: #if a valid second number has been given, compare the numbers:
                if num2 > num1:
                    print("larger!")
                elif num2 < num1:
                    print("smaller!")
                else:
                    print("same!")
                num1 = num2 #the new number now becomes the old number and the loop repeats

def randomize_string(word):
    """
    Takes a word and shuffles the letters around
    """
    my_list = list(word) #change the word into a list of letters
    random.shuffle(my_list) #shuffle the list
    randomized = ""
    for i in range (len(word)): #add all the shuffled letters to a new string
        randomized += str(my_list[i])
    answer = word + " --> " + randomized
    return answer

def get_acronym(word):
    """
    creates an acronym of a word by taking all the capital letters in it
    """
    acronym = ""
    for letter in word: #for each letter in the word:
        if letter.isupper(): #if the letter is upper case
            acronym += letter #add it to the acronym
    return acronym

def multiply_str(string,integer):
    """
    takes a word and an integer and multiplies the word by the integer, creating a new string
    """
    output = integer*string
    return output

def mask_string(string):
    """
    takes a string and replaces all but the last four digits with ####
    """
    answer = multiply_str("#",(len(string)-4)) # create the desired no of ### (word length -4)
    for i in range (len(string)-4,len(string)): # add the last four letters of the word
        answer += string[i]
    return answer

def find_all_indexes(string1, string2):
    """
    compares two strings, where the second should be contained within the first one
    and lists all indices where the second string is contained within the first
    """
    present = False #keeps track of whether string2 is present even once in string1
    try:
        first_index = string1.index(string2) #try to find string2 in string1
        answer = str(first_index) # this is the index at which it first appears
        present = True # it is present at least once
        latest_index = first_index # this is now the latest occurrence of string2 in string1
    except ValueError: #if string2 isn't present at all, return ""
        answer = ""
    while present: #if string2 occurrs at least once
        try:
            new_index = string1.index(string2, (latest_index + 1)) #try to find string2 later than
            # its most recent position
            answer = answer + "," + str(new_index) # add the new index to the list
            latest_index = new_index # the new position is now the latest position
        except ValueError: # if another occurrence is not found, break
            break
    return answer

def a1():
    """
    Takes two words and determins if all the letters of the second word are present in the first
    """
    print("Write the first word!")
    word1 = input("--> ")
    print("Write the second word!")
    word2 = input("--> ")
    match = True
    for letter in word2:
        if letter not in word1: #as soon as one letter doesn't match, break
            match = False
            break
    if match:
        print("Match!")
    else:
        print("No match!")

def a2():
    """
    Checks how many times a number needs to be multiplied by 2 until it contains all ten digits
    """
    print("What number would you like to test?")
    user_no = get_integer()
    print("How many times should I try before I give up?")
    give_up = get_integer()
    for i in range (give_up):
        test_no = user_no * 2**i
        contains = 0 # this var checks how many of the ten digits are present
        for j in range (0,10): # loops through numbers from 0 to 9
            if str(j) in str(test_no): # if the number is contained within the current value
                contains += 1 # increase the digit count
            else:
                break
        if contains == 10: #if the current value contains all 10 digits
            answer = i # i is the power to which we raised 2
            break
        else:
            answer = -1 # if all the digits are not present, return -1
    print("Answer: %s times" % answer)

def a3():
    """
    replaces all tabs with three spaces
    """
    print("Write something with at least one indentation.")
    user_input = input("--> ")
    user_input = user_input.replace("\t","   ")
    print(user_input)

def a4():
    """
    creates a portmontau of 2 names
    """
    print("Please write two names you'd like to combine: ")
    name1 = (input("---> ")).lower() # change to lower case so that A=a etc
    name2 = (input("---> ")).lower() # ditto
    vowels = "aeiouy"
    vowel_name1 = len(name1) # I assume the first vowel to be at the very end and go from there
    vowel_name2 = len(name2) # ditto
    for letter in vowels: # for each vowel
        vowel_position1 = name1.find(letter) # find if it is present within name1
        if 0 <= vowel_position1 < vowel_name1: # if this vowel is present, is it earlier than the previous vowels?
            vowel_name1 = vowel_position1 # if so, it now becomes the first (earliest-occuring) known vowel
        if vowel_name1 == 0: # if there is a vowel in the first position, we're done
            break
    for letter in vowels: #repeat the same for name2
        vowel_position2 = name2.find(letter)
        if 0 <= vowel_position2 < vowel_name2:
            vowel_name2 = vowel_position2
            if vowel_name2 == 0:
                break
    portmontau = name1[:(vowel_name1)] + name2[(vowel_name2):] 
    #create the portmontau, cutting the words at the respective vowel positions
    print(portmontau)

def a5():
    """
    takes a string that denotes points gained and lost by various players,
    where the players are represented by different letters
    the points gained represented by lower case letters
    and the points lost represented by upper case letters
    the function calculates all the final scores and returns them as a string
    """
    print("Please write the input: ")
    user_input = input("--> ")
    all_letters = "" #this var will store all different letters present
    for char in user_input.lower(): #lower case so that h=H etc
        if char.isnumeric() is False: #if a character is not numeric
            if char not in all_letters: #and it's not already accounted for
                all_letters += char #then add it to the list
    final = "" #this var stores the final answer
    for i, letter in enumerate(all_letters): #for every letter present in the string
        input_testing = user_input #we're copying the user input because we're gonna edit it within the loop
        #and then use it again from the start for the next letter
        input_lower = input_testing.lower() 
        #change the input to lower case to find all scores relating to the same player
        position = input_lower.find(all_letters[i]) #find the position of the letter in the given string
        final += letter + " " # add the letter to the final answer
        current_score = 0 #keeps track of the score for the current player
        while position != -1: #until we've found all instances of a certain letter
            score = ""
            no_digits = 0 #number of digits storing the point value
            for j in range (position+1, len(input_lower)): #from the current letter to the end of the string
                if input_lower[j].isdigit():#if the next character is a digit
                    score = score + input_lower[j] #copy it to the score (as a string)
                    no_digits += 1 #increase the number of digits storing the value
                else:
                    break
            if input_testing[position].islower(): #if the letter was lower case
                score_int = int(score) #then the points are added (positive)
            else: #if the letter was upper case
                score_int = -int(score) #then the points are negative
            current_score = current_score + score_int #add the points to the current score
            input_testing = input_testing[(position+1+no_digits):] #remove everything up to the current letter
            #including the digits storing the relevant score; from now on, we will consider the rest of the string
            input_lower = input_testing.lower() #make this new, shorter string lower case
            position = input_lower.find(all_letters[i]) 
            #check if that same letter appears somewhere else in the string
        final += str(current_score) + ", " 
        #when done counting the points for that player, add the total to the final answer
    final = final[:-2] #remove the last comma and space
    print(final)
        
def points_to_grade(max_points, points):
    """
    convert a point value to a grade based on % of max points possible
    """
    percentage = float(points) / float(max_points)
    # I am only feeding floats into this function anyway ( it is determined in the menu, since 
    # that's where you wanted the input to happen) but the program doesn's pass validation if
    # I don't specify once again that the numbers need to be floats here, within the function
    if percentage >= .9:
        answer = "score: A"
    elif percentage >= .8:
        answer = "score: B"
    elif percentage >= .7:
        answer = "score: C"
    elif percentage >= .6:
        answer = "score: D"
    else:
        answer = "score: F"
    return answer

def has_strings(str1, str2, str3, str4):
    """
    checks if the 1st string starts with the second, contains the 3rd and ends with the 4th
    """
    answer = "No match"
    if str1.startswith(str2):
        if str3 in str1:
            if str1.endswith(str4):
                answer = "Match"
    return answer
