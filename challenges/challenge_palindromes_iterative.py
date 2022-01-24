def is_palindrome_iterative(word):
    if word == '':
        return False
    word_list = list(word)
    for i in range(len(word)):
        low = 0
        high = len(word_list) - 1
        while low - high not in (0, 1):
            if word_list[low] != word_list[high]:
                return False
            low += 1
            high -= 1
    return True
