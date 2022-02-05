def is_palindrome_recursive(word, low_index, high_index):
    if word == "":
        return False

    if word[low_index] != word[high_index]:
        return False

    if low_index == len(word) // 2:
        return True

    return is_palindrome_recursive(word, low_index + 1, high_index - 1)
