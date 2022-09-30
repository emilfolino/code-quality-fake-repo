"""
Functions page
"""
import random

def greet():
    """
    Menu choice 1
    """
    name = input("What is your name? ")
    print(f"Hello Devin my name is {name}")
    print("\nDevin says:\n")
    print(f"Hello {name}! Are you perhaps an adventurer")
    print("What may I assist you with?!")

def celcius_to_farenheit():
    """
    Menu choice 2
    """
    cel = float(input("Please tell me the great Devin the temperature you wish to convert in to the... "))
    fah = round(cel * 9 / 5 + 32, 2)
    print(f"When you convert {cel} celsius into fahrenheit you will get {fah} fahrenheit" )

def word_manipulation():
    """
    Menu choice 3
    """
    word = input("What word do you want to multiply... ")
    times = int(input("How many times do you want to multiply it... "))
    end_word = multiply_str(word, times)
    print(f"The word {word} {times} times becomes {end_word}") 

def sum_and_average():
    """
    Menu choice 4
    """
    totalValue = 0
    count = 0
    inValue = ""
    while inValue != "done":
        inValue = input("Please tell my the number or are you done? (If you are done please write done)")
        if inValue == "done":
            pass
        else:
            try:
                totalValue = round(totalValue + float(inValue), 2)
                count = count + 1
            except ValueError:
                print("Please write a number or done")
    med = round(totalValue / count, 2)
    print(f"The sum of all the numbers are {totalValue} and the average number is {med}")

def hyphen_string():
    """
    Menu choice 5
    """
    word = input("Please give me a word adventurer...")
    times = 1
    end_word = ""
    for letter in word:
        count = 0
        if end_word != "":
            end_word = end_word + "-"
        while count < times:
            end_word = end_word + letter
            count = count + 1
        times = times + 1
    print(f"The word {word} becomes {end_word}")

def is_isogram():
    """
    Menu choice 6
    """
    word = input("Please tell me the word that you want me to check...")
    end_value = ""
    for letter in word:
        count = 0
        for let in word:
            if let == letter:
                count = count + 1
        if count > 1:
            end_value = "not a isogram"
            break

    if end_value == "not a isogram":
        print("No match!")
    else:
        print("Match!")

def compare_numbers():
    """
    Menu choice 7
    """
    oldValue = ""
    inValue = input("Please tell me a number or are you done? (If you are done please write done)")
    while True:
        if inValue == "done":
            break

        oldValue = inValue
        inValue = input("Please tell me a number or are you done? (If you are done please write done)")
        
        if oldValue == "":
            oldValue = inValue
            inValue = input("Please tell me a number or are you done? (If you are done please write done)")

        try:
            oldValue = float(oldValue)
            inValue = float(inValue)
            if oldValue > inValue:
                print("smaller!")
            elif oldValue < inValue:
                print("larger!")
            else:
                print("same!")
        except ValueError:
            if inValue == "done":
                break
            inValue = oldValue
            print("not a number!")

def randomize_string(inText):
    """
    Menu choice 8
    """
    outText = ""
    temp = inText

    while inText:
        i = random.randint(0, len(inText) - 1)

        outText = outText + inText[i]

        inText = inText[0:i] + inText[i + 1:]
    
    outText = f"{temp} --> {outText}"

    return outText

def get_acronym(inText):
    """
    Menu choice 9
    """
    out = ""
    for letters in inText:
        if letters.isupper():
            out = out + letters
        
    return out

def mask_string(inText):
    """
    Menu choice 10
    """
    last = ""
    i = len(inText)
    mask_i = i - 4
    print(mask_i)
    for n in range(4):
        last = last + inText[mask_i + n]
    mask = multiply_str("#", mask_i)

    return mask + last

def find_all_indexes(inText, search):
    """
    Menu choice 11
    """
    i = 0 - len(search)
    out = ""
    temp = ""
    while True:
        try:
            i = inText.index(search, i + len(search))
            temp = out
            out = out + str(i) + ","
        except ValueError:
            if i > -1:
                out = temp + str(i)
            break
    
    return out

def multiply_str(word, times):
    """
    Multiply string
    """
    n = 0
    end_word = ""
    while n < times:
        n = n + 1
        end_word = end_word + word
    
    return end_word
