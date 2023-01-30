#C:\cygwin64\home\zacki\python\me\kmom06\analyzer\analyzer.py
#analyzer.py
"""
this file is for the diferent funktions
"""
#phil C:\cygwin64\home\zacki\python\me\kmom06\analyzer\phil.txt 

def sorter(dic, len_for_p):
    """
    sorting the list
    """
    temp = {}
    return_dic = {}
    pv = (0,0)
    pk = (0,0)
    p = []
    c = 0
    temp_return = {}

    dic = dict(sorted(dic.items(), key = lambda x: x[1], reverse = True))

    for i in dic.values():
        p.append(procent(i, len_for_p))
    
    for i in dic:
        return_dic[i] = dic[i], p[c]
        c += 1

    for key, value in return_dic.items():

        if value[1] == pv[1]:
            temp[key] = value
            temp[pk] = pv
            try:
                temp_return.pop(pk)
            except KeyError:
                """ do nothing """
        
        else:
            temp_return[key] = value

        pk = key
        pv = value

    sorted_temp = {}
    for key in sorted(temp.keys(), reverse=True):
        sorted_temp[key] = temp[key]

    for key, value in sorted_temp.items():
        temp_return[key] = value

    list_return = sorted(temp_return.items(), key = lambda x: x[1], reverse = True)
    return list_return



def change():
    """
    declare a global variable outside the funk and redifine it in this funk
    """
    global file 
    file = input("enter file:")
    return file


file = "phil.txt"


def lines():
    """
    line count
    """
    with open(file, "r") as text:
        t = text.read().split("\n")
    return len(t)


def words():
    """
    word count
    """
    word_list = []
    count = 0
    new_string = ""

    with open(file, "r") as text:
        t = text.read().split("\n")
        word = " ".join(t)
    
    for w in word.split():
        if w.lower().strip() not in word_list:
            word_list.append(w.lower().strip(",."))

        new_string += w.lower().strip(",.") + " "
        count += 1
    return count, word_list, new_string
        

def letters():
    """
    letter count
    """
    count = 0
    uniq_letter = []
    split_letters = ""
    with open(file, "r") as text:
        t = text.read().split("\n")
    
    for line in t:
        for word in line:
            if word.isalpha():
                if word.lower() not in uniq_letter and word != " ":
                    uniq_letter.append(word.lower())
                
                if word not in " .,": 
                    split_letters += word.lower() + " "
                count += 1
    return count, uniq_letter, split_letters


def word_frequency():
    """
    couts the frequency of words and prints the seven most frequent and the procentage
    """

    word_dic = {}
    return_dic = {}
    word_list = words()[1]

    for word in word_list:
        word_dic[word] = None
    
    for key in word_dic:
        word_dic[key] = specifik_word_count(key, words()[2])

    dic = sorter(word_dic, words()[0])
    seven = list(dic)[:7]
 
    for i in range(0, 7):
        return_dic[seven[i][0]] = seven[i][1], seven[i][1]

    
    print_frequency(return_dic)  


def letter_frequency():
    """
    couts the frequency of letters and prints the seven most frequent and the procentage
    """
    letters_dic = {}
    return_dic = {}
    letters_list = letters()[1]
    
    for l in letters_list:
        letters_dic[l] = None
    
    for key in letters_dic:
        letters_dic[key] = specifik_word_count(key, letters()[2])

    dic = sorter(letters_dic, letters()[0])
    seven = list(dic)[:7]
 
    for i in range(0, 7):
        return_dic[seven[i][0]] = seven[i][1], seven[i][1]

    
    print_frequency(return_dic)  
    

def specifik_word_count(word, text):
    """
    count how many times a specifik word is repited
    """
    count = 0
    for word1 in text.split():
        if word == word1:
            count += 1
    return count


def procent(value, count):
    """
    procent kalk
    """
    return round((value/count) * 100, 1)


def print_frequency(dic):
    """
    print statment for frequency
    """
    for (key, value) in dic.items():

        print(f"{key}: {value[0][0]} | {value[0][1]}%")


def alla():
    """
    prints all the funktions
    """
    print(lines())
    print(words()[0])
    print(letters()[0])
    word_frequency()
    letter_frequency()
