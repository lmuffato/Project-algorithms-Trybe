def is_palindrome_recursive(word, low_index, high_index):
    """ Faça o código aqui. """
    if not word:
        return False
    if not low_index:
        low_index = 0
        high_index = len(word) - 1
    if low_index == high_index or high_index == -1:
        return True
    if word[low_index] != word[high_index]:
        return False
    else:
        return is_palindrome_recursive(word, low_index + 1, high_index - 1)


word = "AGUA"
is_palindrome_recursive(word, 0, len(word) - 1)
