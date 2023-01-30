#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
This file contains the analyzer functions.
"""

import menu
def clear_terminal():
    """Function to clear the terminal"""
    print(chr(27) + "[2J" + chr(27) + "[;H")

def read_file_string(file_name):
    """Function to read the file contents as a string"""
    with open(file_name) as fd:
        return fd.read()

def get_input(message):
    """Function to get input from the user"""
    print(message)
    return input(" --> ")

def count_lines(file_string):
    """Function to count the non-empty lines of a file"""
    file_list = file_string.split("\n")
    linecount = len([line for line in file_list if line])
    return linecount

def get_string_one_line(file_string):
    """Function to remove all line breaks from a string"""
    return file_string.replace("\n", " ")

def get_alpha_only(file_string, include_chars = ""):
    """Function to remove all characters that are not letters, with option to include other characters"""
    file_string_one_line = get_string_one_line(file_string)
    alpha_only_string = "".join([char for char in file_string_one_line if char.isalpha() or char in include_chars])
    return alpha_only_string

def get_word_list(file_string):
    """Function to list all the words in a file"""
    file_string_without_punctuation = get_alpha_only(file_string, " -")
    word_list = file_string_without_punctuation.split()
    return word_list

def count_words(file_string):
    """Function to count the words in a file"""
    word_list = get_word_list(file_string)
    return len(word_list)

def count_letters(file_string):
    """Function to count the letters in a file"""
    letters = get_alpha_only(file_string)
    return len(letters)

def get_statistics(data_list, limit):
    """Function to rank the most frequent elements in a list, and present the results"""
    counted_list = [(data_list.count(word), round(data_list.count(word)/len(data_list) * 100, 1), word)
        for word in set(data_list)]
    sorted_list = sorted(counted_list, key = lambda x:(x[0],x[2]), reverse = True)
    output = ""
    for output_tuple in sorted_list[:limit]:
        output += f"{output_tuple[2]}: {output_tuple[0]} | {output_tuple[1]}%\n"
    return output

def word_frequency(file_string, limit):
    """Function to rank the most frequent words in a string, and present the results"""
    word_list = get_word_list(file_string)
    return get_statistics(word_list, limit)

def letter_frequency(file_string, limit):
    """Function to rank the most frequent letters in a string, and present the results"""
    letter_list = list(get_alpha_only(file_string))
    return get_statistics(letter_list, limit)

def do_all(file_string, limit):
    """Function to count the lines, words and letters in a string, and rank the most frequent words and letters."""
    output = f"{count_lines(file_string)} \n"
    output += f"{count_words(file_string)} \n"
    output += f"{count_letters(file_string)} \n\n"
    output += f"{word_frequency(file_string, limit)} \n"
    output += f"{letter_frequency(file_string, limit)} \n"
    return output

def change_file(current_filename):
    """Function to let user choose which file to analyze"""
    new_filename = get_input(f"Which file do you want to use instead of {current_filename}?")
    if new_filename == current_filename:
        menu.display(current_filename)
        print(f"Already using {current_filename}!")
        return current_filename
    try:
        with open(new_filename):
            menu.display(new_filename)
            print(f"Changed from {current_filename} to {new_filename}!")
            return new_filename
    except FileNotFoundError:
        menu.display(current_filename)
        print(f"There is no {new_filename} in the directory!")
        return current_filename
