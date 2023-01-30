"""Analyzes texts based on user input"""


current_file = "phil.txt"

def lines():
    """Counts the amount of lines in a file"""
    with open(current_file) as txt:
        txt_lines = txt.readlines()
    
    for _ in range(0, len(txt_lines)):
        try:
            txt_lines.remove("\n")
        except ValueError:
            pass

    return len(txt_lines)


def words():
    """Counts the amount of words in the document"""
    with open(current_file) as txt:
        txt_whole = txt.read()
    
    word_list = txt_whole.split()
    
    return len(word_list)

 


def letters():
    """Counts the amount of words in the document"""
    with open(current_file) as txt:
        txt_whole = txt.read()
    
    txt_alph = ""
    for i in txt_whole:
        if not i in (" ", "-", ",", ".", "\n"):
            txt_alph += i

    return len(txt_alph)


def word_frequency():
    """Returns the highest frequency words in a file"""
    with open(current_file) as txt:
        txt_whole = txt.read()

    temp_list = txt_whole.split()

    word_str = ""
    for _, k in enumerate(temp_list):
        if "," in k:
            temp = k.replace(",", " ")
            word_str += temp.casefold()

        elif "." in k:
            temp = k.replace(".", " ")
            word_str += temp.casefold()
        
        else:
            word_str += k.casefold() + " "
        
    word_list = word_str.split()
    frequency_dict = {}

    for i in word_list:
        if i in frequency_dict:
            frequency_dict[i] += 1
        else:
            frequency_dict[i] = 1

    sorted_words = sorted(frequency_dict.items(), key=lambda x: (x[1], x[0]), reverse=True)

    sorted_output = ""
    values_shown = 7

    for i in range(0, values_shown):
        sorted_output += (
            f"{sorted_words[i][0]}: {sorted_words[i][1]} | {round(sorted_words[i][1] / words() * 100, 1)}%\n")

    return sorted_output


def letter_frequency():
    """Returns the highest frequency letters in a file"""
    with open(current_file) as txt:
        txt_whole = txt.read()
    
    txt_str = ""
    for i in txt_whole:
        if not i in (" ", "-", ",", ".", "\n"):
            txt_str += i.casefold() + " "
    
    char_list = txt_str.split()
    frequency_dict = {}

    for i in char_list:
        if i in frequency_dict:
            frequency_dict[i] += 1
        else:
            frequency_dict[i] = 1

    sorted_char = sorted(frequency_dict.items(), key=lambda x: (x[1], x[0]), reverse=True)
    
    sorted_output = ""
    values_shown = 7

    for i in range(0, values_shown):
        sorted_output += (
            f"{sorted_char[i][0]}: {sorted_char[i][1]} | {round(sorted_char[i][1] / letters() * 100, 1)}%\n")

    return sorted_output


def All():
    """Shows the result for all functions"""
    output = (f"{lines()}\n{words()}\n{letters()}\n{word_frequency()}{letter_frequency()}")

    return output


def change():
    """Changes the file in use"""
    global current_file
    current_file = input("Please enter a new file name: ")
