"""
Functions for inventory commands
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def pick(pack_list, object_1, position=None):
    """
    Takes 3 argument, add objects to a list
    """
    if position is None:
        pack_list.append(object_1)
        print (f"´Marvin added {object_1} to list!")

    else:
        pos= int(position)

        if pos > len(pack_list):
            print(f"Error, index position {pos} is out of range")

        else:
            pack_list.insert(pos, object_1)
            print(f"Marvin added {object_1} to position {pos}")

    return pack_list


def inventory(pack_list):
    """
    Print the number of items in the list (backpack) and what it contains
    """
    print(f"Marvin says: You have {len(pack_list)} items in your \
backpack and it contains: {pack_list}")


def drop(pack_list, object_1):
    """
    Drop an object from the list
    """
    try:
        pack_list.remove(object_1)
        print(f"Marvin dropped {object_1} from the list!")

    except ValueError:
        print (f"Error, {object_1} not in you list!")

    return pack_list


def swap(pack_list, object_1, object_2):
    """
    Swap place of two objects in the list
    """
    if object_1==object_2:
        print("Error, the names are identical")

    else:
        try:
            a = pack_list.index(object_1)
            b = pack_list.index(object_2)

            temp_item = pack_list[a]
            pack_list[a] = pack_list[b]
            pack_list[b] = temp_item

            print(f"{object_1} and {object_2} has swapped places!")

        except ValueError:
            if (object_1 or object_2) not in pack_list:
                print(f"Error, {object_1} and {object_2} not in list!")

            elif object_1 not in pack_list:
                print(f"Error, {object_1}  not in list!")

            elif object_2 not in pack_list:
                print(f"Error, {object_2}  not in list!")


    return pack_list
