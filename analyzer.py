"""
Functions that analyze a given text.
"""

def strip_punc(s):
    """
    Strips punctuation from beginning and end of string until reaching a letter.
    """
    while not s[0].isalpha():
        s = s[1:]
    while not s[-1].isalpha():
        s = s[:-1]
    return s


list_non_empty_lines = lambda text: [line for line in text.split('\n') if line]

non_empty_line_count = lambda text: len(list_non_empty_lines(text))


list_words = lambda text: [s for s in map(strip_punc, text.split()) if s]

word_count = lambda text: len(list_words(text))


list_letters = lambda text: [char for char in text if char.isalpha()]

letter_count = lambda text: len(list_letters(text))


def get_freqs(text, mode):
    """
    Returns a dict of words or letters, their count, and comparative frequency percentage in
    the text. Case insensitive and ignores punctuation.
    """
    token_list = []
    freqs = {}

    #modes
    if mode == 'words':
        token_list = list_words(text)
    elif mode == 'letters':
        token_list = list_letters(text)

    total = len(token_list) 
    if total > 0:
        for token in token_list:
            token = token.casefold()
            if token in freqs:
                freqs[token] += 1
            else:
                freqs[token] = 1
        pct = lambda n: n / total * 100
        freqs = {token: (count, pct(count)) for token, count in freqs.items()}
    return freqs


def freq_printout(text, mode):
    """
    Returns a formatted string of the 7 highest count tokens in descending frequency, along with
    their count, and comparative frequency percentage in the text. Ties are broken by alphabetical
    order.
    """
    freqs = get_freqs(text, mode)

    # I know the sorting should be by zyx... easier but kind of weird! So I figured out a cool way
    # to tiebreak by abc while numbers descend!
    # Uncomment:
    # freqs = sorted(freqs.items(), key=lambda i: (-i[1][0], i[0]))
    freqs = sorted(freqs.items(), key=lambda i: (i[1][0], i[0]), reverse=True)

    for token, (count, pct) in freqs[:7]:
        pct = round(pct, 1)
        print(f"{token}: {count} | {pct}%")
