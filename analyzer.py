#Project by Croyse

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Funktioner för analysatorn
'''
def line_counter(file):
    '''
    Räknar antal linjer
    '''
    with open(file, "r") as the_line_counter:
        return len(the_line_counter.readlines())

def word_counter(file):
    '''
    Räknar antal ord
    '''
    with open(file, "r") as the_word_counter:
        word_counter1 = the_word_counter.read()
        word_counter_res = word_counter1.split()
    return len(word_counter_res)

def letter_counter(file):
    '''
    Räknar antal bokstäver
    '''
    with open(file, "r") as the_letter_counter:
        letter_counter1 = the_letter_counter.read()
        l = letter_counter1.replace(" ","").replace("\n", "").replace(",", "").replace(".", "").replace("-", "") 
        letter_counter_res = len(l)
        
    return letter_counter_res

def word_frequency(file):
    '''
    Räknar hur mycket man använder orden
    '''
    with open(file, "r") as text:
        contents = text.read()

    words = [word.lower() for word in contents.split()]

    total = len(words)
    for i in range(total):
        words[i] = words[i].strip(",")
        words[i] = words[i].strip(".")
    
    unique = list(set(words))
    
    unique_total = len(unique)
    frequency = [[0 for x in range(2)] for x in range(unique_total)]

    for i in range(unique_total):
        frequency[i][0] = unique[i]
        frequency[i][1] = words.count(unique[i])

    frequency.sort(reverse=True)
    frequency.sort(key=lambda x: x[1], reverse=True)
    
    results = unique_total if unique_total < 7 else 7
    for i in range(results): 
        word = frequency[i][0]
        freq = frequency[i][1]
        perc = round((freq/total)*100,1)
        print(word + ": " + str(freq) + " | " + str(perc) + "%")

def letter_frequency(file):
    '''
    Räknar hur mycket man använder bokstäver
    '''
    with open(file, "r") as text:
        contents = text.read()

    letters = []
    contents = list(contents)
    contents_string = len(contents)
    for i in range(contents_string):
        if contents[i].isalpha():
            letters.append(contents[i].lower())
    
    total = len(letters)
    unique = list(set(letters))

    unique_total = len(unique)
    frequency = [[0 for x in range(2)] for x in range(unique_total)]

    for i in range(unique_total):
        frequency[i][0] = unique[i]
        frequency[i][1] = letters.count(unique[i])

    frequency.sort(reverse=True)
    frequency.sort(key=lambda x: x[1], reverse=True)
    
    results = unique_total if unique_total < 7 else 7
    for i in range(results): 
        letter = frequency[i][0]
        freq = frequency[i][1]
        perc = round((freq/total)*100,1)
        print(letter + ": " + str(freq) + " | " + str(perc) + "%")

def every_function(file):
    '''
    Använda sig av alla funktioner
    '''
    print(line_counter(file))
    print(word_counter(file))
    print(letter_counter(file))
    word_frequency(file)
    letter_frequency(file)
