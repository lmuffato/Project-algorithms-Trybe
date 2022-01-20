def is_palindrome_recursive(word, low_index, high_index):
    if len(word) == 0:
        return False
    backwards_word = backwards(word)
    if backwards_word == word:
        return True
    else:
        return False


def backwards(word):
    if len(word) == 1:
        return word
    first_letter = word[:1]
    rest_backwards = backwards(word[1:])
    return rest_backwards + first_letter
