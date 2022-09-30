"Modules/functions for main"
import random



def greet():
    "Checks name"
    name = input("What is your name? ")
    print("\nAamon says:\n")
    print("Welcome %s to my kingdom!" % name)
    print("What do you want?")

def celcius_to_farenheit():
    "Converts c to f"
    print("\nAamon says:\n")
    Temper = float(input("What is the temperature in celsius? "))
    Temperkonv = round((Temper * 1.8) + 32, 2)
    print("\nAamon says:\n")
    print("You could have google but the temperature is " + str(Temperkonv) + " in fahrenheit")

def word_manipulation():
    "Repeats words x given amount"
    print("\nAamon says:\n")
    inputword = input("Tell me a word: ")
    print("\nAamon says:\n")
    inputrepeat = int(input("How many times do you want it repeated: "))
    print("\nAamon says:\n")
    print("Well, this was a easy task that you could have done yourself but here is the answer")
    print(multiply_str(inputword, inputrepeat))

def sum_and_average():
    "Gives a sum and a avrage"
    numsinput = ""
    sum1 = 0
    midsum = 0
    mids = 0
    print("\nAamon says:\n")
    print("Enter as many numbers as you want, write done when finished")
    while numsinput != "done":
        numsinput = input("Enter a number: ")
        if numsinput == "done":
            break
        sum1 += float(numsinput)
        mids += 1
    midsum = sum1 / mids
    print("\nAamon says:\n")
    print("Here you have the answer mortal")
    print("The sum is " + str(round(sum1, 2)) + " and the avrage is " + str(round(midsum, 2))) 

def hyphen_string():
    "Increase the value of letter example: a-pp-aaa"
    wordm = ""
    multcharac = 1
    print("\nAamon says:\n")
    wordmult = input("Write your word: ")
    for let in wordmult:
        if multcharac > 1:
            wordm += "-"
        wordm += (let * multcharac)
        multcharac += 1  
    print("\nAamon says:\n")
    print("The answer: " + wordm)

def is_isogram():
    "Checks for isograms"
    wordansw = ""
    wordinp = input("Pick a word and I will analyze it: ")
    letrlist = {}
    for letr in wordinp:
        if letr in letrlist:
            print("\nAamon says:\n")
            print("No match!")
            wordansw = "1"
            break  
        else:
            letrlist[letr] = 1
    if wordansw != "1":
        print("\nAamon says:\n")
        print("Match!") 
            
def compare_numbers():
    "Compare number, bigger smaller or same"
    check = 0
    
    while True:
        if check == 1:
            print("Stopping program")
            break
        num1 = (input("Choose your number. Type done when finished with program: "))
        while True:
            try:
                num1 = float(num1)
                num1t = 1
                break
            except ValueError:
                print("not a number!")
                num1 = (input("Choose your number: "))
        num2 = (input("Choose your number: "))
        while True:
            try:   
                num2 = float(num2)
                num2t = 1
                break
            except ValueError:
                print("not a number!")
                num2 = (input("Choose your number: "))
        if (num1t + num2t) == 2:
            while True:
                if str(num2) == "done":
                    check = 1
                    break
                while True:
                    try:
                        float(num2)
                        break
                    except ValueError:
                        if num2 == "done":
                            check = 1
                            break
                        print("not a number!")
                        num2 = input("Choose your number: ")
                if check == 1:
                    break  
                if float(num2) < float(num1):
                    print("smaller!")
                elif float(num1) < float(num2):
                    print("larger!")
                elif float(num1) == float(num2):
                    print("same!")
                num1 = num2
                num2 = input("Choose another number: ")   


def randomize_string(strrand: str):
    "randomizes a string using random.shuffle"
    listcnvr = list(strrand) 
    random.shuffle(listcnvr)
    answer = strrand + " --> " + "".join(listcnvr) 
    return answer

def get_acronym(akroword):
    "looks for akronyms"
    akros = ""
    for i in akroword:
        if i.isupper() is True:
            akros += i
        
    return akros

def multiply_str(str1, int1):
    "A multiplyer"
    answmult = ""
    answmult = str(str1) * int1
    return str(answmult)

def mask_string(mask):
    "Mask a string"
    mask = str(mask)
    wordansw = ""
    counter = 0
    maskedansw = multiply_str("#", (len(mask)-4))
    for i in mask:
        counter += 1
        if len(mask)-4 < counter:
            wordansw += i
    return maskedansw + wordansw
    

def find_all_indexes(index, indexlet):
    "The index searches for the lowest value and with the while loop and the pos+1 it goes through every pos"
    "alternative, use a for loop. Goes through the word letter by letter. when it finds the same letter, add to list"
    pos = -1
    indexposlst = []
    while True:
        try:
            pos = index.index(indexlet, pos + 1)
            indexposlst.append(pos)
        except ValueError:
            indexansw = ','.join(str(i) for i in indexposlst)
            return indexansw
           