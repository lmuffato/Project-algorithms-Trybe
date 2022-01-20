def is_palindrome_iterative(word):
    if not word:
        return False
    reverseWord = []
    for letter in word:
        reverseWord.insert(0, letter)

    return "".join(reverseWord) == word
