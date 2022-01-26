def alfabeth_list(string):
    new_list = []
    chars = list(string)
    while chars:
        lower_char = chars[0]
        for char in chars:
            if char < lower_char:
                lower_char = char
        new_list.append(lower_char)
        chars.remove(lower_char)
    return new_list


def is_anagram(first_string, second_string):
    if len(first_string) != len(second_string):
        return False
    return alfabeth_list(first_string) == alfabeth_list(second_string)
