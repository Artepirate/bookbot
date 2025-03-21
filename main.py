from stats import word_count
from stats import indy_character_count
from stats import sorted_character_count
import sys

def check_arguments():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)


def get_book_text(book):
    with open(book) as f:
        file_contents = f.read()
    return file_contents

def main():
    check_arguments()
    book = sys.argv[1]
    book_text = get_book_text(book)
    total_word_count = word_count(book_text)
    character_counts = indy_character_count(book_text)
    sorted_counts = sorted_character_count(character_counts)

    # print(book_text)


    print("========== BOOKBOT ==========",)
    print(f"Analysing book found at {book}...",)
    print("--------- Word Count---------",)
    print(f"Found {total_word_count} total words",)
    print("--------- Character Count---------",)
    for character, count in sorted_counts:
        print(f"{character}: {count}")
    print("========== END ==========",)

check_arguments()


main()