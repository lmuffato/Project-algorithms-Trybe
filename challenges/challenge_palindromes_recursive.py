def is_palindrome_recursive(word, low_index, high_index):
    if len(word) == 0 or word is None:
        return False
    if word[low_index] != word[high_index]:
        return False
    if low_index >= high_index or len(word) == 1:
        return True
    is_palindrome_recursive(word, low_index + 1, high_index - 1)
