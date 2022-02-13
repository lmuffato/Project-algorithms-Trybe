def is_palindrome_iterative(word):
    # string[::-1] -> retorna o inverso da entrada (stringa ou array)
    inverted_word = word[::-1]
    if not word or word == '':
        return False
    if word == inverted_word:
        return True
    if word != inverted_word:
        return False


# Teste manual
# print(is_palindrome_iterative('amor'))


# Teste automatizado
# python3 -m pytest tests/test_palindromes_iterative.py