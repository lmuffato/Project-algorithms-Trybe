def is_palindrome_recursive(word, low_index, high_index):
    if len(word) - 1 == low_index:
        return True
    # Verificando se a palavra é uma string vazia e se não é um palíndromo
    elif len(word) == 0 or word[low_index] != word[high_index]:
        return False

    return is_palindrome_recursive(word, low_index + 1, high_index - 1)


print(is_palindrome_recursive("ANA", 0, 2))
# print(is_palindrome_recursive("COXINHA", 0, 6))
