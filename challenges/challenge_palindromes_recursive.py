def is_palindrome_recursive(word, low_index, high_index):
    if word == '':
        return False

    stop_num = len(word) // 2
    if stop_num == low_index:
        return True
    elif word[low_index] == word[high_index]:
        return is_palindrome_recursive(word, low_index + 1, high_index - 1)
    else:
        return False
