def is_palindrome_recursive(word, low_index, high_index):
    """ Faça o código aqui. """
    if len(word) < 1:  # comprimento zero não é palindromo
        return False
    if low_index >= len(word) // 2:  # percorreu metade?
        return True
    if word[low_index] != word[high_index]:  # compara indices equidistantes
        return False
    # testa próximo indice
    return is_palindrome_recursive(word, low_index + 1, high_index - 1)
