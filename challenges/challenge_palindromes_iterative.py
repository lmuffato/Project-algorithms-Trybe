def validate_word(word):
    if not word or word == "":
        return False

    return True


def is_palindrome_iterative(word):
    if validate_word(word):

        # fonte:
        # https://www.delftstack.com/pt/howto/python/python-palindrome/:

        if word == word[::-1]:
            return True
        else:
            return False
    else:
        return False
