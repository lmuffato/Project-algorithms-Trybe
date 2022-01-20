def is_palindrome_recursive(word, low_index, high_index):
    if word == "":
        return False
    if len(word) == 1:
        return True
    else:
        return word[0] == word[1] and is_palindrome_recursive(
            word[1:-1], low_index, high_index
        )
