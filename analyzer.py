"""
Functions used to main the
"""
import string
from operator import itemgetter

def lines():
    """
    Hur ånga linjen finns det i textfilen
    """
    file = read_last_file_name()
    with open(file, "r") as file:
        list_of_lines = file.readlines()
        result = len(list_of_lines)

        return result

def words():
    """
    hur många ord finns details
    """
    file = read_last_file_name()
    with open(file, "r") as file:
        list_of_lines = file.readlines()
        new_list = []
        
        for line in list_of_lines:
            if "\n" in line:
                line = line.translate(line.maketrans('', '', string.punctuation))
                new_list.append(line.rstrip() + " ")
            else:
                new_list.append(line)
        
        count = 0
        for line in new_list:
            count += len(line.split())

        return count

def letters():
    """
    letters counting
    """
    file = read_last_file_name()
    with open(file, "r") as file:
        list_of_lines = file.readlines()
        words_list = []
        letter_string = ""
        
        for line in list_of_lines:
            line = line.rstrip()
            line = line.translate(line.maketrans('', '', string.punctuation))
            words_list.append(line.split())
        
        for list_of_words in words_list:
            letter_string += "".join(list_of_words)
        
    return len(letter_string)

def frequency(choes=None):
    """
    count the frequency of words or letters
    """
    file = read_last_file_name()
    if choes == "word":
        result = {}
        with open(file, "r") as file:
            list_of_lines = file.readlines()
            text = ""

            for line in list_of_lines:
                line = line.translate(line.maketrans('', '', string.punctuation))
                line = (line.rstrip() + " ")
                text += line.lower()

            dictionary = {}
            text_list = text.split()
            for word in text_list:
                count_word = text_list.count(word)
                dictionary[word] = count_word
            
            sort_by_name = sorted(dictionary.items())
            sort_dict = sorted(sort_by_name, key=itemgetter(1), reverse=True)
        result = sort_dict
        
    else:
        with open(file, "r") as file:
            list_of_lines = file.readlines()
            letters_list = []
            text = ""

        for line in list_of_lines:
            line = line.translate(line.maketrans('', '', string.punctuation))
            text += line.lower()
            
        dictionary = {}
        text_list = text.split()
        for char in text_list:
            for letter in char:
                letters_list.append(letter)
        
        for letter in letters_list:
            count_letter = letters_list.count(letter)
            dictionary[letter] = count_letter
        
        sort_dict = sorted(dictionary.items(), key=itemgetter(1), reverse=True)
        result = sort_dict
        
    return result

def word_frequency():
    """
    word frequency in the text
    """
    sort_dict = frequency("word")
    dicti = {}
    sort_by_name = sorted(sort_dict, reverse=True)
    new_sort_dict = sorted(sort_by_name, key=itemgetter(1), reverse=True)
    for i in range(7):
        word = new_sort_dict[i][0]
        number = new_sort_dict[i][1]
        dicti[word] = number
    
    result = ""
    tot_words = words()
    for key, value in dicti.items():
        procent = (value/tot_words)*100
        result += (f"{key}: {value} | {round(procent, 1)}%\n")

    return result

def letter_frequency():
    """
    letter frequency in the text
    """
    sort_dict = frequency("letter")
    dicti = {}
    for i in range(7):
        letter = sort_dict[i][0]
        number = sort_dict[i][1]
        dicti[letter] = number
        
    sort_by_name = sorted(dicti.items(), reverse=True)
    new_sort_dict = sorted(sort_by_name, key=itemgetter(1), reverse=True)
    result = ""
    tot_letters = letters()
    for key, value in new_sort_dict:
        procent = (value/tot_letters)*100
        result += (f"{key}: {value} | {round(procent, 1)}%\n")

    return result
def all_functions():
    """
    Skriver alla funktioner resultat
    """
    lines_sum = lines()
    words_sum = words()
    letters_sum = letters()
    freq_word = word_frequency()
    freq_letter = letter_frequency()
    answer = f"{lines_sum}\n{words_sum}\n{letters_sum}\n{freq_word}{freq_letter}\n"
    return answer

def change(choic=None):
    """
    Change filename
    """
    if choic is not None:
        with open("last_file_name.txt", "w") as fn:
            fn.write(choic)
        print(f"The old file has been replaced with {choic}")

def read_last_file_name():
    """
    Read the last file name from the file `last_file_name.txt`
    """
    
    with open("last_file_name.txt", "r") as fn:
        filename = fn.read()
    return filename
