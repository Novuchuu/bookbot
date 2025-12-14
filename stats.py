# --- stats.py ---

def count_words(text):
    return len(text.split())

def count_chars(text):
    char_dict =  {}
    lower = text.lower()
    for letter in lower:
        if letter in char_dict:
                char_dict[letter] += 1 
        else:
                char_dict[letter] = 1
    return char_dict

# --- ADDED: Helper function for sorting ---
def sort_on_num(dict):
    """Returns the value of the 'num' key for use in sorting."""
    return dict["num"]

# --- ADDED: The missing function to resolve the NameError ---
def get_sorted_list_from_dict(chars_dict):
    """
    Converts the character dictionary into a sorted list of dictionaries,
    filtering out non-alphabetical characters.
    """
    sorted_list = []
    
    # 1. Build the list of dictionaries, filtering non-alphabetical chars
    for char, count in chars_dict.items():
        if char.isalpha(): 
            sorted_list.append({"char": char, "num": count})
            
    # 2. Sort the list by the 'num' value (greatest to least) using the helper
    sorted_list.sort(reverse=True, key=sort_on_num)
    
    return sorted_list

# --- Original gen_report (now correct) ---
def gen_report(text):
    # This line now works because get_sorted_list_from_dict is defined above
    char_counts_dict = count_chars(text)
    sorted_chars_list = get_sorted_list_from_dict(char_counts_dict)
    
    # Calculate the total word count
    word_count = count_words(text)

    # 3. Print the formatted report (using generic header as requested previously)
    print(f"""
============ BOOKBOT ============
Analyzing book...
----------- Word Count ----------
Found {word_count} total words
--------- Character Count -------""")
    
    # Print the character counts in the requested format
    for item in sorted_chars_list:
        print(f"{item['char']}: {item['num']}")
        
    print(f"""
============= END ===============
""")
