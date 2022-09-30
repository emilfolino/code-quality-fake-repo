"""
Only code to show the menu.
"""

def print_menu():
    """
    Prints the menu for analyzer.
    """
    menu_str = """
    Count lines --> 'lines'
    Count words --> 'words'
    Count letters --> 'letters'
    Find 7 most used letters --> 'word_frequency'
    Do everything --> 'all'
    Change file --> 'change'
    Quit --> 'q'
    """
    return f"{menu_str}"






if __name__ == "__main__":
    print_menu()
