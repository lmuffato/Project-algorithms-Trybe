def is_palindrome_iterative(word):
    if word:
        reverse_word = word[::-1]
        if word == reverse_word:
            return True
        return False
    return False
# Slicing:
# Referência consultada:
# https://www.oreilly.com/content/how-do-i-use-the-slice-notation-in-python/
# Exemplo 4:
# https://python-reference.readthedocs.io/en/latest/docs/brackets/slicing.html
