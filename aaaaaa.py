def find_longest_word(text):
    for words in text.split():
        if len(words) > longest:
            longest = len(words)
            longest_word = words
    return longest_word, len(longest_word)

def main():
    input_string = input("Please input a list of words to evaluate: ")
    longest_word = find_longest_word(input_string)
    print("The longest word is", longest_word, "with length", len(longest_word))
