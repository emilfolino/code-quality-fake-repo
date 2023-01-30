#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Inventory functions"""





def pick(backpack, item, index = None):
    """Picks up an item"""
    if index is None:
        backpack.append(item)
        print(f"{item} added at the end of the list")
    else:
        try:
            if int(index) <= len(backpack) and int(index) >= 0:
                backpack.insert(int(index), item)
                print(f"{item} added at [{index}]")
            else:
                print(f"Error: index[{index}] is out of bounds")
        except ValueError:
            print("Error: index must be integer")
    return backpack

def swap(backpack, item1, item2):
    """Swaps 2 items if they exist"""
    if item1 != item2:
        index1 = -1
        index2 = -1
        try:
            index1 = backpack.index(item1)
        except ValueError:
            print(f"Error: {item1} is not in the backpack")
        try:
            index2 = backpack.index(item2)
        except ValueError:
            print(f"Error: {item2} is not in the backpack")
        if index1 != -1 and index2 != -1:
            temp = backpack[index1]
            backpack[index1] = backpack[index2]
            backpack[index2] = temp
            print(f"{item1} [{index1}] was swapped with {item2} [{index2}]")
    else:
        print("Error: you cant swap the same values")
    return backpack

def drop(backpack, item):
    """Removes 1 item from the list"""
    try:
        backpack.remove(item)
        print(f"{item} was removed from the backpack")
    except ValueError:
        print(f"Error: {item} is not in the backpack")
    return backpack



def handle_pick(backpack, args):
    """Handles the pick command. Pass argument list"""
    if len(args) == 2:
        backpack = pick(backpack, args[0], int(args[1]))
    elif len(args) == 1:
        backpack = pick(backpack, args[0])
    else:
        print("Error: Invalid pick arguments(inv pick [item] [index=default])")
    return backpack

def handle_swap(backpack, args):
    """Handles the swap function"""
    if len(args) == 2:
        backpack = swap(backpack, args[0], args[1])
    else:
        print("Error: Invalid swap arguments (inv swap [item1] [item2]")
    return backpack

def handle_drop(backpack, args):
    """Handels the drop function"""
    if len(args) == 1:
        backpack = drop(backpack, args[0])
    else:
        print("Error: Invalid drop arguments (inv drop [item]")
    return backpack


def inventory(backpack, start = None, stop = None):
    """Print list"""
    if not start is None and not stop is None:
        try:
            print("Number of items => " + str(len(backpack)))
            print("[", end="")
            print(*backpack[int(start) : int(stop)], sep=", ", end="")
            print("]")
        except ValueError:
            print("Error: index not valid")
    else:
        print("Number of items => " + str(len(backpack)))
        print("[", end="")
        print(*backpack, sep=", ", end="")
        print("]")

def parse_command(backpack, string_command):
    """Parses and rediricts command"""
    command_list = string_command.split()
    if(string_command == "inv"):
        inventory(backpack)
    elif len(command_list) > 1:
        args = command_list[2:]
        if command_list[1] == "pick":
            backpack = handle_pick(backpack, args)
        elif command_list[1] == "swap":
            backpack = handle_swap(backpack, args)
        elif command_list[1] == "drop":
            backpack = handle_drop(backpack, args)
        elif command_list[1].isnumeric() and command_list[2].isnumeric():
            inventory(backpack, int(command_list[1]), int(command_list[2]))
    else:
        print("Error: Not a valid command")
    return backpack
