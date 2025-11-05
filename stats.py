def get_num_words(text):
    words = text.split()
    return len(words)

def get_num_chars(text):
    freq = {}
    chars = text.lower()
    for char in chars:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    return freq