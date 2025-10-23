def count_book_words(book_path):
    return len(get_book_text(book_path).split())

def get_book_text(book_path):
    with open(book_path) as file:
        return file.read()
    
def count_unique_characters(book_path):
    character_counts = {}
    book_text_string = get_book_text(book_path)
    letter_list = list(book_text_string)
    for letter in letter_list:
        letter = letter.lower()
        if not letter in character_counts:
            character_counts[letter] = 0
        character_counts[letter] += 1
    return character_counts

def sort_by_count(book_path):
    def sort_on(items):
        return items["num"]
    
    char_count_list = []
    character_counts = count_unique_characters(book_path)
    for ch in character_counts:
        if ch.isalpha():
            char_count_list.append({"char": ch, "num": character_counts[ch]})
    char_count_list.sort(reverse=True, key=sort_on)
    return char_count_list