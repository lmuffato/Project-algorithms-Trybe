def is_palindrome_iterative(word):
    word_len = len(word)

    if word == "":
        return False
    for index in range(word_len // 2):
        if word[index] != word[word_len - index - 1]:
            return False
    return True
