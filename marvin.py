"""
Marvin with a simple menu to start up with.
Marvin doesnt do anything, just presents a menu with some choices.
You should add functinoality to Marvin.
"""

import random
import emission_functions

def data_function(country):
    """ Middlefunction for country data"""
    try:
        print(emission_functions.print_country_data(emission_functions.get_country_data(country)))
    except ValueError:
        print("Something went wrong!")

def change_function(country, year1, year2):
    """ Middlefunction for change country """
    try:
        print(country + ":" + str(emission_functions.get_country_change_for_years(country, year1, year2)) + "%")
    except ValueError as e:
        print(e)

def search_function(search_word):
    """ Middlefunction for search country """
    try:
        emission_functions.search_country(search_word)
    except ValueError as e:
        print(e)

def greet():
    """ A function saying hello."""
    name = input("What is your name? ")
    print("\nMarvin says:\n")
    print("Hello %s - your awesomeness!" % name)
    print("What can I do you for?!")

def celcius_to_farenheit():
    """ Celcius to farenheit converter"""
    temp = input("What is the real temperature in celcius? I will convert it for you...")
    farenheit_temp = float(temp) / 5 * 9 + 32
    print("The temperature in farenheit is: " + str(round(farenheit_temp, 2)))

def word_manipulation():
    """ Word manipulation function"""
    parrot = input("What word do you want me to boost your ego with? ")
    parrot_amount = input("How many times should I boost your ego? ")
    print(multiply_str(parrot, int(parrot_amount)))  

def sum_and_average():
    """ A function counting sum an average"""
    total = 0
    status = "active"
    total_count = 0

    while(status == "active"):
        number_input = input("Give me a number please: ")
        if(number_input == "done"):
            status = "done"
        else:
            total += float(number_input)
            total_count += 1
    average = float(total) / float(total_count)
    print("The sum of all numbers are " + str(round(total, 2)) + " and the average is " + str(round(average, 2)))    

def hyphen_string():
    """ A function repeating letters of a word"""
    word = input("Give me a word and I'll repeat the letters for you: ")
    word_max = 1
    final_word = ""

    for letter in word:
        for _ in range(0, word_max):
            final_word += letter

        final_word += "-"
        word_max += 1

    print(final_word[:-1])    

def is_isogram():
    """ An function checking if word is an isogram"""
    isogram = input("Give me a word, I'll see if it's an isogram: ")
    empty_string = ""
    status = "Match!"
    for letter in isogram:
        if(letter in empty_string):
            status = "No match!"
        empty_string += letter

    print(status)    

def compare_numbers():
    """ A function comparing numbers"""
    compare = input("Give me a number and I'll compare it for you: ")
    status = "active"
    while(status == "active"):     
        compare_next = input("Now, give me one more number: ")
        try:
            if compare_next == "done":
                status = "done"
                print("Thank you for letting me help you!")
            elif int(compare_next) > int(compare):
                print("larger!")
            elif int(compare_next) < int(compare):
                print("smaller!")
            elif int(compare_next) == int(compare): 
                print("same!") 
            compare = compare_next
        except ValueError:
            print("not a number!")

def word_exist():
    """ Function checking if letters exist in word"""
    first_check = input("Give me a word: ")
    second_check = input("Now, give me some letters: ")
    counter = 0
    for letter in second_check:
        if letter.lower() in first_check.lower():
            counter += 1
    if counter == len(second_check):
        print("Match!")   
    else:
        print("No match!")         

def multiply_number():
    """ A function multiplying number"""
    target_number = input("Give me a number you want me to check: ")
    target_tries = input("How many times to you want me to multiply it?: ")
    target_number_int = int(target_number)
    counter = 10

    for i in range(0, int(float(target_tries))):
        counter = 0
        for x in range(10):
            if str(x) in str(target_number_int):
                counter += 1

        if counter == 10:
            print("Answer: " + str(i) + " times")
            break

        target_number_int = target_number_int * 2

    if counter != 10:
        print("Answer: -1 times")     

def tab_converter():
    """ A function converting tabs in string"""
    tab_string = input("Give me a word including tab: ")
    new_string = ""

    for letter in tab_string:
        if letter != "\t":
            new_string += letter
        else:
            new_string += "   "

    print(new_string)

def consunants_vowels():
    """ A function making a mixed name"""
    first = input("Give me a name: ")
    second = input("Give me the second name: ")
    vocals = "aeiouy"

    first_newname = ""
    second_newname = ""

    for letter in first:
        if letter not in vocals:
            first_newname += letter
        else:
            break

    count = 0
    for letter in second:            
        if letter in vocals:
            second_newname = second[count:]
            break
        else:
            count += 1

    print(first_newname + second_newname)

def score_line():
    """ A function defining a score-line"""
    player_score = input("Give me the score-line (e.g x2y4x5s3Y1): ")

    player_string = ""
    final_score = ""
    current_player = ""

    #Skapar en lista för spelarna, 1 spelare = 1 liten bokstav
    for letter in player_score:
        if letter.isdigit() is False and letter.lower() not in player_string:
            player_string += letter.lower()     

    for player in player_string:
        current_player = ""
        math_score = 0    
        for letter in player_score:

            if(letter.islower() and letter.lower() == player):
                current_player = letter
            if(letter.isupper() and letter.lower() == player):
                current_player = letter    
            if(letter.isdigit() and current_player.islower() and current_player.lower() == player):
                math_score += int(letter)
                current_player = ""
            if(letter.isdigit() and current_player.isupper()):
                math_score -= int(letter) 
                current_player = ""
        final_score += "" + player + " " + str(math_score) + ", "

    print(final_score[:-2])          

def randomize_string(string):
    """Randomizes a string"""
    final_string = ""

    final_string = "".join(random.sample(string, len(string)))
    
    return string + " --> " + final_string

def get_acronym(string):
    """Gets an acronym of string"""
    final_string = ""
    next_param = True

    for letter in string:
        if letter.isupper() and next_param:
            final_string += letter
        else:
            next_param = False  

        if letter == " ":
            next_param = True

    return final_string

def multiply_str(string, number):
    """Multiplies string by number"""
    return (string * number)

def mask_string(string):
    """Masks a string"""
    final_string = ""

    mask = multiply_str("#", (len(string) - 4))
    final_string += mask

    mask_count = 0
    for letter in string:
        mask_count += 1
        if(mask_count > (len(string) - 4)):
            final_string += letter

    return final_string

def find_all_indexes(string, partstring):
    """Finds all indexes of partstring in string"""
    final_string = ""
    running = True
    start_index = 0
    while(running):
        
        try:
            final_string += "" + str(string.index(partstring, start_index)) + ","
            start_index = string.index(partstring, start_index) + 1
        except ValueError:
            running = False
        

    return final_string[:-1]

def points_to_grade(maxpoints, mypoints):
    """Converts points of text to grade"""
    grade = ""

    if(int(mypoints) / int(maxpoints) >= 0.9):
        grade = "score: A"
    elif(int(mypoints) / int(maxpoints) >= 0.8):
        grade = "score: B"
    elif(int(mypoints) / int(maxpoints) >= 0.7):
        grade = "score: C"
    elif(int(mypoints) / int(maxpoints) >= 0.6):
        grade = "score: D"
    elif(int(mypoints) / int(maxpoints) < 0.6):
        grade = "score: F"

    return grade
