"""
Functions For Main.py
"""

import random


def greet():
    """
    Funktion to Print Out Variable - "Name"
    And A Text
    """
    PersonName = input("What is your name Plaaayaaah: ")
    return print(PersonName +  " Realllly?!!! " + PersonName + " That's a fucking ugly name my dude")
    

def celcius_to_farenheit():
    """
    Function To Convert An Float Input
    Into Fehreinheil
    """
    
    Temprature = float(input("Hey Suckahfool, Provide me with Celicus: "))
    Fahrenheit = float((Temprature * 9) / 5 + 32)
    RoundUp = round(Fahrenheit,2)
    return print(f"{Temprature} Celcius ISZZZZZZZSSZZ {RoundUp} Fahrenheit you foooool!")
    
    
def word_manipulation():
    """
    Function To MultiPly A Word
    """
    
    WordChoice = input("What is the word you're thinking of you fool?: ")
    SpamTime = int(input("Ok Ok Ok  How many times would you like me to say that..... bitch: "))
    return print(multiply_str(WordChoice, SpamTime))
    
def sum_and_average():
    """
    Function to Calculate Average
    
    """
    
    Totalt = 0
    Antal = 0
    while True:
        Counter = input("Skriv Ett Hel Tal Eller Done: ")
        if (Counter == "done"):
            break
        Totalt += float(Counter)
        Antal += 1
    Average = round((Totalt/Antal), 2)
    print(f"The sum of all numbers are {Totalt} and the average is {Average},")
    
def hyphen_string():
    """
    Function To Print An String In a Funny Way
    """
    
    Word = input("Give me a Word and ill make a magic trick")
    Multi = 1
    Guess = ""
    for Char in Word:
        if len(Word) > Multi:
            Guess += Char * Multi + "-"
            Multi += 1
        else:
            Guess += Char * Multi
    print(f"Check This Trick {Guess}")
    

def is_isogram():
    """
    Function To Test If A Word Is an Isogram
    """
    Word = input("Write a Word: ")
    Isogram = bool
    for Char in Word:
        if Word.count(Char) > 1:
            Isogram = False
            break               
        else:
            Isogram = True
            
    if Isogram is True:
        print("Match!")
    else:
        print("No match!")
        
def compare_numbers():
    """
    Function To Compare Previous To Entered Int
    """
    
    Previous = int(input("Provie a number: "))
    Current = ""
    
    while True:
        
        Current = input(f"Your Previous is: {Previous}, Give me another one to compare: ")
        if Current == 'done':
            break
        else:
            try:
                Current = int(Current)
                if Current > Previous:
                    print("larger!")
                elif Current < Previous:
                    print("smaller!")
                else:
                    print("same!")
                Previous = (Current)
            except ValueError:
                print("not a number!")


def randomize_string(RandomString):
    """
    A Function That Takes An String
    And Shuffles The Word
    """
    Listan = []
    for letter in RandomString:
        Listan.append(letter)
    random.shuffle(Listan)
    
    return RandomString + " --> " + "".join(Listan)


def get_acronym(Namn):
    """
    Function To Print Out
    All Upper Characters In 
    A Text
    """
    
    Text = ""
    for Char in Namn:
        if Char.isupper() is True:
            Text += Char
    return str(Text)
            
            
            
def mask_string(String):
    """
    Function To Mask All Input Expect
    The Last 4
    """
    return multiply_str("#" , len(String) - 4) + String[len(String) -4 : None]


def multiply_str(a, b):
    """
    A Function To Multyply A Word Into
    Many Words
    """
    
    String = a * int(b)
    return String

def find_all_indexes(Texten, Ordet):
    """
    Find Indexes In A String
    """
    Save = []
    Start = 0
    Stop = (Texten.count(Ordet))
    Answer = ""

    for i in range(Start, Stop):
        if i != Stop:
            try:
                Result = Texten.index(Ordet, Start)
                Save.append((Result))
                Start = 1 + Result

            except ValueError:
                print("")
                break

    for char in Save:
        Answer += (str(char) + ",")
    Answer = Answer[:-1]

    return (Answer)
     