def is_palindrome_iterative(word):
    if len(word) == 1:
        return True

    low_index = 0
    high_index = len(word) - 1
    _break = len(word) // 2

    for i in range(_break):
        if word[low_index] == word[high_index]:
            low_index += 1
            high_index -= 1
        if low_index == _break:
            return True

    return False

