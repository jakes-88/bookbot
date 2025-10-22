def main():
    book_path = "books/frankenstein.txt"
    print(get_book_text(book_path))

def get_book_text(book_path):
    with open(book_path) as file:
        book = file.read()
    return book

main()