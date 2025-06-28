from stats import count_word, number_letters, sorted_dict
import sys

def get_book_text(f): 
    return f.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    with open(sys.argv[1]) as f:
        file = get_book_text(f)
        num_words = count_word(file)
        num_let = number_letters(file)
        sorted = sorted_dict(num_let)

        print("============ BOOKBOT ============")
        print("Analyzing book found at ./books/frankenstein.txt")
        print("----------- Word Count ----------")
        print(f'Found {num_words} total words')
        print("--------- Character Count -------")
        for i in sorted:
            print(f'{i['char']}: {i['num']}')
        print("============= END ===============")
    
main()