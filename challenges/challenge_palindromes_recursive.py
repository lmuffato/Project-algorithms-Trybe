def is_palindrome_recursive(word, low_index, high_index):
    size = len(word) // 2
    if word == '':
        return False
    if word[low_index] != word[high_index]:
        return False
    elif low_index<= size:
        low_index += 1
        high_index -= 1
        is_palindrome_recursive(word, low_index, high_index)
    return True
