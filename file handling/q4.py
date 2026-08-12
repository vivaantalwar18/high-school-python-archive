def count_words():
    file_name = "my_text_file.txt"
    try:
        with open(file_name, "r") as f:
            content = f.read()
            words = content.split()
            print(f"Total words in '{file_name}': {len(words)}")
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")

count_words()