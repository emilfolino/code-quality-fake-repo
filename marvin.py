"""
Functions for choices in Marvin.py

"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import random

def greet():
    """
    function for meny choice 1, ask for name
    """
    name = input("What is your name? ")
    print("\nMarvin says:\n")
    print("Hi " + name + "! How are you today?")
    print("What would you like me to do?")


def celcius_to_farenheit():
    """
    meny choice 2, convert celsius to fahrenheit
    """
    print("This is the Celsius to Fahrenheit converter!")
    print("Marvin says:")
    temp_c = float(input("Enter a temperature in °C then press enter: "))# anv matar in temp i c, omv till float
    temp_f = temp_c * 9 / 5 + 32 #omvandlar temp i celsius till Fahrenheit

    print()
    #skriver ut temp omvandlat till 2 decimaler
    print("Marvin says: {tempc} °C is the same as {tempf} °F!".format(tempc=temp_c, tempf=round(temp_f, 2)))


def word_manipulation():
    """
    meny choice 3,multiply a string
    """

    print("---Wordgame---")
    print("Marvin: This is a word game!")
    word= input("Enter a word: ")
    number = int(input("Enter a number: "))
    print()

    multipl_word = multiply_str(word, number)
    print("Marvin says: " + multipl_word)


def sum_and_average():
    """
    meny choice 4, calculate the sum and average of number from the user
    """

    print("---Sum and average---")
    sum_= 0.0
    turns=0
    average =0.0
    while True:
        input_nr = input("Enter a number or type \"done\" if you are ready: ")

        if input_nr == "done":
            break

        else:
            try:
                input_nr = float(input_nr)

            except ValueError:
                print("not a number!")
                continue

            sum_ = sum_ + input_nr
            turns += 1
            average = sum_/turns
            print()
            print(f"Marvin: The sum of all numbers are {round(sum_,2)} and the average is {round(average, 2)}")


def hyphen_string():
    """
    Meny 5, Marvin ask for a string and print a new string where each character is +1
    """
    print("---Letters---")
    string = input("Enter a string: ")
    new_string= ""
    nr_turns = 1

    for letter in string:
        letter = letter * nr_turns
        new_string = new_string + letter +"-"
        nr_turns += 1

    # Skriver ut längden på strängen men tar bort sista tecknet så det ej blir "-" på slutet
    print (new_string[0:(len(new_string) -1)])


def is_isogram():
    """
    Meny choice 6, check if a word is a isogram word
    """
    print("---Isogram---")
    isogram_word = input("Marvin says: Enter a word: ")
    new_string =""

    for letter in isogram_word:
        if letter in new_string: #om bokstaven redan finns i ordet
            print ("No match!")
            break

        else:
#skapar en ny sträng av samma ord som används för att jämföra nästa bokstav
            new_string = new_string + letter

# då man gått iegon hela strängen från början till slut och de är likadana
            if new_string == isogram_word:
                print ("Match!")


def compare_numbers():
    """
    Meny choice 7, check if the input nr is larger or smaller
    """
    print("---Larger or smaller---")
    while True:
        try:
            start_value = int(input("Enter a number: "))
            break
        except ValueError:
            print("not a number!")

    while True:
        new_number = input("Enter a number or type \"done\" if you are ready: ")
        if new_number == "done":
            break

        else:
            try:
                new_number = int(new_number)

            except ValueError:
                print("not a number!")
                continue


            if new_number> start_value:
                print ("larger!")
                start_value = new_number

            elif new_number< start_value:
                print("smaller!")
                start_value = new_number

            elif new_number== start_value:
                print("same!")
                start_value = new_number


def randomize_string(user_string):
    """
    Meny choice 8, randomice a string from the user
    """
    list_string= list(user_string)
    random.shuffle(list_string)
    result= "".join(list_string)

    output_string= user_string + " --> " + result
    return output_string


def get_acronym(input_string):
    """
    Meny choice 9, creates a acronyme with the uppercase letters
    """
    acronyme_string = ""

    for char in input_string:
        if char.isupper():
            acronyme_string = acronyme_string + char

    return acronyme_string


def mask_string(inp_string):
    """
    Meny choice 10, replace all letter except the last 4 with "#"
    """
    last_4= inp_string[len(inp_string)-4:]
    string_length= len(inp_string)-4


    maskstring= multiply_str("#", string_length)

    newstring= maskstring+ last_4
    return newstring


def find_all_indexes(str_1, str_2):
    """
    Meny choice 11, Find all index positions in a string
    """
    start=0
    index=0
    index_string=""

    while (start<= len(str_1)):
        try:
            index= str_1.index(str_2, start, len(str_1))
            index_string= index_string + str(index) + ","
            start = index +1

        except ValueError:
            break

    return index_string[0:len(index_string)-1]



def multiply_str(str_input, int_input):
    """
    Takes two argument,a string and a int and multiply them
    """
    multiplyed_string = str_input* int_input
    return multiplyed_string
