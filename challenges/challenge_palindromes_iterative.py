def is_palindrome_iterative(word):
    if not word:
        return False
    for index in range(len(word)-1):
        if word[index] != word[(index*-1)-1]:
            return False
    return True
