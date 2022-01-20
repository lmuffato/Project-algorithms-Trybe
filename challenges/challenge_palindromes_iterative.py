# Mesma lógica para reverter a string,
# faz o mesmo que o slicing mas de forma iterativa.
def is_palindrome_iterative_vsbeta(word):
    key = len(word) - 1
    reverse_word = []
    if key < 0:
        return False
    while key > -1:
        reverse_word.append(word[key])
        key = key - 1
    return word == ''.join(reverse_word)


def is_palindrome_iterative(word):
    if word:
        for _ in word:
            reverse_word = word[::-1]
            if word == reverse_word:
                return True
            return False
        return False
    return False
# Slicing:
# Referência consultada:
# https://www.oreilly.com/content/how-do-i-use-the-slice-notation-in-python/
# Exemplo 4:
# https://python-reference.readthedocs.io/en/latest/docs/brackets/slicing.html
