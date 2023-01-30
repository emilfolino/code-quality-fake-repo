"""
Shows the menu
"""
def menu_show():
    """
    The menu
    """
    all_options = ("Hi and welcome to the file analyzer!\n\n" + 
    "Below you can see all the options\n\n" +
    "words) Word counter\n\n" + 
    "lines) Line counter\n\n" + "letters) Letter counter\n\n" + 
    "word_frequency) Prints out the most used words\n\n" + 
    "letter_frequency) Prints out the most used letters\n\n" + 
    "all) Does all the options above\n\n" + "change) Change file\n\n" + "q) Quit\n")
    
    return(all_options)
