"""
analyzer functions

    """
def lines(file):
    """
counts the lines

    """
    lines_amount = sum(1 for line in open(file))
    return lines_amount

def words(file):
    """
counts the words

    """
    file = open(file)
    file_content = file.read()
    word = file_content.split()
    word_amount = len(word)
    return word_amount

def letters(file):
    """
counts the letters

    """
    file = open(file)
    file_content = file.read()
    count = 0
    for letter in file_content:
        if letter.isalpha():
            count += 1
    return count

def word_frequency(file):
    """
show the frequency of the top 7 words

    """
    word_dict = {}
    procentlist = []
    top_wordlist = []
    count = 0
    result = ""
    listwords = ""
    file = open(file)
    file_content = file.read().lower()
    file_content = file_content.replace(',','')
    file_content = file_content.replace('.','')
    file_content = file_content.replace('-','')
    wordlist = file_content.split()
    for i in wordlist:
        word_dict[i]=wordlist.count(i)
        count +=1

    sorted_words = dict(sorted(word_dict.items(), key=lambda t: t[::-1],reverse=True))
    first_seven = dict(list(sorted_words.items())[:7])

    for values in first_seven.values():
        procentage = values/count
        procentage = round(procentage*100,1)
        procentlist.append(procentage)

    for key,value in first_seven.items():
        listwords = str(key) + ": " + str(value)
        top_wordlist.append(listwords)

    for i in range(7):
        result += str(top_wordlist[i]) + " | " + str(procentlist[i]) + "%" + "\n"
    return result.strip()
    
def letter_frequency(file):
    """
shows the frequency of the top 7 letters

    """
    count = 0
    letter_dict = {}
    procentlist = []
    letterlist = []
    result = ""
    file = open(file)
    file_content = file.read().lower()
    
    for letter in file_content:
        if letter.isalpha():
            count += 1
            letter_dict[letter]= file_content.count(letter)

        sorted_letters = dict(sorted(letter_dict.items(), key=lambda t: t[::-1],reverse=True))
        first_seven = dict(list(sorted_letters.items())[:7])

    for values in first_seven.values():
        procentage = values/count
        procentage = round(procentage*100,1)
        procentlist.append(procentage)

    for key,value in first_seven.items():
        listwords = str(key) + ": " + str(value)
        letterlist.append(listwords)

    for i in range(7):
        result += str(letterlist[i]) + " | " + str(procentlist[i]) + "%" + "\n"

    return result.strip()
