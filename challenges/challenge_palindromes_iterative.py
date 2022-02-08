def is_palindrome_iterative(word):
    if not word:
        return False
    max_iterations = (len(word) // 2)
    has_difference = False
    for i in range(0, max_iterations):
        if word[i] != word[len(word) - (i + 1)]:
            has_difference = True
    return not has_difference
