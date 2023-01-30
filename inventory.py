#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Inventory functions
"""

def pick(returned_list, item, ind_item=-1):
    """
    Returns an updated inventory based on user picked items
    """
    length_list = len(returned_list)
    x_ind = int(ind_item)
    if x_ind > length_list:
        print(f"Error, {ind_item} är utom räckvidd")
        return returned_list
    if x_ind == -1:
        returned_list.append(item)
        print(f"'{item}' har lagts till")
        return returned_list
    returned_list.insert(x_ind, item)
    print(f"'{item}' har lagts till på plats {x_ind}")
    return returned_list

def inventory(inv):
    """
    Returns inventory
    """
    print(f"Ryggsäcken innehåller {len(inv)} saker: {inv}")

def drop(returned_list, item):
    """
    Drops an item from the list
    """
    if item in returned_list:
        returned_list.remove(item)
        print(f"'{item}'' har tagits bort")
        return returned_list
    print(f"Error, {item} finns inte i ryggsäcken")
    return returned_list

def swap(returned_list, item_one, item_two):
    """
    Swaps the items in the list
    """
    try:
        x_item = returned_list.index(item_one)
        y_item = returned_list.index(item_two)
        if item_one == item_two:
            print(f"Error, {item_one} och {item_two} kunde inte bytas")
            return returned_list
        returned_list[x_item], returned_list[y_item] = returned_list[y_item], returned_list[x_item]
        print(f"Bytte plats på {item_one} och {item_two}")
        return returned_list
    except ValueError:
        print(f"Error, {item_one} eller {item_two} finns inte i ryggsäcken")
        return returned_list

if __name__ == "__main__":
    bag = ["windows","mac","mac","linux"]
    x = "mac"
    y = "mac"
    print(swap(bag, x, y))
