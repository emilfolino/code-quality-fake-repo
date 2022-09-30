"""
Functions for marvin
"""
import random
def multiply_str(word_to_multiply: str, multiply_times: int):
    """
    Takes a word and multiplies it
    """
    string_multiplied = ""
    try:
        for dummy in range(multiply_times):
            string_multiplied += word_to_multiply

    except TypeError:
        print("Function takes str and int")
    
    return(string_multiplied)
    
def greet():
    """
    Greets the user
    """
    name =  input(" Hello my name is Marvin, Please tell me your name to continue? ")
    print("\nMarvin says:\n")
    print("Hello %s - your awesomeness!" % name)
    print("What can I do you for?!")

def celcius_to_farenheit():
    """
    Converts celcius to farenheit
    """
    celcius_var = float(input("Please enter the temperature in celcius: "))
    converted_var = celcius_var * 1.8 + 32
    print(f"{celcius_var} celcius is {round(converted_var, 2)} f")


def error_message():
    """
    prints invalid message
    """
    print("Invalid!!! You can only enter a number")
    

def sum_and_average():
    """
    summs numbers and finds average
    """
    total_var = 0
    count_var = 0
    var_list = []

    while True:
                
        number_var = input("Enter a number or type done when you are done: ")

        if number_var == "done":
            try:
                total_var = sum(var_list)
                avrage_var = total_var/count_var
                print(f"The sum of all numbers are {round(total_var, 2)} and the avrage is {round(avrage_var, 2)} ")
                break
            except ZeroDivisionError:
                print("Error must enter atleast 1 number:")
                continue
        try:
            number_var_i = float(number_var)
            var_list.append(number_var_i)
            count_var += 1

        except ValueError:
            print("ERROR ERROR ERRPOR. enter a number or done ")
            continue

def hyphen_string():
    """
    word play. increments letter
    """
    final_word_var = ""
    word_add_var = input(" please enter a Word!: ")
    word_incrementor = 1
    for i in word_add_var:
        
        final_word_var = final_word_var + (i * word_incrementor) + "-"
        word_incrementor += 1
        
    name_var = final_word_var.rstrip(final_word_var[-1])    
    print(name_var)    

def is_isogram():
    """
    check for isogram
    """
    game = True
    while game is not False:

        isogram_var = input(" Give me a word and i can tell you if it´s a isogram: ")
        isogram_check_var = ""
    
        if (isogram_var):
            for i in isogram_var:
                if i in isogram_check_var:
                    print("No match!")
                    game = False
                    break

                isogram_check_var += i
            else:
                print("Match!")
                break

def compare_numbers():
    """
    compares numbers
    """
    game7 = True
    number_compare_var = None
    while game7 is not False:
        number_input = input("Input a number:  (type done to exit) ")
        if number_input == "done":
            game7 = False
        elif number_input != "done":
            try:
                number_input_float = float(number_input)
                if number_compare_var is None:
                    number_compare_var = number_input_float
                    continue
                if number_compare_var > number_input_float:
                    print("smaller!")
                    number_compare_var = number_input_float
                    continue
                if number_compare_var == number_input_float:
                    print("same!")
                    number_compare_var = number_input_float
                    continue
                if number_compare_var < number_input_float:
                    print("larger!")
                    number_compare_var = number_input_float
                    continue
            except ValueError:
                print("not a number!")
                continue

def randomize_string(word):
    """
    takes a string and randomizes the letters
    """
    random_word_generated = ""
    length_word = len(word)
    return(f"{word} --> {random_word_generated.join(random.sample(word,length_word))}")

def get_acronym(word_to_acronym):
    """
    creates accronym aout of uppercase
    """
    acronym = ""
    for character in word_to_acronym:
        if character.isupper() is True:
            acronym += character
    return acronym

def mask_string(string_mask):
    """
    takes a string and masks it with # 
    """
    temp_string = string_mask[-4::1]
    string_to_mask_lenght = (len(string_mask) -4)
    mask_holder = (multiply_str("#", string_to_mask_lenght))
    return((mask_holder) + (temp_string))

def word_manipulation():
    """
    takes a word and a number and multiplies
    """
    try:
                
        word_var = input("Hello, this is the word multiplyer. Start by giving me a word: ")
        word_num = int(input("Now give me a number: "))
        print(multiply_str(word_var, word_num))
    
    except ValueError:
        print(" ERROR ERROR ERROR!! please enter a correct values next time")

def find_all_indexes(main: str, sub: str):
    """
    Fins substing in string and prints index numbers
    """
    start_val = 0
    test_list = []
    sub_length = len(sub)
    while start_val < len(main):
        try:
            start_val = main.index((sub), (start_val), len(main))
            test_list.append(main.index((sub), (start_val), len(main)))
            start_val = start_val + sub_length
        except ValueError:
            break
    string_list = [str(ele) for ele in test_list]
    final_word = ",".join(string_list)
    dummy_holder = ""
    if final_word:
        return(final_word)
    if not final_word:
        return(dummy_holder)
