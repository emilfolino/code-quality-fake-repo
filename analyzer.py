"""Dotline"""

Files = ["phil.txt", "lorum.txt"]
textFile = "phil.txt"

def count_lines():
    """dotstring"""
    try:
        with open(textFile, "r", encoding="UTF-8") as line:
            return(len(line.readlines())) 
    except FileNotFoundError:
        return("Error: ")

def count_words():
    """dotstring"""
    try:
        with open(textFile, "r", encoding="UTF-8") as word:
            data = word.read()
            data = data.replace("\n", " ", data.count("\n"))
            words = data.split(" ")
            return(len(words))
    except FileNotFoundError:
        return("Error: ")

def count_letters():
    """dotstring"""
    count = 0
    try:
        with open(textFile, "r", encoding="UTF-8") as letter:
            for char in letter.read():
                if char.isalpha() is True:
                    count += 1
        return(count)
    except FileNotFoundError:
        return("Error: ")

def word_frequency():
    """dotstring"""
    try:
        with open(textFile, "r", encoding="UTF-8") as word:
            file = " ".join(word.readlines())
            file = file.split(" ")
            corect_str = [''.join(c for c in string if c.isalnum()) for string in file]
            file = corect_str
            counts = {}
            
            for line in file:
                counts[line.lower()] = counts.get(line.lower(), 0) + 1
            
            sort_words = dict(sorted(counts.items(), key=lambda x: (x[1], x[0]), reverse=True))
            sort_list = list(sort_words)

            for key in sort_list[0:7]:
                procent = format(counts[key] / count_words() * 100, ".1f")
                print(key + ": " + str(counts[key]) + " | " + str(procent) + "%")

            
    except FileNotFoundError:
        print("Error: ")

def letter_frequency():
    """dotstring"""
    with open(textFile, "r", encoding="UTF-8") as letter:
        file = letter.read()
        file = file.replace(",", "", file.count(","))
        counts = {}
        for latter in file:
            if latter.isalpha() is True:
                counts[latter.lower()] = counts.get(latter.lower(), 0) + 1
                

        
        sort_latters = dict(sorted(counts.items(), key=lambda x: (x[1], x[0]), reverse=True))
        sort_list = list(sort_latters)

        for key in sort_list[0:7]:
            procent = format(counts[key] / count_letters() * 100, ".1f")
            print(key + ": " + str(counts[key]) + " | " + str(procent) + "%")

def allData():
    """dotstring"""
    print(count_lines())
    print(count_words())
    print(count_letters())
    word_frequency()
    letter_frequency()


def change_file():
    """dotstring"""
    try:
        nameFile = input("Enter file name: ")
        if nameFile in Files:
            print("File exist... Changing to " + nameFile)
            global textFile
            textFile = nameFile.strip().lower()
        else:
            print("Error: ")
    except FileNotFoundError:
        print("Not existing file")
