def is_palindrome_iterative(word):
    if not word:
        return False
    i = 0
    j = len(word) - 1
    while i < j:
        if word[i] != word[j]:
            return False
        i += 1
        j -= 1
    return True
