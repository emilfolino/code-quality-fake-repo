"""Menu file for analyzer"""

def main():
    """Contains the menu choices"""

    print(chr(27) + "[2J" + chr(27) + "[;H")
    print("lines")
    print("words")
    print("letters")
    print("word_frequency")
    print("letter_frequency")
    print("all")
    print("change")
    print("q) Quit.")

if __name__ == "__main__":
    main()
