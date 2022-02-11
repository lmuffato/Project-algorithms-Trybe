def is_palindrome_iterative(word):
    palindrome = word[::-1]

    if not word:
        return False
    if word == palindrome:
        return True
    else:
        return False
