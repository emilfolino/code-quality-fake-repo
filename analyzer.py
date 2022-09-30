#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
modul-dokument, funktioner för textanalysering
"""
from operator import itemgetter

def lines(filename):
    """
    Funktion som skriver ut antal rader
    """
    count_lines = 0

    with open(filename, "r") as fp:
        for num_lines in fp:
            if num_lines.strip() != "":
                count_lines += 1
        return count_lines

def words(filename):
    """
    Funktion som skriver ut antal ord
    """
    with open(filename, "r") as fp:
        text = fp.read()
        all_words = text.split()
        count_words = len(all_words)
    return count_words

def letters(filename):
    """
    Funktion som skriver ut antal bokstäver
    """
    number_of_characters = 0

    with open(filename, "r") as fp:
        for num_char in fp:
            num_char = num_char.strip()
            erase_space = len(num_char) - num_char.count(" ") 
            erase_comma = erase_space - num_char.count(",") 
            erase_dot = erase_comma - num_char.count(".") 
            erase_line = erase_dot - num_char.count("-")
            number_of_characters += erase_line
    return number_of_characters

def word_frequency(filename):
    """
    Funktion som skriver ut de mest förekommande orden
    """
    new_dict = {}
    counter = 0
    #Lägger till alla ord i en dict och antalet gånger ordet förekommer i texten.
    with open(filename, "r") as fp:
        for line in fp:
            line = line.strip()
            line = line.lower()
            line = line.replace('.', '')
            line = line.replace(',', '')
            line = line.replace('-', '')
            num_words = line.split(" ")
            for word in num_words:
                if word in new_dict:
                    new_dict[word] = new_dict[word] + 1
                else:
                    new_dict[word] = 1

    #sorterar dict i numerisk fallande ordning med det ord som förekommer mest först.
    #De med samma value sorteras i alfabetisk fallande ordning.
    get_item = itemgetter(0)
    sorted_key = sorted(new_dict.items(), key = get_item, reverse = True)
    sorted_val = sorted(sorted_key, key = lambda x: x[1], reverse = True) 
    for quant_word, freq_word in sorted_val:
        percent = round(freq_word / words(filename) * 100, 1)
        result = "{word}: {integ} | {percent}%".format (
        word = quant_word,
        integ = freq_word,
        percent = percent
        )
        print(result)
        counter += 1
        if counter == 7:
            break

def letter_frequency(filename):
    """
    Funktion som skriver ut de mest förekommande bokstäverna
    """
    new_dict = {}
    counter = 0
     #Lägger till alla bokstäver i en dict och antalet gånger bokstaven förekommer i texten.
    with open(filename, "r") as fp:
        for line in fp:
            line = line.strip()
            line = line.lower()
            line = line.replace('.', '')
            line = line.replace(',', '')
            line = line.replace('-', '')
            line = line.replace(' ', '')
            num_letters = list(line)
            for letter in num_letters:
                if letter in new_dict:
                    new_dict[letter] = new_dict[letter] + 1
                else:
                    new_dict[letter] = 1

    #sorterar dict i numerisk fallande ordning med det bokstäver som förekommer mest först.
    #De med samma value sorteras i alfabetisk fallande ordning.
    get_item = itemgetter(0)
    sorted_key = sorted(new_dict.items(), key = get_item, reverse = True)
    sorted_val = sorted(sorted_key, key = lambda x: x[1], reverse = True) 
    for quant_letter, freq_letter in sorted_val:
        percent = round(freq_letter / letters(filename) * 100, 1)
        result = "{letter}: {integ} | {percent}%".format (
        letter = quant_letter,
        integ = freq_letter,
        percent = percent
        )
        print(result)
        counter += 1
        if counter == 7:
            break
