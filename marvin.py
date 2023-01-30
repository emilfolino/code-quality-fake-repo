#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Functions for the menu choices in the
marvin program
"""
import random

def greet():
    """
    The user enters a name and is greeted by that name
    """
    name = input("What is your name? ")
    print("\nQuirk says:\n")
    print(f"Hello {name} - nice to meet you!")
    print("What can I do to help?!")

    
def celcius_to_farenheit():
    """
    The user enters a temperature in celsius this is converted to fahrenheit and presented to the user
    Variable to check if user is done (has entered a correct value for celsius)
    """
    done = False
    while not done:
        celsius = input(
            "Sure I will help you convert a temperature value from celsius to fahrenheit."
            "\nGive me a temperature value in celsius ('r' to return to main menu): ")
        #If user enters 'r' thus indicating they want to return to the main menu, break the loop
        if celsius == 'r':
            break

        #Try to convert the value the user supplied to a float, if succesful we are done, else loop continues
        try: 
            celsius = float(celsius)
            done = True
        except ValueError:
            print("That was not a number!")
            continue
        #Round value to two decimals
        fahrenheit = round(celsius * 9 / 5 + 32, 2)
        #Present value to user
        print(f"The given value in celsius is equivalent to {fahrenheit} degrees fahrenheit.")

    
def word_manipulation():
    """
    The user enters a word and a nr of times to repeat it, the function repeats it that nr of times
    """
    word = input(
        "Sure I can help you say the same words several times!\n"
        "Give me a word to repeat: ")

    #Variable to check if user is done (has entered a correct value for the nr of times to repeat the word)
    done = False
    while not done:
        repeat = input("How many times do you wish me to repeat the word: ")
        #Try to convert the value the user supplied to an int, if succesful we are done, else loop continues
        try: 
            repeat = int(repeat)
            done = True
        except ValueError:
            print("That was not a number!")
            continue

    #Using multiply_str to repeat the word
    print(multiply_str(word, repeat))

def sum_and_average():
    """
    User enters numbers and the function sums them and calculates the average
    """
    print("Sure I'll help you sum some numbers and calculate the average!")

    #Variable for the sum of the numbers
    num_sum = 0
    #Counter for the nr of numbers, used to calculate the average
    counter = 0

    while True:
        number = input("Enter a number please (or enter 'done' if you want me to calculate the sum and average): ")
        if number == "done":
            break
        #Try to convert the number to a float if succesful add it to num_sum and increase counter,
        # else loop continues
        try:
            number = float(number)
            num_sum += number
            counter += 1
        except ValueError:
            print("That's not a number!")
            continue

    #Round the sum to two decimals
    num_sum = round(num_sum, 2)

    #Try to calculate the average, if user entered no numbers there will be 
    #a ZeroDivisionError, in that case return to main menu
    try:
        average = round(num_sum/counter, 2)
        print(f"The sum is {num_sum} and the average is {average}")
    except ZeroDivisionError:
        print("Seems you entered no numbers, oh well!")


def hyphen_string():
    """
    User enters a word and the letters in the word is repeated by +1 for each letter, separated with a '-'
    """
    word = input("Sure I'll help you repeat letters in a word!\nPlease enter a word: ")

    #The last index of the entered string (word)
    last_index = len(word)-1

    #Variable for the modified string
    string = ""

    #For each letter in the word, "string-multiply" the letter with it's position+1,
    # if it's not the last letter append a '-'
    for i in range(0, last_index + 1):
        string += word[i]*(i+1) 
        if i != (last_index):
            string += "-"

    print(f"The word with letters repeated is: {string}")

def is_isogram():
    """
    Checks if a word entered by the user is an isogram (contains no repeated letters)
    """
    word = input("Sure I'll help you check if a word is an isogram!\nPlease enter the word: ")

    #Transform the word to lower case using the string method lower()
    word = word.lower()

    #Calculate last index of the supplied string (word)
    last_index = len(word)-1

    #Variable for a counter that keeps track of the position in a string
    counter = 1

    #Variable for a message telling user if there is a match or not (Match! means the word is an isogram)
    match = "Match!"

    #For each letter in the word, create a string that contains all letters in the word from the current
    #letter's position to the last letter in the word. If the current letter is found in the string, change
    #match to "No match" (a letter is repeated - the word is not an isogram). Increase the counter for each 
    #pass in the loop so that the string starts from the letter after the next letter in the word.
    for letter in word:
        string = word[counter:last_index+1]
        if letter in string:
            match = "No match!"
        counter += 1

    print(f"{match}")

    
def compare_numbers():
    """
    Two nrs entered by the user is compared. The user can continue to enter a nr and it will be compared to the last
    entered nr until user is done
    """
    print("Sure I'll help you check if a number is larger or smaller than another!")

    #Variable to determine if user is done
    done = False
    #Variable to determine if user has entered a correct value
    correct_input = False

    #Get the first nr
    while not correct_input: 
        number_one = input("Please enter a number ('done' to quit): ")
        #If user enters 'done' set done to true and break this loop
        if number_one == "done":
            done = True
            break
        #Try to convert number_one to an int, if succesful set correct_input to True, else loop will continue
        try:
            number_one = int(number_one)
            correct_input = True
        except ValueError:
            print("not a number!")

    #Get more nrs from user until user is done
    while not done:
        #Initialize a variable, result, to "same!" this is the "baseline case message" for the comparison
        result = "same!"
        #Reset correct_input to False
        correct_input = False

        #Get the second nr from user
        while not correct_input: 
            number_two = input("Please enter another number ('done' to quit): ")
            #If user enters 'done' set done to True and break this loop
            if number_two == "done":
                done = True
                break
            
            #Try to convert number_two to an int if not succesful print
            # a message and let user try again (loop continues)
            try:
                number_two = int(number_two)
                correct_input = True
            except ValueError:
                print("not a number!")

        #If done is not true (user has not entered 'done' in the above loops)
        #Compare number_one and number_two and change the value of result accordingly, then print result
        if not done: 
            if number_two > number_one:
                result = "larger!"

            elif number_two < number_one:
                result = "smaller!"

            print(f"{result}")

            #Set number_one to number_two to let user compare with last entered nr in the next pass of the loop
            number_one = number_two

    
def check_strings():
    """
    Checks if one string entered by user contains all characters of another string entered by user
    """
    print("Sure I'll help you check if one string contains all characters of another string!")

    #Let user input string and transform them to lower case with string method lower()
    string_one = input("Please enter the first string: ")

    string_one = string_one.lower()

    string_two = input("Please enter the other string: ")

    string_two = string_two.lower()

    #Variable for a message to the user initialize to "Match" 
    # ( this message should be issued if string_one contains all characters of string_two
    match = "Match!"

    #For each letter in string_two, check if the letter is not present in the first string
    # if the letter is not found change match to "No match" and break the loop
    for letter in string_two:
        if letter not in string_one:
            match = "No match!"
            break
        string_one = string_one.replace(letter, "", 1)

    print(f"{match}")

    
def double_a_number():
    """
    #Lets user enter a number and the number of times (tries) the program will try to multiply the
    number by two. The program checks if the number after multiplication contains all 
    characters from 0-9. If it does the number of times the original number was multiplied
    is returned. If all characters from 0-9 is not present in the number after it has been 
    multiplied the number of times the user entered (the tries) -1 will be returned.
    """
    print(
        "Sure I'll help you check how many times you have to multiply "
        "a number by two for it to contain all integers between 0 - 9")

    #Variable to determine if user input is correct
    correct_input = False
    while not correct_input:
        number = input("Please enter the number: ")
        #Try to convert number to an int, if successful set correct_input to true, else loop continues
        try:
            number = int(number)
            correct_input = True
        except ValueError:
            print("That is not a number")

    #Variable to determine if user input is correct
    correct_input = False
    while not correct_input:
        tries = input("How many times should i try to multiply the number before giving up: ")
        #Try to convert tries to an int, if successful set correct_input to true, else loop continues
        try:
            tries = int(tries)
            correct_input = True
        except ValueError:
            print("Please enter a number")

    #Variable holding a string with all characters 0-9
    integers = "0123456789"

    #Variable to keep track of the times we have multiplied
    times_multiplied = 0

    #Variable to determine if we are done
    done = False

    while not done:
        #Subtract 1 from tries for each pass in the loop
        tries -= 1
        #Variable to keep track of the number of integers found, reset to 0 for each pass
        integers_found = 0
        #For each digit in integers if the digit is not found in the number
        #multiply number by 2 and increase times_multiplied by 1 then break the for-loop.
        #Otherwise increase integers_found by one, check if integers_found equals the length
        #of integers, in that case we have found all 10 digits in integers and are done.
        for digit in integers:
            if digit not in str(number):
                number = number * 2
                times_multiplied += 1
                break
            integers_found += 1
            if integers_found == len(integers):
                done = True

        #If tries are <=0 and we are not done. We couldn´t find all digits in integers
        # in the alloted tries. set times_multiplied to -1 and done to True
        if tries <= 0:
            if not done:
                times_multiplied = -1
                done = True

    print(f"Answer: {times_multiplied} times")

    
def tabs_to_spaces():
    """
    User enters a string with tabs the program replaces each tab in the string with three spaces
    """
    print("Sure I'll help you change from tabs to spaces in a string!")

    #Get the string
    string = input("Enter a string with one or more tabs in it: ")

    #Get the length of string
    string_length = len(string)

    #For i = 0 to string length, set first_part_of_string and second_part_of_string to ""
    # Set string_length to len(string) check if the character at position i in string is a tab
    # if so assign the part of string before position i to first_part_of_string and append three spaces.
    # Then assign the part  of string after position i to second_part_of string. Concatenate first_part_of_string
    #to second_part_of_string and assign the new string (thus with the tab replaced by three spaces)
    #to string.
    for i in range(0, string_length):
        first_part_of_string = ""
        second_part_of_string = ""
        string_length = len(string)
        if string[i] == "\t":
            first_part_of_string = string[0:i] + "   "
            second_part_of_string = string[i+1:string_length]
            string = first_part_of_string + second_part_of_string

    print(f"{string}")

    
def merge_names():
    """
    The user enters two strings (names) and the program merges them to a new string so that the first part of the new
    string contains all consonants up until the first vowel in the first name and the second string contains all
    characters from the second string except the consonants up until the first vowel
    """
    print("Sure I'll help you merge two names!")

    #Get the names and convert them to lowe case  with string method lower()
    name_one = input("Enter the first name: ")

    name_one = name_one.lower()

    name_two = input("Enter the second name: ")

    name_two = name_two.lower()

    #Variable holding a string with the vowels
    vowels = "aeiouy"

    #String variable for first part of the merged name
    first_part = ""

    #String variable for the second part of the merged name
    second_part = ""

    #For each letter in name_one, if the letter is not in vowels add the letter to first part.
    #If the letter is in vowels break this loop.
    for letter in name_one:
        if letter not in vowels:
            first_part += letter
        else:
            break

    #Variable for keeping track of "where we are" in the second name
    index = 0

    #For each letter in name_two if the letter is in vowels set second_part to
    #the string slice of name_two starting at the value of index to the last letter
    # in name_two then break this loop. For each pass in the loop increase the value of
    #index by 1
    for letter in name_two:
        if letter in vowels:
            second_part = name_two[index:len(name_two)+1]
            break
        index += 1

    #Concatenate first_part and second_part and assign to new_name
    new_name = first_part + second_part

    print(f"{new_name}")

    
def scoring():
    """
    The user enters a string where every other character is a number
    and every other character is an alphabetical character (upper or lower case).
    The alphabetical characters (big and small) represents players
    (A and a represents the same player) and the numerical characters represents scores.
    The program sums the score for each player in the string by adding scores
    after a lower case character and substracting scores after an upper case character.
    E.g. a5A5 means player a gets 0 points.
    """
    print("Sure I'll help you figure out the scores!")

    #Get the string
    string = input("Please enter the scoring string: ")

    #Variable for the final scoring string
    scoring_string = ""

    #For i = 0 to to length of the string, increase each step by two
    # (to "catch" all alphabetical characters)if the character is already in the scoring
    # string continue(skip this pass of the loop). Else get the point(numerical character)
    # next to position i, convert it to an int. If the alphabetical character at i is upper
    # case multiply point with -1
    for i in range(0, len(string), 2):
        if string[i].lower() in scoring_string:
            continue
        point = int(string[i+1])
        if string[i].isupper():
            point *= -1
        
        # For each alphabetical character in string starting from the one after the one at i
        # if character at position j equals the character at i in lower case add the point value at
        # position j+1 to point. If character at position j equals the character at i in upper case
        # substract the point value at position j+1 to point. Thus we are adding or substracting all
        # scores for the player at i. 
        for j in range(i+2, len(string), 2):
            if string[j] == string[i].lower():
                point += int(string[j+1])
            elif string[j] == string[i].upper():
                point -= int(string[j+1])
        #Concatenate the character representing the player (in lower case)
        # with the string value of point, add ", " for formatting.
        scoring_string += (string[i].lower() + " " + str(point)) + ", "

    #Remove last ", " in the scoring string
    scoring_string = scoring_string[0:-2]

    print(scoring_string)

def randomize_string(string):
    """
    Takes a string and randomizes it using random modules sample.
    Returns the original string concatenated with --> and the
    randomized string
    """
    #Make sure string is a string
    string = str(string)

    #Create a randomized sequence of the letters in the string
    #using randoms sample
    randomized_sequence = random.sample(string, k=len(string))

    randomized_string = ""

    #Loop through the randomized sequence
    #and add the letter to randomized string
    for character in randomized_sequence:
        randomized_string += randomized_string.join(character)

    return string + " --> " + randomized_string

def get_acronym(string):
    """
    Takes a string and creates an acronym
    from all upper case letters in the string
    """
    string = str(string)

    acronym = ""

    #Loop through string and check if
    #letters are upper case, if so add
    #them to acronym
    for letter in string:
        if letter.isupper():
            acronym += letter

    return acronym

def mask_string(string):
    """
    Takes a string and returns a new 
    string where all characters
    except the last 4 are replaced with '#' 
    """

    string = str(string)

    #Get the number of characters in string
    nr_of_characters = len(string)

    #Calculate nr of masks
    nr_of_masks = nr_of_characters - 4

    masked_string_part = multiply_str('#', nr_of_masks) 

    unmasked_string_part = ""

    #Create a string with the characters from
    #string from the character after last mask
    for i in range(nr_of_masks, len(string)):
        unmasked_string_part += string[i]

    return masked_string_part + unmasked_string_part

def multiply_str(string, integer):
    """
    Takes a string and returns it 
    multiplied by the second argument
    """
    return string * integer

def find_all_indexes(string, substring):
    """
    Takes two strings and returns all
    indexes in the first string where
    the second string is found as a substring
    of the first
    """
    string = str(string)
    substring = str(substring)
    start = 0

    indexes = ""

    #Loop from 0 to length of string
    #try to find an index of substring
    #using the string.index method
    #break loop if the substring is not found
    #(when a ValueError is raised). If an index is found
    #add it to indexes, append a ','. Set start to the value
    #of the index + length of substring to try to find the
    #index of the next substring in the next pass of the loop
    for _ in range(len(string)):
        try:
            index = string.index(substring, start)
        except ValueError:
            break

        indexes += str(index) + ","
        start = index + len(substring) 

    #Remove last ','
    if indexes != "":
        indexes = indexes[0:-1]

    return indexes

def points_to_grade(max_score, score):
    """
    Takes a max score and a score and returns a string with
    the grade associated with the score/max score
    """
    #Check and transform values
    try:
        max_score = float(max_score)
        score = float(score)
    except ValueError:
        return "Either max score or score is not a number"

    #Divide score/max_score, watch out for ZeroDivision error
    try:
        result_score = round(score/max_score, 2) * 100
    except ZeroDivisionError:
        return "Max score was zero - strange exam!"

    score = "score: F"

    if result_score >= 90:
        score = "score: A"
    elif result_score >= 80:
        score = "score: B"
    elif result_score >= 70:
        score = "score: C"
    elif result_score >= 60:
        score = "score: D"

    return score

def has_strings(string, start_string, contained_string, end_string):
    """
    Takes four strings and checks if the first string starts with the second
    contains the third and ends with the fourth. In that case "Match" is returned,
    else "No match" is returned. Using string methods startswith() and endswith()
    """
    if string.startswith(start_string) and contained_string in string and string.endswith(end_string):
        return "Match"

    return "No match"
