def is_palindrome_iterative(word):
    if len(word) == 0:
        return False
    # https://stackoverflow.com/questions/31487696/most-efficient-palindrome-program-for-python
    return word == word[::-1]
