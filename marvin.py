"""
functions or marvin choices
"""

import random

def greet():
    """
    This function is used when you greet Marvin
    """
    name = input("What is your name? ")
    print("\nMarvin says:\n")
    print("Hello %s - What's up?" % name)
    print("What can I do you for?!")

def celcius_to_farenheit():
    """
    This function is used to convert from celsius to fahrenheit
    """
    temp_c = float(input("Tell me the temperature in celsius and i shall convert it to fahrenheit: "))
    temp_f = round(temp_c * 9 / 5 + 32, 2)
    print(f"{temp_c} °C is equivalent to {temp_f} °F")
    
def word_manipulation():
    """
    This function is used to repeat a word the user puts in
    """
    word3 = input("Give me a word and i'll repeat it... ")
    repeat_amount = int(input("How many times do you want me to repeat it? "))
    print(multiply_str(word3, repeat_amount))
    
def sum_and_average():
    """
    This function does the sum and average of numbers
    """
    number = 0
    total = 0
    counter = 0
    while number != "done":
        number = input("Write numbers and I will add them upp and tell you the average. 'done' to quit... ")
        if number != "done":
            counter += 1
            total += float(number)
    print("The sum of all the numbers are " + str(round(total, 2)) + " Average: " + str(round(total/counter, 2)))

def hyphen_string():
    """
    This function adds one letter on per letter in a word
    """
    word5 = input("Give me a word: ")
    new_word5 = ""
    letter_amount = 1
    for letter in word5:
        if letter_amount == 1:
            new_word5 += letter * letter_amount
        else:
            new_word5 += "-" + letter * letter_amount
        letter_amount += 1
    print(new_word5)

def is_isogram():
    """
    This function checks if a word is an isogram or not
    """
    word6 = input("Give me a word an I will check if it is an isogram or not: ")
    new_word6 = ""
    match = True
    for char in word6:
        if char in new_word6:
            print("No match!")
            match = False
        else:
            new_word6 += char
    if match:
        print("Match!")

def compare_numbers():
    """
    This function compares number given by the user
    """
    old = input("Give me a number, 'done' to quit: ")
    try:
        old = float(old)
    except ValueError:
        print("Bye bye...")
    while old != "done":
        new = input("Give me another number: ")
        if new == "done":
            print("Bye bye...")
            break
        try:
            new = float(new)
            if new > old:
                print("larger!")
            elif new < old:
                print("smaller!")
            else:
                print("same!")
            old = new
        except ValueError:
            print("not a number!")
            continue

def randomize_string(string):
    """
    This function randomizes a string
    """
    return str(string) + " --> " + "".join(random.sample(string,len(string)))

def get_acronym(sentence):
    """
    Turns a string into a acronym
    """
    acronym = ""
    for char in sentence:
        if char.isupper():
            acronym += char
    return acronym

def multiply_str(string, integer):
    """
    This function multiplies a string x amount of times
    """
    return string * integer

def mask_string(string):
    """
    This function mask all characters in a string except the last four
    """
    amount_of_number_signs = multiply_str("#", (len(string)-4))
    masked_string = f"{amount_of_number_signs}{string[-4:]}"
    return masked_string

def find_all_indexes(string, substring):
    """
    This function finds all indexes of a substring in a string 
    """
    i = 0
    start = 0
    result = ""
    try:
        while start < len(string):
            i = string.index(substring, start)
            if result == "":
                result += str(i) 
            else:
                result += "," + str(i)
            start = i + 1
        return result
    except ValueError:
        return result
