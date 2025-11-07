def get_num_words(text):
    words = text.split()
    return len(words)


def get_num_chars(text):
    freq = {}
    chars = text.lower()
    for char in chars:
        # Count only alphabetic and selected accented letters
        if char.isalpha() or char in ['æ', 'â', 'ê', 'ë', 'ô']:
            freq[char] = freq.get(char, 0) + 1
    return freq


def sort_on(item):
    # Sort helper: return the count (value)
    return item[1]
