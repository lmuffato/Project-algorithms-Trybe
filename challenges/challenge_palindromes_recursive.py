def is_palindrome_recursive(word, low_index, high_index):
    """ Faça o código aqui. """
    result = False
    if word == "":
        return result
    if low_index > high_index:
        result = True
        return result
    if word[low_index] == word[high_index]:
        return is_palindrome_recursive(word, low_index + 1, high_index - 1)
    return result
