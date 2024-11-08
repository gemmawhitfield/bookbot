# Main function to read in a text file and print it to the console:
# 1. Open the file
# 2. Read the file
# 3. Print the file contents to the console
def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    
    print(file_contents)
    print("Number of words in the file: ", num_of_words(file_contents))
    print(count_characters(file_contents))
    print_report(file_contents)

# Function that counts the number of words in a text file:
# 1. Split the file contents into words
# 2. Count the number of words
# 3. Return the number of words
def num_of_words(file_contents):
    words = file_contents.split()
    return len(words)

# Function that takes the text from the book as a string,
# and returns the number of times each character appears in the string:
def count_characters(file_contents):
    char_count = {}
    for char in file_contents:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

# Function that creates an overall report and prints it to the console:
def print_report(file_contents):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_of_words(file_contents)} words found in the document.\n")
    
    chars_dict = get_chars_dict(file_contents)
    chars_sorted_list = chars_dict_to_sorted_list(chars_dict)
    
    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")
    
    print("--- End report ---")

def sort_on(d):
    return d["num"]

def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

# Calls the main function       
if __name__ == "__main__":
    main()