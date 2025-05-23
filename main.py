import sys
from stats import get_num_words, get_num_characters, sorted_characters


if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)


def get_book_text(path):
    """
    Reads the content of a book from a text file and returns it as a string.
    Args:
        path (str): The path to the text file containing the book.
    -Returns:
        str: The content of the book as a string.
    """
    with open(path) as file:
        return file.read()


def main():
    """
    Main function to execute the script.
    """
    # Path to the book file
    book_path = sys.argv[1]
    # Call the function to get the book text    
    book_text = get_book_text(book_path)
    # Call the function to count words
    word_count = get_num_words(book_text)
    # Call the function to count characters
    character_count = get_num_characters(book_text)
    # Call the function to sort characters
    sorted_characters_list = sorted_characters(character_count)

    # Print the results
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for item in sorted_characters_list:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['count']}")
    print("============= END ===============")

if __name__ == "__main__":
    main() 