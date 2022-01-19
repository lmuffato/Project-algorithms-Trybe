def is_anagram(first_string, second_string):
    if not first_string or not second_string:
        return False
    first = [letter for letter in first_string]
    second = [letter for letter in second_string]

    first_string_ordered = "".join(sorter(first))
    second_string_ordered = "".join(sorter(second))
    return True if first_string_ordered == second_string_ordered else False


def sorter(divided_string):

    last_position = len(divided_string) - 1

    if last_position < 1:
        return divided_string

    current_position = 0

    for pos in range(0, last_position):
        if divided_string[pos + 1] <= divided_string[0]:
            current_position += 1
            divided_string[pos + 1], divided_string[current_position] = (
                divided_string[current_position],
                divided_string[pos + 1],
            )

    divided_string[0], divided_string[current_position] = (
        divided_string[current_position],
        divided_string[0],
    )

    start = sorter(divided_string[0:current_position])
    end = sorter(divided_string[current_position + 1:last_position + 1])

    sorted_string = start + [divided_string[current_position]] + end

    return sorted_string
