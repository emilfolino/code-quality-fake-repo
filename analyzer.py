#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Text analyzer function module
current module does not preload file content.
each new function call opens file.
"""

def handle_error(e):
    """Prints info of error for user"""
    if isinstance(e, FileNotFoundError):
        print(f"Specified file does not exist..[{e.filename}]")
    else:
        print(f"How the hell did you get here?\n{e}")

def count_lines(string_to_count):
    """counts the number of lines in a string"""
    return len(string_to_count.split(sep="\n"))

def get_unformated_string(filename):
    """Returns unformated string from provided file"""
    try:
        with open(filename) as filehandle:
            file_content = filehandle.read()
    except FileNotFoundError as e:
        handle_error(e)
    return file_content

def remove_symbols(string_to_process, sep = " ", chars = ".,-_"):
    """removes unwanted symbols and characters and replaces with space"""
    #chars_to_remove = []
    #for c in chars:
    #    chars_to_remove.append(c)
    for c in chars:
        string_to_process = string_to_process.replace(c, sep)
    return sep.join(string_to_process.split())

def get_sorted_dictionary_keys(dict_to_sort, length = None, reverse = False):
    """Returns sorted """
    if length is None:
        length = len(dict_to_sort.keys())
    #this gets list of tuples sorted by value.
    #sorted goes thru list of tuples, sorts by first index. if tiebreaker, then next index decides...
    #therefore i swapped indices from (key,value) to (value,key)
    #list comprehension to extract first index of tuple(keys)
    sorted_keys = [x[0] for x in sorted(dict_to_sort.items(), key=lambda x: (x[1],x[0]), reverse=reverse)]
    #sorted_keys = []
    #for i in sorted_keys_value:
    #    sorted_keys.append(i[0])
    #print(sorted_keys)
    return sorted_keys[0 : length]

def handle_line_count(filename):
    """handles """
    unformated_content = get_unformated_string(filename)
    line_count = count_lines(unformated_content)
    print(f"[{filename}] contains {line_count} lines")

def handle_word_count(filename):
    """handles """
    words = remove_symbols(get_unformated_string(filename), chars=",.").split(sep=" ")
    word_count = len(words)
    print(f"[{filename}] contains {word_count} words")
    #print(words)

def handle_letter_count(filename):
    """handles letter count funcitons"""
    letters = remove_symbols(get_unformated_string(filename), sep="").lower()
    letter_count = len(letters)
    #print(letters)
    print(f"[{filename}] contains {letter_count} letters")


def handle_word_fq(filename):
    """handles """
    words = remove_symbols(get_unformated_string(filename), chars=",.").lower().split(sep=" ")
    word_count = len(words)
    word_dictionary = {}
    for word in words:
        if word in word_dictionary:
            word_dictionary[word] += 1
        else:
            word_dictionary[word] = 1
    sorted_keys = get_sorted_dictionary_keys(word_dictionary, length=7, reverse=True)
    for key in sorted_keys:
        word_fq_percent = round(word_dictionary[key] / word_count * 100, 1)
        print(f"{key}: {word_dictionary[key]} | {word_fq_percent}%")



def handle_letter_fq(filename):# basically samma som wordfq. refactor
    """handles """
    words = remove_symbols(get_unformated_string(filename), sep="").lower()
    word_count = len(words)
    word_dictionary = {}
    for word in words:
        if word in word_dictionary:
            word_dictionary[word] += 1
        else:
            word_dictionary[word] = 1
    sorted_keys = get_sorted_dictionary_keys(word_dictionary, length=7, reverse=True)
    for key in sorted_keys:
        word_fq_percent = round(word_dictionary[key] / word_count * 100, 1)
        print(f"{key}: {word_dictionary[key]} | {word_fq_percent}%")


def handle_all(filename):
    """handles all"""
    handle_word_count(filename)
    handle_letter_count(filename)
    handle_line_count(filename)
    handle_word_fq(filename)
    handle_letter_fq(filename)


def change_file(old_filename):
    """handles """
    current_file = old_filename
    try:
        entered_file = input("Enter filename >>>")
        with open(entered_file) as filehandle:
            print(f"File [{filehandle.name}] successfully opened")
            current_file = entered_file
    except FileNotFoundError as e:
        handle_error(e)
    return current_file
