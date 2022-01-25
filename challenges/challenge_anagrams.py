def is_anagram(first_string, second_string):
    if (not first_string or not second_string):
        return False
    word_two = list(second_string)
    word_one = list(first_string)
    anagram = ''
    for index in range(len(word_one)):
        if (word_two[index] in word_one):
            anagram = 'true'
    if (anagram != 'true'):
        return False
    return True
