def is_palindrome_iterative(word):
    """ Faça o código aqui. """
    drow = word[::-1]

    if not word:
        return False  # sem palavras sai
    """" Solução lenta """
    # for index, letter in enumerate(word):
    #     if word[index] != drow[index]:  # compara o invertido e sai
    #         return False
    """ Solução correta """
    if word == drow:
        return True  # tudo certo só vai
    else:
        return False
