def is_palindrome_iterative(word):
    """Faça o código aqui."""
    if word == "":
        return False
    elif word[::-1] == word:
        return True
    else:
        return False
