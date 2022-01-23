def is_palindrome_iterative(word):
    if word:
        reverse_index = len(word) - 1
        reverse_word = []

        while reverse_index >= 0:
            reverse_word.append(word[reverse_index])
            reverse_index -= 1

        return True if ("".join(reverse_word) == word) else False

    return False


# revertendo listas
# https://www.delftstack.com/pt/howto/python/python-reverse-a-list/

# print(is_palindrome_iterative("ama"))
