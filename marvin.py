"""
This is marvin the chatbot!
"""
import random

def greet ():
    """
    Greets you
    """
    name = input("What is your name? ")
    print("\nMarvin says:\n")
    print("Hi %s, you look great today!" % name)
    print("What can I do you for?!")

def celcius_to_farenheit():
    """
    converts celcius to farenheit
    """
    Celsius = input("This is a temperature converter! Please type in a temperature in Celsius\n")
    Fahrenheit = float(Celsius) * 9 /5 + 32
    print(str(Celsius) + " Celsius is " + str(round(Fahrenheit,2)) + " Fahrenheit!")
    
def word_manipulation():
    """
    multiplies words
    """
    print("Here you can type a word and multiply it!")
    word = input("Please type a word:\n")
    number = input("Please type a number:\n")
    manipulated_word = multiply_str(word,number)
    print("Here is your multiplied word!\n" + manipulated_word)

def sum_and_average():
    """
    sums numbers and gives you the total
    """
    print("Here you can add numbers together and get the sum and average of it!")
    total_number = 0
    numbers_used = 0
    while True:
        try:
            number_output = input("Please type a number or type done:\n")
            if number_output == "done":
                print("The total number was: " + str(round(total_number, 2)) + " And the "
                "average was: " + str(round(total_number/numbers_used, 2)))
                break
            else:
                total_number += float(number_output)
                numbers_used += float(1)
        except ValueError:
            print ("You wrote: " + str(number_output) + "\nWhich is no a number or done")
        except ZeroDivisionError:
            if number_output == "done":
                break

def hyphen_string():
    """
    enhances words 
    """
    print("Here you can type any word and I shall 'enhance' it!")
    enhanced_word = input("Please type a word:\n")
    length = len(enhanced_word)
    index = 0
    word_multiplier = 1
    new_enhanced_word = ""
    while index < length:
        letter = enhanced_word[index]
        if index != 0:
            letter *= word_multiplier
        if index == length -1:
            new_enhanced_word += letter
        else:
            new_enhanced_word += letter + "-"
        index += 1
        word_multiplier +=1
    print(new_enhanced_word)
    
def is_isogram():  
    """
    checks if word is a isogram
    """
    print("Welcome to the isogram checker!")
    isogram_word = input("Type a word:\n")
    isogram_list: list = []

    x = 1
    y = 0

    isogram_list += isogram_word
    isogram_list.sort()

    try:
        while isogram_list[y] != isogram_list[x]:
            x += 1
            y += 1
        print(str(isogram_word) + " No match!")
    except IndexError:
        print(str(isogram_word) + " Match!")  

def compare_numbers():
    """
    compares numbers 
    """
    print("Aha you want to know which number is the biggest, smallest"
    " or the same? type in two numbers at the start!")
    number_list: list = []
    number_save_1 = 0
    number_save_2 = 1
    input_count = 0

    while True:

        number_input = input("Type in a number or done\n")

        if number_input == "done":
            break
        try:
            number_list.append(int(number_input))                   
            input_count += 1

            if input_count == 2:
                if int(number_list[number_save_1]) == int(number_list[number_save_2]):
                    print("same!")
                    input_count = 1
                    number_list.pop(0)
            
                elif int(number_list[number_save_1]) < int(number_list[number_save_2]):
                    print("larger!")
                    input_count = 1
                    number_list.pop(0)
            
                else:
                    print("smaller!")
                    input_count = 1
                    number_list.pop(0)
            
        except ValueError:
            print("not a number!")

def randomize_string(og_string):
    """
    randomizes a string 
    """
    random_string = ""
    old_string = og_string
    list_for_random_string:list = []
    list_for_random_string += og_string
    random.shuffle(list_for_random_string)
    og_string = "" .join(list_for_random_string)
    random_string = old_string + " --> " + og_string
    return random_string
    
def get_acronym(string):
    """
    gets the acronym out a string
    """
    acronym_word = ""
    for char in string:
        if char.isupper():
            acronym_word += char
    return acronym_word
    
def multiply_str(string1,string2):
    """
    multiplies a word and an interger
    """
    multiplied_string = str(string1)*int(string2)
    return multiplied_string


def mask_string(number_string):
    """
    Mask all numbers except the four last digits
    """
    length_of_string = len(number_string)
    if length_of_string > 4:
        last_digits = len(number_string)-4
        new_string = multiply_str("#",last_digits)
        return(new_string + number_string[last_digits:])
    return number_string
    

def find_all_indexes(string1,find_me):
    """
    find all the indexes in a string
    """
    length = len(string1)
    start = 0
    index_string = ""
    try:
        while length !=start:
            index_places = string1.index(find_me,start,length)
            start = index_places+1
            index_string += str(index_places) + ","
        coma_destroyer = len(index_string)-1
        index_string = (index_string[:coma_destroyer])
        return index_string
    except ValueError:
        coma_destroyer = len(index_string)-1
        index_string = (index_string[:coma_destroyer])
        return index_string

def points_to_grade(max_points,your_points):
    """
    Finds out what grade you got
    """
    #try:
    your_score = "score: "
    #if int(max_points) < int(your_points):
        #over_max_point = "Wow you got more points than possible!"
        #return over_max_point
    percentage = 100*(float(your_points)/float(max_points))
    score_list: list = ["A","B","C","D","F"]
    if percentage >= 90:
        your_score += score_list[0]
        return your_score
    if percentage >= 80:
        your_score += score_list[1]
        return your_score
    if percentage >= 70:
        your_score += score_list[2]
        return your_score
    if percentage >= 60:
        your_score += score_list[3]
        return your_score
    if percentage < 60:
        your_score += score_list[4]
        return your_score
    return your_score
    #except (ValueError, ZeroDivisionError):
        #not_a_number = "You probably did not type a number or wrote two zeros!"
        #return not_a_number
    
def has_strings(string, string_first, string_contain, string_end):
    """
    A function that checks if a string contains things
    """
    string_match = "Match"
    string_no_match = "No match"
    if string.startswith(string_first):
        if string_contain in string:
            if string.endswith(string_end):
                return(string_match)
    
    return string_no_match
    