
def test_each_char_in_word(word):
    key = len(word) - 1
    reverse_word = []
    while key > -1:
        reverse_word.append(word[key])
        key -= 1
    return "".join(reverse_word)


def is_palindrome_iterative(word):
    if word:
        if word == test_each_char_in_word(word):
            return True
        return False
    return False
