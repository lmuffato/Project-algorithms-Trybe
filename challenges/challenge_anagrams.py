from challenges.merge_sort import merge_sort


def is_anagram(first_string, second_string):
    if(len(first_string) == 0 or len(second_string) == 0):
        return False

    str1 = [*first_string]
    str2 = [*second_string]
    output = True

    merge_sort(str1)
    merge_sort(str2)

    for x, y in zip(str1, str2):
        output = output and (x == y)

    return output


print(is_anagram('amor', 'roma'))
# print(is_anagram('pedra', 'perda'))
# print(is_anagram('coxinha', 'empada'))

# first_string = (
#             "Lorem ipsum dolor sit amet, consectetur "
#             "adipiscing elit, do sed eiusmod tempor "
#             "incididunt ut labore et dolore magna aliqua."
#         )

# second_string = (
#     "Lorem ipsum dolor sit amet, consectetur "
#     "adipiscing elit, do sed eiusmod tempor "
#     "incididunt ut labore et dolore magna aliqua."
# )

# print(is_anagram(first_string, second_string))
