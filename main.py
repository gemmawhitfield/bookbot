# Main function to read in a text file and print it to the console:
# 1. Open the file
# 2. Read the file
# 3. Print the file contents to the console
def main ():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()    
    print(file_contents)
    
    
    # Function to count the number of words in a text file:
    # 1. Split the file contents into words
    # 2. Count the number of words
    # 3. Return the number of words
    # 4. Print the number of words to the console
    def num_of_words(file_contents):
        words = file_contents.split()
        return len(words)
    
    print("Number of words in the file: ", num_of_words(file_contents))
        
if __name__ == "__main__":
    main()