def is_palindrome_iterative(word):
    if word:
        reverse_word = word[::-1]
        return True if (reverse_word == word) else False

    return False


# revertendo listas
# https://www.delftstack.com/pt/howto/python/python-reverse-a-list/


# print(is_palindrome_iterative("ama"))
