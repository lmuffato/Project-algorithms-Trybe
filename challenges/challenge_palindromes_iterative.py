def is_palindrome_iterative(word):
    if len(word) == 0:
        return False
    half_way = len(word) // 2
    for index in range(half_way):
        if word[index] != word[-1 - index]:
            return False
    return True
