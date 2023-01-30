"""
Marvin with a simple menu to start up with.
Marvin doesnt do anything, just presents a menu with some choices.
You should add functinoality to Marvin.
"""
import random


def greet():
    """
    greeting function.
    """
    name = input("What is your name? ")
    print("\nMaro says:\n")
    print("Hello %s - your awesomeness!" % name)
    print("What can I do you for?!")

def celcius_to_farenheit():
    """
    Celcius to farenheit function.
    """
    far = float(input("Temperature in Celsius:")) * 9 / 5 + 32
    print("Temperature in Fahrenheit:" + str(round(far, 2)))

def word_manipulation():
    """
    word manipulation function.
    """
    word = str(input("Enter a word:"))
    mul = int(input("Enter a number:"))
    print(word * mul)

def sum_and_average():
    """
    sum_and_average function.
    """
    num_cal=0
    num_av=0
    while True:
        in_text=input("Enter numbers to calculate or write (done) to finish:")
        if in_text.isalpha():
            if in_text in ("done", "Done"):
                new_av = round(float(num_cal / num_av),2)
                print(f"The sum of all numbers are {round(float(num_cal),2)} and the average is {new_av}")
                break
            else:
                print("write a number or (done) only")
        else:
            num_cal = num_cal + float(in_text)
            num_av += 1

def hyphen_string():
    """
    hyphen_string function.
    """
    letters = ""
    i =1
    word =str(input("Enter a word:"))
    for letter in word:
        new_num = letter * i
        letters = letters + f"-{new_num}"
        i += 1
        print(letters[1:])

def is_isogram():
    """
    is_isogram function.
    """
    string = str(input("Enter a word: "))
    test_boal=True
    for char in string:
        if string.count(char) > 1:
            test_boal = False
    if test_boal:
        print("Match!")
    else:
        print("No match!")  

def compare_numbers():
    """
    compare_numbers function.
    """
    num = ""
    while True:
        try:
            text = input("Enter numbers or (done) to quit: ")
            if num == "":
                num = float(text)
            else:
                if float(text) < float(num):
                    print("smaller!")
                    num = float(text)
                elif float(text) > float(num):
                    print("larger!")
                    num = float(text)
                elif float(text) == (num):
                    print("same!")
                    num = float(text)
        except Exception:
            if text in ("done", "Done"):
                break
            else:
                print("not a number!")
        
def randomize_string(textW):
    """
    randomly_reversed function.
    """ 
    rand = random.sample(textW, len(textW))
    randText = "".join(rand)
    return textW + " --> " + randText
    

def get_acronym(acrText):
    """
    get_acronym function.
    """
    arc = ""
    for letter in acrText:
        if letter.isupper():
            arc = arc + letter
    return arc
def mask_string(unmasked):
    """
    mask_string function.
    """
    lastFour=unmasked[-4:]
    counter = 0   
    count = 0 
    TextH="#"
    for _ in unmasked:
        counter += 1
    if counter >= 4:
        count= counter - 4
        return multiply_str(count,TextH) + f"{lastFour}"
    return multiply_str(TextH,counter)
       
def multiply_str(word,t):
    """
    multiply hash function.
    """
    return word*t

def find_all_indexes(stre, strTwo):
    """
    find_all_indexes function.
    """
    try:
        indexco=""   
        i = 0
        for _ in stre:
            indexco =indexco +"," +str(stre.index(str(strTwo),i,len(stre)))
            i = int(stre.index(str(strTwo),i,len(stre))) + 1
        return indexco[1:]
    except ValueError:
        return indexco[1:]
   
