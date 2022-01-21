def is_palindrome_recursive(word, low_index, high_index):
    """ Faça o código aqui. """
    # Entendi parte do requisito 2 com ajuda do Rafael Medeiros. Grazie Mille!*
    if (word is None or not word or word[low_index] != word[high_index]):
        return False

    if (low_index >= high_index):
        return True

    # Usando recursividade abaixo*
    return is_palindrome_recursive(word, low_index + 1, high_index - 1)

    # ABAIXO NÃO FUNCIONOU
    # if (word is None):
    #     return False

    # palavra = []
    # for x in range(len(word)):
    #     palavra += word[-(x+1)]

    # resultado = ''.join(palavra)
    # if (word == resultado):
    #     return True
    # else:
    #     return False
