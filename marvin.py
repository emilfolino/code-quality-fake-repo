"""
Functions for marvin.
"""
import random

def greet():

    """
    This function is used to greeting.
    """
    name = input("What is your name? ")
    print("\nMarvin says:\n")
    print("Hello %s - your awesomeness!" % name)
    print("What can I do you for?!")

def celcius_to_farenheit():

    """
    This functions is used to convert from C to F.
    """

    temp_c = float(input("Enter the temp in C: "))
    temp_f = float(temp_c * (9/5) + 32)
    print(round(temp_f,2))
    

def multiply_str(string,factor):
    """
    Multiply function is a function that multiply the string by a factor.
    """
    repetition = string * factor
    return repetition


def word_manipulation(): 
    """
   Word manipulation is functions that repeats a string.
    """
    string= input("Enter a word: ")
    factor = int(input("Enter the number of times you want your word multiplied by: "))
    print(multiply_str(string,factor))


def sum_and_average():
    """
    Sum and average is a functions that print sum and average and brakes when the users enter done.
    """
    count = 0
    num = 0
    sum_numbers = 0
    arithmetic_average = 0
    while True:
        try:
            num = float(input("Enter the numbers to get the sum and average. OBS: Enter (done) to end: "))
            count +=1
            sum_numbers = sum_numbers + num
            arithmetic_average = sum_numbers/count
            sum_numbers = round(sum_numbers,2)
            arithmetic_average = round(arithmetic_average,2)

        except ValueError:
            print("The sum of all numbers is ",sum_numbers," and the average is ",arithmetic_average)
            break


def hyphen_string():
    """
    Hyphen is a functions that takes string and repeats the characters of it.
    """
    word = input("Enter a word: ")
    count = 0
    new_string = ""
    for i in word:
        count +=1  
        new_string += i * count + "-"
        print(f"'{new_string[0:-1]}'")

def is_isogram():
    """
    Is_isogram is a functions that checks wheres if any repeated character in the given word.
    """
    word = input("PLese enter a word to check if it an isogram word: ")
    new_word = ""
    s = ""
    count = 0
    for i in word:
        new_word = s
        count += 1
        s += i
        if i in new_word:
            if count == len(word):
                print("No match!")
                break
            elif i in new_word:
                print("No match!")
            break

        elif i not in new_word and count == len(word):


            print("Match!")



def compare_numbers():
    """
    Compare function is a functions that compars tow numbers entered by user.
    """
    while True:
    
        try:
            num1 = int(input("Enter the first number: "))
            break

        except ValueError:
            print("not a number!")

    while True:

        try:

            current = input("Enter the second number, or done to get out: ")
            current = int(current)
            if current > num1 :
                print("larger!")
            elif current < num1:
                print("smaller!")
            elif current == num1:
                print("same!")

            num1 = current
        except ValueError:

            if current != "done":
                print("not a number!")
            elif current == "done":
                break



def randomize_string(word):
    """
    Randomize_string is a fiction that shuffles the characters of a given word. 
    """

    new_word = ""
    original_word = word
    for random_ch in (word):
        random_ch = random.choice(word)
        new_word += random_ch
        word = word.replace(random_ch,"",1)
        final_output = (f"{original_word} --> {new_word}")
    return final_output


def get_acronym(word):
    """
    Get acronym is a function that prints the upper letter and puts then in a string.    
    """

    shortcut = ""
    for i in word:
        if i.isupper():
            shortcut += i
    return shortcut


def mask_string(number):
    """
    Mask string is a function that replace all characters except tha last 3 digits with "#".
    """
    first_part = ""
    second_part = ""
    for i,word in enumerate(number):
        if i <= (len(number)-5):
            first_part= multiply_str(string="#",factor=len(number)-4)

        elif i > (len(number)-5):
            second_part += str(word)
    final_output = (first_part+second_part)
    return final_output

def find_all_indexes(word,ch):
    """
    I assume that the name of this function explains its self.
    """

    count = 0
    indexes = ""
    z = 0
    l =""
    if ch not in word:
        all_indexes = ("")
        return all_indexes
    try:
        while count <= len(word):


            z = word.index(ch, count, len(word))
            count += 1

            if count <= z:
                continue
            indexes += str(z) + ","
            l= indexes
    except ValueError:
        count += 1

    all_indexes = (l[:-1])
    return all_indexes
