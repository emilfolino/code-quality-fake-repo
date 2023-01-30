"""
functions for marvin choices
"""
import random 

def greet():
    """
    introdos your self 
    """
    name = input("What can i call you? ")
    print("\nAbodeh says:\n")
    print("Hello %s - its nice to meet you!" % name)
    print("What can I do for you today?!")


def celcius_to_farenheit():
    """
    convert celcius to farenheit 
    """
    res1 = 0
    str1 = input("Convert Celsius to Fahrenheit ")
    res1 = float(str1) * 9 / 5 + 32
    print("the answer is : ", end = "")
    print(round(res1, 2), end = "")


def word_manipulation():
    """
    print the word many time 
    """
    str2 = input("Enter a word : ")
    num1 = int(input("how many times? "))
    while num1 > 0 : 
        print(str2, end = "")
        num1 -= 1

def sum_and_average(): 
    """
    sum many number and find the average 
    """
    i4 = 0
    y1 = 0
    num15 = 0
    while True:
        str3 = input("Enter number, write done when you finish : ")
        y1 += 1
        if (str3 != "done"):
            i4 += float(str3) 
        else:
            break 
        num15 = float(i4) / y1
    print("the sum is : ", end="")
    print(i4)
    print("the average  is : ",round(num15, 2), end ="")


def hyphen_string():
    """
    Print a word like this hello = h-ee-lll-llll-ooooo
    """
    str4 = input("write a word : ")
    i = 0
    res5 = ""
    for res4 in str4 :
        i += 1
        if i == 1:
            res5 += res4 * i
        else:
            res5 += "-" + res4 * i
    print(res5)

def compare_numbers():
    """
    number game 
    """
    str8 = input("write a number, write done when you finish : ")
    str5 = ""
    i2 = float(str8)
    while True :
        str5 = input("write a number : ")
        if (str5 != "done"):
            try :
                if float(str5) > i2 :
                    print("larger!")
                    i2 = float(str5)
                elif float(str5) < i2 :
                    print("smaller!")
                    i2 = float(str5)
                elif float(str5) == i2 :
                    print("same!")
                            
            except ValueError :
                print("not a number!")
        else :
            break

def is_isogram() :
    """
    check if the words have upper latter and same 
    ex "Hello = not match"
        "name = match
    """
    str6 = input("Enter a word : ")
    word = str6.lower()
    cr_list = []
    i3 = 0
    j = 0
    nothing = ""
    try :
        for char in word : 
            j += 1
            if char in cr_list:
                i3 -= 1
            else:
                cr_list.append(char)
                i3 += 1
    except IndentationError :
        print(nothing)
    if j <= i3 :
        print("Match!")
    else :
        print("No match!")

def randomize_string(s):
    """
    Write a word and the output will be differnt 
    """
    res1= ""

    set1 =''.join(random.sample(s,len(s)))
    res1 = (s + " " + "-->" + " " + set1 )
    return res1



def get_acronym(str7): 
    """
    Print all upper Latter 
    """

    upper_chars_only = ""
    for char_up in str7:
        if char_up.isupper():
            upper_chars_only += char_up

    return upper_chars_only

def multiply_str(word1,number1):
    """
    print the word many time 
    """
    res1 = word1 * int(number1)
    return res1

def mask_string(a_string):
    """
    Hide last 4 numbers 
    """
    m_string = "#"
    a_s_l = len(a_string)
    multiply_str(a_string, a_s_l)
    return (multiply_str(m_string,(a_s_l-4))) + (a_string[-4:])

def find_all_indexes(str23,str45):
    """
    Find all indexes that you are searching för and print the position     
    """
    w = 1
    v = ""
    try:
        for i6 in range(len(str23)):
            if str23.startswith(str45,i6):
                w += 1
                v += str(i6) + ","
        
    except ValueError:
        print("")
    return v.rstrip(",")
