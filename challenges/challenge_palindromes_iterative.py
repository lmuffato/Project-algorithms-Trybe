def is_palindrome_iterative(word):
    if word:
        result = True

        for i in range(len(word) // 2):
            result = False
            if word[i] == word[len(word) - (i + 1)]:
                result = True

        return result

    return False
