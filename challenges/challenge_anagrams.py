def is_anagram(first_string, second_string):
    if not first_string or not second_string:
        return False
    word1 = list(first_string)
    word2 = list(second_string)
    anagram = ""
    for gokuSsj in range(len(word1)):
        if word2[gokuSsj] in word1:
            anagram = "true"
    if anagram != "true":
        return False
    return True
