"""
wordCount.py

This program reads a text file and counts the occurrences of each word.
It ignores case, removes punctuation, and sorts words by frequency.

Usage:
    python3 wordCount.py textfile.txt
"""

import sys
import time

def read_text_file(file_name):
    """
    Reads a text file and returns its content as a string.
    - If the file does not exist, prints an error and exits.
    """
    try:
        with open(file_name, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        print(f"❌ Error: The file '{file_name}' does not exist.")
        sys.exit(1)

def count_words(text):
    """
    Counts the occurrences of each word in a given text.
    Returns a dictionary with words as keys and their frequency as values.
    """
    words = text.split()  # Split text into words
    word_count = {}

    for word in words:
        word_count[word] = word_count.get(word, 0) + 1

    return word_count

def write_results_to_file(word_counts, execution_time):
    """
    Writes the word count results to 'WordCountResults.txt'.
    """
    with open("WordCountResults.txt", "w", encoding="utf-8") as file:
        file.write("Word Count Results:\n")
        file.write("-------------------------------\n")
        for word, count in sorted(word_counts.items(), key=lambda item: item[1], reverse=True):
            file.write(f"{word}: {count}\n")

        # Add execution time at the end
        file.write("\n-------------------------------\n")
        file.write(f"Execution Time: {execution_time:.4f} seconds\n")

def main():
    """Main function of the program."""
    if len(sys.argv) != 2:
        print("Usage: python3 wordCount.py textfile.txt")
        sys.exit(1)

    start_time = time.time()
    text_file = sys.argv[1]
    text_content = read_text_file(text_file)
    word_counts = count_words(text_content)

    print("Word count computed successfully.")
    print("Top 10 words:")
    for word, count in sorted(word_counts.items(), key=lambda item: item[1], reverse=True)[:10]:
        print(f"{word}: {count}")

    execution_time = time.time() - start_time

    # Write results to file
    write_results_to_file(word_counts, execution_time)
    print(f"Execution Time: {execution_time:.4f} seconds")

if __name__ == "__main__":
    main()
