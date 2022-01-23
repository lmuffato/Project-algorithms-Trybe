def is_palindrome_iterative(word):
    if len(word) > 0:

        comparison_position = 0
        result = True

        for i in range(len(word) // 2):
            comparison_position += 1
            result = False
            if word[i] == word[len(word) - comparison_position]:
                result = True

        return result

    return False
