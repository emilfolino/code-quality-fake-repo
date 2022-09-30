# Modulen menu.py skall enbart innehålla kod för att visa menyn.

"""
Menu functions
"""

def start(file_name):
    """
    A menu
    """
    menu = f"""
Welcome to the Word Analyzer 2000.

     ___T_     
    | - - |    
    |__v__|    
   .=[::+]=.   
 ]=' [___] '=[ 
     /  |      
   _/   |_      

Choice:             Action:
"change"            Change the file to analyze.
"lines"             Analyzes amount of lines in a file.
"words"             Analyzes amount of words in a file.
"letters"           Analyzes amount of letters in a file.
"word_frequency"    Analyzes word frequency in a file.
"letter_frequency"  Analyzes word frequency in a file.
"all"               Runs all of the above at the same time.

The analysis will be done on the file {file_name}.
"""

    return menu
