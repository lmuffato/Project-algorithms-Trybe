def is_palindrome_recursive(word, low_index, high_index):
    if word == "":
        return False

    if len(word) == 1:
        return True

    if high_index >= len(word) - 1:
        palindrome = word[high_index]
        return is_palindrome_recursive(word, palindrome, high_index - 1)

    if high_index <= 0:
        palindrome = low_index + word[high_index]
        return word == palindrome

    palindrome = low_index + word[high_index]
    return is_palindrome_recursive(word, palindrome, high_index - 1)
