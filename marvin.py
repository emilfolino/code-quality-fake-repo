#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Marvin with a simple menu to start up with.
Marvin doesnt do anything, just presents a menu with some choices.
You should add functinoality to Marvin.
"""
import random

def multiply_str(multiply_string, multiply_number):
    """multiplicerar ett värde med en sträng"""
    output = multiply_string*int(multiply_number)
    return output

def greet():
    """Hälsar på användaren med deras namn"""
    name = input("What is your name? ")
    print("\nYoda says:\n")
    print("Hello %s - In a dark place we find ourselves, and a little more knowledge lights our way." % name)
    print("Your path you must decide.")

def celcius_to_farenheit():
    """Omvandlar celcius till farenheit"""
    celsius = input("Truly wonderful the mind of a child is. Name the Celsius young Padawan: ")
    fahrenheit = float(celsius) * 9 / 5 + 32
    fahrenheit = round(fahrenheit, 2)
    print(fahrenheit)

def word_manipulation():
    """Skriver ut angivet ord angivet antal gånger"""
    multiply_string = input("Train yourself to let go of everything you fear to lose. What is your favorite word? ")
    multiply_numbers = input("Your path you must decide. What is your favorite number? ")
    multiply_number = int(multiply_numbers)
    print("Then you will love this young Padawan:")
    multiply_words = multiply_str(multiply_string, multiply_number)
    print(multiply_words)



def sum_and_average():
    """Räknar ut summa och medelvärde för angivna nummer"""
    
    sum_of_numbers = 0
    done = False
    counter = 0
            
    while not done:
        number = input("How many laser sables you think I have? (if you are out of guesses just say 'done'): ")
        if number == "done":
            done = True
        else:
            sum_of_numbers = sum_of_numbers + float(number)
            counter = counter + 1
        average = sum_of_numbers / counter
        average = round(average, 2)
        sum_of_numbers = round(sum_of_numbers, 2)
        print("The sum of all numbers are " + str(sum_of_numbers) + " and the average is " + str(average)) 
        
    # Marvin ska fråga efter en sträng och skriva ut en ny
    # sträng där varje karaktär har ökat med +1 och är separerad med “-“. 

def hyphen_string():
    """omvandlar ett angivet ord """
    word = input("Always pass on what you have learned. Tell me a word to transform :")
    number = 1
    sum_of_numbers = ""
    for letter in word:
        sum_of_numbers += letter * number + "-"
        number = number + 1
    print(sum_of_numbers [:-1])

    #Menyval 6: Gör så Marvin kan kolla om ett ord är ett isogram. 
    # Ett ord är ett isogram om det inte innehåller några återupprepande bokstäver, 
    # både i följd och icke i följd. Det är OK om den är case-sensitive, a != A. 

def is_isogram():
    """Kan berätta om ett ord är ett isogram"""
    value = ""
    word = input("Truly wonderful the mind of a child is. I can tell you if a word is a isogram. Give me a word: ")
    for letter in word:
        if letter in value:
            print("No match!")
            break
        else:
            value = value + letter
            if word == value:
                print("Match!")

    # Frågar efter tal och för varje tal angivet så ska Marvin skriva ut “larger!”
    #  om det nya talet är större, “smaller!” om mindre
    #Första gången = 2 tal
    # Om inget tal = not a number!"

def compare_numbers():
    """Jämför två nummer för att se om det är större, mindre eller lika med"""
    number_input = input("Give me a number and I will tell you if its smaller or larger! :")
    done = True
    while done is True:
        input_number2 = input("Tell me another number: ")
        try:
        
            if input_number2 == "done":
                done = False
                break
            
            input_number2 = float(input_number2)
        
        except ValueError:
            print("not a number!")
            continue
        
        else:           
    
            if float(input_number2) == float(number_input):
                print("same!")

            elif float(input_number2) < float(number_input):
                print("smaller!")

            elif float(input_number2) > float(number_input):
                print("larger!")

        number_input = input_number2

def randomize_string(for_random_word):
    """Ändrar ordningen på angivet ord"""

    random_word_list = list(for_random_word)

    random.shuffle(random_word_list)

    new_sentence = "".join(random_word_list)
    new_sentence = (f"{for_random_word} --> {new_sentence}")
    return new_sentence
            
            


if __name__ == "__main__":
    randomize_string("for_random_word")
    
            


def get_acronym(input_word):
    """Skriver ut stora bokstäver från angiven text"""
    akronym_word = ""
    for word in input_word:
    
        if word.isupper() is True:
            akronym_word += word
            
        else:
            continue
    return akronym_word

if __name__ == "__main__":
    get_acronym("akronym_word") 

def mask_string(string):
    """Maskerar alla utom de fyra sista siffrorna i ett lösenord"""

    
    for string2 in [string]:
        new_list = string[0:-4]
        multiply_numbers = len(string) - 4
        multiply_string = "#"
        hidden = multiply_str(multiply_string, multiply_numbers)
        string2 = string.replace(new_list, hidden, 1)
        return string2

if __name__ == "__main__":
    mask_string("string")

def find_all_indexes(long_word, short_word):
    """Hittar alla indexpositioner för angivet i en ord eller mening"""
    new_word = 0
    result_word =""
    for last_result in long_word:
        try:
            new_word = long_word.index(short_word, new_word)
            result_word += str(new_word) + ","
            new_word += 1
            
        except ValueError:
            continue
        
    result_word = list(result_word)
    divide =""
    last_result = divide.join(result_word[:-1])
    return last_result

if __name__ == "__main__":
    find_all_indexes("string", "string2")






    
