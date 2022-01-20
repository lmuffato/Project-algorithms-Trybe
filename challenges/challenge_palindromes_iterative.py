def is_palindrome_iterative(word):
    """ Faça o código aqui. """
    if not word:
        return False

    high_index = len(word) - 1

    for i in range(len(word)):
        if i == high_index:
            return True
        if word[i] != word[high_index]:
            return False
        high_index -= 1
    return True
