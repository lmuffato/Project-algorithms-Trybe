def is_anagram(first_string, second_string):
    w1 = list(first_string)
    w2 = list(second_string)
    if (first_string == "" or second_string == ""):
        return False
    if (w2 == w1):
        return True
    if (w2 != w1):
        return False
    return True
