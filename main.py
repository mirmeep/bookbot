def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = count_words(text)
    chars_in_text = count_char(text)
    chars_sorted_list = sort_dict(chars_in_text)

    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    for item in chars_sorted_list:
        if item["char"].isalpha():
            print(f"The '{item['char']}' character was found {item['num']} times")
    print("--- End Report ---")

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    words = text.split()
    return len(words)

def sort_on(d):
    return d["num"]

def sort_dict(chars_in_text):
    sorted_list = []
    for c in chars_in_text:
        sorted_list.append({"char": c, "num": chars_in_text[c]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def count_char(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

main()