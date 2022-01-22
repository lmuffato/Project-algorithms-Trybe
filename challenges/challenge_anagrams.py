def anagram_check(first_string, second_string):
    return False


def strings_check(first_string, second_string):
    if (
        first_string == ""
        or second_string == ""
        or len(first_string) != len(second_string)
    ):
        return False
    return True


def is_anagram(first_string, second_string):
    """Faça o código aqui."""
    strings = strings_check(first_string, second_string)

    if not strings:
        return False
    return True
