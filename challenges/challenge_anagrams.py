def is_anagram(first_string, second_string):
    if first_string == "" or second_string == "":
        return False
    if len(first_string) != len(second_string):
        return False
