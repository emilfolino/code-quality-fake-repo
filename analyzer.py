"""
functions used to analyse the text
"""

def get_file_list(file_name):
    """
    returns the contents of a txt-file as a list
    """
    with open(file_name) as file:
        text = file.readlines()
    return text

def remove_newlines(tmp_list):
    """
    Removes \n from every line in a list
    """
    for index, word in enumerate(tmp_list):
        if "\n" in word:
            word = word.split("\n")
            tmp_list[index] = word[0]
    return tmp_list

def get_word_count(file_name):
    """
    Gets the number of words in a file
    """
    text_list = get_file_list(file_name)
    text_list = remove_newlines(text_list)

    words_count = 0
    for line in text_list:
        line = line.split(" ")
        words_count += len(line)
    return words_count
    
def get_letter_count(file_name):
    """
    Gets the number of letters in a file (only counts things in the alphabet)
    """
    text_list = get_file_list(file_name)
    text_list = remove_newlines(text_list)

    letter_count = 0
    for line in text_list:
        for letter in line:
            if letter.isalpha():
                letter_count += 1

    return letter_count

def get_word_frequency(file_name):
    """
    Prints the 7 most used letters, sorted numerically then alphabetically
    """
    total_words = get_word_count(file_name)
    text_list = get_file_list(file_name)
    text_list = remove_newlines(text_list)

    words_dict = {}
    for line in text_list:
        line = line.replace(",", "")
        line = line.replace(".", "")
        line = line.split(" ")
        for word in line:
            word = word.casefold()
            if word in words_dict:
                words_dict[word] = words_dict[word] + 1
            else:
                words_dict[word] = 1
    #Removes , and . from the list, split on empty space (" ") to count words. 
    #Then counts the amount of times a words is used

    words_dict = sorted(sorted(words_dict.items(), key = lambda x: x[0], reverse = True), 
        key = lambda x: x[1], reverse = True)
    #sorts alphabetically first, then numerically.

    for index in range(0,7):
        precent = round((words_dict[index][1] / total_words) * 100, 1)
        print(f"{words_dict[index][0]}: {words_dict[index][1]} | {precent}%")

def get_letter_frequency(file_name):
    """
    Prints the 7 most used letters, sorted numerically then alphabetically
    """
    total_letters = get_letter_count(file_name)
    text_list = get_file_list(file_name)
    text_list = remove_newlines(text_list)

    letters_dict = {}    
    for line in text_list:
        for letter in line:
            letter = letter.casefold()
            if letter != " ":
                if letter in letters_dict:
                    letters_dict[letter] = letters_dict[letter] + 1
                else:
                    letters_dict[letter] = 1
    #makes all chars lowercase, counts the amount of times a char is in the list,
    #doesnt count empty spaces

    letters_dict = sorted(sorted(letters_dict.items(), key = lambda x: x[0], reverse = True), 
        key = lambda x: x[1], reverse = True)
    #sorts alphabetically first, then numerically.
    
    for index in range(0,7):
        percent = round((letters_dict[index][1] / total_letters) * 100, 1)
        print(f"{letters_dict[index][0]}: {letters_dict[index][1]} | {percent}%")

def everything(file_name):
    """
    Uses every callable function used in the main module.
    """
    print(len(get_file_list(file_name)))
    print(get_word_count(file_name))
    print(get_letter_count(file_name))
    get_word_frequency(file_name)
    get_letter_frequency(file_name)
