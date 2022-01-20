# Remover um character de uma string
# https://stackoverflow.com/questions/3559559/how-to-delete-a-character-from-a-string-using-python


def validate_entries(first, second):
    if (
        not first
        or not second
        or len(first) != len(second)
    ):
        return False
    return True


def anagram_check(first_string, second_string):
    for first_index in range(len(first_string)):
        for second_index in range(len(second_string)):
            if first_string[first_index] == second_string[second_index]:
                second_string = (
                    second_string[:second_index] +
                    second_string[(second_index+1):]
                )
                break
    if len(second_string) > 0:
        return False
    return True


def is_anagram(first_string, second_string):
    validate = validate_entries(first_string, second_string)
    anagram = anagram_check(first_string, second_string)
    if not validate or not anagram:
        return False
    return True
