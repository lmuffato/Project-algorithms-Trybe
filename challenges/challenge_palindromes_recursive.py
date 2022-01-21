"""
https://www.askpython.com/python/array/reverse-an-array-in-python
sobre a reversão da string
"""


def is_palindrome_recursive(word, low_index, high_index):
    if len(word) == 0:
        return False
    if word[low_index] != word[high_index]:
        return False
    if (high_index - low_index) in [0, 1]:
        return True
    else:
        return is_palindrome_recursive(word, low_index + 1, high_index - 1)


"""
low_index "menor index"
high_index "maior index"
"""
