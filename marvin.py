#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
modules for marvin
"""

from random import sample

morvin_image = r"""

      ──────────▓▓▓▓▓▓▓────────────▒▒▒▒▒▒
      ────────▓▓▒▒▒▒▒▒▒▓▓────────▒▒░░░░░░▒▒
      ──────▓▓▒▒▒▒▒▒▒▒▒▒▒▓▓────▒▒░░░░░░░░░▒▒▒
      ─────▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▒▒░░░░░░░░░░░░░░▒
      ────▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░▒
      ────▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░▒
      ───▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░▒
      ──▓▓▒▒▒▒▒▒░░░░░░░░░░░▒▒░░▒▒▒▒▒▒▒▒▒▒▒░░░░░░▒
      ──▓▓▒▒▒▒▒▒▀▀▀▀▀███▄▄▒▒▒░░░▄▄▄██▀▀▀▀▀░░░░░░▒
      ──▓▓▒▒▒▒▒▒▒▄▀████▀███▄▒░▄████▀████▄░░░░░░░▒
      ──▓▓▒▒▒▒▒▒█──▀█████▀─▌▒░▐──▀█████▀─█░░░░░░▒
      ──▓▓▒▒▒▒▒▒▒▀▄▄▄▄▄▄▄▄▀▒▒░░▀▄▄▄▄▄▄▄▄▀░░░░░░░▒
      ───▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░▒
      ────▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░▒
      ─────▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▀▀▀░░░░░░░░░░░░░░▒
      ──────▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░▒▒
      ───────▓▓▒▒▒▒▒▒▒▒▒▒▄▄▄▄▄▄▄▄▄░░░░░░░░▒▒
      ────────▓▓▒▒▒▒▒▒▒▄▀▀▀▀▀▀▀▀▀▀▀▄░░░░░▒▒
      ─────────▓▓▒▒▒▒▒▀▒▒▒▒▒▒░░░░░░░▀░░░▒▒
      ──────────▓▓▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░▒▒
      ────────────▓▓▒▒▒▒▒▒▒▒▒░░░░░░░░▒▒
      ─────────────▓▓▒▒▒▒▒▒▒▒░░░░░░░▒▒
      ───────────────▓▓▒▒▒▒▒▒░░░░░▒▒
      ─────────────────▓▓▒▒▒▒░░░░▒▒
      ──────────────────▓▓▒▒▒░░░▒▒
      ────────────────────▓▓▒░▒▒
      ─────────────────────▓▒░▒
      ──────────────────────▓▒
  
"""

def morvin_greeting():
    """initial menu"""
    print(chr(27) + "[2J" + chr(27) + "[;H")
    #print(morvin_image)
    print("Hello hello, I'm Morvin. I know a thing or two. What can I do for you?")
    print("1) Present yourself to Morvin.")
    print("2) Calculate Farenheit from Celsius.")
    print("3) Word multiplier.")
    print("4) Sum and average.")
    print("5) String letter multiplier.")
    print("6) Isogram checker.")
    print("7) Number comparer.")
    print("a1) Check string with string.")
    print("a2) Number doubles.")
    print("a3) Replace tab with space.")
    print("a4) Add names.")                            
    print("a5) Point counter.")
    print("q) to exit.")

def wait_function_end():
    """allows user to wait"""
    input("\nPress enter to continue...")

def end_morvin():
    """print end phrase"""
    print("Buh-buy - and welcome back anytime!")

def greet():
    """greet morvin"""
    name = input("What is your name? ")
    print("\nMorvin says:\n")
    print(f"Hello {name} - your awesomeness!")
    print("What can I do you for?!")
    #wait_function_end()

def celcius_to_farenheit():
    """converts c to f"""

    celsius = float(input("Please enter temperature in Celsius: "))
    farenheit = round((celsius * 9) / 5 + 32, 2) # [°F] = [°C] * 9 / 5 + 32
    print(f"{celsius} degrees Celsius is equal to {farenheit} degrees Farenheit")

    #wait_function_end()

def word_manipulation():
    """repeats word"""
    word_input = input("Please enter a word to repeat: ")
    repetitions = int(input("Please enter the number of repetitions: "))

    print(multiply_str(word_input, repetitions))   
    #wait_function_end()

def sum_and_average():
    """displays sum n avarage"""
    count_input = 0
    sum_input = 0
    input_string = ""

    while True:
        input_string = input("Enter a number (or done to exit): ")
        if input_string != "done":
            count_input += 1
            sum_input += float(input_string)
        else:
            break

    print(f"The sum of all numbers is {round(sum_input, 2)} and the average is {round(sum_input/count_input, 2)}")
    #wait_function_end()

def hyphen_string():
    """makes a string wierd"""
    string_input = input("Enter a string to space out: ")
    string_converted = ""
    letter_counter = 0
    for letter in string_input:
        letter_counter += 1
        string_converted = string_converted + letter * letter_counter + "-"
    print(string_converted)
    #wait_function_end()

def is_isogram():
    """checks if isogram"""
    is_isogram_string = ""
    letter_counter = 0
    word_length = 0
    word_to_check = input("Enter a word to check for isogramness: ")
    for letter in word_to_check: #checks letters in word
        word_length += 1
        for letter2 in word_to_check:
            if letter == letter2:
                letter_counter += 1
    if letter_counter <= 1: #for words with 1 char, isogram
        is_isogram_string = "Match!"
    elif letter_counter > word_length: #if more l1=l2 than letters, not isogram
        is_isogram_string = "No match!"
    
    else:
        is_isogram_string = "Match!"
    print(is_isogram_string)
    #wait_function_end()

def compare_numbers():
    """compares numbers.."""
    first_run = True
    while True:
        if first_run is True: #pylint did not like == True
            input2 = input("Enter a number: ")
            input1 = input2 #saves previous input
            if input2 == "done":
                break
            try: 
                input1 == int(input1)
            except ValueError:
                print("not a number!")
                continue  
            first_run = False
            continue
        input2 = input("Enter a number: ")
        if input2 == "done": #checks for done before input check
            break
        try: 
            input2 == int(input2)
        except ValueError:
            print("not a number!")
            continue  
        if int(input2) > int(input1):
            print("larger!")
        elif int(input2) == int(input1):
            print("same!")
        else:
            print("smaller!")
        input1 = input2 #saves previous input
        print(input2)
    #wait_function_end()   
    print("exiting")
    #sum and av
   
def randomize_string(word):
    """randomizes string"""
    
    new_string = ""
    
    while True:
        temp_string = sample(word, len(word)) #ger random sample från pop, 
        
        for i in temp_string: #sample -> ny sträng
            new_string += i
        
        if word != new_string:
            break
    
    output_string = f"{word} --> {new_string}"
    return output_string

def get_acronym(string):
    """get acronym from capitals"""
    new_string = ""
    for letter in string:
        if letter.isupper() is True:
            new_string += letter
    return new_string

def mask_string(string):
    """masks a string 03030303 -> ####0303"""

    masked_string = multiply_str("#", len(string)-4)

    for i in range(len(string)-4, len(string)):
        masked_string += string[i]
    return masked_string


def multiply_str(string, times):
    """multiplies string"""
    return string * times

def find_all_indexes(str1, str2):
    """finds all indexes"""
    out_string = ""
    start_pos = 0
    stop_pos = len(str1)

    for i in range(0, stop_pos): #finds all str2 in str1
        try:
            if str1.index(str2, start_pos) == i:
                out_string += str(i) + ","
                start_pos += 1
            else:
                start_pos += 1
        except ValueError:
            return out_string

    if out_string[len(out_string)-1] == ",": #fix for trailing ,
        out_string = out_string[0:len(out_string)-1] 

    return out_string
