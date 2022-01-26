def is_palindrome_recursive(word, low_index, high_index):
    size = len(word)
    if size == 0:
        return False
    else:
        return word[0] == word[1] and is_palindrome_recursive(
            word[1:-1], low_index, high_index)

# referencia, agradeço ao amigo Lucas Lara pelo auxilio no requisito
