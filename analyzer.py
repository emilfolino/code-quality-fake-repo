'''
text reader
'''

#with open ("lorum.txt") as l:
 #   lines = l.readlines()

#from fileinput import filename
#from msilib.schema import File
#from posixpath import split
#from re import L
#from subprocess import _TXT


def lines(file_inp):

    '''
    line counter function
    '''
    with open(file_inp) as p:
        lines_phil = p.readlines()
        
        
        line_counter = 0
        for txt in lines_phil:
            
            if txt != "\n":
                line_counter +=1
            
            
        return(print("Lines: ", line_counter))


def  letters(file_inp):
    '''
    letter counter
    '''
    with open (file_inp) as p:
        letter_phil = p.read()
        letter_counter= 0
        for letter in letter_phil:
            
            
            
            if letter.isalpha() is True:

                letter_counter += 1
        

        print(letter_counter)

def words(file_inp):
    '''
    word counter
    '''
    with open (file_inp, "r") as p:
        info = p.read()
        wordz = info.split()
        
        
        print("Words: " + str(len(wordz)))

def word_frequency(file_inp):
    '''
    Print out  7 most common words
    '''
    with open(file_inp, "r") as p:
        wordz = p.read().strip().split()
        

    set_of_words = []
    for word in wordz:
        set_of_words.reverse()
        result = ""
        for letter in word:
            if letter.isalpha():
                result += letter.lower()

        set_of_words.append(result)

    set_of_words.sort()
    set_of_words.reverse()
    
    counter = {}

   
   
    for word in set_of_words:
        if word in counter:
            counter[word] += 1
        else:
            counter[word] = 1

    sorted_words = sorted(counter.items(), key=lambda x: x[1], reverse=True)

    for i, (word, count) in enumerate(sorted_words):
        sorted_words[i] = (
            word, f"{count} | {round(count / len(wordz) * 100, 1)}%")


        
    for word, count in sorted_words[:7]:
        print(f"{word}: {count}")


        
def letter_frequency(file_inp):

    """
    letters
    """
    with open(file_inp, "r") as p:
        wordz = p.read().strip()
        wordz = wordz.replace(" ", "").lower()
        wordz = wordz.replace(".", "")
        wordz = wordz.replace(",", "")
        wordz = wordz.replace("-", "")
        wordz = wordz.replace("\n", "")
       
    set_of_words = []
        
    for letter in wordz:
        result = ""
        if letter.isalpha():
            result += letter.lower()
        set_of_words.append(result)
      
    counter = {}
   
    for hord in set_of_words:
        if hord in counter:
            counter[hord] += 1
        else:
            counter[hord] = 1

    sorted_words = sorted(counter.items(), key=lambda x: x[1], reverse=True)
    
    for i, (hord, count) in enumerate(sorted_words):
        sorted_words[i] = (
            hord, f"{count} | {round(count / len(wordz) * 100, 1)}%")


    for word, count in sorted_words[:7]:
        print(f"{word}: {count}")



def show_all(file_inp):
    """
    all functions
    """
    print(lines(file_inp))
    print(words(file_inp))
    print(letters(file_inp))
    print(word_frequency(file_inp))
    print(letter_frequency(file_inp))

def change():
    """
    changes file
    """
    
    
    while True:
        fil_inp = input("skriv: ")
        if  fil_inp == "phil.txt" :
            break
        elif fil_inp == "lorum.txt":
            break
        else:
            print("Wrong input! ")
    print(fil_inp)
    return str(fil_inp)
    
    
        
      
   