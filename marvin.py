#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
this is the page for all of the funktions that will be used in the main file for a variety of diferent tasks
"""

import random


marvin_image = r"""


 ███╗   ███╗ █████╗ ██████╗ ██╗   ██╗██╗███╗   ██╗
 ████╗ ████║██╔══██╗██╔══██╗██║   ██║██║████╗  ██║
 ██╔████╔██║███████║██████╔╝██║   ██║██║██╔██╗ ██║
 ██║╚██╔╝██║██╔══██║██╔══██╗╚██╗ ██╔╝██║██║╚██╗██║
 ██║ ╚═╝ ██║██║  ██║██║  ██║ ╚████╔╝ ██║██║ ╚████║
 ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝  ╚═══╝  ╚═╝╚═╝  ╚═══╝
"""
"""
 this is where the funktions are lokated for the diferent tasks
"""

def greet():
    """
    the greating funk
    """

    name = input("What is your name? ")
    print("\nMarvin says:\n")
    print("Hello %s - your awesomeness!" % name)
    print("What can I do you for?!")


def f_converter():
    """
    converters feren and celsius.
    """ 
    feren = input("input fahrenheit to be converted: ")

    celsius = (int(feren) - 32)
    celsius = float(celsius)  * (5/9)
    print("\nfrom " + str(feren) + " fahrenheit you get " + str(round(celsius, 2)) + " celsius")


def celcius_to_farenheit():
    """
    convert f to c 
    """ 
    celsius = input("input celsuis to be converted: ")
    feren = float(celsius) * (9/5) + 32
    print("\nfrom " + str(celsius) + " celsius you get " + str(round(feren, 2)) + " fahrenheit")


def word_manipulation():
    """
    2 funk string manipulators, first multi play string and then count bokstäver
    """
    str1 = input("enter the string ")
    int1 = int(input("enter the int "))
    print(multiply_str(str1, int1))
 


def sum_and_average():
    """
    defining the avrage and the sum of a string of floats or ints
    """
    the_sum = 0
    ave = 0
    count = 0
    while True:

        i = input("enter num int or float: ")

        try:
            
            the_sum += float(i)

        except ValueError:
            if str(i) == "done":

                if count == 0:
                    ave = the_sum
                else:
                    ave = the_sum / count
                print(f"The sum of all numbers are {round(the_sum, 2)} and the average is {round(ave, 2)}") 
                break

            else:
                print("invalid input")
        
    
        count += 1


def hyphen_string():
    """
    multiply the number of letters with the number of itturations sepperated wit a "-"
    """
    x = input("enter a string: ")
    new_str = ""
    count = 1
    for i in x:
        if count == len(x):
            new_str += (i * count)
        else:
            new_str += (i * count) + "-"
        count += 1
    print(new_str) 


def is_isogram():
    """
    isotone checking funktion
    """
    x = input("enter a string: ")
    new_str2 = ""
    if_is_in = 0
    for i in x:
        if i in new_str2:
            if_is_in = 1 
        new_str2 = new_str2 + i
    if if_is_in == 1:
        print("No match!")
    else:
        print("Match!")


def compare_numbers():
    """
    compare two numbers
    """

    print("enter a number and i will tell if it was larger or smaler. type done when you want to exit")
    input1 = input(" --->")
        
    int2 = int(input1)

    while input1 != "done":
        input1 = input(" --->")
        try:
            if float(input1) < int2:
                print("smaller!")
            
            elif float(input1) == int2:
                print("same!")
            
            elif float(input1) > int2: 
                print("larger!")
                
            int2 = float(input1)       
        except ValueError:
            if input1 != "done":
                print("not a number!")


def a1_funk():
    """
    word check
    """
    w1 = input("enter first string: ")
    w2 = input("enter second string: ")
    counter = 0
    for i in w2:
        if i.lower() in w1.lower():
            counter += 1
    if counter == len(w2):
        print("Match!")
    else:
        print("No match!")


def a2_funk():
    """
    mult by two untill we have 1234567890 in it
    """
    count = 0
    num_check = 0
    the_res = 0
    mult = int(input("the num to multiply: "))
    rep = input("how many times to try: ")

    for i in range(int(rep)):
        for num_check in range(10):
            if str(num_check) in str(mult):
                count += 1
        
        if count == 10:
            the_res = i

        mult = mult * 2
    if i != 0:
        print(f"Answer: {the_res} times")
    else:
        the_res = -1
        print(f"Answer: {the_res} times")


def a3_funk():
    """
    a funktion that removes /t and ads 3 spaces in its sted
    """
    x = input("enter string with \t: ")
    lst1 = x.replace("\t", "   ")
    print(lst1) 


def a4_funk():
    """
    conkatunating string
    """
    nam = input("your name: ")
    efter = input("last name: ")
    print("hi")
    vo = "a e i o u y"
    na_ny = ""
    ef_ny = ""
    found = 0
    for i in nam:
        if i not in vo:
            na_ny += i

        else:
            break

    for y in efter:
        if y in vo:
            found = 1
        if found != 0:
            ef_ny += y
    
    conca = na_ny + ef_ny
    print(conca)


def a5_funk():
    """
    a tally system for points
    """
    score = input("enter the score like 'a4g5A4h3': ")
    upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    result = []
    temp = []
    index = 1
    res_string =""

    for i in score:
        
        if i.isalpha() == 1:  
            temp = [i, int(score[index])]
            if temp[0] not in upper:
                if temp[0] in result:
                    alin = result.index(i)
                    result[alin + 1] += int(temp[-1])
                else:
                    result += temp
            if temp[0] in upper:
                if temp[0].lower() in result:
                    alin = result.index(i.lower())
                    result[alin + 1] -= temp[1]
                else:
                    result += [i.lower(), (int(score[index]) * (-1) )]
        index += 1

    for x in enumerate(result):
        if x[0] % 2 == 0:
            res_string += str(result[x[0]]) + " "
        else:
            res_string += str(result[x[0]]) + ", "

    res_string = res_string.strip(", ")
       


    
    print(str(result))
    print(res_string) 


def randomize_string(string):
    """
    randomize a string with the use of random
    """
    result = ''.join(random.sample(string,len(string)))
    return f"{string} --> {result}"


def get_acronym(string):
    """
    a funk that gets the akronym
    """
    new_string = ""

    for i in string:
        if i.isupper():
            new_string += i
    return new_string

def mask_string(statment):
    """
    word manipulation
    """
    last_dig = statment[-4:]
    length = len(statment) - 4
    first_part = multiply_str("#", length)

    new_string = first_part + last_dig
    return new_string


def multiply_str(string, integer):
    """
    funk that mult string and int
    """
    statment = string * integer
    return statment


def find_all_indexes(string, sub_string):
    """
    find all the indexes of a specifik string in another word
    """
    the_list = []
    start = 0
    answer = ""
    new_answer = ""

    while True:
        try:
            index = string.index(sub_string, start) 
            the_list.append(index)
            start = int(index + 1)

        except ValueError:
            break
    
    if the_list != []:
        for i in the_list:
            answer += f"{i},"
        new_answer = answer.strip(",")
    return new_answer
