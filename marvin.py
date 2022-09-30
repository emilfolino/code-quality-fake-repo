#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Funktioner för marvin
"""

import random

def greet():
    """
    Marvin tar in och skriver ut användarens namn
    """
    localname = input("What is your name? ")
    print("\nMarvin says:\n")
    print("Hello %s - your awesomeness!" % localname)
    print("What can I do you for?!")


def celcius_to_farenheit():
    """
    Celcius till Farenheit. Marvin ska fråga efter en temperatur
    i Celcius och sedan skriva ut motsvarande i Farenheit.
    """
    localtemp = input("Enter celsius: ")
    print(str(round(float(localtemp) * 9 / 5 + 32, 2)) + " fahrenheit")


def word_manipulation():
    """
    Ordmultiplicering. Marvin ska fråga efter ett ord och
    en siffra och sedan skriva ut det ordet så många gånger.
    """
    word = input('Write a word: ')
    multiply_by = input("Enter how many times: ")

    print(multiply_str(word, multiply_by))


def sum_and_average():
    """
    Summa och medel: Marvin ska fråga efter tal tills du anser
    dig vara klar (t.ex skriver “done”) och sedan ska
    Marvin skriva ut summan och medelvärdet för dessa tal.
    """

    print("\nThe Magic Bucket says:\n")
    print("Enter unlimited amount of numbers, write done when done\n")

    sum_numbers = 0
    loop_round = 0

    while loop_round >= 0:

        add_number = input('Enter a number: ')

        if add_number == "done":

            r_sum_num = round(sum_numbers, 2)
            r_avg_num = round(sum_numbers/loop_round, 2)

            print("The sum of all numbers are {} and the average is {}".format(r_sum_num, r_avg_num))

            loop_round = -2
        else:
            sum_numbers += float(add_number)

        loop_round += 1



def hyphen_string():
    """
    Marvin ska fråga efter en sträng och skriva ut en ny sträng där
    varje karaktär har ökat med +1 och är separerad med “-“. Exempel:
    """
    stringToMessUp = input('Enter a word to mess up with hypens: ')

    counter = 1
    new_string = ""

    for character in stringToMessUp:
        local_counter = 0

        while local_counter < counter:
            new_string += character
            local_counter += 1

        new_string += "-"
        counter += 1

    print(new_string[:-1])


def is_isogram():
    """
    Gör så Marvin kan kolla om ett ord är ett isogram.
    Ett ord är ett isogram om det inte innehåller några
    återupprepande bokstäver, både i följd och icke i följd.
    Det är OK om den är case-sensitive, a != A.
    """
    stringToCheck = input('Enter a word to check if isogram: ')


    counter = 0
    match = 1

    for character in stringToCheck:

        if stringToCheck.find(character, counter+1) != -1:
            match = 0

        counter += 1

    if match == 1:
        result = "Match!"
    else:
        result = "No match!"

    print(result)

def compare_numbers():
    """
    Lägg till så att Marvin frågar efter tal och för varje tal angivet så
    ska Marvin skriva ut om det talet var större, mindre eller samma
    som det förra talet som skrev in. Tänk på att vid första talet
    angivet finns inget att jämföra med. Detta ska göras tills användaren
    skriver att denne är klar (t.ex “done”).
    """
    print("\nThe Magic Bucket says:\n")
    print("Compare the previous value with a new one\n")

    second_round = False
    old_number = 0

    while True:
        try:
            input_new_number = input('Enter a number: ')
            if input_new_number == "done":
                break

            new_number = int(input_new_number)

            if second_round:
                if new_number < old_number:
                    print("smaller!")
                elif new_number > old_number:
                    print("larger!")
                else:
                    print("same!")
            old_number = new_number
            second_round = True
        except ValueError:
            print("not a number!")



def randomize_string(word):
    """
    Kasta om bokstäver. Marvin ska be dig skriva in ett ord
    som sedan slumpmässigt kastas om. Det omkastade ordet
    ska sedan skrivas ut.
    """

    newWordList = []
    newWord = ""

    for char in word:
        newWordList.insert(random.randint(0, len(word)-1), char)

    return word + " --> " + newWord.join(newWordList)


def checkAnagram():
    """
    Anagram. Skapa ett val där marvin ber om två
    strängar och kollar om de är anagram. Ett anagram är när
    man kan få fram samma sträng genom att kasta om bokstäverna
    i den andra. Tips, sorted() och lower().
    """

    firstWord = input("Enter the first word: ")
    secondWord = input("Enter the second word: ")

    firstWord = firstWord.lower()
    secondWord = secondWord.lower()

    firstWord = sorted(firstWord)
    secondWord = sorted(secondWord)

    if firstWord == secondWord:
        print("Match!")
    else:
        print("No Match!")


def get_acronym(p_akronym):
    """
    Akronym skapare. Marvin ska be om en sträng och skapa en akronym för
    den genom att plocka ut alla stora bokstäver och sätta ihop till en
    ny sträng.
    """

    akronym = ""

    for char in p_akronym:
        if char.isupper():
            akronym += char

    return akronym

def mask_string(string_to_mask):
    """
    Sträng maskering. Skapa ett nytt
    val där Marvin ber om en sträng och ersätter
    alla utom de fyra sista karaktärerna med “#”.
    """
    first_part = string_to_mask[0:-4]
    second_part = string_to_mask[-4:]

    return multiply_str("#", len(first_part)) + second_part

def multiply_str(word, multiply_by):
    """
    Används för att multiplicera en sträng
    """
    index = 0
    word_string = ""

    while index < int(multiply_by):
        word_string += word
        index += 1

    return word_string

def find_all_indexes(p_first_string, p_second_string):
    """
    Hitta alla index. Marvin ska be om två strängar, där den andra strängen är
    en del-sträng av den första. Funktionen ska
    returnera en kommaseparerad sträng med
    alla index platser där den andra strängen
    finns med i den första.
    """
    indexes = ""
    last_index = 0

    while True:
        try:
            current_index = str(p_first_string.index(p_second_string, last_index))
            indexes += str(current_index) + ","
            last_index = int(current_index) + 1
        except ValueError:
            break

    return indexes[0:-1]

def filterList():
    """
    Filtrera listor. Marvin ska ta emot en sträng med
    olika nummer. Dessa skall omvandlas till en lista som endast
    innehåller värden över 10
    """
    stringOfNumbers = input("Enter a list of numbers:")

    listOfNumbers = stringOfNumbers.split(" ")

    listOfNumbersAbove10 = []

    for value in listOfNumbers:

        if int(value) > 10:
            listOfNumbersAbove10.append(value)

    listOfNumbersAbove10.sort()
    print(listOfNumbersAbove10)
