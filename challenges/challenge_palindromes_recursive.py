def is_palindrome_recursive(word, low_index, high_index):
    if not word or word == '':  # Se não conter o parâmerto word
        return False
    # Se as letras forem direfentes
    if word[low_index] != word[high_index]:
        return False
    # Quando chegar no meio da palavra
    if low_index >= high_index:
        return True
    # Invoca a própria função recursivamente
    return is_palindrome_recursive(word, low_index + 1, high_index - 1)


# Teste manual
# print(is_palindrome_recursive('REVIVER', 0, 6))

# Teste automatizado
# python3 -m pytest tests/test_palindromes_recursive.py
