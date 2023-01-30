"""
Module with all the functions
"""
def change(file):
    """
    Changing file who reads
    """
    file = str(input("What file are you looking for?"))
    print("File is now:" , file)
    return file

def line_count(file):
    """
    Counts all the lines i the file
    """
    # Open the file in read mode
    text = open(file)
    a = 0
    # Loop through each line of the file
    for _ in text:               
        a += 1              
    return(a)

def word_count(file):
    """
    Counts the words in the file
    """
    # Open the file in read mode
    text = open(file)
    a = 0
    # Loop through each line of the file
    for line in text:
        # Remove the leading spaces and newline character
        line = line.strip()    
        # Convert the characters in line to 
        # lowercase to avoid case mismatch
        line = line.lower()    
        # Split the line into words
        words = line.split(" ")    
        # Iterate over each word in line
        for _ in words:            
            a += 1
    return(a)

def letter_count(file):
    """
    Counts all the letters in the file but erases everything else
    """
    text = open(file)
    a = 0
    # Loop through each line of the file
    for line in text:
        line = line.strip()
        line = line.replace(" ", "")
        line = line.replace(",", "")
        line = line.replace(".", "")
        line = line.replace("\n", "")
        line = line.replace("-", "")        
        for word in line:
            word = word.split()       
            a += 1            
    return(a)

def word_frequency(file):
    """
    Counts the words and shows in historygram
    """    
    # Open the file in read mode
    text = open(file)
    lst = ()    
    # Create an empty dictionary
    d = {}
    a = word_count(file)
    # Loop through each line of the file
    for line in text:
        # Remove the leading spaces and newline character
        line = line.strip() 
        line = line.lower()        
        words = line.split(" ")
        # Iterate over each word in line
        for word in words:            
            # Check if the word is already in dictionary
            word = word.replace(",", "")
            word = word.replace(".", "")            
            if word in d:                
                # Increment count of word by 1
                d[word] = d[word] + 1
            else:
                # Add the word to dictionary with count 1
                d[word] = 1
    lst = []
    for key, val in list(d.items()):
        lst.append((val, key))
    lst.sort(reverse=True)
    for key, val in lst[:10]:
        print(val + ": " + str(key) + " | " +  str(round(((key / a)*100), 1)) + "%")

def letter_frequency(file):
    """
    Counts the letters and shows in historygram
    """    
    text = open(file)
    lst = []   
    # Create an empty dictionary
    d = {} 
    # Loop through each line of the file
    for line in text:
        # Remove the leading spaces and newline character
        line = line.strip()    
        # Convert the characters in line to 
        # lowercase to avoid case mismatch
        line = line.lower()
        # Split the line into words
        words = line.split(" ")
        # Iterate over each word in line
        for word in words:        
            for w in word:                
                if w in d:
                    d[w] = d[w] + 1
                else:
                    # Add the word to dictionary with count 1
                    d[w] = 1
    #Sort the dictionary
    a = letter_count(file)
    lst = []
    for key, val in list(d.items()):
        lst.append((val, key))
    lst.sort(reverse=True)
    for key, val in lst[:10]:
        print(val + ": " + str(key) + " | " +  str(round(((key / a)*100), 1)) + "%")
    
def alla(file):
    """
    Prints out all the functions
    """    
    print(word_count(file))
    print(line_count(file))
    print(letter_count(file))
    word_frequency(file)
    letter_frequency(file)
