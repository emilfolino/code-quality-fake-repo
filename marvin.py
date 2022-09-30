"""
Functions for Log Lady choices
"""

import random

answered = False

def greet():
    """
    Introduce yourself to the log.
    """
    name = input("What is your name? ")
    print("\nThe Log Lady says:\n")
    print("Hello %s." % name)
    print("My name is Margaret. I do not introduce the log.")

def celcius_to_farenheit():
    """
    Convert Celsius to Fahrenheit
    """
    global answered
    print("My log wants to know the temperature in Celsius.")
    degrees_c = input("Enter temperature in °C: ")
    try:
        degrees_c = float(degrees_c)
        degrees_f = degrees_c * 9 / 5 + 32
        degrees_f = round(degrees_f, 2)
        print("My log converted %2f°C to %2f°F." % (degrees_c, degrees_f))
        answered = True
    except ValueError:
        print("My log is upset that you didn't enter a number.")

def word_manipulation():
    """
    Make the log say a word x number of times.
    """
    global answered
    print("What do you want my log to say?")
    word = input("Enter a word: ")
    print("How many times should my log say this word?")
    multiplier = input("Enter a number: ")
    word = multiply_str(word, multiplier)
    if isinstance(word, str):
        print("... Oh. I guess you can't hear it. My log said '%s'." % word)
        answered = True

def sum_and_average():
    """
    Calculate the sum and mean of a set of numbers.
    """
    global answered
    inp = ""
    sum_choice4 = 0
    count = 0
    while inp != "done":
        if count == 0:
            print("My log is asking you to input a number.")
            inp = input("Enter a number: ")
        else: 
            inp = input("Enter another number or type 'done': ")
        if inp == "done":
            break
        else:
            try:
                sum_choice4 += float(inp)
                count += 1
            except ValueError:
                print("That wasn't a number.")
    mean = round(sum_choice4 / count, 2)
    print("My log says the sum of your numbers is %g, and the mean is %g" % (sum_choice4, mean))
    answered = True

def hyphen_string():
    """
    Make the log say your word with increasing number of letters separated by hyphens.
    """
    print("What do you want my log to say slowly?")
    word = input("Enter a word: ")
    slow_word = ""
    i = 0
    while i < len(word):
        if i > 0:
            slow_word += "-"
        slow_char = word[i] * (i + 1)
        slow_word += slow_char
        i += 1
    print("My log said '%s'." % slow_word)

def is_isogram():
    """
    Check if a word is an isogram (contains only each letter once)
    """
    global answered
    print("Oh... you want my log to check if a given word is an isogram?")
    word = input("Enter a word: ")
    isogram = True
    i = 0
    while i < len(word) - 1:
        j = 0
        while j < len(word):
            if i != j and word[i] == word[j]:
                isogram = False
                break
            else:
                j += 1
        if not isogram:
            break
        i += 1
    if isogram:
        print("My log says yes, your word is an isogram. Match!")
    else: 
        print("My log says no, your word is not an isogram. No match!")
    answered = True

def compare_numbers():
    """
    Compare two numbers to each other.
    """
    global answered
    print("My log is asking you for two numbers.")
    inp = ""
    current_num = None
    prev_num = None
    while inp != "done":
        try:
            if not isinstance(prev_num or current_num, float):
                inp = input("Enter your first number: ")
            else:
                if not isinstance(current_num, float):
                    inp = input("Enter a second number: ")
                else:
                    inp = input("Enter another number or type 'done': ")
            if inp == 'done':
                break
            else:
                if isinstance(prev_num, float):
                    current_num = float(inp)
                else:
                    prev_num = float(inp)
                    continue
                if isinstance(current_num and prev_num, float):
                    if current_num > prev_num:
                        print("My log says: Compared to the previous number, this one is larger!")
                        answered = True
                    elif current_num < prev_num:
                        print("My log says: Compared to the previous number, this one is smaller!")
                        answered = True
                    elif current_num == prev_num:     # elif in case there is an unforeseen issue
                        print("My log says: This number and the previous one are the same!")
                        answered = True
                    prev_num = current_num
        except ValueError:
            print("That's not a number!")

def contains_letters():
    """
    Check if the first word contains all the characters in the second.
    """
    print("My log wants to be given two words...")
    print("It wll tell you if the first word contains all the characters of the second word.")
    word1 = input("Enter your first word: ").casefold()
    word2 = input("Enter your second word: ").casefold()
    j = 0
    match = True
    while j < len(word2) and match:
        i = 0
        match = False
        while i < len(word1):
            if word1[i] == word2[j]:
                match = True
                break
            else:
                i += 1
        j += 1
    if match:
        print("My log says yes, word 1 contains all characters from word 2. Match!")
    else: 
        print("My log says no, word 1 does not contain all characters from word 2. No match!")

def multiply():
    """
    Ask how many times a number must be multiplied by two to achieve a product with all digits
    0-9. Asks for a max number of attempts before giving up trying to find a solution.
    """
    global answered
    print("My log wants to multiply a number by 2 until it contains all digits 0-9")
    num = None
    max_attempts = None
    times_multiplied = 0
    DIGITS = "0123456789"
    match = False
    while not isinstance(num, int) and not isinstance(num, float):
        try:
            num = input("Enter a number: ")
            # To take away trailing .0's from floats, and not add unnecessary .0's to ints. 
            if float(num) == int(float(num)):
                num = int(float(num))
            else:
                num = float(num)
        except ValueError:
            print("That's not a number!")
    print("After how many tries should my log stop trying to find a solution?")
    while not isinstance(max_attempts, int):
        try:
            max_attempts = int(input("Enter number of attempts: "))
        except ValueError:
            print("You must enter an integer.")
    while times_multiplied <= max_attempts and not match:
        i = 0
        while i < len(DIGITS):
            if str(num).find(DIGITS[i]) == -1:
                match = False
                break
            elif i == len(DIGITS) - 1:
                match = True
            i += 1
        if not match:
            num *= 2
            times_multiplied += 1
        print(num)
    if not match:
        times_multiplied = -1
    print(("My log says it had to multiply the number %d times"
        " to get the product to contain all digits.") % times_multiplied)
    print("The final product was %s." % str(num))
    answered = True

def tabs_to_3spaces():
    """
    Replaces all tabs with 3 spaces in a string.
    """
    print("My log will change all tabs to 3 spaces in any string.")
    inp = input("Enter a string: ")
    inp = inp.replace("\t", "   ")
    print("My log says:", inp)

def make_portmanteau():
    """
    Take a slice of the first name up to the first vowel. Take a slice of the second
    name including the first vowel onward. Combine the names.
    """
    global answered
    CONSONANTS = "bcdfghjklmnpqrstvwxz"
    VOWELS = "aeiouy"
    name1 = ""
    name2 = ""
    part1 = ""
    part2 = ""
    i = 0
    j = 0
    portmanteau = ""
    print("My log wants you to input two names to combine into a portmanteau.")
    while not name1 or not name2:
        if not name1:
            name1 = input("Enter name 1: ").casefold()
            if not all(char in CONSONANTS + VOWELS for char in name1):
                name1 = ""
                print("The name may only contain letters a-z.")
        else: 
            name2 = input("Enter name 2: ").casefold()
            if not all(char in CONSONANTS + VOWELS for char in name2):
                name2 = ""
                print("The name may only contain letters a-z.")
    for char in name1:
        if char in VOWELS:
            i = name1.find(char)
            part1 = name1[:i]
            break
    for char in name2:
        if char in VOWELS:
            j = name2.find(char)
            part2 = name2[j:]
            break
    portmanteau = part1 + part2
    print("My log combined the names to make '%s.'" % portmanteau)

def count_points():
    """
    User inputs a string of alternating letters and digits. Each digit pair represents a
    player scoring or losing points. A capital letter represents losing that number of
    points and a lower-case letter represents gaining that number of points. Outputs
    a string with the final scoreboard.
    """
    global answered
    print("My log wants to count points.")
    print(("Input a string. The characters must alternate between letters and digits,"
            " starting with a letter. Letters represent players, and the digit after"
            " each letter is the amount of points that player scored. If the letter is"
            " lower case, they score the points. If the letter is upper case,"
            " they lose the points. My log will figure out the total number of points"
            " that each player finishes with."))
    inp = ""
    i = -1
    player = ""
    scoreboard = {}
    points = 0
    polarity = 1
    while i < len(inp):
        if inp == "":
            inp = input("Input a string: ")
            i = 0
        elif i % 2 == 0 and inp[i].isalpha():
            player = inp[i].casefold()
            if inp[i].islower():
                polarity = 1
            else:
                polarity = -1
            i += 1
        elif i % 2 != 0 and inp[i].isdigit():
            points = int(inp[i]) * polarity
            if player in scoreboard:
                scoreboard[player] += points
            else:
                scoreboard[player] = points
            i += 1
        else:
            i = 0
            inp = ""
            print("Your string must contain alternating letters and digits, starting"
                  " with a letter!")
    scoreboard = str(scoreboard).replace(":","").replace("'","").replace("{","").replace("}","")
    print("My log calculated the scoreboard:")
    print(scoreboard)
    answered = True

def randomize_string(string):
    """
    Shuffles the order of characters in a string.
    """
    return (string + " --> " + ''.join(random.sample(string, len(string))))

def get_acronym(string):
    """
    Returns an acronym consisting of the capital letters in a string.
    """
    acronym = ""
    for char in string:
        if char.isupper():
            acronym += char
    return acronym

def multiply_str(string, multiplier):
    """
    Repeats a string the number of times specified by the multiplier (must be an integer).
    """
    try:
        if float(multiplier) == round(float(multiplier)):
            multiplier = int(multiplier)
            return string * multiplier
        print("My log can't repeat a word a non-integer number of times.")
        return None
    except ValueError:
        print("My log is upset that you didn't enter a number.")
        return None

def mask_string(string):
    """
    Replaces all the characters in a string with # except the last four.
    """
    return multiply_str("#", len(string) - 4) + string[len(string) - 4:]

def find_all_indexes(string, substring):
    """
    Finds all instances of the substring withing the string and outputs
    their indices as a string connected by commas.
    """
    global answered
    indices = ""
    start = 0
    searching = True
    while searching: #until search fails
        try:
            i = string.index(substring, start)
            if bool(indices):
                indices += ","
            indices += str(i)
            start = i + 1
        except ValueError:
            searching = False
            continue
    if len(indices) >= 1: #removes final comma
        indices = indices[:len(indices)]
    answered = True
    return indices

def points_to_grade(max_points, your_points):
    """
    Divides your earned points by max points and returns letter grade.
    """
    try:
        pct_grade = float(your_points) / float(max_points)
    except ValueError:
        return "My log is upset that one of your inputs wasn't a number."
    if pct_grade >= 0.9:
        letter_grade = "A"
    elif pct_grade >= 0.8:
        letter_grade = "B"
    elif pct_grade >= 0.7:
        letter_grade = "C"  
    elif pct_grade >= 0.6:
        letter_grade = "D"
    else:
        letter_grade = "F"
    return "score: " + letter_grade

def has_strings(main_str, initial_str, contained_str, end_str):
    """
    Will output "Match" if the main string begins with the second
    argument, contains the third argument, and ends with the fourth
    argument. Otherwise, "No match".
    """
    if main_str.startswith(initial_str) and contained_str in main_str and main_str.endswith(end_str):
        return "Match!"
    return "No match"
