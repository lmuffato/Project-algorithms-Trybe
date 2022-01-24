def is_palindrome_recursive(word, low_index, high_index):
    if word == "":
        return False
    if len(word) == 1:
        return True
    elif word[low_index] != word[high_index]:
        return False
    elif low_index == high_index or low_index - high_index == -1:
        return True
    else:
        return is_palindrome_recursive(word, (low_index + 1), (high_index - 1))
