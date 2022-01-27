def is_palindrome_iterative(word):
    """ Faça o código aqui. """
    if not word:
        return False  # sem palavras sai
    for index, letter in enumerate(word):
        if word[index] != word[::-1][index]:  # compara o invertido e sai
            return False

    return True  # tudo certo só vai
