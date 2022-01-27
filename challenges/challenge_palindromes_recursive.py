def is_palindrome_recursive(word, low_index, high_index):
    """ Faça o código aqui. """
    if not word:
        return False
    if low_index >= high_index:
        if word[low_index] == word[high_index]:
            return True
        else:
            return False
    return is_palindrome_recursive(word, low_index + 1, high_index - 1)
