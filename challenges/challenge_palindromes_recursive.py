def reverse(list):
    if len(list) < 2:
        return list
    else:
        return reverse(list[1:]) + [list[0]]


def is_palindrome_recursive(word, low_index, high_index):
    if not word:
        return False
    reversed = ''.join(reverse(list(word)))
    normal = ''.join(list(word))
    if normal == reversed:
        return True
    return False
