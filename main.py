from stats import count_unique_characters
from stats import count_book_words
from stats import sort_by_count
import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

book_path = sys.argv[1]

def main():
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {count_book_words(book_path)} total words")
    print("--------- Character Count -------")
    sorted_list = sort_by_count(book_path)
    for pair in sorted_list:
        ch=pair["char"]
        print(f"{ch}: {pair['num']}")
    print("============= END ===============")

main()