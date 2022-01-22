def is_anagram(first_string, second_string):
    if first_string == '' or second_string == '':
        return False
    for f in first_string:
        counter_f = first_string.count(f)
        counter_s = second_string.count(f)
        if counter_f != counter_s:
            return False
    return True


""" first_string = 'perda'
second_string = 'pedra'
teste = is_anagram(first_string, second_string)
print(teste) """
