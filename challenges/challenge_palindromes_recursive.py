def is_palindrome_recursive(word, low_index, high_index):
    if word == "":
        return False

    word_length = len(word)
    if word[low_index] != word[high_index]:
        return False
    elif word_length <= 2 and word[low_index] == word[high_index]:
        return True
    else:
        new_word = word[1:-1]
        return is_palindrome_recursive(new_word, 0, len(new_word) - 1)
