"""
Analyzer new Cod
"""

def lines(file = "phil.txt"):
    """
    number of lines in text
    """
    line_1 = open(file, "r")
    return len(line_1.readlines())

def letters(file= "phil.txt"):
    """
    count all letters in text file
    """
    file = open(file, "r")

    data = file.read().replace(" ","")
    data = data.replace(".","")
    data = data.replace(",","")
    data = data.replace("-","")
    data = data.replace("\n","")

    number_of_letters = len(data)
    return number_of_letters

def words(file= "phil.txt"):
    """
    Check how many letters
    """
    number_of_words = 0
    words_1 = open(file, "r")
    words_2 = words_1.read()
    lines_1 = words_2.split()
    for word in lines_1:
        if not word.isnumeric():         
            number_of_words += 1
    
    return number_of_words

def letter_frequency(file= "phil.txt"): 
    """
    something
    """
    my_dict_2 = {}
    str_2 = ""
    letters_1 = open(file, "r")
    data_letters = letters_1.read().lower()
    data_letters = data_letters.replace(" ","")
    data_letters = data_letters.replace(".","")
    data_letters = data_letters.replace(",","")
    data_letters = data_letters.replace("-","")
    data_letters = data_letters.replace("\n","")
    for index_2 in data_letters :
        my_dict_2[index_2] = data_letters.count(index_2)
    sort_orders = sorted(my_dict_2.items(), key=lambda x: x[1], reverse=True)

    for i in sort_orders[0:7]:
        str_2 +=  f"{i[0]}: {i[1]} | {round(((i[1])/letters(file)* 100),1)}%\n"
    str_2.strip("\n")

    return str_2

def word_frequency(file = "phil.txt"):
    """
    Print the frequency words and how much %
    """
    my_dict = {}
    str_1 = ""
    document_text = open(file, "r")
    data_letters = document_text.read().lower()
    data_letters = data_letters.replace(".","")
    data_letters = data_letters.replace(",","")
    data_letters = data_letters.replace("-","")
    data_letters = data_letters.replace("\n"," ")
    split_words = data_letters.split(" ")
    for i in split_words:
        my_dict[i] = split_words.count(i)
  
    dict_items = my_dict.items()
    sorted_items = sorted(dict_items,reverse=True)
    sort_orders = sorted(dict(sorted_items).items(), key=lambda x: x[1],reverse=True)

    for i in sort_orders[0:7]:
        str_1 += f"{i[0]}: {i[1]} | {round(((i[1])/words(file)* 100),1)}%" + "\n"
    return str_1

def print_all(file= "phil.txt"):
    """
    print all information about text 
    """
    return f"""
    {words(file)}
    {lines(file)}
    {letters(file)}
    {word_frequency(file)}
    {letter_frequency(file)}"""

def change():
    """
    switch file
    """
    Text_file = input("file name: ")

    if Text_file == "lorum.txt":
        file = "lorum.txt"
    else: 
        file = "phil.txt"
    return file
