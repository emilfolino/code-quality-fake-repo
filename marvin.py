"""
Marvin with a simple menu to start up with.
Marvin doesnt do anything, just presents a menu with some choices.
You should add functinoality to Marvin.
Its an eternal loop, until q is pressed.
It should check the choice done by the user and call a appropriate
function.
"""

import random

def greet():
    """Menyval 1"""
    name = input("What is your name? ")
    print("\nThe penguin says:\n")
    print("Hello %s! Nice to meet you." % name)
    print("What can I do you for?!")

def celcius_to_farenheit():
    """Menyval 2"""
    cel = input("What Celcius degree would you like to convert to Farenheit? ")
    cel = float(cel)
    fa = round(cel * 9 / 5 + 32,2)
    print(fa)

def word_manipulation():
    """Menyval 3"""
    word = input("Say a word, and I'll repeat it! ")
    repeat = input("How many times shouln I repeat it? ")
    rword = int(repeat) * word
    print(rword)

def sum_and_average():
    """Menyval 4"""
    summa = 0.0
    av = 0.0
    count = 0
    while True:
        tal = input("Say a number! Write 'done' when you are done: ")
        if tal == "done":
            print("The sum of all numbers are " + str(summa) + " and the average is " + str(av))
            break         
        count = count + 1
        summa = round(summa + float(tal), 2)
        av = round(summa / count, 2)

def hyphen_string():
    """Menyval 5"""
    word5 = input("Say a word, come on! ")
    newword = word5[0]
    for i in range(len(word5) - 1): 
        newword = newword + "-" + str(word5[i+1] * (i+2))
    print(newword)

def is_isogram():
    """Menyval 6"""
    match = 0
    word6 = input("Say a word, and I'll tell you if it's an isogram! ")
    for j in range(len(word6)-1): 
        index = word6.find(word6[j],j+1)
        if index > j:
            match = match + 1
    if match >= 1:
        print("No match!")
    else:
        print("Match!")
            
            
def compare_numbers():
    """Menyval 7"""
    oldval = input("Enter a number! ")
    try:
        oldval = int(oldval)
        while True:
            newval = input("Enter a new number and I'll compare! ")
            if newval == "done":
                break
            try:                
                newval = int(newval)
                if newval < oldval:
                    print("smaller!")
                elif oldval == newval:
                    print("same!")
                elif newval > oldval:
                    print("larger!")
                oldval = newval
            except ValueError:
                print("not a number!")
                continue
    except ValueError:
        print("not a number!")


def letter_in_word():
    """Menyval a1"""
    word1 = input("Enter a word! ")
    word2 = input("Enter another word or letters! ")
    word1 = word1.lower()
    word2 = word2.lower()
    for i in word2:
        letter = i
        if letter in word1:
            outp = "Match!"
        else:
            outp = "No match!"
            break
    print(outp)


def something():
    """Menyval a2"""
    tal = input("Skriv ett tal: ")
    maxtak = int(input("Vad vill du ha för maxtak? "))
    go_on = True
    count = 0

    while go_on:  
        if count > maxtak:
            count = -1
            break
        for i in range(10):
            i = str(i)
            if i in tal: 
                go_on = False
            else:
                go_on = True
                tal = 2 * int(tal)
                count = count + 1
                tal = str(tal)
                break
    
    print("Answer: " + str(count) + " times")

def replace_tab():
    """Menyval a3"""
    word_a3 = input("Skriv en mening med tabb mellan orden: ")
    word_a3 = word_a3.replace("\t","   ")
    print(word_a3)


def brangelina():
    """Menyval a4"""
    name1 = input("Skriv det första namnet: ")
    name2 = input("Skriv det andra namnet: ")
    vocals = "aeiouy"

    for letter in name1:
        if letter in vocals:
            pos = name1.find(letter)
            start_name = name1[:pos]
            break

    for letter2 in name2:
        if letter2 in vocals:
            pos = name2.find(letter2)
            end_name = name2[pos:]
            break

    print(start_name + end_name)


def game_sum():
    """Menyval a5"""
    game = input("Skriv in varannan bokstav och varannan siffra: ")
    lower = game.lower()
    scoreboard = ""
    skip = False

    for i in lower:
        if skip:
            skip = False
        elif i in scoreboard:
            skip = True
        else:
            skip = True
            points = 0
            pos = - 1
            for j in lower:
                pos = pos + 1
                if i == j:
                    point = int(lower[pos + 1])
                    if game[pos].islower():
                        points = points + point
                    elif game[pos].isupper():
                        points = points - point
            scoreboard = scoreboard + i + " " + str(points) + ", "
            
    print(scoreboard[:-2])

def randomize_string(word):
    """Menyval 8"""
    new_word = word
    shuffle = ""
    while new_word:
        letter_index = random.randint(0, len(new_word) -1)
        shuffle = shuffle + new_word[letter_index]
        new_word = new_word[0:letter_index]+new_word[letter_index + 1:]

    text = word + " --> " + shuffle
    return text

def get_acronym(sentence):
    """Menyval 9"""
    acronym = ""
    for letter in sentence:
        if letter.isupper():
            acronym += letter
    return acronym

def mask_string(mask):
    """Menyval 10"""
    masking = multiply_str("#", len(mask[:-4]))
    masked_word = masking + mask[-4:]
    return masked_word

def multiply_str(tecken, tal):
    """Hör till menyval 10"""
    multi = int(tal) * tecken
    return multi

def find_all_indexes(long, sub):
    """Menyval 11"""
    return_str = ""
    ind = 0
    try:
        while ind < len(long):
            ind = long.index(sub, ind)
            return_str = return_str + str(ind) + ","
            ind = ind + 1
    except ValueError:
        pass
    
    return return_str[:-1]

def points_to_grade(maxpoints, points):
    """Menyval b1"""
    score = int(points) / int(maxpoints)
    grade = "score: F"
    if score >= 0.9:
        grade = "score: A"
    elif score >= 0.8:
        grade = "score: B"
    elif score >= 0.7:
        grade = "score: C"
    elif score >= 0.6:
        grade = "score: D"
    return grade


def has_strings(compare, start, contain, ends):
    """Menyval b2"""
    match = "No match"
    if compare.startswith(start):
        if contain in compare:
            if compare.endswith(ends):
                match = "Match"
    
    return match
    