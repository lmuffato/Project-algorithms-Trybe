def is_palindrome_recursive(word, low_index, high_index):
    if low_index > len(word)/2:
        return True
    if len(word) == 0:
        return False
    if len(word) == 1:
        return True
    if word[low_index] != word[high_index]:
        return False
    return is_palindrome_recursive(word, low_index + 1, high_index - 1)


""" word = "REVIVER"
teste = is_palindrome_recursive(word, 0, len(word) - 1)
print(teste) """
