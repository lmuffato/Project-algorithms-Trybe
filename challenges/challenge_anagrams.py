def sort(string):
        ordem = []
        new_array = ''
        array = list(string)
        while len(array) > 0:
            low_letter = min(array)
            array.remove(low_letter)
            ordem.append(low_letter)
        return new_array.join(ordem)

def is_anagram(first_string, second_string):
    first = list(first_string)
    second = list(second_string)
    
    if len(first_string) != len(second_string):
        return False
    if first_string == '' or second_string == '':
        return False
    return sort(first_string) == sort(second_string)
    return False