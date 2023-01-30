#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
This file contains all of Marv-inu's fuctions. And the picture!
"""

import random

marvinu_image = r"""
                                                                             .    (           .   `
                                                                    `           ` ` (   `     ,
                                               ,»▄¿┌,.              `           ` , `        .
                                     ╓▄▒▓████████████████▓▓▒▄▄╓           :              ) ,       ,
                             .   ╓▄█████████████████████████████▓▒,.      .                ` (   `
                            .(╔▄▓██████████████████████████████████▓▄     ,                  `
         .         .▄▄████▓▒██████████████████████████████████████████▄,, `      ` .         .
         ⌠/¿,▄▄▓█████████████████████████████████████████▓▓▓▓▓▓▒▓▓██████▓▄▄,▄╓,  , (         .
  ▄██████████████████████████████████████████████████████▓▓▒▓▓▓▓████▓███████▓▓▓▓▒╢»}         .
  ╙▀██████████████████████▀▀▒███████████████████████████▓▓▓▓▓▒▒▓▓▒█████████▓▒▒▒▒▒▒▒▓▒╢▄,     `
      └└╙▀▀██████▀▀▀▀▌▒▒▓░(⌠▓████████████████████████████▓▓▓▓▓▓▓▓███████████▒║▒▒▒▒▒▒▒▒▒▓▓▓▒╢M▄»,
           └│▒▒▒╚││╚╠║││└(╔▓████████████████████████████████████████████▓████░┤╚╢▒▒╢▒▒▒▒▓▓▓▓▒▒▓▓▓M
           ( ╙▓▒╢║░∩/;:╓░╠███████████▀▀▀▀▀▀╢▀████████████████████████████████▒Ñ╚╚╠╚╚╚Ñ╠║║║╢▒▒▒Ñ╙└
           (  `▒Ñ╢▒╠░│#║▒██████▓▒▒▒▓▓▒M@▄│   ╙▀▀███████████████████▀▀╚▒▀▀▓████▄∩└│N░╠║▒▒▒▓▓▓▓▓▒M¿
           (    ╫▒▒Ñ#▒▒▓██████▓▓▒▒▒██████████▓▄▒▒███████████████▒╢░░▄╫▓▓██▒▓███▒╢▒▒▓▓▓▓▓▒▓▓▓▓▒▓▒▒▒m
           (    (▒▒▒▒▒██▓████▓▓▓▓██████▓█████████████████████████▓▒▓████████████▒▓▒▒▓▓█▓▓▓▓▒▓▒▓▓▓▒▒▒
   .           .╠▒▒▓▓█▓▓█▓████▓██████████████████████████████████████████████████▒▓▓██▓▓▓██▓▓▓▓▒▓▓▓▓
               (▒▓███▓▓▓▓████▓▓██████████████████████████████████████████████████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█▓█▓
               ╞▒▓███▓▓▓█████▓▓███████████████████████▒███████████████████████████▓▓▓▒▓▓▓▓▓▓▓██▓▓▓▓█
               ├▒▓█████▓█████▓▒████████████████████████▓▀▒╠╙╙╙╚▀██████████████████▓▓█▓▓▓▓▓▓▓▓▓▓▓▓▓██
               ║█▓▓███████████▓▓███████▀▒▒███████████Ñ▒▀┘└`╘╙╫╢⌐└█████████████████▓███▓▓▓█▓▓▓▓▓▓▓▓▓▓
              .▓█▓▓█▓██▓▓▓██▓▓▓▓███████╠.,╚█████████▓╠.          ╫████████████████▓█▓▓▓█▒▓▓▓▓▓▓▓▓▓▓█
              :▒█▓▒▓▓█▓▓▓▓▓▓▒▓▓▓▓▓█████▓░╔`╙███████▌╠Ñ.        ⁿ(████▌███████████▓██▓▓▓█▓▒▓██▓▓▓▓██▓
▒.             ▒█▓▓▓▒▒▒▓▓▓▓▓▓▓▓▓▓███████▓╢∩((▀████▒║└`         »▓██████████████▓▓███▓▓▓▓▓▓▓▓▓██▓▓▓█▓
∩             (▒▓▓▓▓▓▒▒║▒▒█▓█▓▓▓▓▓▓▓██████▒▒▒╔y╠▒║Ñ∩┌┌:;:(  :`(⌠╠▀███████▓▓▓▒▒▒▓▓████▓▒▓▓▓█▓▓███▓▓▓█
              (╢▒▒▓▓▓▓▒▒╢▒▒▓▒▓▓▓▓▓▓████▓███▓▓▒▓╢▒▒M╔/,       .(╔▒▓████████▓▒▒▒▓▓█▓███▓▓▓▓▓▓▓▓▓▓███▓▓
           ╓»∩(╢▒▒▓▓▓▓▓▒▒▒╢╢▒▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▓▓▓▒▀▓║▒║░U│/y╔#▒▒▓████████▓▓▒▒▒▓▓███████▓█▓▓▓▓▓▓▓████▓
▓▒.      ▄▀⌐`  ╠▒▒▓▓▓▓▓▒▒▒║╢╢╢║▒▒▒▒▒▒▒╢╢║╠╠║║╢║╢▒▒▒▒║╢║Ñ░░║╢▒▒║▒▓██████▓▒▒▒▒▓██████████▓▓▓▓▓▓▓▓████▓
▓██µ.╓▄Ñ█▌∩  ┌╡Ñ▒▓▓▓▓▓▒▒▒╢╢║╠Ñ╙╚╚╚╚Ñ╠║╠╠╠╠║╢▒▒▒╢╢▒▒╠╠░░#║▓▓▒░Ñ╠║▒▓▀▀▀▀▒▒▒▒▒▓███████████▓▓▓▓▓▓▓█████▓
╜╜╜╜▀╜╙ └▀  êÑ┘└╙╜╜╜╜╜╜╙╙┴┘└└└*"`"ººº└└└└└┴╙┘┘┴┴╙╜╜╙┴┘┴╙╙╜╜└└└└ºº└└└└┘╙┴┴╜▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
"""
marvinu_image = "( ͡° ͜ʖ ͡°)"

# Functions

def redraw_marvinu(redraw_marvinu_message = ""):
    """Function to draw Marv-inu and let him speak"""
    print(chr(27) + "[2J" + chr(27) + "[;H")
    print(marvinu_image)
    if redraw_marvinu_message:
        print("Marv-inu says:\n ", redraw_marvinu_message)

def show_menu():
    """Function to show the menu"""
    print("1) Present yourself to Marv-inu!     (a1) Check chars in string!")
    print("2) Convert temperatures!             (a2) Double number to get all digits!")
    print("3) Multiply words!                   (a3) Replace tabs with spaces!")
    print("4) Calculate sum and average!        (a4) Combine names!")
    print("5) Stretch your words out!           (a5) Count points from a string!")
    print("6) Check isograms!                   (a6) Think of a number!")
    print("7) Compare numbers!                  (b1) Grade your points!")
    print("8) Randomize a string!               (b2) Check 4 strings!")
    print("9) Create an acronym!                (e1) Sort countries by emissions!")
    print("10) Mask a string!                   (e2) Check emissions per capita!")
    print("11) Find all indexes!                (e3) Check emissions per area!")
    print("12) Search for countries!            (q) Quit.")
    print("13) Compare yers of emission!")
    print("14) Present country emission data!")


def get_user_input(marvinu_input_request, marvinu_input_error_message, input_type):
    """Function to make Marv-inu ask for user input and validate it."""

    marvinu_input_messsage = marvinu_input_request
    user_input = ""
    output = ""

    while output == "" and user_input != "done":
        redraw_marvinu(marvinu_input_messsage)
        marvinu_input_messsage = marvinu_input_error_message
        user_input = input("\n--> ")

        if input_type == "string": # If Marv-inu wants a string
            if user_input:
                return user_input

        elif isinstance(input_type, tuple) and input_type[0] == "comma_separated_string": # Or a comma separated string
            if len(user_input.split(",")) == input_type[1]: # Check if it has the specified number of arguments
                return user_input

        elif input_type == "y/n": # If Marv-inu wants a yes or no answer
            if user_input in ["y", "n"]:
                return user_input

        elif input_type in ["number", "int", "posint"]: # If Marv-inu wants a numeric value
            try:
                output = float(user_input)
                if input_type == "number":
                    return output
            except ValueError:  # If it is not a numeric value:
                if user_input == "done":
                    output = ""
                continue

            # Define booleans to decide what to do next
            user_input_is_int = int(user_input) == float(user_input)
            user_input_is_positive = int(user_input) > 0

            if user_input_is_int and (input_type == "int") or (input_type == "posint" and user_input_is_positive):
                return output

        elif input_type == "upper_lower":
            has_upper = False
            has_lower = False

            for char in user_input:
                if char.isupper():
                    has_upper = True
                if char.islower():
                    has_lower = True
            if has_upper and has_lower:
                return user_input

        output = ""

def press_enter():
    """Function to pause and ask the user to press enter"""
    return input("\nPress enter to continue...")

def multiply_str(input_string, factor):
    """Function to multiply a string"""
    return input_string * factor

# Menyval

def quit_marvinu():
    """Function to terminate Marvinu"""
    redraw_marvinu("OK bye! See ya later!! \n")
    return False

def greet():
    """Menu choice 1: Greet the user by name"""
    name = get_user_input("What's your name?", "Tell me your name please!", "string")
    marvinu_message = f"Hello {name}! Nice to meet you! \n"
    redraw_marvinu(marvinu_message)

def celcius_to_farenheit():
    """Menu choice 2: Convert Celsius to Farhenheit"""
    marvinu_request = "Tell me the temperature in °C and I'll convert it to Farhenheit for you!"
    marvinu_error_message = "Only numbers please! Tell me the temperature in °C"
    temp_c = get_user_input(marvinu_request, marvinu_error_message, "number")
    if temp_c is not None:
        temp_f = round(temp_c * 9/5 + 32,2)
        marvinu_message = f"{temp_c}°C is {temp_f}°F!"
        if temp_c < -273.15:
            marvinu_message += " That's too cold!"
        redraw_marvinu(marvinu_message)

def word_manipulation():
    """Menu choice 3: Repeat a word"""
    word = ""
    marvinu_message = "What word do you want me to repeat for you?"
    while not word:
        redraw_marvinu(marvinu_message)
        word = input("\n--> ")
        if not word:
            marvinu_message = "Give me a word to repeat please!"

    marvinu_message = "How many times do you want me to repeat it?"
    repetitions = 0

    while repetitions < 1:
        redraw_marvinu(marvinu_message)
        try:
            repetitions = int(input("\n--> "))
        except ValueError:
            marvinu_message = "Only integers please! How many times do you want me to repeat the word?"
            continue

        if repetitions < 1:
            marvinu_message = "I can't do that! How many times do you want me to repeat the word? Give me a number!"
            continue

    repeated_string = multiply_str(word, repetitions)
    redraw_marvinu(repeated_string)

def sum_and_average():
    """Menu choice 4: Calculate sum and average of numbers"""
    total_sum = 0
    counter = 0
    ask_more_numbers = True
    marvinu_message = "Give me a number!"
    marvinu_error_message = "Only numbers please! Give me a number!"

    while ask_more_numbers:

        number = get_user_input(marvinu_message, marvinu_error_message, "number")
        if number is None:
            ask_more_numbers = False
        else:
            total_sum += number
            counter += 1

            marvinu_message = f"You have given me {counter} number"
            if counter > 1: # Add plural s if more than 1 number given
                marvinu_message += "s"
            marvinu_message += "! Give me another number, or write \"done\" if you're done!"

    if counter:
        average = round(total_sum/counter, 2)

        marvinu_message = f"The sum of all numbers are {total_sum} and the average is {average}"
        redraw_marvinu(marvinu_message)

def hyphen_string():
    """Menu choice 5: Stretch a word out with hyphens"""
    word_to_stretch = ""
    marvinu_request = "Tell me a word and I'll stretch it out in a weirdly specific way!"
    marvinu_error_message = "Tell me a word to stretch please!"
    word_to_stretch = get_user_input(marvinu_request, marvinu_error_message, "string")
    counter = 0
    stretched_word = ""
    for letter in word_to_stretch:
        counter += 1
        if counter > 1:
            stretched_word += "-"
        stretched_word += letter * counter
    redraw_marvinu(stretched_word)

def is_isogram():
    """Menu choice 6: check if a word is an isogram"""
    marvinu_request = "Give me a word and I'll check if it's an isogram!"
    marvinu_error_message = "Give me a word please!"
    potential_isogram = get_user_input(marvinu_request, marvinu_error_message, "string")
    repetition_counter = len(potential_isogram) # Count the letters in the word
    for letter in potential_isogram:
        repetition_counter -= potential_isogram.count(letter) # Subtract the number of letters including repetitions

    if repetition_counter: # If number of letters differs from number of letters including repetitions
        marvinu_message = "No match!" + potential_isogram + " is not an isogram!"
    else:
        marvinu_message = "Match!" + potential_isogram + " is an isogram!"

    redraw_marvinu(marvinu_message)

def compare_numbers():
    """Menu choice 7: Check if the last number is smaller, bigger or the same as the last"""
    current_number = get_user_input("Give me a number!", "I said give me a number!", "number")
    marvinu_error_message = "That's not a number! Give me a number please!"
    result = ""
    while current_number:
        previous_number = current_number
        marvinu_request = "Give me another number! Or type \"done\" when you're done."
        current_number = get_user_input(result + marvinu_request, marvinu_error_message, "number")
        if current_number is not None:
            if current_number == previous_number:
                result = "That's the same! The same as the last one! \n "
            elif current_number < previous_number:
                result = f"That's smaller! {current_number} is smaller than {previous_number}! \n "
            if current_number > previous_number:
                result = f"That's larger! {current_number} is larger than {previous_number}! \n "

def check_chars():
    """Menu choice a1: Check if a string is present in another string"""
    marvinu_request = "Give me a string of text!"
    marvinu_error_message = "Write some text please!"
    string_1 = get_user_input(marvinu_request, marvinu_error_message, "string")
    marvinu_request = "Give me another string and I'll check if all its characters are also in the first one!"
    string_2 = get_user_input(marvinu_request, marvinu_error_message, "string")

    for char in string_2:
        if string_2.count(char) > string_1.count(char):
            marvinu_message = f"No match! Not every character in {string_2} is also in {string_1}!"
            break
        else:
            marvinu_message = f"Match! Every character in {string_2} is also in {string_1}!"

    redraw_marvinu(marvinu_message)

def double_number():
    """Menu choice a2: Check how many times to double a number to get a number with all the digits"""
    counter = -1
    number = ""
    max_times = ""

    try:
        marvinu_request = "Give me a number! \n"
        marvinu_request += "  I'll tell you how many times to double it to get a number with all the digits!"
        marvinu_error_message = "Give me a positive integer please!"
        number = int(get_user_input(marvinu_request, marvinu_error_message, "int"))

        marvinu_request = "What's the maximum number of times I should try doubling the number?"
        marvinu_error_message = "Give me a positive integer please! How many times?"
        max_times = int(get_user_input(marvinu_request, marvinu_error_message, "posint"))
    except TypeError:
        pass
    if number != "" and max_times != "":
        all_digits = {}
        result = ""

        while counter < max_times and sum(all_digits.values()) < 10:
            counter += 1
            result = number * 2 ** counter
            for i in range(10):
                all_digits[i] = str(i) in str(result)
            # print(f"{number}*2^{counter} = {result} ({sum(all_digits.values())} digits)")

        if sum(all_digits.values()) == 10:
            answer = counter
        else:
            answer = -1
        marvinu_message = f"Answer: {answer} times ({number}*2^{counter} = {result})"
        redraw_marvinu(marvinu_message)

def replace_tabs():
    """Menu choice a3: Replace tabs with triple spaces"""
    marvinu_request = "Give me some text with tabs in it and I'll replace them with triple spaces!"
    marvinu_error_message = "Type some text with tabs in it please!"
    input_string = ""
    # while "\t" not in input_string:
    input_string = get_user_input(marvinu_request, marvinu_error_message,"string")
    result = input_string.replace("\t", "   ")
    redraw_marvinu(result)

def combine_names():
    """Menu choice a4: Combine two names"""
    marvinu_request = "Tell me someone's name!"
    marvinu_error_message = "Type a name please!"
    name_1 = get_user_input(marvinu_request, marvinu_error_message,"string")
    marvinu_request = "Tell me another name and I'll combine it with the first one!"
    name_2 = get_user_input(marvinu_request, marvinu_error_message,"string")

    vowels = "aouåeiyäö"
    vowels += "ãõőüűëïÿ"
    vowels += "àáâãèéêìíòóôõùúýỳỹỷỵựửữừứưụủũợởỡờớơộổỗồốọỏịỉĩệểễềếẹẻẽặẳẵằắăậẩẫầấạả"

    result = ""
    letter_index = 0
    while  letter_index < len(name_1) and name_1[letter_index].lower() not in vowels:
        print("LETTER INDEX:", letter_index, "LETTER:", name_1[letter_index])
        result += name_1[letter_index]
        letter_index += 1

    letter_index = 0
    first_vowel_reached = False
    for letter in name_2:
        if letter.lower() in vowels:
            first_vowel_reached = True
        if first_vowel_reached:
            result += letter

    if not result:
        result = "Yeah.. that didn't work. Try different names next time!"
    redraw_marvinu(result)

def count_points():
    """Menu choice a5: Calculate points from a string in a specific way"""
    marvinu_request = "Type a string of alternating letters and numbers, starting with a letter!"
    marvinu_error_message = "Type a string of letters and numbers please!"
    input_string = get_user_input(marvinu_request, marvinu_error_message,"string")

    char_index = 0
    players = {}

    for char in input_string:
        char_index += 1
        if char.isalpha() and char_index < len(input_string) and input_string[char_index].isnumeric():
            current_number = int(input_string[char_index])
            if char.upper() == char:
                current_number *= -1
            try:
                players[char.lower()] += int(current_number)
            except KeyError:
                players[char.lower()] = int(current_number)

    result =""
    counter = 0
    for player in players.items():
        if counter:
            result += ", "
        counter += 1
        result += f"{player[0]} {player[1]}"
    if not result:
        result = "OK, never mind then!"
    redraw_marvinu(result)

def think_of_a_number():
    """Menu choice a6: Marv-inu will figure out what number the user is thinking of"""
    lowest_number = 1
    highest_number = 1000
    ask_number = 0
    counter = 0

    marvinu_message = "Think of a whole number between 1 and 1000. \n "
    marvinu_message += " I will figure it out by asking 10 yes/no questions!\n"

    redraw_marvinu(marvinu_message)
    press_enter()
    while highest_number != lowest_number:
        higher = ""
        counter += 1
        span = highest_number - lowest_number
        ask_number = int(lowest_number + span/2)
        marvinu_request = f"({counter}) Is your number bigger than {ask_number}? (y/n)"
        marvinu_error_message = f"Only answer \"y\" or \"n\" please! \n Is your number bigger than {ask_number}? "
        higher = get_user_input(marvinu_request, marvinu_error_message, "y/n")
        if higher == "y":
            lowest_number = ask_number + 1
        elif higher == "n":
            highest_number = ask_number

    marvinu_message=f"Your number is {lowest_number}!"
    redraw_marvinu(marvinu_message)

def randomize_string(input_string):
    """Menu choice 8: Randomize a string"""
    input_array = []
    input_array[0:] = input_string
    marvinu_message = input_string + " --> "
    while len(input_array) > 0:
        random_number = random.randrange(0, len(input_array))
        marvinu_message += input_array.pop(random_number)
    return marvinu_message

def get_acronym(input_string):
    """Menu choice 9: Create an acronym from all the upper case letters in a string"""
    marvinu_message = ""
    for char in input_string:
        if char.isupper():
            marvinu_message += char
    return marvinu_message

def mask_string(input_string):
    """Menu choice 10: Replace all the letters in a string with # except the last 4"""
    last_4 = input_string[-4:]
    chars_to_mask = len(input_string)-4
    marvinu_message = multiply_str("#", chars_to_mask) + last_4
    return marvinu_message

def find_all_indexes(input_string, input_chars):
    """Menu choice 11: Find all the index places of a string in another string"""
    start = 0
    end = len(input_string)
    index_list = []

    if input_chars in input_string:

        while start < end:
            try:
                index_found = input_string.index(input_chars, start)
                index_list.append(str(index_found))
                start = index_found + 1
            except ValueError:
                start = end
    if len(index_list) > 0:
        marvinu_message = ",".join(index_list)
    else:
        marvinu_message = ""

    return marvinu_message

def points_to_grade(input_max, input_score):
    """Menu choice b1: Grade points with A-F grades"""
    marvinu_message = "score: "
    percent_score = float(input_score) / float(input_max) * 100

    if percent_score >= 90:
        marvinu_message += "A"
    elif percent_score >= 80:
        marvinu_message += "B"
    elif percent_score >= 70:
        marvinu_message += "C"
    elif percent_score >= 60:
        marvinu_message += "D"
    else:
        marvinu_message += "F"

    return marvinu_message

def has_strings(input_string_1, input_string_2, input_string_3, input_string_4):
    """Menu choice b2: Check if a string contains 3 other strings in specific places"""
    print(input_string_1, input_string_2, input_string_3, input_string_4)
    counter = 0
    if input_string_1.startswith(input_string_2):
        counter += 1
        print("starts")
    if input_string_3 in input_string_1:
        counter += 1
    if input_string_1.endswith(input_string_4):
        counter += 1
        print("ends")

    if counter == 3:
        marvinu_message = f"Match! {input_string_1} \
        starts with {input_string_2}, \
        contains {input_string_3} \
        and ends with {input_string_4}!"
    else:
        marvinu_message = "No match"

    return marvinu_message
