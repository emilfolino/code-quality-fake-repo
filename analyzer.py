#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Functions for analyzing a text for lines, words and letters"""

def replace_non_alpha(string1, remove_spaces = False):
    """Takes two arguments, string1 to be prepared and the bool remove_spaces, indicating
    whether spaces should be removed. The function prepares a string for analysis by
    removing all non-alpha numerical characters and replacing \n with space. 
    If remove_spaces is True, all spaces are removed as well."""
    
    string1 = string1.replace("\n", " ")
    string_list = list(string1)
    return "".join(l if l.isalpha() or (l.isspace() and not remove_spaces) else "" for l in string_list)

def remove_empty_line(content):
    """Takes string content as argument Removes empty lines 
    from string and returns the string"""
    
    content = content.split("\n")
    
    for index, line in enumerate(content):
        if not line:
            content.pop(index)

    return "\n".join(content)

def change_filename():
    """Prompts user input asking for a filename and checks if the file exists
    by trying to open (and close) the file. If succesful, prints 
    a success-message and returns the filename, if not raises a FileNotFoundError"""
    
    filename = input("Please type in the filename:\n-->")

    try:
        with open(filename):
            print("File changed to " + filename)
            return filename
    except FileNotFoundError as e:
        raise FileNotFoundError(str(e)) from e

def count_lines(filename):
    """Takes argument filename and counts and prints 
    the number of lines in the file."""

    try:
        with open(filename, 'r', 1, "utf-8") as filehandler:
            file_content = filehandler.read()
        
        file_content = remove_empty_line(file_content)

        print(str(len(file_content.split("\n")))) 

    except FileNotFoundError as e:
        raise FileNotFoundError(str(e)) from e

def count_words(filename):
    """Takes argument filename and counts and prints the number 
    of words in the file"""

    try:
        with open(filename, 'r', 1, "utf-8") as filehandler:
            file_content = filehandler.read()

        file_content = remove_empty_line(file_content)
        file_content = replace_non_alpha(file_content)
        file_content = file_content.split(" ") 

        print(str(len(file_content))) 

    except FileNotFoundError as e:
        raise FileNotFoundError(str(e)) from e

def count_letters(filename):
    """Takes argument filename and counts and prints the nubmer 
    of letters in the file"""
    
    try:
        with open(filename, 'r', 1, "utf-8") as filehandler:
            file_content = filehandler.read()
        
        file_content = replace_non_alpha(file_content, True)
        
        print(str(len(file_content)))

    except FileNotFoundError as e:
        raise FileNotFoundError(str(e)) from e


def word_frequency(filename, result_number = 7):
    """Takes arguments filename and result_number and calculates and prints
    the frequency of the words in the file. The number of words
    to be printed is given in result number, with default being 7."""

    try:
        with open(filename, 'r', 1, "utf-8") as filehandler:
            file_content = filehandler.read().lower()
        
        file_content = replace_non_alpha(file_content)
        word_list = file_content.split(" ")

        total_words = len(word_list)

        word_freq_list = {}
        
        for word in word_list:
            if word not in word_freq_list:
                word_freq_list[word] = 1
            else:
                word_freq_list[word] += 1
        
        for word, freq in sorted(word_freq_list.items(), \
            key = lambda item: (item[1],item[0]), reverse=True)[:result_number]:
            print(word + ": " + str(freq) + " | " + str(round(freq / total_words * 100, 1)) + "%")
    
    except FileNotFoundError as e:
        raise FileNotFoundError(str(e)) from e

def letter_frequency(filename, result_number = 7):
    """Takes argument filename result_number and calculates and prints
    the frequency of the letters in the file. The number of letters
    to be printed is given in result number, with default being 7."""

    try:
        with open(filename, 'r', 1, "utf-8") as filehandler:
            file_content = filehandler.read().lower()

        file_content = replace_non_alpha(file_content, True)
        total_char = len(file_content)
        letter_freq_list = {}
        
        for letter in file_content:
            if letter not in letter_freq_list:
                letter_freq_list[letter] = 1
            else:
                letter_freq_list[letter] += 1
        
        for letter, freq in sorted(letter_freq_list.items(), \
            key=lambda item: (item[1],item[0]), reverse=True)[:result_number]:
            print(letter + ": " + str(freq) + " | " + str(round(freq / total_char * 100, 1)) + "%")
    
    except FileNotFoundError as e:
        raise FileNotFoundError(str(e)) from e

def run_all(filename):
    """Runs all checks, count_lines, count_words, count_letters,
    word_frequency and letter_frequency on the file given 
    as argument."""

    count_lines(filename)
    count_words(filename)
    count_letters(filename)
    word_frequency(filename)
    letter_frequency(filename)
