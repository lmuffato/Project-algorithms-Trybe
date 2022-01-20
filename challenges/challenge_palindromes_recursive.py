def is_palindrome_recursive(word, low_index, high_index):
    meio = len(word)//2
    index = low_index
    while index < (meio):
        if word[low_index + index] == word[high_index - index]:
            index += 1
        else:
            return False
    return True
