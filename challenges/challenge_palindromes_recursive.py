# Carlos Melo me ajudou a refatorar e melhorar o código: https://github.com/casm3

def is_palindrome_recursive(word, low_index, high_index):
    if(not word or word[low_index] != word[high_index]):
        return False
    if(low_index >= high_index):
        return True

    return is_palindrome_recursive(word, low_index + 1, high_index-1)
