import math


def is_palindrome_recursive(word, low_index, high_index):
    if not word:
        return False
    if len(word) == 1 or low_index == high_index or high_index < low_index:
        return True
    if word[low_index] != word[high_index]:
        return False
    return is_palindrome_recursive(word, low_index+1, high_index-1)
