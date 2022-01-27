def order_string(string):
    ordered_string = ""
    while len(ordered_string) < len(string):
        lower = min(string)
        ordered_string += lower
        string = string.replace(lower, "", 1)
    return ordered_string


def is_anagram(first_string, second_string):
    """ Faça o código aqui """
    if first_string == "" or second_string == "":
        return False
    return order_string(first_string) == order_string(second_string)
