def is_palindrome_iterative(word):
    if not word:
        return False
    reverse = []
    for letter in word:
        reverse.append(letter)

    # Sugestão de mudança por instrutor Calos Melo
    reverse.reverse()

    reversed_word = "".join(reverse)

    return True if reversed_word == word else False
