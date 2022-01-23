def is_palindrome_recursive(word, low_index, high_index):
    if len(word) == 0:
        return False
    elif word[low_index] != word[high_index]:
        return False
    elif (low_index - high_index) in (0, 1):
        return True
    else:
        return is_palindrome_recursive(word, low_index + 1, high_index - 1)
