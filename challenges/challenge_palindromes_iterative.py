def is_palindrome_iterative(word):
    if not word:
        return False
    palindrom = []
    for gokuSsj2 in word:
        palindrom.append(gokuSsj2)

        if "".join(palindrom) == word:
            return True
        else:
            return False
