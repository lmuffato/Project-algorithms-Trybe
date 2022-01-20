def is_palindrome_iterative(word):
    """ Faça o código aqui. """
    # https://pt.stackoverflow.com/questions/401489/inverter-as-palavras-de-uma-frase-mantendo-a-ordem-delas-na-frase
    # count_1 = 0
    # count_2 = len(word) - 1
    word_aux = word[::-1]
    if not word:
        return False
    elif word == word_aux:
        return True
    else:
        return False
