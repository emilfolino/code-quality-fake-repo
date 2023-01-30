" Menu module"


def menu():
    """
    Prints the menu choices
    """
    offset_text = len("letter_frequency") + 1
    print("=" * offset_text + " MENU " + "=" * offset_text)
    print("Please select one of the options below:\n")
    print("lines)".ljust(offset_text), "Count number of lines")
    print("words)".ljust(offset_text), "Count number of words.")
    print("letters)".ljust(offset_text), "Count number of letters.")
    print("word_frequency)".ljust(offset_text), "Print top 10 words.")
    print("letter_frequency)".ljust(offset_text), "Print top 10 letters.")
    print("all)".ljust(offset_text), "Print all of the above.")
    print("change)".ljust(offset_text), "Change between lorum.txt and phil.txt.")
    print("menu)".ljust(offset_text), "Re-print the menu")
    print("q)".ljust(offset_text), "Quit.\n")
