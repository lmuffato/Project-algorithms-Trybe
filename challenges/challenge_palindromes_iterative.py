def is_palindrome_iterative(word):
    size = len(word)
    if size == 0:
        return False
    for i in range(0, size // 2):
        if word[i] != word[size - i - 1]:
            return False
    return True

# referencia
# https://pt.stackoverflow.com/questions/120421/como-identificar-se-uma-string-%C3%A9-um-pal%C3%ADndromo
