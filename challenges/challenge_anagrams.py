def is_anagram(first_string, second_string):
    if (not first_string or not second_string):
        return False
    string_2 = list(second_string)
    string_1 = list(first_string)
    res = ''
    for index in range(len(string_1)):
        if (string_2[index] in string_1):
            res = 'true'
    if (res != 'true'):
        return False
    return True
