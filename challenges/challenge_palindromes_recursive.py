import math


def is_palindrome_recursive(word, low_index, high_index):
    if not word:
        return False
    if word[low_index] != word[high_index]:
        return False
    if low_index == math.floor(len(word) / 2):
        return True
    return is_palindrome_recursive(word, low_index+1, high_index-1)
