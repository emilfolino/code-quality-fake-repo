"""
A question bot who answers your questions.
"""
import random

def bulldog_ai():
    #!/usr/bin/env python3
    # -*- coding: utf-8 -*-
    """
    The magical AI who can answer all your questions
    """
    return r"""
       ,_____ ,
      ,._ ,_. 7\
     j `-'     /
     |o_, o    \
    .`_y_`-,'   !
    |/   `, `._ `-,
    |_     \   _.'*\
      >--,-'`-'*_*'``---.
      |\_* _*'-'         '
     /    `               \
     \.         _ .       /
      '`._     /   )     /
       \  |`-,-|  /c-'7 /
        ) \ (_,| |   / (_
       ((_/   ((_;)  \_))) 
    """

def greet():
    """
    A greeting module
    """
    name = str(input("Whats your name?\n"))
    print("Welcome: " + name)

def celcius_to_farenheit():
    """
    Converter between Celcius and Fahrenheit
    """
    C = float(input("Skriv in graderna i Celcius \n"))            
    F = float(C * (9/5) +32)
    print("Det motsvarar: ",round(F, 1) , " grader Fahrenheit")

def word_manipulation():
    """
    Changing words
    """  
    r_w = str(input("Whats the word you want repeated?\n"))
    r_n = int(input("How many times?"))      
    print(multiply_str(r_w, r_n))

def sum_and_average(a=0,count=0):
    """
    Count sum and average
    """
    while True:
        n = input("Enter a number:\n")
        if n == "done":
            break
        num = float(n)
        a = a + num
        count = count +1
    print(round(a,2), round(a/count, 2))          
   
def hyphen_string():
    """
    Changing a word
    """ 
    word_input = input("Write a word for me to play with: ")
    new_input = ""
    for index, char in enumerate(word_input):
        new_input += char * (index + 1) + "-"
    print(new_input[:-1])

def is_isogram():
    """
    Look if it is a isogram
    """
    word = input("Give me a word!\n")
    letter_list = []
    a = True
    for letter in word:
        if letter in letter_list:
            a = False        
        letter_list.append(letter)
        
    if a:
        print("No Match!")
    else:
        print("Match!")

def compare_numbers():
    """
    Comparing numbers
    """
    input1 = int(input("First number:\n"))
    while True:
        try:
            input2 = input("Second number:\n")
            if input2 == "done":
                break
            input3 = int(input2)
            if input1 == input3:
                print("same!")
            elif input1 > input3:
                print("lower!")
            elif input1 < input3:
                print("larger!")
            input1 = input3
        except ValueError:
            print("Only numbers!")
def word_match():
    """
    Checking words if match
    """
    input1 = str(input("Please write first word"))
    input2 = str(input("Please write second word"))
    if input2 in input1:
        print("Match")
    else:
        print("No match")

def number_searching():
    """
    Controls numbers with search
    
    input1 = int(input("Please choose a number"))
    input2 = int(input("Please choose how many times it should try"))
    count = 0
    while count < input2:        
        if "1" in str(input1):
            if "2" in str(input1):
                if "3" in str(input1):
                    if "4" in str(input1):
                        if "5" in str(input1):
                            if "6" in str(input1):
                                if "7" in str(input1):
                                    if "8" in str(input1):
                                        if "9" in str(input1):
                                            if "0" in str(input1):
                                                print("match!")
                                                print ("Answer:", count, "times.")
                                                break    
        count += 1
        input1 *= 2
    if count == input2:
        print("Answer: -1")
"""
def tab_replace():
    """
    Replaces a tab with spaces
    """
    letters = input("Choose a word:\n")
    word = letters.replace("\t", "   ")
    print(word)

def vocal_count():
    """
    Counts all vocals
    """
    name1 = input("Name 1 please\n")
    name2 = input("Name 2 please\n")
    count = 0
    count2 = 0
    vokaler = ["a", "e", "i", "o", "u", "d"]
    for char in name1:
        if char in vokaler:
            break
        count2 += 1
    for char in name2:
        count += 1
        if char in vokaler:
            break   
    print(name1[:(count2)] + name2[(count-1):])

def randomize_string(word):
    """
    Makes a string and print it random
    """    
    random_word = "".join(random.sample(word,len(word)))
    string_return = (str(word) + " --> " + str(random_word))
    return (string_return)

def get_acronym(word):
    """
    Gets acronyms
    """
    new_word = ""
    for char in word:    
        if char.isupper():            
            new_word += char
        elif char.islower:
            continue
    return new_word

def points_to_grade(score):
    """
    Makes points to grade
    """      
    if 1.0 >= score >= 0.9:
        grade = ("Score: A")
    elif 0.9 > score >= 0.8:        
        grade = ("Score: B")
    elif 0.8 > score >= 0.7:        
        grade = ("Score: C")
    elif 0.7 > score >= 0.6:        
        grade = ("Score: D")
    elif score < 0.6:
        grade = ("Score: F")
    else:
        grade = ("Error, out of range")
    return grade

def multiply_str(string, times):
    """
    Multiply strings
    """
    multi_string = string * times
    return multi_string

def mask_string(numbers):
    """
    Masks all numbers except the last 4
    """
    count = 0
    last_four = ""
    for num in numbers:
        count += 1
        if count >= (len(numbers)-3):
            last_four += str(num)
    string = multiply_str("#", len(numbers)-4)
    return_string = (string + last_four)
    return return_string

def find_all_indexes(string1, string2):
    """
    Finding all indexes
    """
    start = 0
    lst =[]    
    length = (len(string1)-len(string2))
    while start < length:
        try: 
            lst.append(string1.index(string2, start))
        except ValueError:
            break
        start += 1
    lst = list(dict.fromkeys(lst))  
    lst_new = [str(a) for a in lst]
    lst_joined = ("," . join(lst_new))
    return lst_joined
