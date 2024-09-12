def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    count = count_words(text)
    character_count = count_characters(text)
    print(character_count)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    lower_case = text.lower()
    char_count = {}

    for char in lower_case:
        char_count[char] = char_count.get(char, 0) + 1
    return char_count

main()


