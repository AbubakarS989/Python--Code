def count_words_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            words = content.split()
            return len(words)
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return -1

if __name__ == "__main__":
    file_path = input("Enter the path to the text file: ")
    word_count = count_words_from_file(file_path)
    
    if word_count != -1:
        print(f"The number of words in the file is: {word_count}")
