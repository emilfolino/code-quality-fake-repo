"""
This file contains all functions that are called in the options in main.py.
"""

import random


def greet():
    """
    Asks the user to enter a name, then greets the user with 'Good day' and then the inputted name.
    """
    name = input("What is your name? ")
    print("\nHomer says:\n")
    print("Good day " + name + "!")
    print("What can I do for you?!")


def celcius_to_farenheit():
    """
    Asks the user to enter a temperature in Celsius, then calculates the corresponding temperature in Fahrenheit,
    then prints it.
    """
    temp = input("Enter your temperature please. ")
    temp = str(round((float(temp) * 1.8 + 32), 2))
    print("Okay, I am calculating your temperature to the imperial system.")
    print("Your temperature is " + temp + " Fahrenheit.")


def word_manipulation():
    """
    Concatenates the string the user entered with itself as many times as the number the user entered.
    """
    utskrift = ""
    ordet = input("Tell me a word. ")
    numret = input("Now tell me a number. ")
    utskrift = multiply_str(ordet, numret)
    print("Im gonna say your word as many times as you told me to now")
    print(utskrift)


def sum_and_average():
    """
    Calculates the sum and the average of the numbers the user has entered before they have written "done".
    If something thats not number is entered, it program asks for a new number.
    """
    summa = 0
    average = 0
    antaltal = 0
    choice4 = ""
    while choice4 != "done":
        choice4 = input("Tell me a number, or type done when you're done. ")
        if choice4 == "done":
            break
        else:
            try:
                float(choice4)
            except (ValueError, NameError):
                print("That is not a number. Try again.")
                continue
        summa = summa + float(choice4)
        antaltal = antaltal + 1
    average = str(round((summa/(antaltal)), 2))
    print("The sum of your numbers is " + str(round(summa, 2)) + " and the average is " + average + ".")


def hyphen_string():
    """
    Concatenates a new string that contains every character repeated as many times as it's index number (plus one).
    Also adds a '-' in between every new character from the original string.
    Doesn't work with the '%' symbol as it is used to stop the loop. Removes the last '-' at the end.
    """
    mening = ""
    antal = 0
    sentence = input("Type a sentence or whatever you feel like: ") + "½"
    for letters in sentence:
        antal += 1
        if letters != "½":
            for _ in range(antal):
                mening = mening + letters
            mening = mening + "-"
    mening = mening.rstrip("-")
    print(mening)


def is_isogram():
    """
    This function turns tells the user if the word they entered is an isogram.
    It does it by giving every letter from the inputted
    string an index number, and checks if a character is the same as another character,
    while the index number of the character isn't
    the same as the other, confirming it is a new letter, and not the same (but the same letter/character).
    """
    testordet = input("Tell me a word that you want me to check: ")
    talnummer1 = 0
    talnummer2 = 0
    isogram = 0
    for letters1 in testordet:
        talnummer1 += 1
        talnummer2 = 0
        for letters2 in testordet:
            talnummer2 += 1
            if letters1 == letters2 and talnummer1 != talnummer2:
                isogram += 1
    if isogram == 0:
        print("Match!")
    else:
        print("No match!")


def compare_numbers():
    """
    This function compares tells the user to enter two numbers, and then compares them,
    and prints if it's smaller, the same,
    or bigger. After the two first it asks the user to enter a new one to compare forever,
    until the user types 'done' which closes the function.
    """
    while True:
        try:
            gamla = float(input("Give me the first number: "))
            break
        except ValueError:
            print("not a number!")
    nya = 0
    while nya != "done":
        try:
            nya = input("Now give me a second number, or type 'done' to leave: ")
            if nya == "done":
                break
            nya = float(nya)
            break
        except ValueError:
            print("not a number!")
    while nya != "done":
        if nya > gamla:
            print("larger!")
        elif nya == gamla:
            print("same!")
        elif nya < (gamla):
            print("smaller!")
        gamla = float(nya)
        while2loop = True
        while while2loop and nya != "done":
            nya = input("Enter a new number to compare, or type 'done' to leave: ")
            try:
                if nya == "done":
                    break
                nya = float(nya)
                while2loop = False
            except ValueError:
                print("not a number!")
            

def randomize_string(original_string):
    """
    Shuffles the order of the input string characters by turning the entered string into a list,
    and then removes a random character per iteration of the for-loop, that lasts as long as the length of the string.
    Then adds the removed character to a new variable. When the for loop is over the returned variable contains all the
    original character in a new order.
    """
    originalordet = original_string
    original_string = list(original_string)
    randomized_string = ""
    for _ in range(0, len(original_string)):
        randomized_string += original_string.pop(random.randint(0, len(original_string)-1))
    returnering = originalordet + " --> " + randomized_string
    return returnering


def get_acronym(strängen):
    """
    The function checks if a character in the string is uppercase, which if is true,
    then adds the character into a new string.
    Does this for the entire length of the original string, which gives us an acronym of all the uppercase characters
    from the original string.
    """
    acronym = ""
    for i in strängen:
        if i.isupper() is True:
            acronym += i
    return acronym


def multiply_str(stri, inte):
    """
    Takes two variables, the first one is a string, the second a number.
    The function then concatenates the entered string as many times as
    the number says, with itself.
    """
    n_stri = ""
    for _ in range(int(inte)):
        n_stri = n_stri + str(stri)
    return n_stri

def mask_string(inputt):
    """
    Creates a new string with as many '#'s as the original string has characters minus four.
    Then concatenates the last four characters to it,
    creating the illusion that it has masked all except the last four.
    """
    outputt = multiply_str("#", (len(inputt) - 4))
    outputt = outputt + inputt[(len(inputt)-4):]
    return outputt

        
def find_all_indexes(tolv, arg12):
    """
    Returns a concatenated string of all index positions where the second entered string appears in the first string.
    It does this by running a while-loop that pushes the starting search-point of the index() function
    ahead in the first entered string, so it doesn't tell us the same index position twice.
    For every iteration of the loop, it adds a ',', after every index-number.
    If no more indexes are found, index() gives us a ValueError, that closes the while-loop.
    It then removes the last ',' so the last character is an index number.
    Then returns the full concatenated string.
    """
    start = 0
    bryten = 1
    all_indexes = ""
    while bryten:
        try:
            starttal = tolv.index(arg12, start)
            all_indexes = all_indexes + str(tolv.index(arg12, start)) + ","
            start = tolv.index(arg12, (starttal + 1))
        except ValueError:
            bryten = 0
    return all_indexes.rstrip(",")
