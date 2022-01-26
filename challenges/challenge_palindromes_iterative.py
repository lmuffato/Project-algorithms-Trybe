def is_palindrome_iterative(word):
    try:
        palavra = len(word)
        x = 0
        low_index = 0
        high_index = -1
        while x < palavra:
            if word[low_index] == word[high_index]:
                low_index += 1
                high_index -= 1
                x = x + 1
            else:
                return False
        return True
    except KeyError:
        raise False
