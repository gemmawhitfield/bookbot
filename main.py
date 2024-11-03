# FUNCTION 1 - the main function that reads in a text file and prints it to the console...
# # Main function to read in a text file and print it to the console:
# 1. Open the file
# 2. Read the file
# 3. Print the file contents to the console
def main ():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()    
    print(file_contents)
    
    
    
    # FUNCTION 2 - the function that counts the number of words in a text file...
    # 1. Split the file contents into words
    # 2. Count the number of words
    # 3. Return the number of words
    # 4. Print the number of words to the console
    def num_of_words(file_contents):
        words = file_contents.split()
        return len(words)  
    print("Number of words in the file: ", num_of_words(file_contents))
    
    
    
     # FUNCTION 3 - takes the text from the book as a string,
     # and returns the number of times each character appears in the string...
     
     


# calls the main function       
if __name__ == "__main__":
    main()