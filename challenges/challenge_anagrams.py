# src: https://panda.ime.usp.br/panda/static/pythonds_pt/
# 02-AnaliseDeAlgoritmos/ExemploDeDeteccaoDeAnagramas.html
def check(word):
    stored_strings = ""
    while len(word) > 0:
        first_letter_word = min(word)
        stored_strings += first_letter_word
        word.remove(first_letter_word)

    return stored_strings


def is_anagram(first_string, second_string):
    return check(list(first_string)) == check(list(second_string))
