import sys
if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
    
def main(arg1):

    book_path = str(arg1)
    # book_path = "books/frankenstein.txt"
    print(arg1)
    from stats import word_count
    from stats import char_count
    from stats import sort_on
    text = get_book_text(book_path)
    num_words = word_count(book_path)
    num_char = char_count(text) 
    sort_char = sort_on(num_char)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char in sort_char:
        character = char["char"]
        count = char["num"]
        if character.isalpha():
            print(f"{character}: {count}")
    print("============= END ===============")

def get_book_text(path):
    with open(path) as f:
        return f.read()


main(sys.argv[1])
