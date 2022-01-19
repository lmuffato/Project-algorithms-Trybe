def is_anagram(first_string, second_string):
    second_string_letters = list(second_string)
    first_string_letters = list(first_string)
    if len(first_string) != len(second_string):
        return False
    for letter in first_string_letters:
        if letter not in second_string_letters:
            return False
        second_string_letters.remove(letter)
    return True
