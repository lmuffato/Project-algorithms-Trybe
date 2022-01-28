def is_palindrome_iterative(word):
    if not word:
        return False

    word_length = len(word)
    for index in range(word_length // 2):
        if word[index] != word[word_length - index - 1]:
            return False

    return True
