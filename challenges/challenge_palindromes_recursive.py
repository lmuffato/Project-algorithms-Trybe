def is_palindrome_recursive(word, low_index, high_index):
    """ Faça o código aqui. """
    if not(word):
        return False
    if high_index - low_index < 1:
        return word[::-1] == word
    return (is_palindrome_recursive(word, low_index + 1, high_index - 1))
