"""Print Menu"""

def menu():
    """Print the Menu choices"""
    print(chr(27) + "[2J" + chr(27) + "[;H")

    print("Select an action to perform:\n")

    print("lines)\t\t  Count Lines")
    print("------------------------------")
    print("words)\t\t  Count Words")
    print("------------------------------")
    print("letters)\t  Count Letters")
    print("--------------------------------")
    print("word_frequency)\t  Find 7 Most Used Words")
    print("-----------------------------------------")
    print("letter_frequency) Find 7 Most Used Letters")
    print("-------------------------------------------")
    print("all)\t\t  Do Everything")
    print("--------------------------------")
    print("change)\t\t  Change File")
    print("------------------------------")
    
    print("q)\t\t  Exit Program")
