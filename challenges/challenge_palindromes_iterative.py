def is_palindrome_iterative(word):
    """ Faça o código aqui. """
    if word == "":
        return False
    length = len(word) // 2
    palindrome = True
    for i in range(0, length):
        left = word[i]
        right = word[len(word)-i-1]
        if left != right:
            palindrome = False
            break
    return palindrome
