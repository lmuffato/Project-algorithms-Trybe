""" def order(str):
    for i in range(len(str)-1):
        for j in range(i+1, len(str)):
            if str[j] < str[i]:
                aux1 = str[i]
                aux2 = str[j]
                str[i] = aux2
                str[j] = aux1

    return "".join(str) """


def order(str):
    ordered_string = ""
    while len(str) > 0:
        aux = min(str)
        ordered_string += aux
        str.remove(aux)

    return ordered_string


def is_anagram(first_string, second_string):
    return order(list(first_string)) == order(list(second_string))
