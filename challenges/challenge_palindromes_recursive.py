def is_palindrome_recursive(word, low_index, high_index):
    size = len(word) // 2
    if word == '':
        return False
    if low_index > size:
        return True
    if word[low_index] != word[high_index]:
        return False
    if low_index <= size:
        is_palindrome_recursive(word, low_index + 1, high_index - 1)
    return True
