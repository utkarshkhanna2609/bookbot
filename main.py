def char_frequency(text):
    text = text.lower()
    freq = {}
    for char in text:
        freq[char] = freq.get(char, 0) + 1
    return freq

def count_chars(text,trimmed=False):
    if trimmed:
        text=text.split()
    return len(text)

def main():
    with open('books/frankenstein.txt') as f:
        file_contents = f.read()

    # Get word count
    word_count = count_chars(file_contents, trimmed=True)
    
    # Get character frequency
    char_counts = char_frequency(file_contents)
    
    # Filter and sort character counts (only letters, sorted by frequency)
    letter_counts = {k: v for k, v in char_counts.items() if k.isalpha()}
    sorted_chars = sorted(letter_counts.items(), key=lambda x: x[1], reverse=True)

    # Print report
    print(f"--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document\n")

    for char, count in sorted_chars:
        print(f"The '{char}' character was found {count} times")

    print("--- End report ---")

main()
