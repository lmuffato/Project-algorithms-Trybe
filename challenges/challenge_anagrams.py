def is_anagram(first_string, second_string):
    if first_string == '' or second_string == '':
        return False
    counter_f = 0
    counter_s = 0
    for f in first_string:
        counter_f = count_f_in_first_string(f, first_string)
        counter_s = count_f_in_second_string(f, second_string)
        if counter_f != counter_s:
            return False
    return True


def count_f_in_first_string(f, first_string):
    counter_f = 0
    for i in first_string:
        if f == i:
            counter_f += 1
    return counter_f


def count_f_in_second_string(f, second_string):
    counter_s = 0
    for i in second_string:
        if f == i:
            counter_s += 1
    return counter_s


first_string = 'perda'
second_string = 'pedra'
teste = is_anagram(first_string, second_string)
print(teste)
