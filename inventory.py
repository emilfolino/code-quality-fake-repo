#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""This program holds function for creating a list"""

def inventory(lista):
    """function for printing out bag"""
    print("Your bag has " + str(len(lista)) + " items: " + str(lista))


def pick(lista, item, pos = None):
    """function for adding item to list"""
    try:
        if pos is not None and int(pos) > len(lista):
            print("Error the index number " + str(pos) + " is to high.")
            return lista

        if pos is not None:
            lista.insert(int(pos), item)
            print(item + " was added at index " + str(pos) + ".")

        if pos is None:
            lista.insert(len(lista) + 1, item)
            print(item + " was added to your list.")
        return lista

    except(ValueError):
        print("Error something went wrong")
        return lista


def drop(lista, item):
    """this function removes an object"""
    try:
        lista.remove(item)
        print("Removed item from the list was: " + str(item))
        return lista

    except(ValueError):
        if lista == []:
            print("Error, cant find " + str(item))
            return lista

        print("Error, your element " + str(item) + " does not exist")
        return lista

def swap(lista, fItem, sItem):
    """this function swaps two elements"""
    try:
        first = lista.index(fItem)
        second = lista.index(sItem)

        if first == second:
            print("Error, can't swap the same element.")
            return lista

        lista[first], lista[second] = lista[second], lista[first]
        print(str(fItem) + " " + str(sItem) + " has been swaped.")
        return lista

    except(ValueError):

        newList = " ".join(lista)

        if fItem not in newList:
            print("Error your item: " + fItem + "is not in bag")

        if sItem not in newList:
            print("Error your item: " + sItem + "is not in bag")

        return lista
