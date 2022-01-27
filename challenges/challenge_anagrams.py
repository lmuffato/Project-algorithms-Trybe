def sort_string(lst):
    if not lst:
        return []
    return (
        sort_string([x for x in lst[1:] if x < lst[0]])
        + [lst[0]]
        + sort_string([x for x in lst[1:] if x >= lst[0]])
    )


def is_anagram(first_string, second_string):
    """ Faça o código aqui. !!"""
    if len(first_string) != len(second_string):
        return False
    else:
        first_string = sort_string(list(first_string))
        second_string = sort_string(list(second_string))

    if first_string == second_string:
        return True
    else:
        return False
