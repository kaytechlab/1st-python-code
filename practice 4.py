def long_words(words, min_length):
    result = []
    for word in words:
        if len(word) > min_length:
            result.append(word)
    return result

word_list = ["apple", "hi", "banana", "cat", "elephant"]
filtered_words = long_words(word_list, 3)
print(filtered_words)