def is_palindrome_recursive(word, low_index, high_index):
    """ Faça o código aqui. """
    if not word:
        return False

    if word[low_index] != word[high_index]:
        return False
        print("1")
        """low_index = low_index + 1
        high_index = high_index - 1"""

    elif low_index < len(word) - 1:
        low_index = low_index + 1
        high_index = high_index - 1
        return is_palindrome_recursive(word, low_index, high_index)

    else:
        return True
        print("2")
        """low_index = low_index + 1
        high_index = high_index - 1"""


low_index = 0
word = "ana"
resp = is_palindrome_recursive(word, low_index, len(word) - 1)
print(resp)
