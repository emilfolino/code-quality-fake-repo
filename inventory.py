#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Funktioner för inventory
"""

def inventory(p_backpack):
    """
    Skriver ut innehåller i ryggsäcken
    """
    print("The backpack has: " + str(len(p_backpack)) + " items")

    print(p_backpack)

    for i, item in enumerate(p_backpack):
        print("{}. {}".format(i + 1, item))

def pick(p_backpack, p_pick, p_index=-1):
    """
    Lägger till något i ryggäscken
    """

    if p_index == -1:
        p_index = len(p_backpack)

    if len(p_backpack) >= int(p_index):
        try:
            p_backpack.insert(int(p_index), p_pick)
            print(p_pick + "was added on index" + str(p_index))
        except ValueError:
            print("Error")
    else:
        print("Error: Index " + str(p_index) + " is not valid")

    return p_backpack

def drop(p_backpack, p_drop):
    """
    Tar bort något från ryggsäcken
    """
    try:
        p_backpack.remove(p_drop)
        print(p_drop + " was dropped")
    except ValueError:
        print("Error: " + p_drop + " is not in the list")
    return p_backpack


def swap(p_backpack, p_swap1, p_swap2):
    """
    Ge Marvin möjligheten att kunna byta plats på två stycken saker.
    """
    try:
        indexChange1 = p_backpack.index(p_swap1)
        localTemp = p_backpack[indexChange1]

        try:
            indexChange2 = p_backpack.index(p_swap2)
            p_backpack[indexChange1] = p_backpack[indexChange2]
            p_backpack[indexChange2] = localTemp
            print(p_swap1 + " and " + p_swap2 + " change positions in the list")

        except ValueError:
            print("Error: " + p_swap2 + " not found in the list")

    except ValueError:
        print("Error: " + p_swap1 + " not found in the list")

        try:
            indexChange2 = p_backpack.index(p_swap2)

        except ValueError:
            print("Error: " + p_swap2 + " not found in the list")

    return p_backpack
