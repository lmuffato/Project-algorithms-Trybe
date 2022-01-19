
def is_palindrome_recursive(word, low_index, high_index):
    saida = False
    if word == '':
        return saida
    if low_index > high_index:
        saida = True
        return saida
    if word[low_index] == word[high_index]:
        return is_palindrome_recursive(word, low_index + 1, high_index - 1)
    return saida

