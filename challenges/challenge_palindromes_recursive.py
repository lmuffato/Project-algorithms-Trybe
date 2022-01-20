def is_palindrome_recursive(word, low_index, high_index):
    _break = len(word) // 2
    if word == "" or word[low_index] != word[high_index]:
        return False
    if low_index == _break:
        return True
    if low_index <= _break:
        return is_palindrome_recursive(word, low_index + 1, high_index - 1)
    return False
