"""
docstring
"""
from operator import itemgetter

textfile = "phil.txt"

def lines():
    """
    lines
    """
    with open(textfile) as filehandle:
        line_list = []
        for line in filehandle.readlines():
            if line != "\n":
                line_list.append(line)
    return len(line_list)


def get_words():
    """
    get all the words, clean
    """
    with open(textfile) as filehandle:
        file_string = filehandle.read().replace("\n", " ").replace(",","").replace(".","").replace("-","").lower()
        words_total = file_string.split(" ")
    return words_total

def words():
    """
    words
    """
    #with open(textfile) as filehandle:
        #file_string = filehandle.read().replace("\n", " ").replace(",","").replace(".","").replace("-","")
        #words_total = file_string.split(" ")
    return len(get_words())

def letters():
    """
    letters
    """
    words_t = get_words()
    new_list = []
    counter = 0
    for word in words_t:
        new_list.append(word.strip().lower())
    for word in new_list:
        counter += len(word.strip())
    return counter

def word_frequency():
    """
    word frequency
    """
    total_words = get_words()
    words_dict = {}
    for word in total_words:
        if word in words_dict:
            words_dict[word] += 1
        else: 
            words_dict[word] = 1
    sorted_words = sorted(words_dict.items(), key=itemgetter(1), reverse=True)
    sorted_words = organize(sorted_words)
    for word, key in sorted_words[:7]:
        print(word + ":",str(key) + " | " + str(round((key*100)/words(),1)) + "%")
    return sorted_words

def letter_frequency():
    """
    letter frequency
    """
    letter_dict = {}
    counter = 0
    for word in get_words():
        for letter in word:
            if letter in letter_dict:
                letter_dict[letter] += 1
            else:
                letter_dict[letter] = 1
            counter +=1
    sorted_dict = sorted(letter_dict.items(), key=itemgetter(1), reverse=True)
    sorted_dict = organize(sorted_dict)
    for letter,key in sorted_dict[:7]:
        print(letter + ":",str(key) + " | " + str(round((key*100)/counter,1)) + "%")
    return sorted_dict

def organize(list1):
    """
    organize in order
    """
    new_list = list1[:]
    counter = 0
    for _ in range(len(new_list)):
        for word,key in new_list:
            if key == new_list[counter-1][1] and word > new_list[counter-1][0]:
                new_list[counter-1], new_list[counter] = new_list[counter], new_list[counter-1]
            counter +=1
        counter = 0
    return new_list

def all_():
    """
    print all functions
    """
    print(lines())
    print(words())
    print(letters())
    word_frequency()
    letter_frequency()

def change(file):
    """
    change textfile
    """
    try:
        with open(file) as _:
            print("New file is: " + file)
            global textfile
            textfile = file
    except FileNotFoundError:
        print("The file could not be found!!! ")
