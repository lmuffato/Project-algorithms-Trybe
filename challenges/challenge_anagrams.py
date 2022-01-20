# def list_words(words):
#     new_list = []

#     for element in words:
#         new_list.append(element)
#     return new_list

# def anagrama_check(array):
#     for i in range(len(array)):
#         value = array[i]
#         position = i

#         while (position > 0 and array[position - 1] > value):
#             array[position] = array[position - 1]
#             position = position - 1
#         array[position] = value
#     return array

# def anagrama_check(array):
#     for i in range(len(array)):
#         min = i
#         for j in range(i + 1, len(array)):
#             if array[j] < array[min]:
#                 min = j
#         array[min], array[i] = array[i], array[min]
#     return array


def aux_check(left, right, merged):
    left_cursor, right_cursor = 0, 0

    while left_cursor < len(left) and right_cursor < len(right):
        if left[left_cursor] <= right[right_cursor]:
            merged[left_cursor + right_cursor] = left[left_cursor]
            left_cursor += 1
        else:
            merged[left_cursor + right_cursor] = right[right_cursor]
            right_cursor += 1
    
    for left_cursor in range(left_cursor, len(left)):
        merged[left_cursor + right_cursor] = left[left_cursor]
    
    for right_cursor in range(right_cursor, len(right)):
        merged[left_cursor + right_cursor] = right[right_cursor]
    
    return merged
        

def anagrama_check(array):
    if len(array) <= 1:
        return array
    
    meio = len(array) // 2

    left, right = anagrama_check(array[:meio]), anagrama_check(array[meio:])
    return aux_check(left, right, array.copy())
    

def is_anagram(first_string, second_string):
    # first_world = list_words(first_string)
    # second_world = list_words(second_string)

    return anagrama_check(list(first_string)) == anagrama_check(list(second_string))
       

# first_string = "pato"
# second_string = "topa"
# iteracoes = 0
# print(len(first_string) - iteracoes - 1)
# print(list_words(first_string))
# print(list_words(second_string))
# print(list(first_array))
# print(is_anagram("pedra", ""))
# print(first_string[0].lower())