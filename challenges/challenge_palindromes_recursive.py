def is_palindrome_recursive(word, low_index, high_index):

    if len(word) == 0:
        return False

    if low_index > (len(word) // 2):
        return True

    if word[low_index] != word[high_index]:
        return False

    return is_palindrome_recursive(word, (low_index + 1), (high_index - 1))


# Utilizei o operador // para trazer um resultado aredondado, pois quando eu
# estava usando apenas o / ele falhava no teste. Utilizei de
# ref o site: https://www.w3schools.com/python/python_operators.asp
