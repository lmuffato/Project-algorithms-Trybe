def is_palindrome_recursive(word, low_index, high_index):
    if len(word) == 0:
        return False
    if len(word) < 2:
        return True
    future_index = low_index + 1
    if future_index == len(word):
        return word[low_index] == word[high_index]
    return (
        word[low_index] == word[high_index] and is_palindrome_recursive(
            word, future_index, high_index - 1))
