# Referência do código Lucas Paz

def is_palindrome_recursive(word, low_index, high_index):
    """ Faça o código aqui. """
    if not word:
        return False
    if len(word) == 1 or low_index > high_index:
        return True
    return word[low_index] == word[high_index] and is_palindrome_recursive(
        word, low_index + 1, high_index - 1
    )
