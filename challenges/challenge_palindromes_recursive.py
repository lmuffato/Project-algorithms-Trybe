def is_palindrome_recursive(word, low_index, high_index):
    splitted_word = list(word)

    if len(word) == 0:
        return False

    if high_index < 0:
        return True

    if splitted_word[low_index] == splitted_word[high_index]:
        if low_index <= (len(splitted_word) / 2):
            return is_palindrome_recursive(word, low_index + 1, high_index - 1)
        return True
    return False
