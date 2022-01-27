def is_anagram(first_string, second_string):
    # Fontes: https://www.programiz.com/python-programming/methods/built-in/ord
    # https://www.digitalocean.com/community/tutorials/how-to-use-the-python-map-function-pt
    # http://pythonclub.com.br/algoritmos-ordenacao.html
    first_string_sum = sum(map(ord, first_string))
    second_string_sum = sum(map(ord, second_string))

    if(first_string_sum != second_string_sum):
        return False

    if(len(first_string) != len(second_string)):
        return False

    for letter in second_string:
        if(first_string.__contains__(letter)):
            result = True
        else:
            result = False
    return result


# print(is_anagram('amor', 'roma'))
# print(is_anagram('amor', 'odio'))
