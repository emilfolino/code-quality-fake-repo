"""
Functions for Marvin
"""

import random

def greet():
    """
    1. Greets the user.
    """
    name = input("What is your name? ")
    print("\nMarvin says:\n")
    print(f"Hello magnificent {name} - you just made my day a bit better!")
    print("My name is Marvin. What can I help you with today?")

def celcius_to_farenheit():
    """
    2. Converts temperature
    """
    print("Time for some temperature conversion.")
    print("Enter the temperature in Celsius and let me convert it into Fahrenheit: ")
    try:
        celsius = float(input("--> "))
        farhenheit = round(celsius * 9 / 5 + 32, 2)
        print(f"{celsius} degrees Celsius is {farhenheit} degrees Fahrenheit.")
    except ValueError:
        print("You did not enter a temperature, try again.")

def word_manipulation():
    """
    3. Multiply words by a number
    """
    print("Let us make some crazy words!")
    print("Write a word and then how many times you want to see it: ")
    word_input = str(input("The word --> "))
    multi_input = int(input("How many times --> "))
    print(f"{multiply_str(word_input, multi_input)}")



def sum_and_average():
    """
    4. Calculates sum and average
    """
    print("Calculate the average and the total sum of the numbers you enter!") 
    input_sum = input("Enter a number: ")
    counter = 0
    total_sum = 0
    while input_sum != "done":
        total_sum += float(input_sum)
        counter += 1
        input_sum = input("Enter a number or write 'done' to get the total and average: ")
    average_sum = round(total_sum/counter, 2)
    print(f"The sum of all numbers are {total_sum} and the average is {average_sum}")

def hyphen_string():
    """
    5. Hyphen string
    """
    print("Enter a word and see the magic get to work.")
    word = input("--> ")
    word_length = len(word)
    new_word = ""
    new_word_cut = ""
    i = 0
    while i < word_length:
        for letter in word:
            i += 1
            new_word += letter * i + "-"
            new_word_cut = new_word[:-1]
    print(new_word_cut)

def is_isogram():
    """
    6. Is the word an isogram?
    """
    print("Is your word a so called isogram?")
    word = input("Enter a word: ")
    new_word = ""
    new_word_pos = 0
    new_word_count = 0
    for letter in word:
        new_word = letter
        new_word_pos += 1
        # utgår från bokstaven och ser om den upprepas
        if new_word in word[new_word_pos:]:
            new_word_count += 1 # antal bokstäver som upprepas
        else:
            continue
    if new_word_count > 0: # om minst 1 bokstav upprepas ej ett isogram
        print("No match!")
    else:
        print("Match!")

def compare_numbers():
    """
    7. Compares numbers
    """
    print("Let us compare some numbers!")
    first_input = input("Enter a number: ")
    second_input = ...
    while first_input != "done":
        second_input = input("Enter another number or write 'done' to exit: ")
        try:
            if second_input == "done":
                first_input = "done"
            elif int(first_input) > int(second_input):
                print("smaller!")
                first_input = second_input
            elif int(first_input) < int(second_input):
                print("larger!")
                first_input = second_input
            elif int(first_input) == int(second_input):
                print("same!")
                first_input = second_input
        except ValueError:
            print("not a number!")

def randomize_string(inp):
    """
    8. Randomize a string.
    """
    listStr = []
    newStr = ""
    for letter in inp:
        listStr += letter
    random.shuffle(listStr)
    for letter in listStr:
        newStr += letter
    return f"{inp} --> {newStr}"

def get_acronym(inp):
    """
    9. Makes an acronym from a string.
    """
    acronym = ""
    for letter in inp:
        if letter.isupper():
            acronym += letter
        else:
            continue
    return f"{acronym}"

def mask_string(inp):
    """
    10. Joins mask_string and multiply_str to create a masked string.
    """
    newStr = inp[len(inp)-4:]
    pos = len(inp) - 4
    posStr = multiply_str("#", pos)
    return f"{posStr}{newStr}"

def multiply_str(a, b):
    """
    Returns string a multiplied by b
    """
    return a * b

def find_all_indexes(inpA, inpB):
    """
    11. Finds all indexes inpB in inpA
    """
    #inpA = str(input("Första sträng: "))
    #inpB = str(input("Andra sträng: "))
    i = 0
    j = 0
    count = ""

    try:
        j = inpA.index(inpB)
        i += 1
        count += str(j) + ","
        for _ in range(len(inpA)):
            try:
                if j != inpA.index(inpB, i+1):
                    j = inpA.index(inpB, i+1)
                    count += str(j) + ","
                    i += 1
                    #print(count)
                else:
                    i += 1
                    continue

            except ValueError:
                continue
    except ValueError:
        count = ""

    count = count.rstrip(",")

    return count





def a1_contain():
    """
    A1. Checks if characters exists in a word.
    """
    print("Let us see if a word is containing the specified characters!")
    a = input("Enter a word: ")
    b = input("Enter some characters: ")
    new_letter = ""
    a_small = a.lower()
    b_small = b.lower() #göra alla tecken samma storlek innan vi kollar mot varandra
    for letter in b_small: #för varje bokstav i "b_small" som finns i "a_small"
        if letter not in a_small:
            new_letter = "No match!"
            break
        else:
            new_letter = "Match!"
            a_small = a_small.replace(letter,"") #tar bort använda bokstäver
    print(new_letter)

def a2_number():
    """
    A2. Tries to multiply a number X times.
    """
    input_number = int(input("Enter a starting number: "))
    input_times = int(input("How many times should we try?: "))
    a = 0
    #b = 0
    c = ""
    counter_total = 0
    counter_test = 0
    #final = ""
    counter_final = 0
    counter_check = True

    while counter_check:
    
        if counter_total == input_times:
            counter_final = -1
            counter_check: False
            break
            
        for _ in range(input_times):
            a = input_number * 2
            input_number = a
            c = str(input_number)
            counter_total += 1

            for i in range(10):

                if str(i) in c:
                    counter_test += 1

                    if counter_test == 10:
                        counter_final = counter_total
                        counter_check = False
                        continue

                else:
                    counter_test = 0
                    break

    if counter_final == 1:
        counter_final = 0
    print("Answer:", counter_final, "times")

def a3_frenzy():
    """
    A3. Removes any tabs in a phrase.
    """
    print("Tab-frenzy!")
    tab_input = input("Enter a phrase with some tab in between the words: ")
    new_output = ""
    for letter in tab_input:
        if letter == "\t":
            letter = "   "
            new_output += letter
        else:
            new_output += letter
    print(new_output)

def a4_crazy():
    """
    A4. Combine names.
    """
    print("Let us make some crazy names!")
    input_namn1 = input("Enter a name: ")
    input_namn2 = input("Enter a second name: ")
    vokaler = "a, e, i, o, u, y"
    new_name1 = ""
    new_name2 = ""
    for letter in input_namn1: # kollar efter första vokalen eller lägger till nytt ord
        if letter not in vokaler:
            new_name1 += letter
        else:
            break
    for letter in input_namn2: # kollar efter första vokalen och bryter när den är hittad
        if letter in vokaler:
            break
        else:
            new_name2 += letter
    new_name2 = input_namn2
    try:
        if new_name1[-1] == new_name2[0]: # om samma konsonant upprepas så tas en bort (för att lösa uppgiften).
            new_name2 = new_name2[1:]
        print(new_name1 + new_name2)
    except IndexError:
        print(new_name1 + new_name2)


def points_to_grade(inpC, inpD):
    """
    B1. Points to grades.
    """
    #input1 = input("Maxpoäng: ")
    #input2 = input("Din poäng: ")

    procent = int(inpD) / int(inpC)
    score = ""

    # print(procent)

    if procent >= 0.9:
        score = "A"
    elif procent >= 0.8:
        score = "B"
    elif procent >= 0.7:
        score = "C"
    elif procent >= 0.6:
        score = "D"
    elif procent < 0.6:
        score ="F"
    
    return f"score: {score}"
        