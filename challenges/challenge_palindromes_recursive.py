def is_palindrome_recursive(word, low_index, high_index):
    """ Faça o código aqui. """
    length = len(word)
    if length == 0:
        return False
    elif (low_index - high_index) in (0, 1):
        return True
    elif word[low_index] != word[high_index]:
        return False
    else:
        return is_palindrome_recursive(word, low_index + 1, high_index - 1)


# is_palindrome_recursive("ana")
