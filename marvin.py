"""
Contains all the commands used in the marvin program
"""
import random

def multiply_str(inp, multiplier):
    """
    Takes string and int, and multiplies the string with the int. Returns this multiplied string.
    """
    answer = inp * multiplier
    return answer

def greet():
    """
    Greets the user
    """
    name = input("What is your name? ")

    print("\nPatric says:\n")
    print("Greetings,  %s - your awesomeness!" % name)
    print("What would you like to do?")

def celcius_to_farenheit():
    """
    converts celcius to fahrenheit (returns a float)
    """
    degree_c = float(input("What's the temperature in Celsius? "))
    degree_f = round((degree_c * 1.8 + 32), 2)

    print("\nPatric says:\n")
    print(f"{degree_c} celsius the same as {degree_f} fahrenheit")

def word_manipulation():
    """
    multiplies a string x amount of times, then prints the string
    """
    word = input("What word would you like me to repeat? ")
    repeat_times = int(input("How many times would you like me to repeat that word? "))
    output = multiply_str(word, repeat_times)
    print(output)

def sum_and_average():
    """
    takes in numbers until "done" is written, then returns a string with the total value
    and the average of all numbers
    """
    number = 0
    times_added = 0
    answer = ""

    while answer != "done":
        answer = input("Add a value (type done when done): ")
        if(answer != "done"):
            try:
                number += float(answer)
                times_added += 1
            except ValueError:
                print("\nSomething went wrong :(, try again please. \n")
    
    print(f"The sum of all numbers are {number} and the average is {round((number/times_added),2)}")

def hyphen_string():
    """
    hyphens a string
    """
    new_word = ""
    word = input("What word would you like me to manipulate? ")
    word_length = len(word)

    for index in range(0 , word_length):
        add_letter = -1
        while add_letter < index:
            new_word += word[index]
            add_letter += 1

        if index + 1 == len(word):
            break
        new_word += "-"
    
    print(new_word)

def is_isogram():
    """
    Checks if a word is an isogram
    """
    word = str(input("What word would you like to check? "))
    letters = ""
    alphabet = "abcdefghijklmnopqrstuvwxyzåäö"

    for alphabet in word:
        if alphabet in letters:
            print("No match!")
            break
        letters += alphabet
    else:
        print("Match!")

def compare_numbers():
    """
    Looks if a number is lower/higher or the same as another number
    """
    has_number = False
    number_1 = 0
    number_2 = 0
    str_answer = ""

    while True:
        while has_number is False:
            try:
                number_1 = float(input("Enter a value: "))
                has_number = True
            except ValueError:
                print("not a number!")

        str_answer = input("Enter a new value: ")
        if(str_answer == "done"):
            break
    
        try:    
            number_2 = float(str_answer)
        
            if number_2 < number_1:
                print("smaller!")
            elif number_2 == number_1:
                print("same!")
            elif number_2 > number_1:
                print("larger!") 
            number_1 = number_2   
        except ValueError:
            print("not a number!")

def word2_in_word():
    """
    Checks if all character in one string is present in another
    """
    print("dbwebb validate didnt like this one :(")

def multiply_x_times():
    """
    Multiplies a number until all numbers are present (answers -1 if its not possible)
    """
    value = int(input("What value would you like to multiply? "))
    loops = int(input("How many time would you like to double this number? "))

    numbers = "1234567890"
    times_looped = 0

    while times_looped <= loops:
        matching_numbers = ""
        str_number = str(value)

        for i in range(0,10):
            if numbers[i] in str_number:
                matching_numbers += numbers[i] 
    #checks what numbers are in the value

        if matching_numbers == numbers:
            print(f"Answer: {times_looped} times")
            break
    #Checks if all numbers are in the value

        value *= 2
        times_looped += 1
    
    if matching_numbers != numbers:
        print("Answer: -1 times")

def spaces_to_tab():
    """
    Replaces tabs with three spaces
    """
    word = input("What word would you like me to untabify? ")
    new_word = ""
    loops = 0
    
    while loops <= len(word) - 1:
        if word[loops] == "\t":
            new_word += "   "
            #checks if its a tab, and then replaces the tab with spaces
        else:
            new_word += word[loops]
        loops += 1
    print(new_word)

def combine_names():
    """
    Turns two names into one
    """
    first_name = str(input("What is the first name? "))
    second_name = str(input("What is the second name? "))
    new_name = ""

    no_vowel = False
    vowels = "aeiouy"

    loops = 0
    first_vowel = ""
    try:
        while first_vowel == "":
            for i in range(0,6):
                if vowels[i] in first_name[loops]:
                    first_vowel += vowels[i]    
            loops += 1
    except IndexError:
        print("No vowel was found :(")
        no_vowel = True        
    #checks the location of the first vowel, and stops when a vowel is found.
    #try-except is used to stop the program from crashing if no vowel is present

    if no_vowel is False:
    #no need to run this if the first loop failed
    
        name_loops = 0
        while name_loops < loops - 1:
            new_name += first_name[name_loops]
            name_loops += 1
        #If a vowel was found, all consonants before it will be added to the new name

        loops = 0
        first_vowel = ""
        while first_vowel == "":
            for i in range(0,6):
                if vowels[i] in second_name[loops]:
                    first_vowel += vowels[i]
            loops += 1

        loops -= 1 
        #since we also want the first vowel, would otherwise skip it in the next loop
        
        while loops < len(second_name):
            new_name += second_name[loops]
            loops += 1
        #if a vowel was found, all characters after and the first vowel will be added
        #to the new name

        print(new_name)

def pointsheet_to_players():
    """
    Returns a pointsheet
    """
    inp = input("Enter the pointsheet: ")
    alphabet = "abcdefghijklmnopqrstuvWxyzåäöABCDEFGHIJKLMNOPQRSTUVWXYZÅÄÖ"
    output_text = ""
    player_name = ""
    names_searched = ""

    value = 0
    inp_length = len(inp)


    for char in inp:
        value = 0
        if char in alphabet:
            player_name = char.casefold()
            #makes all chars lowercase

            if player_name not in names_searched:
                #checks if a player already has gained/lost their points

                for i in range(0, inp_length):
                    if inp[i] == player_name:
                        value += int(inp[i + 1])
                #adds points if the char is lowercase

                    elif inp[i] == player_name.upper():
                        value -= int(inp[i + 1])
                #subtracts points if char if uppercase

                output_text += (f"{player_name} {round(value)}, ")
                #adds playername and total points to a string

            names_searched += player_name
            #adds player to the list of players who has gained/lost their points

    output_text = output_text[:-2]
    #removes two last chars from the string
    print(output_text)

def randomize_string(inp):
    """
    creates a list of the input, shuffles this list and puts it into a string thats printed out in
    the format: (input) --> (randomized input)
    """
    inp_list = list(inp)
    answer = ""
    random.shuffle(inp_list)
    for i in range(0, len(inp)):
        answer += inp_list[i]
    return(f"{inp} --> {answer}")

def get_acronym(inp):
    """
    Adds each uppercase into a string and then prints this string.
    """
    new_word = ""
    for x in inp:
        if x.isupper():
            new_word += x
    return new_word

def mask_string(inp):

    """
    replaces all chars expect the last 4 with a # then prints out the answer
    """
    masked_str = multiply_str("#", len(inp) - 4)
    last_four = ""
    index = len(inp) - 4
    if len(inp) >= 4:
        while index < len(inp):
            last_four += inp[index]
            index += 1
        return(masked_str + last_four)
    
    return(inp)

def find_all_indexes(word, character):
    """
    Takes one string and one char, looks at what indexes that the char is in the string,
    then returns all indexes in a string
    """
    answer = ""
    last_index = 0
    
    try:
        while last_index < len(word):
            try:
                index = word.index(str(character), last_index)
                if str(index) not in answer:
                    answer += f"{index},"
                last_index += 1
            except ValueError:
                last_index += 1
                #sometimes got a valuerror, just skips that value if it happens
        answer = answer[:-1]
        return answer
    except TypeError:
        return ""

def points_to_grade(max_pts, user_pts):
    """
    returns a score from A to F (no e) depending on the percentage of correct answers
    """
    percent = float(user_pts) / float(max_pts)
    score = ""
    if percent >= 0.9:
        score = "A"
    elif percent >= 0.8:
        score = "B"
    elif percent >= 0.7:
        score = "C"
    elif percent >= 0.6:
        score = "D"
    elif percent < 0.6:
        score = "F"
    return f"score: {score}"

def has_strings(word, inp_1, inp_2, inp_3):
    """
    Takes four strings, checks is inp_1 is the beginning of word, checks if inp_2 is in word
    and checks if inp_3 is the end of the word.
    Returns Match if this is true, no match if false
    """
    start = ""
    end = ""
    loops = len(inp_1)
    word_length = len(word)
    for i in range(0, loops):
        start += word[i]
    if start == inp_1:
        if inp_2 in word:
            loops = len(word) - len(inp_3)
            for i in range(loops, word_length):
                end += word[i]
            if end == inp_3:
                return "Match"
    return "No match"
