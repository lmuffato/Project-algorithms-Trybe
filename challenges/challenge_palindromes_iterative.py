
# Mesma lógica para reverter a string. 
# Funciona, mas ultrapassa o tempo de execução
def test_each_char_in_word(word):
    key = len(word) - 1
    reverse_word = []
    if key < 0:
        return False
    while key > -1:
        reverse_word.append(word[key])
        key -= 1
    return ''.join(reverse_word)


def is_palindrome_iterative(word):
    if word:
        reverse_word = word[::-1]
        if word == reverse_word:
            return True
        return False
    return False
# Splicing:
# Referência consultada:
# https://www.oreilly.com/content/how-do-i-use-the-slice-notation-in-python/
# Exemplo 4: 
# https://python-reference.readthedocs.io/en/latest/docs/brackets/slicing.html
