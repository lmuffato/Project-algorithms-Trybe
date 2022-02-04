def is_palindrome_recursive(word, low_index, high_index):
    if not word or word[high_index] != word[low_index] or word is None:
        return False
    if low_index >= high_index:
        return True
    return is_palindrome_recursive(word, low_index + 1, high_index - 1)
