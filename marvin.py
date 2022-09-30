
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
functions for marvin choices
"""



def greet(name):
    """Docstring"""
    name = input("Enter your name: ")
    print("\nMarvin says:\n")
    print("Hello %s you pig!" % name)
    print("What can I do you for?!")

def celsius_to_fahrenheit(ctf):
    """Docstring"""
    celsius = float(input("Enter the amount of °C you want converted to °F:" ))
    fahrenheit = celsius * 9 / 5 + 32
    fahrenheit = str(round(fahrenheit, 2))
    ctf = print("{celsius} °C equals {fahrenheit} °F".format(celsius=celsius, fahrenheit=fahrenheit))
    return ctf

def word_manipulation():
    """Docstring"""
    word = input("Enter a word: ")
    number = int(input("Enter a number: "))
    while number:
        print(word * number)
        break


def sum_and_average():
    """Docstring"""
    number = 0
    total = 0 
    counter = 0
    while True:
        try:
            number = input("Enter a number, type done to finish: ")
            total += float(number)
            counter += 1
        except ValueError:
            if number != "done": 
                print("Not an integer")
        if number == "done":
            print("The total sum is", round(total,2), "and the average is", round(total/counter,2))
            break

def hyphen_string():
    """Docstring"""
    word = input("Write any word: ")
    word1 = ""
    for index, a in enumerate(word):
        word1 += a * (index + 1) + "-"
    print(word1[:-1])


def is_isogram():
    """Docstring"""
    word = input("Write a word:")
    count = 0
    for i in word:
        count += word.count(i)
    if count == len(word):
        print('Match!')
    else:
        print('No match!')

def compare_numbers():
    """Docstring"""
    previous = 0
    current = 0
    num = input("Give me a number: ")
    previous = float(num)

    while True:
        num = input("Give me another number: ")
        if num == "done":
            break
        try:
            current = float(num)
            if current > previous:
                print("larger!")
            elif current == previous:
                print("same!")
            elif current < previous:
                print("smaller!")
            previous = current
        except ValueError:
            print("not a number!")
        continue



def randomize_string():
    """8"""



def get_acronym(acronym):
    """9"""
    caps = [letters for letters in acronym if letters.isupper()]
    capslist = "".join(caps)
    return capslist




#10 FUNKAR EJ
def multiply_str(multword, multnum):
    """10"""
    multstring = multword * int(multnum)
    return multstring


#def mask_string(maskvar):
#    """10"""
#    mask1 = "#"
#    string_length1 = len(maskvar, -4)
#    masked = mask1[-4:].rjust(len(mask1),"#")
#    finishedmask = multiply_str(masked, mask1)
#    return finishedmask



def find_all_indexes(a, b):
    """
    11
    """
    pos = -1
    result = ""
    while True:
        try:
            pos = a.index(b, pos + 1)
            result = result + str(pos) + ","
        except ValueError:
            break

    return(result[:-1])
