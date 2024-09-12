def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    count = count_words(text)
    print(count)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    num_words = 0
    words = text.split()
    
    for word in words:
        num_words += 1
    return num_words

main()