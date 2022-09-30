"""
Contains funktions to analyze text
"""

def char_strip(text_file, string):
    """
    Removes unwanted characters from text.
    """
    try:
        with open(text_file) as fhand:
            chars = fhand.read()
        low_char = chars.lower()
        tot_letters = ""
        for c in low_char:
            if c not in string:
                tot_letters = tot_letters + c       
        return(tot_letters)
    except FileNotFoundError:
        print('File not found')
        raise

def frequency_find(variable):
    """
    Finds frequency and returns list of tuples (word/char, occurrence, precent)
    """
    temp_dict = {}
    for i in variable:
        if i in temp_dict.keys():
            temp_dict[i] += 1
        else:
            temp_dict[i] = 1
    total_char = len(variable)
    orders_list = []
    # tar hösta value och lägger tuple i lista (key, value, percent)
    for dummy in range(len(temp_dict)):
        max_key = max(temp_dict, key=temp_dict.get)            
        new_val = temp_dict.values()
        max_val = max(new_val)
        percent_char = (max_val / total_char) * 100
        orders_list.append((max_key, max_val, round(percent_char, 1)))
        temp_dict.pop(max_key, max_val)
    
    #Bubblesort på lista för de bokstäverna som är lika
    lenght = len(orders_list)
    for dummy in range(lenght):
        for i in range(lenght-1):
            if orders_list[i][1] == orders_list[i + 1][1]:
                if orders_list[i + 1][0][0][0] > orders_list[i][0][0][0]:
                    orders_list[i +1], orders_list[i] = orders_list[i], orders_list[i + 1]
    final_seven = orders_list[0:7]
    return final_seven

def lines(text_file):
    """
    count number of lines in the text
    """
    count = 0
    try:
        with open(text_file) as fhand:
            line_to_count = fhand.readlines()
        for dummy in line_to_count:
            count = count + 1     
        return(count)
        
    except FileNotFoundError:
        print('File not found')
        raise

def letters(text_file):
    """
    Counts letters in Text
    """     
    tot_letters = char_strip(text_file, " ,.-\n")
    return(len(tot_letters))

def words(text_file):
    """
    Count number of words in text
    """
    try:
        words_to_use = char_strip(text_file, ".,")
        count = len(words_to_use.split())
        return(count)
    except FileNotFoundError:
        print('File not found')
        raise

def letter_frequency(text_file):
    """
    Gets letter frequency
    """
    try:
        low_string = char_strip(text_file, " ,.-\n")
        final_seven = frequency_find(low_string)
        return print_formater(final_seven) 
    except FileNotFoundError:
        print('File not found')
        raise

def word_frequency(text_file):
    """
    Get the word frequency
    """
    try:
        words_to_count = char_strip(text_file, ".,")
        word_list = words_to_count.split()
        final_seven = frequency_find(word_list)

        return print_formater(final_seven)
    except FileNotFoundError:
        print('File not found')
        raise

def print_formater(list_to_use):
    """
    Iterates a list of tuples and formats some prints
    """
    for tup in list_to_use:
        print(f"{tup[0]}: {tup[1]} | {tup[2]}%")

def print_all(text_file):
    """
    Prints all funktions
    """
    the_lines = lines(text_file)
    the_words = words(text_file)
    the_letters = letters(text_file)
    print(the_lines)
    print(the_words)
    print(the_letters)
    word_frequency(text_file)
    letter_frequency(text_file)
