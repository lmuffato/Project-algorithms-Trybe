def validate_word(word):
    if not word or len(word) == 0:
        return False


def is_palindrome_iterative(word):
    if validate_word(word):
        counter = 0
        new_word = ""
        word_len = len(word)

        while counter < word_len:
            new_word += word[word_len - counter]
            counter += 1

        if word == new_word:
            return True
        else:
            return False
    else:
        return False
