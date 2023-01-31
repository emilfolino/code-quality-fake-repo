"""
code for main.py
"""
import random


def greet():
    """
    greets person
    """
    name = input("What is your name? ")
    print("\nBarvin says:\n")
    print("Hello there, %s, - nice to meet you" % name)
    print("What do you need from me today?!")


def celcius_to_farenheit():
    """
    converts Celsius to fahrenheit
    :return:
    """
    print("Celsius to Fahrenheit it is")
    try:
        cels = float(input("Please enter your value in Celsius: "))
    except ValueError:
        print("Only numbers please")
        return
    fahr = cels * 1.8 + 32
    print(f"{round(cels, 2)} Celsius is {round(fahr, 2)} Fahrenheit")


def word_manipulation():
    """
    returns the word many times
    """
    print("Give me a word and a number and enjoy :)")
    word = input("Enter a word: ")
    number = int(input("Enter a number: "))
    print(multiply_str(word, number))


def sum_and_average():
    """
    calculates the sum and average of numbers
    """
    print('Type as many numbers you like and make me do math with "done" ')
    total = 0
    amnt = 0
    while True:
        num = input("Number ---> ")
        if num == "done":
            break
        else:
            try:
                total = total + float(num)
                amnt = amnt + 1
            except ValueError:
                print("That is not a valid number")
                continue
    print(f"The sum of all numbers is {round(total, 2)} and the average is {round(total / amnt, 2)}")


def hyphen_string():
    """
    returns the word with more letters
    """
    multiwrd = ""
    n = 1
    c = 0
    wrd = input("Give me a word: ")
    for _ in wrd:
        c = c + 1
    for lettr in wrd:
        if n == c:
            multiwrd = multiwrd + (lettr * n)
        else:
            multiwrd = multiwrd + (lettr * n) + "-"
            n = n + 1
    print(multiwrd)


def is_isogram():
    """
    Checks if the word is an isogram
    """
    count = 0
    hml = 0
    isoword = input("Type a word: ")
    for iso in isoword:
        a = iso
        hml = hml + 1
        for isog in isoword:
            b = isog
            if a == b:
                count = count + 1
    if count > hml:
        print("No match! ")
    else:
        print("Match! ")


def compare_numbers():
    """
    compares numbers and tells if its bigger, smaller or same
    """
    try:
        num_one = int(input("First number: "))
    except ValueError:
        print("Please enter a valid number!")
        return
    while True:
        num_two = (input("Number: "))
        if num_two == "done":
            break
        else:
            try:
                num_two = int(num_two)
            except ValueError:
                print("not a number! ")
                continue
            if num_two == num_one:
                print("same!")
            elif num_two > num_one:
                print("larger!")
                num_one = num_two
            elif num_two < num_one:
                print("smaller!")
                num_one = num_two


def check_letters():
    """
    checks for letters in word
    """
    chckwrd = input("Enter a word: ")
    chcklttrs = input("Enter the letters you would like me to search for: ")
    cnt = 0
    chkc = 0
    for c in chcklttrs:
        if c in chckwrd:
            chkc = chkc + 1
        cnt = cnt + 1
    if chkc == cnt:
        print("Match!")
    else:
        print("No match!")


def number_0_to_9():
    """
    calculates the amount of times a number needs to
    be multiplied by 2 to have all numbers 0-9
    """
    check_number = "0123456789"
    count = 0
    tms_multiplied = 0
    first_number = input("What is your number?: ")
    while True:
        try:
            times = int(input("How many times do you want me to try it?: "))
            break
        except ValueError:
            print("Invalid input, enter a number")
    while True:
        if count == 10:
            print(f"Answer: {tms_multiplied} times")
            break
        elif tms_multiplied == times:
            print("Answer: -1 times")
            break
        else:
            count = count - count
            for i in check_number:
                if i in str(first_number):
                    count = count + 1
                else:
                    first_number = int(first_number) * 2
                    tms_multiplied = tms_multiplied + 1
                    break


def tab_to_spaces():
    """
    Converts a tab to 3 spaces
    """
    new_tab_word = ""
    tab_word = input("Enter a word with tabs --> ")
    for i in tab_word:
        if i != "\t":
            new_tab_word = new_tab_word + i
        elif i == "\t":
            new_tab_word = new_tab_word + "   "
    print(new_tab_word)


def name_concatenator():
    """
    concatenates two names
    """
    vlist = ["a", "e", "i", "o", "u", "y"]
    first_name = input("Enter the first name: ")
    first_name2 = ""
    second_name = input("Enter the second name: ")
    second_name2 = ""
    vindex = 0
    v2index = 0
    for letter in first_name:
        if letter not in vlist:
            vindex = vindex + 1
        else:
            first_name2 = first_name[: vindex]
            break
    for letter in second_name:
        if letter not in vlist:
            v2index = v2index + 1
        else:
            second_name2 = second_name[v2index:]
            break
    print(first_name2 + second_name2)


def randomize_string(string):
    """
    Randomizes the letters in a string
    """
    new_string = ""
    prev_string = string
    lenght = len(string)
    i = 0
    while i < lenght:
        for _ in range(0, lenght - len(new_string)):
            randnumber = random.randint(0, lenght - len(new_string) - 1)
            new_string = new_string + string[randnumber]
            i += 1
            string = string[:randnumber] + string[randnumber + 1:]
        new_string = f"{prev_string} --> {new_string}"
    return new_string


def get_acronym(string):
    """
    Prints the acronym of a text
    """
    new_string = ""
    for letter in string:
        if letter.isupper():
            new_string += letter
    return new_string


def mask_string(string):
    """
    Masks part of a string
    """
    length = len(string)
    masker = multiply_str("#", length - 4)
    masked_string = masker
    last_four = string[length - 4:length]
    masked_string += last_four
    return masked_string


def multiply_str(string, integer):
    """
    multiplies two values
    """
    return string * integer


def find_all_indexes(string1, string2):
    """
    Finds the indexes of a string in another string
    """
    findex = ""
    while True:
        try:
            indexofstr = string1.index(string2)
        except ValueError:
            break
        string1 = string1[:indexofstr] + ">" + string1[indexofstr + 1:]
        findex = findex + str(indexofstr) + ","
    findex = findex[:-1]
    return findex


def points_to_grade(maxpoints, points):
    """
    Tells what score you've got
    :param maxpoints:
    :param points:
    :return:
    """
    try:
        procent = int(points) / int(maxpoints)
    except ValueError:
        answer = "Enter points in numbers!"
    else:
        if procent * 100 >= 90:
            score = "A"
        elif procent * 100 >= 80:
            score = "B"
        elif procent * 100 >= 70:
            score = "C"
        elif procent * 100 >= 60:
            score = "D"
        else:
            score = "F"
        answer = f"score: {score}"
    return answer


def has_strings(first, second, third, fourth):
    """
    Checks if a string (first) begins with second,
    has third in it and ends with fourth
    """
    answer = "No match!"
    if first.startswith(second) and third in first and first.endswith(fourth):
        answer = "Match! "
    return answer
