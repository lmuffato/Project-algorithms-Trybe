def is_palindrome_recursive(word, low_index, high_index):
    """ Faça o código aqui. """
    if high_index == 0:
        return True
    elif high_index == -1:
        return False
    elif word[low_index] == word[high_index]:
        return is_palindrome_recursive(word, low_index + 1, high_index - 1)
    else:
        return False
