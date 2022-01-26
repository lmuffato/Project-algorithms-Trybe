def is_palindrome_recursive(word, low_index, high_index):
    if word == '':
        return False
    
    floor_number = len(word) // 2
    if floor_number == low_index:
        return True
    elif word[low_index] == word[high_index]:
        return is_palindrome_recursive(word, low_index + 1, high_index - 1)
    else:
        return False
