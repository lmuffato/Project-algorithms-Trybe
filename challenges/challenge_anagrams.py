def is_anagram(first_string, second_string):
    if (not first_string or not second_string):
        return False
    S_STRING_LIST = list(second_string)
    F_STRING_LIST = list(first_string)
    RESULT = ''
    for index in range(len(F_STRING_LIST)):
        if (S_STRING_LIST[index] in F_STRING_LIST):
            RESULT = 'V'
    if (RESULT != 'V'):
        return False
    return True
