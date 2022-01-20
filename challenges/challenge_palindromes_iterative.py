def is_palindrome_iterative(word):
    if not word:
        return False
    reverseWord = ''
    for letter in word[::-1]:
        reverseWord += letter

    return reverseWord == word
