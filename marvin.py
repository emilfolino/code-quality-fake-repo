"""
Marvin2 assignment
"""
import random


#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def greet():
    """
    Greets the user with his/her name entered
    """
    namnet = input("Enter your name: ")
    print("Hello " + namnet)

def celcius_to_farenheit():
    """
    converts the entered celcius degree to fahrenheti
    """
    celc_grad = float(input("Enter the grade in Celcius and I'll give you Fahrenheit:\n"))
    print("It's equivalent to " +str(round((celc_grad * 9 /5 + 32),2)) + " Fahrenheit")

def word_manipulation():
    """
    multiplies the string with integer entered and prints the result
    """
    str_m = input("Enter a string : ")
    inp_i = int(input("Enter an integer : "))
    print( multiply_str(str_m,inp_i))

def sum_and_average():
    """
    It adds all input values to the list,
    and returns the sum/average as print
    """
    listecik = []
    summan = 0
    while True:
        integ = input("input: ")
        if integ != "done":
            listecik.append(float(integ))
        else:
            break
    for elvar in listecik:
        summan += elvar
    avg = summan/len(listecik)

    print("The sum of all numbers are " + str(round(summan,2)) + " and the average is " + str(round(avg,2)))

def hyphen_string():
    """
    i iterates from 0 to length of string entered
    for every char of i. index, it multiplies with (i+1) and adds -
    function then prints the new string (except the last char as it's an extra -)
    """
    strang = input("Enter a string and I will make it s-tt-rrr-iiii-nnnnn-gggggg: \n")
    new_strang = ''

    # for i in range(0,len(strang)):
    #     new_strang += strang[i] * (i+1) + '-'

    # new_strang = new_strang [:-1]

    for indexe, chara in enumerate(strang):
        new_strang += (indexe+1) * chara + '-'

    new_strang = new_strang [:-1]

    print(new_strang)

def check_isogram(enter_iso):
    """
    Function to check whether the word entered is isogram
    It creates an empty dictionary, for every character in the word
    if the character is already in the list it returns False
    Otherwise it sets the value of that character to 1 in the dictonary.
    Finally, the function returns True
    """
    min_list = {}
    for charx in enter_iso:
        if charx in min_list:
            return False

        min_list[charx] = 1
    return True


def is_isogram():
    """
    It calls check_isogram function for the input string
    if that returns True, it prints Match!
    Otherwise prints No Match
    """
    check_word = input("input: ")
    if check_isogram(check_word):
        print ("Match!")
    else:
        print ("No match!")

def compare_numbers():
    """
    Compares two integer inputs,
    if second one is bigger than the first
    it prints larger
    if it's smaller than the first, it prints smaller
    if equal, prints same
    """
    value_1 = input ("input1: ")

    while True:
        try:
            value_2 = input ("input: ")
            if value_2 == "done":
                break
            if int (value_1) > int(value_2):
                print ("smaller!")
            elif int(value_2) > int(value_1):
                print ("larger!")
            else:
                print ("same!")
            value_1 = value_2
        except ValueError:
            print("not a number! ")
            continue

def randomize_string(damn_string):
    """
    It uses random module,
    and uses the argument of the function and its length
    Since the return of random.sample is list, it adds
    them with join and creates the new string
    """
    strc = ''.join(random.sample(damn_string,len(damn_string)))
    new_str = damn_string + " --> " + strc
    return new_str

def mask_string(maskstr) :

    """
    it first creates an empty string,
    if lenght of the argument is less than or equals to 4
    it returns the str with lenght of argument times #
    if length is greater than 4 then it calls multiply_str function
    with # and string chars except last 4 index
    it then ends the remaining string and returns it

    """
    strm = ""

    if len(maskstr) <= 4:
        strm += '#' * len(maskstr)
    if len(maskstr) > 4 :
        #str = maskstr[-4:] + multiply_str('#',len(maskstr[:-4]))
        strm =  multiply_str ('#', len(maskstr[:-4])) + maskstr[-4:]
    return strm

def multiply_str(substr, heltal) :
    """
    returns the multiplication of string and the integer
    """
    return substr * heltal

def get_acronym(input_acro) :
    """
    For every character in the string
    that is uppercase, it adds to the empty string
    and returns it
    """
    acro_str = ''
    for elem in input_acro:
        if elem.isupper():
            acro_str += elem
    return acro_str

def find_all_indexes(first_str, sub_strng):
    """
    defines a marker
    starts from 0 and runs as long as it's less than the length of string
    it appends the index of first match found to the empty list
    and moves the marker one char to the right

    """
    liste = []
    marker = 0
    strxx = ''
    while marker < len(first_str):

        try:
            liste.append(first_str.index(sub_strng, marker))
            marker = first_str.index(sub_strng,marker) + 1
        except ValueError:
            break

    for elementet in liste:
        strxx += str(elementet) + ','
    return strxx[:-1]

def a1_f():
    """
    calls another function comparestr
    which was defined before in marvin1 assignment
    """
    str_one = input("input1: ")
    str_two = input("input2: ")
    if comparestr(str_one,str_two):
        print("Match! ")
    else:
        print("No match! ")

def comparestr(str_1, str_2):
    """
    tar två sträng argument och kollar om
    alla karaktärer i str2 finns i str1
    """
    str_1 = str_1.lower()
    str_2 = str_2.lower()
    for cha_r in str_2:
        if cha_r not in str_1:
            return False
    return True



def a2_f():
    """
    it calls the other function rakna_ut
    which was defined already in marvin-1 assignment
    """
    tal_new = int(input("input1: "))
    times_new = int(input("input2: "))
    rakna_ut(tal_new, times_new)

def rakna_ut(int_1, int_2):
    """
    Takes two arguments number and no_of_times
    multiplication should continue max
    it calls other check_it function
    and if it's true ( [0-9] is in the number
    it returns the multiplication numbers and)
    it exits the loop
    otherwise it continues to multiply with 2
    """
    for no_times in range(0,int_2+1):
        if check_it (int_1):
            print( "Answer is " + str(no_times) + " times")
            break
        int_1 = int_1 * 2

        print("Answer is -1 times ")

def check_it(numero):
    """
    Checks if the argument has all numbers [0,9]
    """
    hepsi = (1,2,3,4,5,6,7,8,9,0)
    for x_men in hepsi:
        if str(x_men) not in str(numero):
            return False

    return True

def a3_f():
    """
    it creates an empty list
    iterates through the given string
    once \t is found, replaces it with spaces
    and returns the string...
    """
    strnew = ""
    str_tab = input("input: ")
    for x in str_tab:
        if x == '\t':
            strnew = strnew + "   "
        else:
            strnew += x
    print(strnew)


def a4_f():
    """
    it calls the konvertera function
    which also calls hitta_vokal function
    which were done in marvin1 assignment...

    """
    forst_namn = input("input1: ")
    andra_namn = input("input2: ")
    new_forst = ""
    for x in forst_namn:
        if x in ('a', 'e', 'i' , 'o', 'u', 'y') :
            break

        else:
            new_forst += x

    print("Answer is : " + new_forst + konvertera(andra_namn))

def hitta_vokal (s):
    """
    Hittar den första vokalen i strängen och
    returnerar index
    """
    for index, charbb in enumerate(s):
        if charbb in 'aeiouy':
            return index
        return None

def konvertera (s):
    """
    Split string and return only from the
    first index of vokal till end
    """
    index = hitta_vokal(s)
    return s[index:]


def a5_f():
    """
    This is a part of marvin1 assignment..
    """
    game_string = input("input: ")
    dikt = {}
    len_str = len(game_string) #

    for keyz in range (0,len_str,2):
        valuez = keyz+1
        if game_string[keyz].lower() not in dikt and game_string[keyz].islower() :
            dikt[game_string[keyz].lower()] = int(game_string[valuez])
        elif game_string[keyz].lower() not in dikt and game_string[keyz].isupper():
            dikt[game_string[keyz].lower()] = -int(game_string[valuez])

        elif (game_string[keyz].lower() in dikt) and game_string[keyz].islower():
            dikt[game_string[keyz].lower()] += int(game_string[valuez])

        elif (game_string[keyz].lower() in dikt) and game_string[keyz].isupper():
            dikt[game_string[keyz].lower()] -= int(game_string[valuez])

    """
    konvertera dictionary till sträng
    """
    str_out = ""
    for nycket, varde in dikt.items():
        str_out += nycket + " " + str(varde) + ", "

    print(str_out)




def points_to_grade(maxpoang, yourpoang):
    """
    It converts two str arguments to int
    and if %90 of max is less than or equals to your point, the grade is A
    and if %80 of max is less than or equals to your point, the grade is A
    and if %70 of max is less than or equals to your point, the grade is A
    and if %60 of max is less than or equals to your point, the grade is A
    otherwise the grade is F

    """
    if int(yourpoang) >= int((int(maxpoang) * 0.9)):
        return "score: A"
    if int(yourpoang) >= int((int(maxpoang) * 0.8)):
        return "score: B"
    if int(yourpoang) >= int((int(maxpoang) * 0.7)):
        return "score: C"
    if int(yourpoang) >= int((int(maxpoang) * 0.6)):
        return "score: D"

    return "score: F"

def has_strings(strOne, strTwo, strThree, StrFour):
    """
    it has three boolean args,
    first one is if first str starts with the third
    second one is if third str is in first
    and last one is if first str ends with third
    if all conditions are true, it prints Match
    otherwise it returns no match
    """
    cond1 = strOne.lower().startswith(strTwo.lower())
    cond2 = strThree in strOne.lower()
    cond3 = strOne.endswith(StrFour.lower())

    if cond1 and cond2 and cond3 :
        return "Match"

    return "No match"
