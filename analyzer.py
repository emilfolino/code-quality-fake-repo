"""
A module that contains all the functions to 
analyze a text.
"""
def count_words(file_name):
    """
    count words is a function to count the number of 
    words in the text.
    """
    with open(file_name,"r") as fh:
        list_rows = fh.read().split("\n")
        number_words = 0
        for row in list_rows:
            row_words = str(row).split(" ")
            number_words += len(row_words)
        
    return number_words

def count_lines(file_name):
    """
    Funtiont to count the occupied lines in a text. 
    """
    with open (file_name, "r") as fh:
        list_rows = fh.read().split("\n")
    
    return len(list_rows)


def count_letters(file_name):
    """
    Function to count letters in a text.
    """
    with open(file_name,"r") as fh:
        text = fh.read()
        x = text.count(".")
        y = text.count(",")
        z = text.count("-")
        f = text.count("\n")
        h = text.count(" ")
    return len(text)-(x +y +z +f +h)


def word_frequency(file_name):
    """
    Word frequency is a funciton that used to get the frequency
    of the seventh common words in the text.
    """
    with open(file_name) as fh:
        text_lista = fh.read().split("\n")
        list_of_words = []
        for row in text_lista:
            list_of_words += row.split(" ") 

    word_list = []
    for word in list_of_words:
        words = ""
        for char in word:
            if char.isalpha():
                words += char.lower()
        word_list.append(words)


        
    counted_words = []
    list_repeated_word = []
   
    counted_words = []
    for word in word_list:
        if  word not in counted_words :
            y = word.lower()
            x = word_list.count(y)
            word_repetition = word +": "+ str(x)
            list_repeated_word.append(word_repetition)
            counted_words.append(word)
    
    
    
    list_frequency = []
    for item in list_repeated_word:
        get_frequency = item.split(" ")[1]
        list_frequency.append(int(get_frequency))
        list_frequency.sort(reverse=True)
        list_checked = []
        seventh_common_words = list_frequency[:7]
    
    
    for num in seventh_common_words:
        
        for z in list_repeated_word:
            
            num_frequency = z.split(" ")[1]
            if num == int(num_frequency) and z not in list_checked:
                list_checked.append(z)
                procentge_frequecny = (round(num*100/count_words(file_name),1))
                print(z + " | " + str(procentge_frequecny)+"%")


def letter_frequency(file_name):
    """
    Letter frequency is a funciton that help user
    to get the number of letters in a text.
    """
    
        
    with open (file_name) as fh:
        list_text = fh.read().split("\n")

    letters = ""
    for lista in list_text:

        for char in lista:
            if char.isalpha():
                letters += char.lower()



    letters_english = "abcdefghijklmnopqrstuvwxyz"
    letter_freq_list = []
    for letter in letters_english:

        letter_freq = letter + ": " + str(letters.count(letter))
        letter_freq_list.append(letter_freq)

    list_freq_numbers = []
    for item in letter_freq_list:

        list_freq_numbers.append(int(item.split(" ")[1]))
    list_freq_numbers.sort(reverse=True)
    seven_first_common = list_freq_numbers[:7]

    checked_list =  []
    for num in seven_first_common:
        for item in letter_freq_list:
            if str(num) == item.split(" ")[1] and item not in checked_list:
                checked_list.append(item)
                procentge_frequecny = (round(num*100/count_letters(file_name),1))
                print((item + " | " + str(procentge_frequecny) + "%"))

    
def all_data(file_name):
    """
    All is funtions that prints all the analyzed data.
    """
    print(count_lines(file_name))
    print(count_words(file_name))
    print(count_letters(file_name))
    word_frequency(file_name)
    letter_frequency(file_name)    
