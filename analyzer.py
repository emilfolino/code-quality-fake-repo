#!/usr/bin/env python3
 
"""functions for analyzer"""

from operator import itemgetter

def file_loader(file):
    """reads file returns string"""
    with open(file) as filehandle:
        string_from_file = filehandle.read()
    return string_from_file

def string_to_list(string, splitchar):
    """takes string, split on splitchar, returns list"""
    return_list = string.split(splitchar)
    return return_list

def string_newline_to_space(string):
    """takes string, replaces \n with space, returns string"""
    string = string.replace("\n", " ")
    return string

def string_to_lowercase(string):
    """takes string, returns lowercase"""
    string = string.lower()
    return string

def string_remove_nonalpha(string):
    """removes all nonletters but keep spaces and returns result"""
    new_string = ""
    for letter in string:
        if letter == " ":
            new_string += letter
        elif letter.isalpha():
            new_string += letter
    return new_string
    
def count_lines(string):
    """count and return no non-empty lines"""
    temp_list = string_to_list(string, "\n")
    line_counter = 0
    for i in temp_list:
        if len(i) > 0:
            line_counter += 1
    return line_counter

def count_words(string):
    #currently failing test
    """count and return no. words"""
    temp_list = string_to_list(string_newline_to_space(string), " ")
    word_count = len(temp_list)
    return word_count

def count_letters(string):
    """count and return no. letters"""
    string = string_remove_nonalpha(string)
    return_no = 0
    for each in string:
        if each.isalpha():
            return_no += 1
    return return_no

def dictionary_sorter(dictionary):
    """input dict, sort by value, return dict"""
    temp_dict = {}

    for key in sorted(dictionary.keys(), reverse=True):
        temp_dict[key] = dictionary[key]
    
    dict_as_list = temp_dict.items()
    dict_sorted_on_values = sorted(dict_as_list, key=itemgetter(1, 1), reverse=True)
    return_dict = {}

    for i in dict_sorted_on_values: #put it back into dict
        return_dict[i[0]] = i[1]
    return return_dict

def dictionary_select_7(dictionary):
    """selects first seven items, returns dict"""
    counter = 0
    return_dict = {}
    for item in dictionary.keys():
        if counter < 7:
            return_dict[item] = dictionary[item]
            counter += 1

    return return_dict

def add_word_share(dictionary, string):
    """adds share of frequency to dict based on no of words in string"""
    no_word = count_words(string)

    for i in dictionary:
        dictionary[i] = (dictionary[i], round(float(dictionary[i]/no_word)*100, 1))
    
    return dictionary 

def add_letter_share(dictionary, string):
    """adds share of frequency to dict based of no letters in string"""
    no_letters = count_letters(string)

    for i in dictionary:
        dictionary[i] = (dictionary[i], round(float(dictionary[i]/no_letters)*100, 1))
    
    return dictionary

def word_frequency(string):
    """counts frequency of words, returns dict"""
    string = string_newline_to_space(string)
    string = string_to_lowercase(string)
    string = string_remove_nonalpha(string)
    string_list = string_to_list(string, " ")

    word_freq_dict = {}
    for i in string_list:
        if i in word_freq_dict:
            word_freq_dict[i] += 1
        else:
            word_freq_dict[i] = 1

    word_freq_dict = add_word_share(word_freq_dict, string)
    word_freq_dict = dictionary_sorter(word_freq_dict)
    word_freq_dict = dictionary_select_7(word_freq_dict)
    return word_freq_dict

def letter_frequency(string):
    """counts letter frequency, returns dict"""
    string = string_newline_to_space(string)
    string = string_to_lowercase(string)
    string = string_remove_nonalpha(string)

    letter_freq_dict = {}
    for i in string:
        if i in letter_freq_dict:
            letter_freq_dict[i] += 1
        else:
            letter_freq_dict[i] = 1

    letter_freq_dict.pop(" ")

    letter_freq_dict = add_letter_share(letter_freq_dict, string)
    letter_freq_dict = dictionary_sorter(letter_freq_dict)
    letter_freq_dict = dictionary_select_7(letter_freq_dict)
    return letter_freq_dict

def pretty_print(dictionary):
    """prints word letter freq pretty"""
    for key in dictionary.keys():
        print(str(key) + ": " + str(dictionary[key][0]) + " | " + str(dictionary[key][1]) + "%")
