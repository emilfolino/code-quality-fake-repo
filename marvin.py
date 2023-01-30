"""
high level support for doing this and that.
"""

from random import randint

def greet():
    """ -- """
    name = input("Tell me your Name! ")
    print("\nDroid says:\n")
    print("Welcome %s " % name)
    print("how can i help you today")

def celcius_to_farenheit():
    """ -- """
    TinC = input("What is the temperature in Celcius: ")
    print(TinC, '°C is equivalent to ', round((float(TinC)* 9 / 5 + 32), 2), '°F')

def word_manipulation():
    """ -- """
    word = input("What is the word you want to repeat: ")
    times = int(input("how meny times you want to repeat it: "))  
    print(multiply_str(word, times))

        

def sum_and_average():
    """ -- """
    value = ""
    numList = []

    while value != "done":
        value = input("add numbers and then type done: ")
        try: 
            n = float(value)
        except ValueError:
            value = "done"

        if value != "done":
            numList.append(n)
            print(numList)
            sumNum = sum(numList)
            medNum = sumNum / len(numList)
                
        elif value == "done":
            print(round(sumNum, 2))
            print(round(medNum, 2))
            break
        

def hyphen_string():
    """ -- """
    word = input("Enter a word: ")
    word_f = ""
    for index, i in enumerate(word):
        word_f += i * (index + 1) + "-"
    print(word_f[:-1])

def is_isogram():
    """ -- """
    wordIn = input("Enter a word to check isogram: ")
    setchar = set()
    iso = True
    for i, c in enumerate(wordIn):
        setchar.add(c)
        if(len(setchar) < i+1):
            print("No match!")
            iso = False 
            break
    if(iso):
        print("Match!")

       
      


def compare_numbers():
    """ -- """
    completed = True
    user_input1 = input("enter the first number: ")

    try:
        num1 = int(user_input1)
        it_is = True
    except ValueError:
        it_is = False

    if it_is is True:
        while completed is True:
            user_input2 = input("enter another value: ")
            try:
                num2 = int(user_input2)
                it_is = True
            except ValueError:
                it_is = False
                num2 = user_input2
            if num2 == "done":
                break
            elif it_is is False:
                print("not a number!")      
            elif num1 < num2:
                print("larger!")
                num1 = num2        
            elif num1 > num2:
                print("smaller!")
                num1 = num2        
            elif num1 == num2:
                print("same!")
                num1 = num2
            elif user_input2 == "done":
                break
def randomize_string(word):
    """ -- """
    length = len(word)
    lis = list(word)
    for i in range(0, length-1):
        ran = randint(i+1, length-1)
        lis[ran], lis[i] = lis[i], lis[ran]

        x = ""
        for t in range(length):
            x = x + lis[t]
    return "{} --> {}".format(word, x)

def get_acronym(sent):
    """ -- """
    acronym = ''.join([c for c in sent if c.isupper()])
    return acronym

def multiply_str(p1, times):
    """ -- """
    return p1 * times

def multiply_word():
    """ -- """
    word = input("What is the word you want to repeat: ")
    times = int(input("how meny times you want to repeat it: "))  
    return multiply_str(word, times)

def mask_string(string):
    """ -- """
    fString = string[:-4]
    lString = string[-4:]
    masked = multiply_str("#", len(fString))
    return masked + lString

def find_all_indexes(string, char):
    """ -- """
    result = []
    offset = -1
    while True:
        try:
            offset = string.index(char, offset+1)
        except ValueError:
            return "".join(str(result)[1:-1]).replace(" ", "")
        result.append(offset)
        