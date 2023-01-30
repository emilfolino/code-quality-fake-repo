#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""this module is the holds functions for the main program"""

from operator import itemgetter


def change():
    """this function changes the filename"""
    filename = input("What file should be used? ")
    return filename


def lines_analyzer(filename):
    """prints number of non-empty lines in text"""
    with open(filename, "r") as fd:
        text = fd.readlines()
    antal = 0
    for lines in text:
        if lines != "\n":
            antal = antal + 1
    print(antal)

def words_analyzer(filename):
    """prints number of words in text"""
    with open(filename, "r") as fd:
        text = fd.readlines()
    test = []
    for i in text:
        test.append(i.strip())
    text = test

    text = " ".join(text)
    text = text.split(" ")
    antal = 0
    for i in text:
        antal = antal + 1
    print(antal)

def letters_analyzer(filename):
    """prints number of letters in text"""
    with open(filename, "r") as fd:
        text = fd.readlines()
    antal = 0
    text = "".join(text)
    for i in text:
        if i not in " \n,.-":
            antal = antal + 1
    print(antal)

def letter_frequency(filename):
    """prints frequency of letters in text"""
    with open(filename, "r") as fd:
        text = fd.readlines()

    test = []

    for i in text:
        test.append(i.strip())
    text = test

    text = "".join(text)
    text = text.lower()

    letters = ""
    for i in text:
        if i not in " .,-":
            letters = letters + i

    summa = len(letters)
    text = letters

    lista = []
    for i in text:
        if i not in lista:
            lista.append(i)

    mydict = {word : 0 for word in lista}

    for word in text:
        if word in text:
            mydict[word] = mydict[word] + 1

    mydict = {key : mydict[key] for key in sorted(mydict.keys())}

    lista = mydict.items()
    lista_sorted = sorted(lista, key=itemgetter(1), reverse=True)

    lista_final = []

    for i in range(0,7):
        lista_final.append(lista_sorted[i][0] + ": " + \
        str(lista_sorted[i][1]) + " | " + str(round(lista_sorted[i][1] / summa * 100, 1)) + "%")

    print(lista_final)


def word_frequency(filename):
    """prints word of letters in text"""
    with open(filename, "r") as fd:
        text = fd.readlines()

    test = []

    for i in text:
        test.append(i.strip())
    text = test

    text = " ".join(text)
    text = text.lower()
    text = text.split(" ")

    summa = text

    y = 0
    for i in text:
        text[y] = i.strip(",.")
        y = y + 1

    lista = []
    for i in text:
        if i not in lista:
            lista.append(i)

    mydict = {word : 0 for word in lista}

    for word in text:
        if word in text:
            mydict[word] = mydict[word] + 1

    mydict = {key : mydict[key] for key in sorted(mydict.keys(), reverse=True)}

    lista = mydict.items()
    lista_sorted = sorted(lista, key=itemgetter(1), reverse=True)

    lista_final = []

    for i in range(0,7):
        lista_final.append(lista_sorted[i][0] + ": " + \
        str(lista_sorted[i][1]) + " | " + str(round(lista_sorted[i][1] / len(summa) * 100, 1)) + "%")

    print(lista_final)
