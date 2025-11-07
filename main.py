from stats import get_num_words, get_num_chars, sort_on

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)

    num_words = get_num_words(text)
    num_chars = get_num_chars(text)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    # Sort by frequency (descending)
    sorted_chars = sorted(num_chars.items(), key=sort_on, reverse=True)

    # Print in the correct format: e: 44538
    for char, count in sorted_chars:
        print(f"{char}: {count}")

    print("============= END ===============")


def get_book_text(path):
    with open(path, encoding="utf-8") as f:
        return f.read()


main()
