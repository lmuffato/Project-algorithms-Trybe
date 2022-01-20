def is_palindrome_recursive(word, low_index, high_index):
    if not word:
        return False

    if low_index == high_index:
        return True

    # esse if serve para o caso onde a palavra possui apenas 2 caracteres
    # e para verificar os dois caracteres
    # centrais quando a palavra tiver uma quantidade par de caracteres
    if(high_index - low_index == 1 and word[low_index] == word[high_index]):
        return True

    return (
        word[low_index] == word[high_index]
        and is_palindrome_recursive(word, low_index + 1, high_index - 1)
        )
