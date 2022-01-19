def is_palindrome_iterative(word):
    if not word:
        return False
    reverse = []
    for letter in word:
        reverse.insert(0, letter)

    reversed_word = "".join(reverse)

    return True if reversed_word == word else False
