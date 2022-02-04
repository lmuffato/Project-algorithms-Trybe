def is_palindrome_recursive(word, low_index, high_index):
    new_word = word[high_index]

    if high_index < low_index:
        return new_word == word[::-1]

    return is_palindrome_recursive(word, low_index, high_index - 1)
