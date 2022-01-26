def is_palindrome_recursive(word, low_index, high_index):
    if not word:
        return False
    if (low_index == high_index):
        return True
    if (word[low_index] != word[high_index]):
        return False
    if (low_index < high_index + 1):
        return is_palindrome_recursive(word, low_index + 1,  high_index - 1)
    return True
    # https://stackoverflow.com/questions/952110/recursive-function-palindrome-in-python