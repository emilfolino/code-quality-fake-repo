"""
Functions to analyze text.
"""

from operator import itemgetter as IG

# Always set when starting the program
input_text = "phil.txt"


def read_file(file):
    """
    Function to read a file.
    """
    with open(file, "r") as fhand:
        content = fhand.read().split("\n")
    return content


def line_count():
    """
    Function to count lines in a file.
    """
    content = read_file(input_text)
    #print(len(content))
    return f"{len(content)}"

def word_count():
    """
    Function to count words in a file.
    """
    content = read_file(input_text)
    new_str = " ".join(content) # Insert a space where the newlines were to get a correct count.
    content = new_str.split(" ")
    return f"{len(content)}"

def letter_count():
    """
    Function to count letters in a file.
    """
    content = read_file(input_text)
    new_str = " ".join(content)
    counter = 0
    # Checks if it is letters and adds to counter if true
    for i in new_str:
        if i.isalpha():
            counter += 1
    return f"{counter}"

def word_freq():
    """
    Function to count frequencies of words in a file.
    """
    content = read_file(input_text)
    new_str = " ".join(content).lower() # Make all lower for easy comparision
    new_str = new_str.replace(",", "")
    new_str = new_str.replace(".", "") # Removes characters 
    content = new_str.split(" ")
    
    # Counts occurences
    c_dict = {}
    for i in content:
        if i not in c_dict:
            c_dict[i] = 1
        else:
            c_dict[i] += 1
    # Sorts on number then alphabetically
    c_dict = sorted(c_dict.items(), key=IG(1,0), reverse=True)
    return_str = ""
    for i in range(7):
        return_str += f"{c_dict[i][0]}: {c_dict[i][1]} | {round(int(c_dict[i][1]) / int(word_count()) * 100, 1)}%\n"
    return f"{return_str}"

def letter_freq():
    """
    Function to count frequencies of letters in a file.
    """
    content = read_file(input_text)
    new_str = " ".join(content).lower() # Make all lower for easy comparision
    new_str = new_str.replace(",", "")
    new_str = new_str.replace(".", "") # Removes characters 
    
    # Counts occurences
    c_dict = {}
    for i in new_str:
        if i != " ": # Do not counts whitespace
            if i not in c_dict:
                c_dict[i] = 1
            else:
                c_dict[i] += 1

    # Sorts on number then alphabetically
    c_dict = sorted(c_dict.items(), key=IG(1,0), reverse=True)
    return_str = ""
    for i in range(7):
        return_str += f"{c_dict[i][0]}: {c_dict[i][1]} | {round(int(c_dict[i][1]) / int(letter_count()) * 100, 1)}%\n"
    
    return f"{return_str}"

def all_file():
    """
    Function which return all previous functions in one print-out.
    """
    return f"{line_count()}\n{word_count()}\n{letter_count()}\n{word_freq()}{letter_freq()}"



def change_file(file):
    """
    Function to switch which file is read.
    """
    global input_text
    input_text = file



if __name__ == "__main__":
    letter_freq()
