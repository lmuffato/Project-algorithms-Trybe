def is_palindrome_iterative(word):
    if len(word) == 0:
        return False
    if word == word[::-1]:
        return True
    else:
        return False


print(is_palindrome_iterative("ANA"))
