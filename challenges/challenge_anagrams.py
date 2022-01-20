# Remover um character de uma string
# https://stackoverflow.com/questions/3559559/how-to-delete-a-character-from-a-string-using-python


def is_anagram(first_string, second_string):
    if (
        not first_string 
        or not second_string
        or len(first_string) != len(second_string)
    ):
        return False

    for first_index in range(len(first_string)):
        for second_index in range(len(second_string)):
            if first_string[first_index] == second_string[second_index]:
                second_string = second_string[:second_index] + second_string[(second_index+1):]
                break
    if len(second_string) > 0:
        return False
    return True
