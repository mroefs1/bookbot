from stats import number_of_words, number_of_characters, sort_dict
import sys

def get_book_text(filepath):
    file_contents = ""
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def print_report(num_words, char_list, path):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char in char_list:
        print(f"{char["char"]}: {char["num"]}")
    print("============= END ===============")

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    print(path)
    book_text = get_book_text(path)
    num_words = number_of_words(book_text)
    num_chars = number_of_characters(book_text)
    char_list = sort_dict(num_chars)
    print_report(num_words, char_list, path)


main()