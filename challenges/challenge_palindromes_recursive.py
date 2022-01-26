def is_palindrome_recursive(word, low_index, high_index):
    """ Faça o código aqui. """
    if word == "" or word[low_index] != word[high_index]:
        return False
    elif len(word) == 1:
        return True
    elif low_index >= high_index:
        return True
    return is_palindrome_recursive(word, low_index+1, high_index-1)
