#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Functions for text analysis.
"""

def menyval_lines(lines):
    """Prints the amount of lines."""
    return print(len(lines))

def menyval_words(read):
    """Prints the amount of words."""
    return print(len(read.split()))

def menyval_letters(read):
    """Prints the amount of letters."""
    result = ""
    for i in read:
        if i.isalpha():
            result += i

    return print(len(result))

def menyval_word_frequency(read):
    """Prints the word frequency."""
    read_dict = {}
    read_lst = read.split()
    counter = 0

    for i in read_lst:
        if i.isalpha() and i not in read_dict:
            read_dict[i] = 1
        elif i.isalpha():
            read_dict[i] += 1
        else:
            if i[:-1] not in read_dict:
                read_dict[i[:-1]] = 1
            elif i[:-1] in read_dict:
                read_dict[i[:-1]] += 1

    read_lst_sorted = dict(sorted(read_dict.items(), key=lambda x: x[1], reverse=True))
    for key, value in read_lst_sorted.items():
        print(f"{key}: {value} | {round((value / sum(read_lst_sorted.values())*100), 1)}%")
        counter += 1
        if counter == 25:
            break

def menyval_letter_frequency(read):
    """Prints the letter frequency."""
    read_dict = {}
    counter = 0
    
    for i in read:
        if i.isalpha() and i not in read_dict:
            read_dict[i] = 1
        elif i.isalpha():
            read_dict[i] += 1

    read_dict_sorted = dict(sorted(read_dict.items(), key=lambda x: x[1], reverse=True))
    for key, value in read_dict_sorted.items():
        print(f"{key}: {value} | {round((value / sum(read_dict_sorted.values())*100), 1)}%")
        counter += 1
        if counter == 7:
            break

def all_function(lines, read):
    """Prints all of the values of the functions above."""
    menyval_lines(lines)
    menyval_words(read)
    menyval_letters(read)
    menyval_word_frequency(read)
    menyval_letter_frequency(read)

def change():
    """Changes the file in use."""
    with open("/home/dbwebb/repo/me/kmom06/analyzer/lorum.txt", "r") as file: 
        #Note to self: /cygdrive/c/users/carlm/dbwebb-kurser/python/me/kmom06/analyzer/lorum.txt
        lines = file.readlines()
        file.seek(0)
        read = file.read().lower()

    return [lines, read]

def menyval_q():
    """Prints a goodbye message."""
    print("Bye, bye - and welcome back anytime!")
