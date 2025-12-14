from stats import *
import sys

def get_book_text(path_to_file):
    try:
        with open(path_to_file) as f:
            return f.read()
    except FileNotFoundError:
        print(f"Error: No such file or directory: '{path_to_file}'")
        sys.exit(1)
        
def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    text = get_book_text(sys.argv[1])

    gen_report(text)
    
main()
