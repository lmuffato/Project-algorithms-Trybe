def is_palindrome_iterative(word):
    """ Faça o código aqui. """
    if not word:
        return False
    return word == word[::-1]
