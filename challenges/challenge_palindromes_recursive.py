def is_palindrome_recursive(word, low_index, high_index):
    result = True
    if word == '':
        result = False
    meio = len(word)//2
    if low_index < meio:
        if word[low_index] == word[high_index]:
            return is_palindrome_recursive(word, (
                low_index + 1), (high_index - 1))
        else:
            result = False
    return result
