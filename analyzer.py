#!/usr/bin/env python3
# -- coding: utf-8 --

""" Docstring """

from operator import itemgetter


def line_count(changed_file):

    """ Docstring """

    with open(changed_file, "r") as analyze_txt:
        ana_line = analyze_txt.readlines()

    line_counted = 0

    for numb in ana_line:
        if numb != "\n":
            line_counted += 1
    return(line_counted)

def word_count(changed_file):

    """ Docstring """

    with open(changed_file, "r") as analyze_txt:
        ana_line = analyze_txt.read()

    word_counted = 1

    for word in ana_line:
        if word in (" ", "\n"):
            word_counted += 1
    return(word_counted)

def letter_count(changed_file):

    """ Docstring """

    with open(changed_file, "r") as analyze_txt:
        ana_line = analyze_txt.read()
    
    letter_counted = 0

    for letter in ana_line:
        if letter == " ":
            pass
        elif letter == "\n":
            pass
        elif letter == ",":
            pass
        elif letter == ".":
            pass
        elif letter == "-":
            pass
        else:
            letter_counted += 1

    return(letter_counted)

def word_frequency(changed_file):

    """ Docstring """

    word_dict = {}
    word_dict_unsort = {}
    time = -1
    ana_line1 = ""

    with open(changed_file, "r") as analyze_txt:
        ana_line = analyze_txt.read()
    
    for i in ana_line:
        if i == ",":
            i = i.replace(",", "")
        else:
            i = i.replace(".", "")
            ana_line1 += i

    ana_line3 = ana_line1.lower()
    ana_line2 = ana_line3.split()
    list_ana_line = []

    for i in ana_line2:

        if i not in list_ana_line:

            list_ana_line.append(i)
    
    aa = len(list_ana_line)

    for i in range(0, aa):

        a = " | "
        b = "%"
        x = list_ana_line[i] + ": "
        y = ana_line2.count(list_ana_line[i])
        word_procent = 100 * (ana_line2.count(list_ana_line[i]) / word_count(changed_file))
        numbers_of_words1 = f"{y}{a}{round(word_procent, 1)}{b}"
        numbers_of_words = y
        word_dict[x] = numbers_of_words
        word_dict_unsort[x] = numbers_of_words1
        
    list_dict_words = word_dict.items()
    sorted_dict_words2 = sorted(list_dict_words, key=itemgetter(0), reverse=True)
    sorted_dict_words = sorted(sorted_dict_words2, key=itemgetter(1), reverse=True)

    list_sorted_dict_words = dict(sorted_dict_words)
    yy = ""
    xx = "\n"
    yyy = ""
    yy = tuple(yy)


    for z, ii in word_dict_unsort.items():
        if z in list_sorted_dict_words:
            list_sorted_dict_words[z] = ii

    for count_words, count_value in list_sorted_dict_words.items():
        time += 1

        if time == 7:
            break
        yy = count_words + count_value 
        yyy += str(yy) + xx
    return(yyy)

def letter_frequency(changed_file):

    """ Docstring """

    word_dict = {}
    word_dict_unsort = {}
    time = -1
    ana_line1 = ""

    with open(changed_file, "r") as analyze_txt:
        ana_line = analyze_txt.read()
        ana_line = ana_line.replace(" ", "")
    
    for i in ana_line:
        if i == ",":
            i = i.replace(",", "")
        elif i == "\n":
            pass
        else:
            ana_line1 += i

    ana_line3 = ana_line1.lower()
    ana_line2 = ana_line3.strip()
    list_ana_line = []

    for i in ana_line2:


        if i not in list_ana_line:
            
            list_ana_line.append(i)

    aa = len(list_ana_line)
    
    for i in range(0, aa):
        a = " | "
        b = "%"
        x = list_ana_line[i] + ": "
        y = ana_line2.count(list_ana_line[i])
        word_procent = 100 * (ana_line2.count(list_ana_line[i]) / letter_count(changed_file))
        numbers_of_words1 = f"{y}{a}{round(word_procent, 1)}{b}"
        numbers_of_words = y
        word_dict[x] = numbers_of_words
        word_dict_unsort[x] = numbers_of_words1
        
    list_dict_words = word_dict.items()
    sorted_dict_words2 = sorted(list_dict_words, key=itemgetter(0), reverse=True)
    sorted_dict_words = sorted(sorted_dict_words2, key=itemgetter(1), reverse=True)

    list_sorted_dict_words = dict(sorted_dict_words)
    yy = ""
    xx = "\n"
    yyy = ""
    yy = tuple(yy)



    for z, ii in word_dict_unsort.items():
        if z in list_sorted_dict_words:
            list_sorted_dict_words[z] = ii

    for count_words, count_value in list_sorted_dict_words.items():
        time += 1

        if time == 7:
            break
        yy = count_words + count_value 
        yyy += str(yy) + xx
    return(yyy)

def analyze_all(changed_file):

    """ Docstring """

    x = str(line_count(changed_file)) + "\n" + "\n" + "\n"
    y = str(word_count(changed_file)) + "\n" + "\n" + "\n"
    z = str(letter_count(changed_file)) + "\n" + "\n" + "\n"
    i = str(word_frequency(changed_file)) + "\n" + "\n" + "\n"
    ii = str(letter_frequency(changed_file)) + "\n" + "\n" + "\n"

    print(x + y + z + i + ii)

def change_read_file(new_file):

    """ Docstring """

    return(new_file)
