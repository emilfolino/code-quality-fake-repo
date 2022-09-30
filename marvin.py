'''Marvin'''
import random

def chat():
    '''Prints the options'''
    print("Sup, I'm Kiww. I know almost everything, how can I help you?")
    print("1) Present yourself to ")
    print("2) Convert Celsius to Fahrenheit")
    print("3) Manipulate a word")
    print("4) Sum and average")
    print("5) string manipulation kind of")
    print("6) isogram")
    print("7) Larger, Smaller")
    print("8) String Randomizer")
    print("9) Get an acronym")
    print("10) Mask a string")
    print("11) Find index")
    print("12) Search for country")
    print("13) Show emission change for a coutry")
    print("14) Show all data for a country")
    print("q) Quit.")
    print("")
    print("Try my inv commands!")

def greet():
    '''Greets the user'''
    name = input("What is your name? ")
    print("\nKiww says:\n")
    print("Hello %s - I am at your service!" % name)
    print("What can I do you for?!")

def celcius_to_farenheit(celsius):
    '''Calculates celsius to farenheit'''
    convert = celsius * 9 / 5 + 32
    print(f" {celsius} grader är {round(convert, 2)} fahrenheit.")
    return convert

def word_manipulation(word, count):
    '''prints a word a number of times '''
    print(multiply_str(word, count))
    
    

def sum_and_average():
    '''calculates sum and average of values'''
    summa = 0
    
    amount_of_inputs = 0
    while True:

        inmat = input("input: ")
        if inmat == "done":
            break

        summa += float(inmat)
        amount_of_inputs += 1
        print( "summa = ", summa )
        print( "average", round(summa / amount_of_inputs, 2))
    

def hyphen_string(word):
    '''Docstring'''
    utskrift = ""
    for count, value in enumerate( word ):
        utskrift += f"{value*(count + 1)}-"

    print( utskrift[0:-1] ) #SUbstring, koordinatsystem för string.

    return utskrift 

def is_isogram(word):
    '''Checks if a word is an isogram'''
    word_checker = ""
    lagrare = True

    for letter in word:
        if letter in word_checker:
            lagrare = False
            break

        word_checker += letter

    if lagrare is False:
        print("No match!")
    else:
        print("Match!")

def compare_numbers( num ):
    '''Compares numbers to the '''
    num = input("Write the first number: ")
        
    if not num.isdecimal():
        num = print("number has to be an int! ")
 
        while True:
            secondnum = input("gissning? ")

            if secondnum == "done":
                print( "Ger du upp redan? :( " )
                break

            if not secondnum.isdecimal():
                secondnum = print("not a number!")
                continue

            secondnum = int(secondnum)

            if num < secondnum:
                print("smaller!")

            if num > secondnum:
                print("bigger!")

            if num == secondnum:
                print("same!")
                break

    else:
        print("That is not a valid choice. You can only choose from the menu.")

    input("\nPress enter to continue...")

def randomize_string(word):
    '''
    string randomizer should work
    '''
    word_list = list(word)
    random.shuffle(word_list)
    word_str = "".join(word_list)
    return f"{word} --> {word_str}"

def get_acronym(args):
    '''
    Takes all capital letters from your input to create an acronyn
    '''

    acronym =""

    for letters in args:
        if letters.isupper():
            acronym += letters

    return acronym

def find_all_indexes(arg1, arg2):
    '''
    index finder
    '''
    indexes = []
    start = 0
    
    while True:

        try:
            found = arg1.index(arg2, start)
            indexes.append(found) # append funktionen för att lägga till i listor
            start = found +1
        except ValueError:
            break
    indexes_str = [str(x) for x in indexes]
    return ",".join(indexes_str)

def multiply_str(word, num):
    '''
    string multiplier
    '''
    return word * num
    
def mask_string(word):
    '''
    Takes a word and hides the letters, leaves last four letters shown.
    '''
   # unmasked_word = input(str("Input: "))
    string = multiply_str("#",len(word[:-4]))+word[-4:]
   
    #len(word[:-4])*"#"
    return string
  