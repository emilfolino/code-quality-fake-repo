"""Module that collects frequency counting"""



def open_file():
    """Opens file"""
    inp = open("documentreader.txt", "r")
    words_ = inp.read()
    inp.close()
    try:
        contents_of_file = open(words_)
        
    except FileNotFoundError:
        print("File cannot be opened: ", words_)
        exit()
    return contents_of_file

def change_file(inp_1):
    """Changes the file for the frequency-program"""
    inp = open("documentreader.txt", "w")
    inp.write(inp_1)
    inp.close()
    print(f"new file is {inp_1}")


def count_lines(file_1):
    """Counts lines in file"""
    contents_of_file = file_1.readlines()
    file_1.close()
    count = 0
    for _, _ in enumerate(contents_of_file):
        count += 1
    print(count)

def count_letter(file_1):
    """Counts letters in file"""
    contents_of_file = file_1.read()
    file_1.close()
    count = 0
    new_document = replaced(contents_of_file)
    new_document = new_document.replace("-", "")
    new_document = new_document.replace(" ", "")
    new_dict = {}
    for letter in new_document:
        if letter not in new_dict:
            new_dict[letter] = 1
            count += 1
        else:
            new_dict[letter] += 1
            count += 1
    print(count)


def count_word(file_1):
    """Counts words in file"""
    contents_of_file = file_1.read()
    file_1.close()
    counts = {}
    count = 0
    new_document = replaced(contents_of_file)
    new_document = new_document.split()
    for item in new_document:
        if item in counts:
            counts[item] = counts.get(item)+ 1
            count += 1
        else:
            counts[item] = 1
            count += 1
    print(count) 

def replaced(contents_of_file):
    """Function to replace ., and \n in files"""
    new_document = contents_of_file.replace(".", " ")
    new_document = new_document.replace(",", " ")
    new_document = new_document.replace("\n", " ")
    new_document = new_document.lower()
    return new_document

def letter_frequency(file_1):
    """Gives the frequency of letters in file"""

    contents_of_file = file_1.read()
    file_1.close()
    count = 0
    new_dict = {}
    new_document = replaced(contents_of_file)
    new_document = new_document.replace("-", "")
    new_document = new_document.replace(" ", "")
    for letter in new_document:
        if letter not in new_dict:
            new_dict[letter] = 1
            count += 1
        else:
            new_dict[letter] += 1
            count += 1
    sort_frequency(new_dict, count)


def sort_frequency(new_dict, count):
    """prints the frequencys in given format"""
    new_dict = dict(sorted(new_dict.items(), key = lambda item: (item[1], item[0]), reverse = True))
    list_from_dict = [(k, v) for k, v in new_dict.items()]
    new = list_from_dict[0:7]
    for value in new:
        tuple_1 = value
        value_tuple = value[1]
        percent = (value_tuple/count)*100
        percent = round(percent,1)
        tuple_1 = tuple_1 + (percent,)
        print(f"{tuple_1[0]}: {tuple_1[1]} | {tuple_1[2]}%")


def word_frequency(file_1):
    """Gives the frequency of words in file"""
    contents_of_file = file_1.read()
    file_1.close()
    new_dict = {}
    count = 0
    new_document = replaced(contents_of_file)
    new_document = new_document.split()
    for item in new_document:
        if item in new_dict:
            new_dict[item] = new_dict.get(item)+ 1
            count += 1
        else:
            new_dict[item] = 1
            count += 1
    sort_frequency(new_dict, count)
        