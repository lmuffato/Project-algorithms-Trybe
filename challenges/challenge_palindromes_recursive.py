def is_palindrome_recursive(word, low_index, high_index):
    if not word:
        return False
    else:
        if low_index < high_index:
            if word[low_index] == word[high_index]:
                return is_palindrome_recursive(
                    word, low_index + 1, high_index - 1
                )
            else:
                return False
        else:
            return True
