def is_palindrome_recursive(word, low_index, high_index):
    """ Faça o código aqui. """
    # https://www.delftstack.com/pt/howto/python/python-palindrome/#:~:text=Primeiro%20calculamos%20o%20valor%20reverso,se%20n%C3%A3o%2C%20imprimimos%20Not%20Palindrome%20.
    # https://www.geeksforgeeks.org/recursive-function-check-string-palindrome/
    if not word:
        return False
    if low_index == high_index:
        return True
    if word[low_index] != word[high_index]:
        return False
    if low_index < high_index + 1:
        return is_palindrome_recursive(word, low_index + 1, high_index - 1)
    return True
