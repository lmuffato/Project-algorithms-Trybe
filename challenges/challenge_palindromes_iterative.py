def is_palindrome_iterative(word):
    """ Faça o código aqui. """
    if not word:
        return False
    palindromo = word[::-1]
    result = "".join(palindromo)
    if(result.lower() == word.lower()):
        return True
    return False
