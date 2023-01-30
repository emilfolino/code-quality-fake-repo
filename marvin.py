#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
my collection of marvin functions
"""
import random

def greet():
    ''' greeter '''
    print("Whats your name?")
    test = input()
    print("Hello" + test + " my name is Hampus")

def celcius_to_farenheit():
    ''' converter '''
    print("How hot is it in celcius?")
    c = float(input("--> "))
    f = c * 9 / 5 + 32
    print(round(f, 2))

def word_manipulation():
    ''' manipulater '''
    print("What word do you want multiplied?")
    word = input("--> ")
    print("How many times do you want it multiplied?")
    multiplied_times = int(input("--> "))
    print(word * multiplied_times)

def sum_and_average():
    ''' sum and avrage finder '''
    print("Write numbers, when you are done write \'done\'")
    looping = True
    case4_out = 0
    case4_num = 0
    while looping:
        case4_in = input("--> ")
        if case4_in != "done":
            case4_out += float(case4_in)
            case4_num += 1   
        elif case4_in == "done":  
            looping = False
    temp = "The sum of all numbers are "   #pga validator klagar på längd av line
    print(temp + str(case4_out) + " and the average is " + str(round(case4_out/case4_num, 2)))

def hyphen_string():
    ''' hyphen string '''
    print("Write your string here")
    case5_word = input("--> ")
    case5_out = ""
    case5_num = 1
    for i in case5_word:
        if case5_num != 1:
            case5_out += "-"
        case5_out += (i * case5_num)
        case5_num += 1
    print(case5_out)
    
def is_isogram():
    ''' check for isogram '''
    print("Write the string you want me to check")
    case6_word = input("--> ")
    case6_out = "Match!"
    for i in case6_word:
        if case6_word.count(i) > 1: 
            case6_out = "No match!"
    print(case6_out)

def compare_numbers():
    ''' compares numbers '''
    #print("Write a number")
    case7_old = float(input("--> "))
    looping = True
    while looping:
        #print("Write a new number to compare with")
        case7_new = input("--> ")
        not_a_num = False
        if case7_new == "done":
            looping = False
            break
        try:
            if case7_old < float(case7_new):
                print("larger!")
            elif case7_old > float(case7_new):
                print("smaller!")
            else:
                print("same!")
        except TypeError:
            print("not a number!")
            not_a_num = True
        except ValueError:
            print("not a number!")
            not_a_num = True
        if not not_a_num:
            case7_old = float(case7_new)
        
def randomize_string(string):
    ''' shuffles string '''
    temp = random.sample(string, len(string))
    newtemp = ""
    for i in temp:
        newtemp += str(i)
    return string + " --> " + newtemp

def get_acronym(string):
    ''' makes acronym '''
    acronym = ""
    for i in string:
        if i.isupper():
            acronym += i
    return acronym

def multiply_str(let, num):
    ''' multiples a string '''
    return let * num

def mask_string(string):
    ''' masks a string '''
    new_string = string[-4] + string[-3] + string[-2] + string[-1]
    
    masked_string = multiply_str("#", len(string) - 4)

    return masked_string + new_string

def find_all_indexes(string1, string2):
    ''' find all indexes '''
    numb = 0
    output = ""
    while True:
        try:
            output += str(string1.index(string2, numb)) + ","
            numb = string1.index(string2, numb) + 1 
        except ValueError:
            output = output[:-1]
            return output

    
     