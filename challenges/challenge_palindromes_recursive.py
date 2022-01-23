def is_palindrome_recursive(word, low_index, high_index):
    """ Faça o código aqui. """
    if not word:
        return False
    if (low_index == high_index):
        return True
    if (word[low_index] != word[high_index]):
        return False
    if (low_index < high_index + 1):
        return is_palindrome_recursive(word, low_index + 1,  high_index - 1)
    return True


# Requisito realizado com ajuda de Marília - Turma 10A
# https://stackoverflow.com/questions/952110/recursive-function-palindrome-in-python