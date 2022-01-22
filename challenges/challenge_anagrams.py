def is_anagram(first_string, second_string):
    if first_string == '' or second_string == '':
        return False
    for f in first_string:
        counter_f = count_f(f, first_string)
        counter_s = count_f(f, second_string)
        if counter_f != counter_s:
            return False
    return True


def count_f(f, string):
    counter = 0
    for i in string:
        if f == i:
            counter += 1
    return counter


""" first_string = 'perda'
second_string = 'pedra'
teste = is_anagram(first_string, second_string)
print(teste) """
