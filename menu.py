"""All menu related code"""
def displayMenu():
    """Prints menu"""
    print("""
    lines) Count lines
    words) Count words
    letters) Count letters
    word_frequency) Find 7 most used words
    letter_frequency) Find 7 most used letters
    all) Do all
    change) Change file
    """)


def menu():
    """Main menu code"""
    displayMenu()
    return str(input("--->"))
