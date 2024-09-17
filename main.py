def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    count = count_words(text)
    character_count = count_characters(text)
    char_list = convert(character_count)

    #sort the list of dictionaries
    char_list.sort(key=sort_on, reverse=True)

    print("--- Begin report of books/frankenstein.txt ---")
    print(f" {count} words found in the document\n")
    
    for char_dict in char_list:
        if char_dict['char'].isalpha():
            print(f" The '{char_dict['char']}' character was found {char_dict['num']} times")
    
    print("--- End report ---")

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

def convert(character_count):
    return [{'char': char, 'num': count} for char, count in character_count.items()]

def sort_on(dict):
    return dict["num"]


main()


