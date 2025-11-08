from stats import get_num_words, get_num_chars, sort_on
import sys


def main():
    # Require a path argument
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]

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
    try:
        with open(path, encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        print(f"Error: File not found at {path}")
        sys.exit(1)


if __name__ == "__main__":
    main()
