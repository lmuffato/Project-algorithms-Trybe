def is_palindrome_iterative(word):
    if word is None:
        return False
    elif word == reversed(word):
        return True
    else:
        return False

