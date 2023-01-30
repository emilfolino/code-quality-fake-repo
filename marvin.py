#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Marvin with functions for main"""

import random

marvin_image = r"""
         _                      _______                      _
   _dMMMb._              .adOOOOOOOOOba.              _,dMMMb_
  dP'  ~YMMb            dOOOOOOOOOOOOOOOb            aMMP~  `Yb
  V      ~"Mb          dOOOOOOOOOOOOOOOOOb          dM"~      V
           `Mb.       dOOOOOOOOOOOOOOOOOOOb       ,dM'
            `YMb._   |OOOOOOOOOOOOOOOOOOOOO|   _,dMP'
       __     `YMMM| OP'~"YOOOOOOOOOOOP"~`YO |MMMP'     __
     ,dMMMb.     ~~' OO     `YOOOOOP'     OO `~~     ,dMMMb.
  _,dP~  `YMba_      OOb      `OOO'      dOO      _aMMP'  ~Yb._
 <MMP'     `~YMMa_   YOOo   @  OOO  @   oOOP   _adMP~'      `YMM>
              `YMMMM\`OOOo     OOO     oOOO'/MMMMP'
      ,aa.     `~YMMb `OOOb._,dOOOb._,dOOO'dMMP~'       ,aa.
    ,dMYYMba._         `OOOOOOOOOOOOOOOOO'          _,adMYYMb.
   ,MP'   `YMMba._      OOOOOOOOOOOOOOOOO       _,adMMP'   `YM.
   MP'        ~YMMMba._ YOOOOPVVVVVYOOOOP  _,adMMMMP~       `YM
   YMb           ~YMMMM\`OOOOI`````IOOOOO'/MMMMP~           dMP
    `Mb.           `YMMMb`OOOI,,,,,IOOOO'dMMMP'           ,dM'
      `'                  `OObNNNNNdOO'                   `'
                            `~OOOOO~'   TISSUE
"""



#inv = []


def main():

    """ Docstring"""

    print(chr(27) + "[2J" + chr(27) + "[;H")
    print(marvin_image)
    print("Hi, I'm Bob. And I know all things there is to know.")
    print("So what can I do for you mortal?")
    print("1) Present yourself to Bob.")
    print("2) Convert celcius to farenheit.")
    print("3) Multiply a word.")
    print("4) Get a total value and an average value")
    print("5) Give me a word and I will make it longer in an intresting way")
    print("6) Give me a word and I will check if it is a isogram")
    print("7) Give me a number and I will tell you if it's smaller, equal or bigger")
    print("8) Give me a word and I will shuffle it")
    print("9) Give me some words with capital letters to make them into an acronym")
    print("10) Give me a word and a number and I will mask most of them letters")
    print("11) Give me a many letters and one alone and i will tell you its positions")
    print("12) Find a country or countries")
    print("13) Show the emission change between to seperate dates for a country")
    print("14) Show all relavant data for a country")
    print("old) Old options")
    print("help) Here you can see all the different inv commands")
    print("q) Quit.")
    print("Have a whirle with my new inv commands!")

"""def nothing_added():

    

    no_nothing = "Nothing was added, try again"
    return(no_nothing)
    
def added_inv(choice):

    

    number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '-1', '-2', '-3', '-4', '-5', '-6', '-7', '-8', '-9']
    
    position = "0"
    new_position = ""
    
    
    for char in choice:
        if char in number:
            new_position += char

    for char in choice:
        if char in number:
            position = new_position

    if int(position) > len(inv):
        added = "That is a too high number" 

    else:

        if position in choice:
            new_stuff = choice.replace("inv add", '')
            new_stuff = new_stuff.replace(str(position), "")
            new_stuff = new_stuff.strip(" ")
            position = str(position)
            inv.insert(int(position), new_stuff)
            added = "I have now added: " + new_stuff 

        elif len(inv) == 0:
            new_stuff = choice.replace("inv add", "")
            new_stuff = new_stuff.strip(" ")
            inv.insert(0, new_stuff)
            added = "I have now added: " + new_stuff 

        else:
            new_stuff = choice.replace("inv add", "")
            new_stuff = new_stuff.strip(" ")
            inv.append(new_stuff)
            added = "I have now added: " + new_stuff 

    return(added)
            
def inventory():

    

    constant_inv = "Backpack has " + str(len(inv)) + " " + "items: " + str(inv)
    return(constant_inv)



def inventory_swap(choice):

    

    new_stuff = choice.replace("inv swap", '')
    new_stuff = new_stuff.strip(" ")
    list_of_stuff = []
    if " " in new_stuff:
        list_of_stuff = new_stuff.split()
        item1 = list_of_stuff[0]
        item2 = list_of_stuff[1]

        nothing = False
        none = False
        some = False
        if len(inv) == 0:
            swaped = "There is no such item in the backpack"
        else:
            for items1 in inv:
                if items1 == item1:
                    some = True
            
            for items2 in inv:
                if items2 == item2:
                    none = True

            if some and none:                
                place_in_list1 = inv.index(item1)
                place_in_list2 = inv.index(item2)
                inv[place_in_list1], inv[place_in_list2] = inv[place_in_list2], inv[place_in_list1]
                swaped = "The items have now been swapped" + ":" + str(inv)
            else:
                nothing = True
            
            if nothing:
                swaped = "There is no such item in the backpack"
    else:
        swaped = "You need two items to be able to swap"
    
    return(swaped)

def inventory_drop(choice):

    

    old_stuff = choice.replace("inv drop", "")
    old_stuff = old_stuff.strip(" ")
    something = False
    thing = False
    if len(inv) == 0:
        dropped = "There is no such item in the backpack"
    else:
        for old_item in inv:
            if old_item == old_stuff:
                thing = True      

        if thing:
            dropped = "I have now removed: " + old_stuff
            inv.remove(old_stuff)
        else:
            something = True
                    
                    
        if something:
            dropped = "There is no such item in the backpack"

    return(dropped)"""

def help_inv():

    """ Docstring"""

    print("Here you can see all the inventory commands")
    print("The commands you see in here only works in the main menu \n")
    print("To see your backpack, just enter (inv) in the main menu \n")
    print("To add something to your backpack, enter (inv add) and the item you want to add \n")
    print("To add something in a specific position in you backpack, enter (inv add) and the iem you want to add,")
    print("and also the position you want it to be in \n")
    print("To swap two items position in the backpack, enter (inv swap) and the two items you want to swap \n")
    print("To remove something from your backpack, enter (inv drop) and the item you want to remove \n")
    end = True
    while end:
        leave = input("Type done when you want to return to the main menu: ")
        if leave == "done":
            end = False
        else:
            input("That is not a valid command")

def greet():

    """ Docstring"""

    name = input("So what shall I call you, creature of lesser knowledge? ")
    print("Bob says:\n")
    print("Grettings %s - you of limited existence!" % name)
    print("So what can I do for you mortal?!")

def celcius_to_farenheit():

    """ Docstring"""

    celcius = input("How hot in celcius is it? ")
    farenheit = float(celcius) * 9 / 5 + 32
    temp_con = str(farenheit)
    
    print(temp_con)


def multiply_str (word_multi, num_mult):
    
    """Doctring"""
    new_string = word_multi * int(num_mult)
    

    return(new_string)
    
        
    
def word_manipulation():
    
    """ Docstring"""

    singelword = input("Please write a word you want to multiply: ")
    sing_num = input("Please write your multiplier: ")

    new_str = multiply_str(singelword, sing_num)
    
    print(new_str)

def sum_and_average():

    """ Docstring"""

    average = -1
    end = True
    totalsum = 0
    while end:
        newnumber = input("Write a number you want to add: ")
        average += 1
        if newnumber == "done":
            end = False
            ave_total1 = "This is your total value" + " " + str(round(totalsum, 2)) 
            ave_total2 = "\nAnd this is your average" + " " + str(round(totalsum / average, 2))
            ave_total = ave_total1 + ave_total2
        else:
            totalsum = totalsum + float(newnumber)
            end = True

    print(ave_total)
    
def compare_numbers():

    """ Docstring"""

    oldnumber = 10000000000000000000000000000000000000000000000000000.0
    currentnumber = 0.0
    while True:
        try:
            newnumber = input("Write a number you want to test: ")
            if newnumber == "done":
                break
            currentnumber = float(newnumber)
            if oldnumber < 10000000000000000000000000000000000000000000000000000.0:
                
                if oldnumber > currentnumber:
                    oldnumber = currentnumber
                    print("smaller")
                elif oldnumber == currentnumber:
                    oldnumber = currentnumber
                    print("same!")
                else:
                    oldnumber = currentnumber
                    print("larger!")
            oldnumber = currentnumber
        except ValueError:
            print("not a number!")

    
    
def hyphen_string():

    """ Docstring"""

    letter = ""
    longword = ""
    i = 1
    ii = 1
    a = "-"
    longerword = input("Write a word you want to make longer: ")
    if longerword == "":
        print(longerword, "Please try again")
    else:
        for letter in longerword:
            longword = longword + i * letter + ii * a
            i += 1
        if longerword.count(letter) == longerword.count(letter):
            longword = longword[:-1]
            print(longword)
            i = 1
            ii = 1
            longword = ""



def is_isogram():

    """ Docstring"""

    yesno = False
    letter = ""
    isogramword = input("Write a word to check: ")
    if isogramword == "":
        print(isogramword, "Please try again")
    else:
        isogramword = isogramword.lower()
        for letter in isogramword:
            if isogramword.count(letter) > 1:
                yesno = False
            elif isogramword.count(letter) < 2:
                yesno = True
        if isogramword.count(letter) == isogramword.count(letter):
            if yesno:
                print("Match!")
            else:
                print("No match!")

def randomize_string(r_s):

    """ Docstring"""
    final_shu = ""
    shu_list = list(r_s)
    random.shuffle(shu_list)
    final_shu = "".join(shu_list)
    return(r_s, "-->", final_shu)

def anagram(ana_word):

    """ Docstring"""

    ana_list = []
    
    
    if ana_word == "":
        print(ana_word, "Please try again")
    else:
        ana_list = ana_word.split()
        word1 = ana_list[0]
        word2 = ana_list[1]

        word1_low = word1.lower()
        word2_low = word2.lower()
        if(sorted(word1_low) == sorted(word2_low)):
            match_nomatch = "Match"
        else:
            match_nomatch = "No match"
    return(match_nomatch)

def get_acronym(acro_word):

    """ Docstring"""

    
    
    if acro_word == "":
        print(acro_word, "Please try again")
    else:
        acro_list = list(acro_word)
        acro_list2 = list(filter(str.isupper, acro_list))
        final_acro = "".join(acro_list2)
    return(final_acro)

def above_10(num):
                                
    """ Docstring"""

    num1 = 0

    if(int(num) > 10):
        num1 = num
    return(num1)

def filter_list():

    """ Docstring"""

    end = True
    while end:
        fil_word = input("Write some numbers and I will filter out 10 and anything below: ")
        
        if fil_word == "":
            print(fil_word, "Please try again")
        elif fil_word == "done":
            end = False
        else:
            fil_list = fil_word.split()
            fil_list2 = list(filter(above_10, fil_list))
            print(fil_list2)

def mask_string(str_mask):

    """Docstring"""
    new_mask_str_last = ""
    mask_str_mult = str_mask.split()
    str_mask = mask_str_mult[0]
    mask_multi = mask_str_mult[1]
        
    
    if str_mask == "":
        print(str_mask, "Please try again")

    else:
        new_str_mask = multiply_str(str_mask,mask_multi)
        str_mask_last2 = new_str_mask[:-4]
        str_mask_last = new_str_mask[-4:]
        for letter in str_mask_last2:
            new_mask_str = letter.replace(letter, "#")
            new_mask_str_last = new_mask_str_last + new_mask_str
            
    return(new_mask_str_last + str_mask_last)
            
def find_all_indexes(find_index):
    
    """Docstring""" 
    end = True
    last_list_index = ""
    index_list = []
    new_list_index = ""
    while end:
        
        if find_index == "":
            print(find_index, "Please try again")
        elif find_index == "done":
            end = False
        else:
            first_index_list = find_index.split()
            index_string1 = first_index_list[0]
            index_string2 = first_index_list[1]
            


                        
            curr_index = len(index_string2)
            a = 0
            b = curr_index
            list_length = len(index_string1) + 1 - curr_index
            letter = ""
            
            for letter in range(list_length):
                letter = letter + 1
                if a == 0:
                    new_list_index = index_string1[a:b]
                    last_list_index = last_list_index + new_list_index
                    a += 1
                    b += 1
                else:
                    new_list_index = index_string1[a:b]
                    last_list_index = last_list_index + "," + new_list_index
                    a += 1
                    b += 1
            index_list = last_list_index.split(",")
        return(extra_find_index(index_list, index_string2))

    index_list = []    
    index_string1 = ""
            
            
            
        
        
def extra_find_index(index_list, index_string2):
    
    """Docstring"""
    new_index = 0
    list_of_index = 0
    last_index_string2 = ""
    last_index_string = ""
    index2 = True
    try:
        while index2:
                        
            if len(index_list) == new_index + 1:
                if index_string2 not in index_list[new_index:]:
                    last_index_string2 = last_index_string[1:]
                    index2 = False
                else:
                    list_of_index = index_list.index(index_string2, new_index)
                    last_index_string = last_index_string + "," + str(list_of_index)
                    last_index_string2 = last_index_string[1:]
                break
            elif list_of_index == new_index:
                list_of_index = index_list.index(index_string2, new_index)
                if index_string2 not in index_list[0] and new_index == 0:
                    new_index += 1
                else:
                    new_index += 1
                    last_index_string = last_index_string + "," + str(list_of_index)
                    last_index_string2 = last_index_string[1:]
            else:
                if index_string2 not in index_list[new_index:]:
                    last_index_string2 = last_index_string[1:]
                    index2 = False
                else:
                    list_of_index = index_list.index(index_string2, new_index)
                    new_index = list_of_index
        return(last_index_string2)               
    except ValueError as error:
        error = ""
        return(error)
    else:
        while index2:            
            if len(index_list) == new_index + 1:
                if index_string2 not in index_list[new_index:]:
                    last_index_string2 = last_index_string[1:]
                    index2 = False
                else:
                    list_of_index = index_list.index(index_string2, new_index)
                    last_index_string = last_index_string + "," + str(list_of_index)
                    last_index_string2 = last_index_string[1:]
                break
            elif list_of_index == new_index:
                list_of_index = index_list.index(index_string2, new_index)
                if index_string2 not in index_list[0] and new_index == 0:
                    new_index += 1
                else:
                    new_index += 1
                    last_index_string = last_index_string + "," + str(list_of_index)
                    last_index_string2 = last_index_string[1:]
            else:
                if index_string2 not in index_list[new_index:]:
                    last_index_string2 = last_index_string[1:]
                    index2 = False
                else:
                    list_of_index = index_list.index(index_string2, new_index)
                    new_index = list_of_index
        return(last_index_string2)
if __name__ == "__main__":
    main()
