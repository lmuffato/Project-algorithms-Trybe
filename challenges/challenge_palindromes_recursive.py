def validate_word(word):
    if not word or len(word) == 0:
        return False

    return True


def is_palindrome_recursive(word, low_index, high_index):
    if validate_word(word):
        return print("foi")

    return False
