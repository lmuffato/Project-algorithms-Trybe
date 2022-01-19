def is_palindrome_iterative(word):
    if word == "":
        return False

    aux = ""

    for item in word[::-1]:
        aux += item

    return word == aux
