"""
Functions for text analyzing
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from operator import itemgetter

def count_lines(filename):
    """
    count and return the number of lines (not empty) in a file
    """

    nr_oflines = 0
    with open(filename) as filehandle:
        for line in filehandle:
            if line != "\n":
                nr_oflines += 1

    return nr_oflines


def count_words(filename):
    """
    count and return the number of words in a file
    """

    nr_ofwords = 0
    with open(filename) as filehandle:
        for line in filehandle:
            line = line.rstrip()
            items_as_list = line.split(" ")
            nr_ofwords = nr_ofwords + len(items_as_list)

    return nr_ofwords


def count_letters(filename):
    """
    count and return the number of letters in a file
    """

    letter_list= "abcdefghijklmnopqrstuvwxyz"
    nr_ofletters=0
    with open(filename) as filehandle:
        for line in filehandle:
            line=line.rstrip().lower()
            for char in line:
                if char in letter_list:
                    nr_ofletters = nr_ofletters + 1


    return nr_ofletters


def letter_frequency(filename):
    """
    Analyze and return the most frequent letters
    """
    letter_list= "abcdefghijklmnopqrstuvwxyz "
    letter_dict = {}
    word_as_list=[]

    with open(filename) as filehandle:
        for line in filehandle:
            line = line.rstrip().lower()
            for char in line:
                if char not in letter_list:
                    line=line.replace(char, "")
            words = line.split(" ")
            for word in words:
                word_as_list.append(word)

    word_str= "".join(word_as_list)

    for letter in word_str:
        if letter not in letter_dict.keys():
            percent = round(((word_str.count(letter)/count_letters(filename))*100),1)

            letter_dict[str(letter)]= (word_str.count(letter),percent)

    letter_aslist= letter_dict.items()
    letter_sorted_onvalue = sorted(letter_aslist, key=itemgetter(1,0), reverse=True)

    return letter_sorted_onvalue[0:7]



def word_frequency(filename):
    """
    Analyze and return the most frequent words
    """
    letter_list= "abcdefghijklmnopqrstuvwxyz "
    word_dict = {}
    word_as_list=[]

    with open(filename) as filehandle:
        for line in filehandle:
            line = line.rstrip().lower()
            for char in line:
                if char not in letter_list:
                    line=line.replace(char, "")
            words = line.split(" ")
            for word in words:
                word_as_list.append(word)


    for word in word_as_list:
        if word not in word_dict.keys():
            percent = round(((word_as_list.count(word)/count_words(filename))*100),1)

            word_dict[str(word)]= (word_as_list.count(word),percent)

    word_aslist= word_dict.items()
    word_sorted_onvalue = sorted(word_aslist, key=itemgetter(1,0), reverse=True)

    return word_sorted_onvalue[0:7]



def all_functions(filename):
    """
    Run all the analyzing functions in a row
    """

    dict_all = {}

    dict_all["lines"] = count_lines(filename)

    dict_all["words"]= count_words(filename)

    dict_all["letters"]= count_letters(filename)

    answer_word = word_frequency(filename)
    for key, value in answer_word:
        dict_all[str(key)] = f"{key}: {value[0]} | {value[1]}%"


    answer_letter = letter_frequency(filename)
    for key, value in answer_letter:
        dict_all[str(key)] = f"{key}: {value[0]} | {value[1]}%"


    return dict_all
