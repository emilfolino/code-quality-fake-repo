"""This is the marvin module. In this module all the functions for the marvin chatbot are."""
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random

Marvin_image = r"""
      ,     ,
     (\____/)
      (_oo_)
        (O)
      __||__    \/
   []/______\[] /
   / \______/ \/
  /    /__\
 /\   /____\
"""

def greet():
    """Marvin greets the user"""
    name = input("What is your name? ")
    print("\nMarvin says:\n")
    print("Hello %s - your awesomeness!" % name)
    print("What can I do you for?!")


def celcius_to_farenheit():
    """converts celsius to fareneheit"""
    temp_c = float(input("Please enter the temperature you'd like converted: "))
    temp_i = round(temp_c * 9.0 / 5.0 + 32, 2)
    result = str(temp_c) + ' degrees Celsius is ' + str(temp_i) + ' degrees Farenheit.'
    print(result)

def word_manipulation():
    """Multiplies a given word a given number of times"""
    word = input('Please choose a word: ')
    times = input('How many times do you want it multplied? ')
    number = int(times)
    mult_word =  multiply_str(word, number)
    print(mult_word)


def sum_and_average():
    """Takes inputs and returns the sum and the average of the inputs"""
    state = ''
    i = 0.0
    result = 0.0
    number = input('Please enter a number, or enter "done" when finished. ')
    while state != 'done':
        if number != 'done':
            result += float(number)
        elif number == 'done':
            break
        number = input('Choose another number ')
        i += 1
    average = round(result/i, 2)
    result = 'The sum of all numbers are', str(result), 'and the average is', str(average)
    print(result)


def hyphen_string():
    """Multiplies the character in a string i+1 times for every letter"""
    i = 1
    new_word = ''
    word = input('¨Plese enter a word: ')
    for x in word:
        sequence = (x * i) + '-'
        new_word += sequence
        i += 1
    new_word = new_word[:-1]
    print(new_word)


def is_isogram():
    """Checks if a given word is an isogram"""
    state = True
    char_list = {}
    word = input('Marvin will se if a chosen word is an isogram. Please choose a word: ')
    for char in word:
        if char not in char_list:
            char_list[char] = 1
        elif char in char_list:
            state = False
    if state is True:
        print ('Match!')
    else:
        print('No match!')


def compare_numbers():
    """Compares number inputs and prints if the number is bigger, smaller or the same"""
    i = 0
    number = input('Choose a number ')
    while True:
        if number == 'done':
            break
        try:
            int(number)
        except ValueError:
            print('not a number!')
        else:
            if i == 0:
                last_number = number
                number = input('Choose a second number: ')
                if number == 'done':
                    break
                try:
                    int(number)
                except ValueError:
                    print('not a number!')
                i += 1

            if number == last_number:
                print('same!')
            elif number < last_number:
                print('smaller!')
            elif number > last_number:
                print('larger!')
            print(number + ' ' + last_number)
            last_number = number
        number = input('Choose another number ')


def randomize_string(sentence):
    """Takes a given strign and returns a random string based on that string"""
    l = list(sentence)
    random.shuffle(l)
    shuffled = ''.join(l)
    result = (sentence + ' --> ' + shuffled)
    return result


def get_acronym(sentence):
    """Takes a given string and makes an acronym of all teh capitalized letters"""
    acronym = ''

    for x in sentence:
        y = x.isupper()
        if y is True:
            acronym = acronym + x
    return acronym

def mask_string(series):
    """This function calls on multiply_str() to mask a given string"""
    number = 0
    masked_string = multiply_str(series, number)
    return masked_string

def multiply_str(sentence, number):
    """Take a sentence and either multiply it by a factor, or mask the sequence except for the last four digits"""

    if number > 0:
        mult_word = sentence * int(number)
        return mult_word

    new_series = len(sentence[:-4])*'#'+sentence[-4:]
    return new_series

def find_all_indexes(sequence, subsequence):
    """Find al indwexes for a given substring in a string"""
    indexes = ''
    i = 0
    x = len(sequence) - 1
    if subsequence in sequence:
        while i < x:
            try:
                index = sequence.index(subsequence, i)
            except ValueError:
                i = x
            else:
                indexes += (str(index) + ',')
                i = index
            i += 1
    else:
        print('Not a subsequence!')
    index_list = indexes[0 : -1]
    return index_list

Function_calls = {
'1' : greet,
'2' : celcius_to_farenheit,
'3' : word_manipulation,
'4' : sum_and_average,
'5' : hyphen_string,
'6' : is_isogram,
'7' : compare_numbers,
'8' : randomize_string,
'9' : get_acronym,
'10' : mask_string,
'11' : find_all_indexes
}
